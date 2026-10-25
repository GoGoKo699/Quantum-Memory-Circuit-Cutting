"""Finite reconstruction of the pair-scored gate protocol in science/gate-cuts.md.

The one-slot check contracts the physical Bell vectors directly. The two-slot
check explicitly sums all Bell-record signs before assembling the Choi matrix.
No assumption that Bell outcomes are equiprobable is made.
"""

from __future__ import annotations

import itertools
import json

import numpy as np


PAULI = np.array([np.eye(2), [[0, 1], [1, 0]], [[0, -1j], [1j, 0]],
                  [[1, 0], [0, -1]]], dtype=complex)
PHI = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
BELL_RESOURCES = np.array([np.kron(np.eye(2), p) @ PHI for p in PAULI])
BELL_MEASUREMENTS = np.array([np.kron(np.eye(2), p.conj()) @ PHI for p in PAULI])
F = np.array([[1, 1, 1, 1], [1, 1, -1, -1],
              [1, -1, 1, -1], [1, -1, -1, 1]])
TOLERANCE = 2e-11


def check_close(a, b):
    residual = float(np.max(np.abs(np.asarray(a) - np.asarray(b))))
    if residual > TOLERANCE:
        raise AssertionError(f"gate reconstruction residual {residual:.4g}")
    return residual


def choi_vector(operator):
    # Reference first, output second: (I tensor operator)|Phi_d>.
    return operator.T.reshape(-1) / np.sqrt(operator.shape[1])


def choi_from_kraus(operators):
    vectors = np.array([choi_vector(k) for k in operators])
    return np.einsum("ai,aj->ij", vectors, vectors.conj())


def corrected_kraus(resource, outcome):
    # Q,R,S order: contract <beta_a| on Q,R, then correct S by sigma_a.
    raw = np.einsum("qr,rs->sq", BELL_MEASUREMENTS[outcome].conj().reshape(2, 2),
                    resource.reshape(2, 2))
    return PAULI[outcome] @ raw


def local_sign_checks():
    largest = 0.0
    for a, k in itertools.product(range(4), repeat=2):
        largest = max(largest, check_close(PAULI[a] @ PAULI[k] @ PAULI[a], F[a, k] * PAULI[k]))
        largest = max(largest, check_close(corrected_kraus(BELL_RESOURCES[k], a), F[a, k] * PAULI[k] / 2))
    # Every input matrix unit and every pair of resource Pauli labels, including Y.
    matrix_unit_residual = 0.0
    for a, k, ell, p, q in itertools.product(range(4), range(4), range(4), range(2), range(2)):
        matrix = np.zeros((2, 2), dtype=complex)
        matrix[p, q] = 1
        actual = corrected_kraus(BELL_RESOURCES[k], a) @ matrix @ corrected_kraus(BELL_RESOURCES[ell], a).conj().T
        expected = F[a, k] * F[a, ell] * PAULI[k] @ matrix @ PAULI[ell].conj().T / 4
        matrix_unit_residual = max(matrix_unit_residual, check_close(actual, expected))
    return dict(commutation_sign_table=F.tolist(), pauli_bell_kraus_cases=16,
                kraus_max_residual=largest, resource_input_matrix_unit_cases=256,
                matrix_unit_max_residual=matrix_unit_residual)


def rotation(label, angle):
    return np.cos(angle) * PAULI[0] + 1j * np.sin(angle) * PAULI[label]


