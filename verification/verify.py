#!/usr/bin/env python3
"""Finite checks for the stated memory-constrained circuit-cutting model.

Run from any directory with Python >= 3.10 and NumPy >= 1.26, < 3.
This is an algebra/state-vector verification suite, not a search for a proof.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np


SEED = 20261025
ATOL = 2e-11
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
BELL = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
PHI = np.outer(BELL, BELL.conj())


def projector(v):
    return np.outer(v, v.conj())


def ket(d, i):
    v = np.zeros(d, dtype=complex)
    v[i] = 1
    return v


def kron_all(values):
    out = np.array([1], dtype=complex)
    for value in values:
        out = np.kron(out, value)
    return out


def assert_close(a, b, tolerance=ATOL):
    error = float(np.max(np.abs(np.asarray(a) - np.asarray(b))))
    if error > tolerance:
        raise AssertionError(f"max residual {error:.4g} exceeds {tolerance:.4g}")
    return error


def random_ket(d, rng):
    v = rng.normal(size=d) + 1j * rng.normal(size=d)
    return v / np.linalg.norm(v)


def random_basis(d, rank, rng):
    matrix = rng.normal(size=(d, rank)) + 1j * rng.normal(size=(d, rank))
    return np.linalg.qr(matrix)[0][:, :rank]


def pure_edge_terms(s, left, right):
    """Product-state QPD of a pure Schmidt-correlated edge."""
    for i, value in enumerate(s):
        yield value**2, left[:, i], right[:, i]
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for phase, sign in ((1, 1), (1j, -1)):
                for a in (1, -1):
                    for b in (1, -1):
                        u = (left[:, i] + a * phase * left[:, j]) / np.sqrt(2)
                        v = (right[:, i] + b * phase * right[:, j]) / np.sqrt(2)
                        yield sign * a * b * s[i] * s[j] / 2, u, v


def edge_data(dl, dr, s, rng):
    s = np.asarray(s, dtype=float)
    s /= np.linalg.norm(s)
    left, right = random_basis(dl, len(s), rng), random_basis(dr, len(s), rng)
    omega = sum(np.kron(left[:, i], right[:, i]) for i in range(len(s)))
    psi = sum(s[i] * np.kron(left[:, i], right[:, i]) for i in range(len(s)))
    witness = 2 * projector(omega) - np.eye(dl * dr)
    reconstructed = np.zeros((dl * dr, dl * dr), dtype=complex)
    extent = 0.0
    for c, a, b in pure_edge_terms(s, left, right):
        reconstructed += c * projector(np.kron(a, b))
        extent += abs(c)
    g = 2 * np.sum(s)**2 - 1
    err = assert_close(reconstructed, projector(psi))
    assert_close(extent, g)
    assert_close(np.vdot(psi, witness @ psi), g)
    return dict(dl=dl, dr=dr, left=left, right=right, witness=witness,
                psi=psi, extent=float(g), residual=err)


def graph_product_vector(edges, data, vectors):
    """Convert grouped vertex registers to the ordered edge endpoint registers."""
    vertices = sorted({v for edge in edges for v in edge})
    labels, dimensions = [], []
    for vertex in vertices:
        for e, (left, right) in enumerate(edges):
            if vertex == left:
                labels.append((e, 0)); dimensions.append(data[e]["dl"])
            if vertex == right:
                labels.append((e, 1)); dimensions.append(data[e]["dr"])
    grouped = kron_all([vectors[v] for v in vertices]).reshape(dimensions)
    desired = [(e, side) for e in range(len(edges)) for side in (0, 1)]
    return grouped.transpose([labels.index(label) for label in desired]).reshape(-1)


def check_forests():
    rng = np.random.default_rng(SEED)
    # Rectangular endpoints and proper Schmidt supports exercise the leaf lemma.
    cases = [
        ("path_rectangular_support", [(0, 1), (1, 2)],
         [(3, 2, [1, 2]), (3, 2, [1])]),
        ("three_leaf_star", [(0, 1), (0, 2), (0, 3)],
         [(2, 2, [1, 1]), (2, 2, [1, 3]), (2, 2, [1, 2])]),
        ("disconnected", [(0, 1), (2, 3)],
         [(2, 3, [1, 2]), (2, 2, [1, 1])]),
    ]
    rows = []
    for name, edges, specifications in cases:
        data = [edge_data(*spec, rng) for spec in specifications]
        witness = kron_all([d["witness"] for d in data])
        dimensions, support_vectors = {}, {}
        for vertex in sorted({v for edge in edges for v in edge}):
            local_dims, local_supports = [], []
            for e, (left, right) in enumerate(edges):
                if vertex == left:
                    local_dims.append(data[e]["dl"])
                    local_supports.append(data[e]["left"][:, 0])
                if vertex == right:
                    local_dims.append(data[e]["dr"])
                    local_supports.append(data[e]["right"][:, 0])
            dimensions[vertex] = int(np.prod(local_dims))
            support_vectors[vertex] = kron_all(local_supports)
        largest = 0.0
        for _ in range(64):
            local = {v: random_ket(d, rng) for v, d in dimensions.items()}
            state = graph_product_vector(edges, data, local)
            value = np.vdot(state, witness @ state)
            assert abs(value.imag) < ATOL
            largest = max(largest, abs(float(value.real)))
        assert largest <= 1 + ATOL
        support = graph_product_vector(edges, data, support_vectors)
        assert_close(np.vdot(support, witness @ support), 1)
        target = kron_all([d["psi"] for d in data])
        target_value = float(np.prod([d["extent"] for d in data]))
        assert_close(np.vdot(target, witness @ target), target_value)
        rows.append(dict(case=name, seeded_vertex_products=64,
                         largest_absolute_value=largest, saturating_value=1.0,
                         target_value=target_value,
                         edge_identity_max_residual=max(d["residual"] for d in data)))
    # One full-rank qutrit edge also checks all three pair coherences.
    rank_three = edge_data(3, 4, [1, 2, 3], rng)
    # Four-cycle: each vertex has a local Bell pair. This violates the forest bound.
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    data = [dict(dl=2, dr=2)] * 4
    state = graph_product_vector(edges, data, {v: BELL for v in range(4)})
    witness = kron_all([4 * PHI - np.eye(4)] * 4)
    cycle_value = float(np.vdot(state, witness @ state).real)
    assert_close(cycle_value, 3)
    return dict(forests=rows, rank_three_rectangular_edge_residual=rank_three["residual"],
                four_cycle_local_bell_value=cycle_value)


def apply_one(state, unitary, axis):
    return np.moveaxis(np.tensordot(unitary, state, axes=(1, axis)), 0, axis)


def apply_cnot(state, control, target):
    out = np.empty_like(state)
    for index in np.ndindex(state.shape):
        source = list(index)
        source[target] ^= index[control]
        out[index] = state[tuple(source)]
    return out


def emit_cat_step(state, n, i, j, phase, step, memory, output):
    """Emit only the current bit; all later output ports remain fresh zeros."""
    ib = [(i >> (n - 1 - k)) & 1 for k in range(n)]
    jb = [(j >> (n - 1 - k)) & 1 for k in range(n)]
    differing = [k for k in range(n) if ib[k] != jb[k]]
    if differing:
        if step == differing[0]:
            state = apply_one(state, H, memory)
            state = apply_one(state, np.diag([1, phase]), memory)
        if step in differing:
            if step == differing[-1]:
                state = np.swapaxes(state, memory, output)
            else:
                state = apply_cnot(state, memory, output)
    if ib[step]:
        state = apply_one(state, X, output)
    return state


def wire_terms(n):
    d = 2**n
    for i in range(d):
        yield 1 / d, (i, i, 1), (i, i, 1)
    for i in range(d):
        for j in range(i + 1, d):
            for phase, sign in ((1, 1), (1j, -1)):
                for a in (1, -1):
                    for b in (1, -1):
                        yield sign * a * b / (2 * d), (i, j, a * phase), (i, j, b * phase)


def cat_vector(n, specification):
    i, j, phase = specification
    return ket(2**n, i) if i == j else (ket(2**n, i) + phase * ket(2**n, j)) / np.sqrt(2)


def bell_contract(state, first, second, a, b):
    bell = apply_one(BELL.reshape(2, 2), np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b), 1)
    return np.tensordot(bell.conj(), state, axes=((0, 1), (first, second)))


def online_two_slot_atom(source, target):
    # Registers: R,A1,A2,MA,MB,S1,T1,S2,T2. Future ports are fresh placeholders.
    initial = np.kron(BELL, ket(128, 0)).reshape((2,) * 9)
    state = emit_cat_step(initial, 2, *source, 0, 3, 5)
    state = emit_cat_step(state, 2, *target, 0, 4, 6)
    theta = np.sqrt(2) / 5
    rx = np.cos(theta / 2) * I - 1j * np.sin(theta / 2) * X
    out = np.zeros((8, 8), dtype=complex)
    memory_error = 0.0
    for a in (0, 1):
        for b in (0, 1):
            first = bell_contract(state, 1, 5, a, b)  # R,A2,MA,MB,T1,S2,T2
            first = apply_one(first, np.linalg.matrix_power(Z, b) @ np.linalg.matrix_power(X, a), 4)
            # External tester uses the released first output to prepare the second input.
            first = apply_cnot(first, 4, 1)
            first = apply_one(first, rx, 1)
            first = emit_cat_step(first, 2, *source, 1, 2, 5)
            first = emit_cat_step(first, 2, *target, 1, 3, 6)
            for c in (0, 1):
                for d in (0, 1):
                    last = bell_contract(first, 1, 5, c, d)  # R,MA,MB,T1,T2
                    last = apply_one(last, np.linalg.matrix_power(Z, d) @ np.linalg.matrix_power(X, c), 4)
                    memory_error = max(memory_error, float(np.linalg.norm(last[:, 1, :, :, :])),
                                       float(np.linalg.norm(last[:, :, 1, :, :])))
                    vector = last[:, 0, 0, :, :].reshape(-1)
                    out += projector(vector)
    assert_close(np.trace(out), 1)
    assert memory_error < ATOL
    return out, memory_error


def check_streaming():
    rows = []
    for n in range(1, 5):
        d = 2**n
        target = sum(np.kron(ket(d, i), ket(d, i)) for i in range(d)) / np.sqrt(d)
        rho = np.zeros((d * d, d * d), dtype=complex)
        extent, number = 0.0, 0
        for c, a, b in wire_terms(n):
            rho += c * projector(np.kron(cat_vector(n, a), cat_vector(n, b)))
            extent += abs(c); number += 1
        error = assert_close(rho, projector(target))
        assert_close(extent, 2 * d - 1)
        cat_error, memory_error, count = 0.0, 0.0, 0
        for i in range(d):
            for j in range(i + 1, d):
                for phase in (1, -1, 1j, -1j):
                    state = ket(2**(n + 1), 0).reshape((2,) * (n + 1))
                    for step in range(n):
                        state = emit_cat_step(state, n, i, j, phase, step, n, step)
                    cat_error = max(cat_error, assert_close(state[..., 0].reshape(-1), cat_vector(n, (i, j, phase))))
                    memory_error = max(memory_error, float(np.linalg.norm(state[..., 1])))
                    count += 1
        assert memory_error < ATOL
        rows.append(dict(qubits=n, resource_terms=number, extent=extent,
                         resource_max_residual=error, cats=count,
                         cat_max_residual=cat_error, memory_one_amplitude=memory_error))
    output = np.zeros((8, 8), dtype=complex)
    memory_error = 0.0
    for c, a, b in wire_terms(2):
        atom, error = online_two_slot_atom(a, b)
        output += c * atom
        memory_error = max(memory_error, error)
    ideal = np.kron(BELL, ket(2, 0)).reshape(2, 2, 2)
    ideal = apply_cnot(ideal, 1, 2)
    theta = np.sqrt(2) / 5
    ideal = apply_one(ideal, np.cos(theta / 2) * I - 1j * np.sin(theta / 2) * X, 2)
    error = assert_close(output, projector(ideal.reshape(-1)))
    return dict(resource_and_cat_checks=rows,
                causal_two_slot_tester=dict(resource_atoms=52, teleportation_branches_per_atom=16,
                    output_max_residual=error, final_memory_one_amplitude=memory_error,
                    output_trace=float(np.trace(output).real)))


def temporal_resource(eta):
    rho = np.zeros((4, 4), dtype=complex)
    rho[0, 0] = rho[3, 3] = 0.5
    rho[0, 3] = rho[3, 0] = eta / 2
    return rho


def spatial_order(rho):
    return rho.reshape((2,) * 8).transpose(0, 2, 1, 3, 4, 6, 5, 7).reshape(16, 16)


def isotropic_twirl(rho):
    out = np.zeros((16, 16), dtype=complex)
    for a in (PHI, np.eye(4) - PHI):
        for b in (PHI, np.eye(4) - PHI):
            p = np.kron(a, b)
            out += np.trace(p @ rho) * p / np.trace(p)
    return out


def concurrence_roofs(rho):
    values, basis = np.linalg.eigh((rho + rho.conj().T) / 2)
    root = (basis * np.sqrt(np.maximum(values, 0))) @ basis.conj().T
    flip = np.kron(Y, Y) @ rho.conj() @ np.kron(Y, Y)
    middle = root @ flip @ root
    roots = np.sqrt(np.maximum(np.linalg.eigvalsh((middle + middle.conj().T) / 2), 0))
    roots = np.sort(roots)[::-1]
    return max(0.0, float(roots[0] - np.sum(roots[1:]))), float(np.sum(roots))


def filtered_resources(eta, rng):
    filters = [(I, I), (np.diag([1, 0]), I), (I, np.diag([0, 1])),
               (np.diag([1, 1e-8]), H), (H, np.diag([1e-8, 1]))]
    for _ in range(40):
        a = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        b = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        filters.append((a / np.linalg.norm(a, 2), b / np.linalg.norm(b, 2)))
    states, largest_roof_residual = [], 0.0
    for a, b in filters:
        operation = np.kron(a, b)
        state = operation @ temporal_resource(eta) @ operation.conj().T
        probability = float(np.trace(state).real)
        assert probability > 0
        state /= probability
        c, ca = concurrence_roofs(state)
        largest_roof_residual = max(largest_roof_residual, c - eta * ca)
        # Eigenvalue square roots at rank-deficient states lose several digits.
        assert c <= eta * ca + 2e-7
        states.append(state)
    return states, largest_roof_residual


def check_noisy_memory():
    rng = np.random.default_rng(SEED + 1)
    complement = np.eye(4) - PHI
    plus, minus = PHI / 2 + complement / 6, complement / 3
    w = 4 * PHI - np.eye(4)
    w1, w2 = np.kron(w, np.eye(4)), np.kron(np.eye(4), w)
    target = np.kron(PHI, PHI)
    rows = []
    for eta_a, eta_b in ((0, 0), (0, 1), (0.1, 0.8), (0.4, 0.7), (0.99, 0.99), (1, 1)):
        r = eta_a * eta_b
        e = isotropic_twirl(spatial_order(np.kron(temporal_resource(eta_a), temporal_resource(eta_b))))
        atoms = [np.kron(plus, plus), np.kron(plus, minus), np.kron(minus, plus), e]
        coefficients = [3, -(2 + r) / (1 + r), -(2 + r) / (1 + r), 2 / (1 + r)]
        gamma = 5 + 4 / (1 + r)
        reconstructed = sum(c * a for c, a in zip(coefficients, atoms))
        error = assert_close(reconstructed, target)
        assert_close(sum(coefficients), 1)
        assert_close(sum(abs(c) for c in coefficients), gamma)
        dual = (w1 @ w2 + r * (w1 + w2 - np.eye(16))) / (1 + r)
        assert_close(np.trace(dual @ target), gamma)
        atom_values = [float(np.trace(dual @ atom).real) for atom in atoms]
        assert_close(atom_values, [1, -1, -1, 1])
        a_states, a_residual = filtered_resources(eta_a, rng)
        b_states, b_residual = filtered_resources(eta_b, rng)
        minimum, maximum = float("inf"), -float("inf")
        for a in a_states:
            for b in b_states:
                value = float(np.trace(dual @ spatial_order(np.kron(a, b))).real)
                minimum, maximum = min(minimum, value), max(maximum, value)
        assert minimum >= -1 - ATOL and maximum <= 1 + ATOL
        # Both signs of the universal bound are attained by elementary cases.
        assert_close(np.trace(dual @ spatial_order(np.kron(projector(ket(4, 0)), projector(ket(4, 1))))), -1)
        assert_close(np.trace(dual @ spatial_order(np.kron(temporal_resource(eta_a), temporal_resource(eta_b)))), 1)
        rows.append(dict(eta_a=eta_a, eta_b=eta_b, gamma=gamma,
                         resource_identity_max_residual=error, atom_dual_values=atom_values,
                         local_filters_per_side=len(a_states), filter_pairs=len(a_states) * len(b_states),
                         filter_dual_minimum=minimum, filter_dual_maximum=maximum,
                         concurrence_inequality_max_positive_residual=max(a_residual, b_residual)))
    # If a dephasing flag were given away, conditional local Bell factors would be
    # allowed even at eta=0. They have value 3, contradicting the unflagged bound.
    flagged = float(np.trace((w1 @ w2) @ spatial_order(np.kron(PHI, PHI))).real)
    assert_close(flagged, 3)
    return dict(parameter_checks=rows, flagged_noise_counterexample_dual_value=flagged)


def common_intervals(n, mask_a, mask_b):
    epochs = [0, 0]
    intervals = []
    for slot in range(n):
        if slot:
            epochs[0] += bool(mask_a & (1 << (slot - 1)))
            epochs[1] += bool(mask_b & (1 << (slot - 1)))
        endpoints = (("A", epochs[0]), ("B", epochs[1]))
        if intervals and intervals[-1][0] == endpoints:
            intervals[-1][1] += 1
        else:
            intervals.append([endpoints, 1])
    return intervals


def check_schedules():
    count = 0
    for n in range(1, 7):
        for mask_a in range(1 << (n - 1)):
            for mask_b in range(1 << (n - 1)):
                intervals = common_intervals(n, mask_a, mask_b)
                parent = {}

                def root(vertex):
                    parent.setdefault(vertex, vertex)
                    while parent[vertex] != vertex:
                        vertex = parent[vertex]
                    return vertex

                for (a, b), _ in intervals:
                    a_root, b_root = root(a), root(b)
                    assert a_root != b_root  # Adding this edge never makes a cycle.
                    parent[a_root] = b_root
                assert sum(length for _, length in intervals) == n
                assert len(intervals) == (mask_a | mask_b).bit_count() + 1
                count += 1

    def cost(n, a, b):
        return int(np.prod([2 * 2**length - 1 for _, length in common_intervals(n, a, b)]))

    costs = dict(no_breaks_six_qubits=cost(6, 0, 0),
                 aligned_lengths_3_3=cost(6, 1 << 2, 1 << 2),
                 asynchronous_lengths_2_1_2_1=cost(6, 1 << 2, (1 << 1) | (1 << 4)),
                 every_gap=cost(6, 31, 31))
    assert costs == dict(no_breaks_six_qubits=127, aligned_lengths_3_3=225,
                         asynchronous_lengths_2_1_2_1=441, every_gap=729)
    return dict(exhaustive_partition_pairs_through_six_slots=count, six_qubit_examples=costs)


def check_precision():
    rows = []
    for dimensions in ([2], [2, 2], [3, 2], [4], [2, 2, 2]):
        phis, witnesses = [], []
        for d in dimensions:
            bell = sum(np.kron(ket(d, i), ket(d, i)) for i in range(d)) / np.sqrt(d)
            phis.append(projector(bell))
            witnesses.append(2 * d * projector(bell) - np.eye(d * d))
        witness, target = kron_all(witnesses), kron_all(phis)
        values, basis = np.linalg.eigh(witness)
        g = int(np.prod([2 * d - 1 for d in dimensions]))
        c_min = min(2 * d - 1 for d in dimensions)
        assert_close(values[-1], g)
        assert_close(values[0], -g / c_min)
        epsilon = 0.125
        perturbed = (1 - epsilon) * target + epsilon * projector(basis[:, 0])
        distance = float(np.sum(np.abs(np.linalg.eigvalsh(perturbed - target))) / 2)
        assert_close(distance, epsilon)
        expected = g * (1 - (1 + 1 / c_min) * epsilon)
        assert_close(np.trace(witness @ perturbed), expected)
        rows.append(dict(interval_dimensions=dimensions, target_value=g,
                         minimum_eigenvalue=float(values[0]), epsilon=epsilon,
                         half_trace_distance=distance, calibrated_witness_value=expected))
    return dict(spectral_checks=rows)


def check_calibration():
    complement = np.eye(4) - PHI
    plus, minus = PHI / 2 + complement / 6, complement / 3
    vpp, vpm, vmp = np.kron(plus, plus), np.kron(plus, minus), np.kron(minus, plus)
    w = 4 * PHI - np.eye(4)
    w1, w2 = np.kron(w, np.eye(4)), np.kron(np.eye(4), w)
    target = np.kron(PHI, PHI)
    rows = []
    for actual, nominal in ((0, 1), (1, 0), (0.28, 0.5), (0.9801, 0.8), (0.8, 0.8)):
        resource = isotropic_twirl(spatial_order(np.kron(temporal_resource(actual), temporal_resource(1))))
        a0, b0 = (2 + nominal) / (1 + nominal), 2 / (1 + nominal)
        reconstructed = 3 * vpp - a0 * (vpm + vmp) + b0 * resource
        mismatch = (actual - nominal) / (1 + nominal)
        residual = assert_close(reconstructed - target, mismatch * (w1 @ w2) / 36)
        expected = np.array([1 + mismatch / 4] + [-mismatch / 12] * 6 + [mismatch / 36] * 9)
        eigenvalues = np.linalg.eigvalsh(reconstructed)
        assert_close(eigenvalues, np.sort(expected))
        assert_close(np.trace(reconstructed), 1)
        full_trace_error = float(np.sum(np.abs(np.linalg.eigvalsh(reconstructed - target))))
        assert_close(full_trace_error, abs(mismatch))
        if mismatch:
            assert eigenvalues[0] < 0
        dual = (w1 @ w2 + actual * (w1 + w2 - np.eye(16))) / (1 + actual)
        expected_dual = [(9 + 5 * actual) / (1 + actual)]
        expected_dual += [(actual - 3) / (1 + actual)] * 6
        expected_dual += [(1 - 3 * actual) / (1 + actual)] * 9
        assert_close(np.linalg.eigvalsh(dual), np.sort(expected_dual))
        rows.append(dict(actual_r=actual, nominal_r=nominal, mismatch=mismatch,
                         signed_identity_max_residual=residual,
                         minimum_reconstructed_eigenvalue=float(eigenvalues[0]),
                         full_trace_error=full_trace_error))
    blocks = []
    for mismatches in ((0.2,) * 4, (-0.3,) * 4, (-0.5, 0.1, 1 / 7, -0.25)):
        coefficients = np.array([1.0])
        identity, absolute_sum = 1.0, 1.0
        for d in mismatches:
            block = np.array([1 + d / 4] + [-d / 12] * 6 + [d / 36] * 9)
            coefficients = np.kron(coefficients, block)
            identity *= 1 + d / 4
            absolute_sum *= 1 + d / 4 + 3 * abs(d) / 4
        assert_close(np.sum(coefficients), 1)
        coefficients[0] -= 1
        error = float(np.sum(np.abs(coefficients)))
        expected = abs(identity - 1) + absolute_sum - identity
        assert_close(error, expected)
        upper = float(np.prod([1 + abs(d) for d in mismatches]) - 1)
        assert error <= upper + ATOL
        if all(d == mismatches[0] for d in mismatches):
            d, m = mismatches[0], len(mismatches)
            closed = (1 + d)**m - 1 if d >= 0 else (1 + abs(d) / 2)**m + 1 - 2 * (1 - abs(d) / 4)**m
            assert_close(error, closed)
        blocks.append(dict(mismatches=mismatches, enumerated_pauli_paths=len(coefficients),
                           exact_coefficient_error=error, product_upper_bound=upper))
    return dict(single_blocks=rows, repeated_blocks=blocks)


def main():
    from gate_checks import check_gates

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the deterministic report to this JSON file.")
    args = parser.parse_args()
    report = dict(status="PASS", seed=SEED,
                  runtime=dict(python=platform.python_version(), numpy=np.__version__),
                  forests=check_forests(), streaming=check_streaming(),
                  noisy_memory=check_noisy_memory(), schedules=check_schedules(),
                  precision=check_precision(), calibration=check_calibration(),
                  gates=check_gates())
    encoded = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