def gate_data(angles, slot):
    # XX, YY, ZZ commute. Multiplying their exact elementary exponentials avoids SciPy.
    core = np.eye(4, dtype=complex)
    for label, angle in enumerate(angles, 1):
        core = (np.cos(angle) * np.eye(4) + 1j * np.sin(angle) * np.kron(PAULI[label], PAULI[label])) @ core
    coefficients = np.array([np.trace(np.kron(p, p).conj().T @ core) / 4 for p in PAULI])
    check_close(sum(u * np.kron(p, p) for u, p in zip(coefficients, PAULI)), core)
    check_close(np.sum(np.abs(coefficients)**2), 1)
    assert np.min(np.abs(coefficients)) > 1e-3  # All four complex Schmidt paths are exercised.
    va, wa = rotation(1, 0.17 + slot * 0.03), rotation(2, -0.23 + slot * 0.05)
    vb, wb = rotation(3, 0.29 - slot * 0.04), rotation(1, -0.11 - slot * 0.02)
    alice = np.array([va @ p @ wa for p in PAULI])
    bob = np.array([vb @ p @ wb for p in PAULI])
    gate = np.kron(va, vb) @ core @ np.kron(wa, wb)
    check_close(gate.conj().T @ gate, np.eye(4))
    return dict(gate=gate, coefficients=coefficients, alice=alice, bob=bob,
                va=va, wa=wa, vb=vb, wb=wb)


def one_slot_terms(coefficients):
    magnitude, phases = np.abs(coefficients), np.angle(coefficients)
    for k in range(4):
        yield magnitude[k]**2, BELL_RESOURCES[k], BELL_RESOURCES[k], k, k
    for k in range(4):
        for ell in range(k + 1, 4):
            for axis, sign in ((1, 1), (1j, -1)):
                for s, t in itertools.product((-1, 1), repeat=2):
                    alice = (np.exp(1j * phases[k]) * BELL_RESOURCES[k]
                             + s * axis * np.exp(1j * phases[ell]) * BELL_RESOURCES[ell]) / np.sqrt(2)
                    bob = (BELL_RESOURCES[k] + t * axis * BELL_RESOURCES[ell]) / np.sqrt(2)
                    yield magnitude[k] * magnitude[ell] * sign * s * t / 2, alice, bob, k, ell


def direct_one_slot(data):
    reconstructed = np.zeros((16, 16), dtype=complex)
    without_pair_scores = np.zeros_like(reconstructed)
    count, extent, completeness_residual = 0, 0.0, 0.0
    for coefficient, alice, bob, k, ell in one_slot_terms(data["coefficients"]):
        local_a = [data["va"] @ corrected_kraus(alice, a) @ data["wa"] for a in range(4)]
        local_b = [data["vb"] @ corrected_kraus(bob, b) @ data["wb"] for b in range(4)]
        for kraus in (local_a, local_b):
            completeness_residual = max(completeness_residual, check_close(sum(op.conj().T @ op for op in kraus), np.eye(2)))
        for a, b in itertools.product(range(4), repeat=2):
            vector = choi_vector(np.kron(local_a[a], local_b[b]))
            branch = np.outer(vector, vector.conj())
            score = F[a, k] * F[a, ell] * F[b, k] * F[b, ell]
            reconstructed += coefficient * score * branch
            without_pair_scores += coefficient * branch
        count += 1
        extent += abs(coefficient)
    target = choi_from_kraus([data["gate"]])
    residual = check_close(reconstructed, target)
    check_close(np.trace(reconstructed), 1)
    expected_extent = 2 * np.sum(np.abs(data["coefficients"]))**2 - 1
    check_close(extent, expected_extent)
    omitted_score_error = float(np.max(np.abs(without_pair_scores - target)))
    assert omitted_score_error > 1e-3  # Ordinary local corrections alone fail here.
    return dict(physical_resource_terms=count, bell_records_per_term=16,
                local_instrument_completeness_max_residual=completeness_residual,
                extent=float(extent), choi_max_residual=residual,
                omitted_pair_score_max_error=omitted_score_error)


def two_slot_with_intervention(first, second):
    labels = list(itertools.product(range(4), repeat=2))
    weights = np.array([first["coefficients"][a] * second["coefficients"][b] for a, b in labels])
    magnitude, phases = np.abs(weights), np.angle(weights)
    damping = 0.27
    damping_kraus = [np.diag([1, np.sqrt(1 - damping)]),
                     np.array([[0, np.sqrt(damping)], [0, 0]])]
    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    intervention = [cnot @ np.kron(k, rotation(1, 0.197)) for k in damping_kraus]
    check_close(sum(k.conj().T @ k for k in intervention), np.eye(4))

    def paths(a, b):
        before = np.kron(first["alice"][a[0]], first["bob"][b[0]])
        after = np.kron(second["alice"][a[1]], second["bob"][b[1]])
        return np.array([choi_vector(after @ channel @ before) for channel in intervention])

    # Each row is one complete (a1,b1,a2,b2) Bell record.
    outcomes = np.array(list(itertools.product(range(4), repeat=4)))
    a_signs = np.array([F[outcomes[:, 0], k[0]] * F[outcomes[:, 2], k[1]] for k in labels]).T
    b_signs = np.array([F[outcomes[:, 1], k[0]] * F[outcomes[:, 3], k[1]] for k in labels]).T
    reconstructed = np.zeros((16, 16), dtype=complex)
    count, extent = 0, 0.0
    for i, k in enumerate(labels):
        vectors = paths(k, k)
        reconstructed += magnitude[i]**2 * np.einsum("ri,rj->ij", vectors, vectors.conj())
        extent += magnitude[i]**2
        count += 1
    for i, j in itertools.combinations(range(len(labels)), 2):
        k, ell = labels[i], labels[j]
        path_vectors = np.array([paths(a, b) for a, b in ((k, k), (k, ell), (ell, k), (ell, ell))])
        signs = np.array([a_signs[:, a] * b_signs[:, b]
                          for a, b in ((i, i), (i, j), (j, i), (j, j))]).T
        score = a_signs[:, i] * a_signs[:, j] * b_signs[:, i] * b_signs[:, j]
        assert np.all(np.abs(score) == 1)
        # Exact finite sum of Kraus products. Each branch has amplitude 4^-2,
        # so the density operator factor is 16^-2; probabilities remain in the
        # Kraus vectors and are never replaced by uniform outcome probabilities.
        record_sum = signs.T @ (score[:, None] * signs) / 16**2
        for axis, outer_sign in ((1, 1), (1j, -1)):
            for s, t in itertools.product((-1, 1), repeat=2):
                a_cat = np.array([np.exp(1j * phases[i]), s * axis * np.exp(1j * phases[j])]) / np.sqrt(2)
                b_cat = np.array([1, t * axis]) / np.sqrt(2)
                amplitudes = np.kron(a_cat, b_cat)
                coefficient = magnitude[i] * magnitude[j] * outer_sign * s * t / 2
                reconstructed += coefficient * np.einsum("ab,a,b,ari,brj->ij", record_sum,
                    amplitudes, amplitudes.conj(), path_vectors, path_vectors.conj())
                extent += abs(coefficient)
                count += 1
    target = choi_from_kraus([second["gate"] @ k @ first["gate"] for k in intervention])
    residual = check_close(reconstructed, target)
    check_close(np.trace(reconstructed), 1)
    expected_extent = 2 * np.sum(magnitude)**2 - 1
    check_close(extent, expected_extent)
    return dict(physical_resource_terms=count, bell_records_per_term=len(outcomes),
                intervention_kraus_operators=len(intervention), extent=float(extent),
                choi_max_residual=residual, choi_trace=float(np.trace(reconstructed).real),
                intervention="Alice amplitude damping 0.27, Bob X rotation 0.197, then CNOT")


def check_gates():
    first = gate_data((0.13, 0.21, -0.07), 0)
    second = gate_data((0.11, -0.19, 0.23), 1)
    return dict(local_teleportation=local_sign_checks(),
                non_clifford_one_gate=direct_one_slot(first),
                two_gate_causal_intervention=two_slot_with_intervention(first, second))


if __name__ == "__main__":
    print(json.dumps(check_gates(), indent=2, allow_nan=False))
