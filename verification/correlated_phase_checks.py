#!/usr/bin/env python3
"""Finite contractions for the q=5 correlated-phase-memory theorem.

The physical branch vectors are computed before any sector formula is used.
The twirl is evaluated by its four orthogonal sector projectors rather than
enumerating Clifford group elements. Universal optimality and timing follow
from the analytical witness and streaming argument in the scientific note.
"""

import argparse
import json
from pathlib import Path
import sys

import numpy as np


Q = 5
TOL = 2e-11
OMEGA = np.exp(2j * np.pi / Q)
BASIS = np.eye(Q, dtype=complex)
PHI_VECTOR = np.eye(Q).reshape(-1) / np.sqrt(Q)
PHI = np.outer(PHI_VECTOR, PHI_VECTOR)
R = (np.eye(Q * Q) - PHI) / (Q * Q - 1)
TARGET_VECTOR = np.kron(PHI_VECTOR, PHI_VECTOR)
TARGET = np.outer(TARGET_VECTOR, TARGET_VECTOR)
SECTORS = [np.kron(PHI, PHI), np.kron(PHI, R),
           np.kron(R, PHI), np.kron(R, R)]
PROJECTORS = [np.kron(PHI, PHI), np.kron(PHI, np.eye(25) - PHI),
              np.kron(np.eye(25) - PHI, PHI),
              np.kron(np.eye(25) - PHI, np.eye(25) - PHI)]


def max_error(left, right):
    return float(np.max(np.abs(np.asarray(left) - np.asarray(right))))


def record(checks, name, error, **details):
    value = float(error)
    checks.append({"name": name, "passed": bool(np.isfinite(value) and value <= TOL),
                   "maximum_absolute_error": value, "tolerance": TOL, **details})


def phase(x):
    return np.diag(OMEGA ** (x * np.arange(Q)))


def spatial_vector(alice, bob):
    """Temporal coefficient matrices a1,a2 and b1,b2 -> a1,b1,a2,b2."""
    return np.einsum("ac,bd->abcd", alice, bob).reshape(-1)


def sector_coefficients(operator):
    return np.array([np.einsum("ij,ji->", p, operator).real for p in PROJECTORS])


def twirl(operator):
    coefficients = sector_coefficients(operator)
    return sum(c * s for c, s in zip(coefficients, SECTORS)), coefficients


def parity_resources(checks):
    symmetric = [(BASIS[:, j] + BASIS[:, -j]) / np.sqrt(2) for j in (1, 2)]
    antisymmetric = [(BASIS[:, j] - BASIS[:, -j]) / np.sqrt(2) for j in (1, 2)]
    even = (np.outer(BASIS[:, 0], BASIS[:, 0])
            + np.outer(BASIS[:, 1], symmetric[0])
            + np.outer(BASIS[:, 2], symmetric[1]))
    odd = (np.outer(BASIS[:, 2], antisymmetric[0])
           + np.outer(BASIS[:, 1], antisymmetric[1]))
    decoders = [even, odd]
    record(checks, "complete parity instrument",
           max_error(sum(k.conj().T @ k for k in decoders), np.eye(Q)))
    preparation = (np.outer(BASIS[:, 1], symmetric[0])
                   + np.outer(BASIS[:, 2], symmetric[1])) / np.sqrt(2)
    record(checks, "normalized temporal preparation", abs(np.vdot(preparation, preparation) - 1))
    raw = {}
    branches = {}
    for law in ("linear", "cubic"):
        operator = np.zeros((Q ** 4, Q ** 4), dtype=complex)
        positive_probability = 0.0
        total_probability = 0.0
        saturation_error = 0.0
        branches[law] = []
        for x in range(Q):
            y = x if law == "linear" else x ** 3 % Q
            for a, ka in enumerate(decoders):
                left = preparation @ phase(x).T @ ka.T
                for b, kb in enumerate(decoders):
                    right = preparation @ phase(y).T @ kb.T
                    vector = spatial_vector(left, right)
                    density = np.outer(vector, vector.conj()) / Q
                    branches[law].append(density)
                    score = 1 if a == b else -1
                    probability = np.vdot(vector, vector).real / Q
                    operator += score * density
                    total_probability += probability
                    if score == 1:
                        positive_probability += probability
                    witness = (50 * abs(np.vdot(TARGET_VECTOR, vector)) ** 2
                               - np.vdot(vector, vector).real) / Q
                    saturation_error = max(saturation_error, abs(witness - score * probability))
        raw[law] = operator
        record(checks, f"{law}: complete physical branch probabilities", abs(total_probability - 1),
               branch_count=Q * 4)
        record(checks, f"{law}: equal-parity physical probability", abs(positive_probability - 5 / 8),
               observed=float(positive_probability), expected=5 / 8)
        record(checks, f"{law}: branch witness saturation", saturation_error)
        expected = np.array([1 / 40, 1 / 40, 0, 1 / 5])
        record(checks, f"{law}: contracted four-sector coefficients",
               max_error(sector_coefficients(operator), expected), expected=expected.tolist())
    record(checks, "linear and cubic: every unscored decoder branch agrees",
           max(max_error(a, b) for a, b in zip(branches["linear"], branches["cubic"])),
           branch_count=20)
    record(checks, "linear and cubic: raw signed operators agree",
           max_error(raw["linear"], raw["cubic"]))
    return raw


def deterministic_resources(checks):
    baseline = np.zeros((625, 625), dtype=complex)
    linear = np.zeros_like(baseline)
    kappa = sum(OMEGA ** ((x + 3 * x ** 3) % Q) for x in range(Q)) / Q
    record(checks, "direct proposed upper: cubic phase average", abs(kappa - 1 / np.sqrt(5)))
    for x in range(Q):
        alice = (np.outer(BASIS[:, 0], BASIS[:, 0])
                 + OMEGA ** x * np.outer(BASIS[:, 1], BASIS[:, 1])) / np.sqrt(2)
        bob = (np.outer(BASIS[:, 0], BASIS[:, 0])
               + OMEGA ** ((3 * x ** 3) % Q) * np.outer(BASIS[:, 1], BASIS[:, 1])) / np.sqrt(2)
        vector = spatial_vector(alice, bob)
        baseline += np.outer(vector, vector.conj()) / Q
        alice = np.diag(OMEGA ** (x * np.arange(Q))) / np.sqrt(Q)
        bob = np.diag(OMEGA ** (-x * np.arange(Q))) / np.sqrt(Q)
        vector = spatial_vector(alice, bob)
        linear += np.outer(vector, vector.conj()) / Q
    expected = np.array([1 + kappa.real, 4 - kappa.real, 4 - kappa.real, 41 + kappa.real]) / 50
    record(checks, "direct proposed upper: contracted sectors",
           max_error(sector_coefficients(baseline), expected), expected=expected.tolist())
    record(checks, "direct linear resource: contracted sectors",
           max_error(sector_coefficients(linear), [1 / 25, 0, 0, 24 / 25]))
    return twirl(baseline)[0], twirl(linear)[0]


def teleportation_checks(checks):
    """Contract each physical Bell bra, including all resource/error labels."""
    shift = np.roll(np.eye(Q), 1, axis=0)
    clock = phase(1)
    maximum = 0.0
    completeness = 0.0
    for u in range(Q):
        for v in range(Q):
            error = np.linalg.matrix_power(shift, u) @ np.linalg.matrix_power(clock, v)
            resource = np.eye(Q) @ error.T / np.sqrt(Q)
            ideal_vector = error.T.reshape(-1) / (Q * np.sqrt(Q))
            ideal_density = np.outer(ideal_vector, ideal_vector.conj())
            normalization = np.zeros((Q, Q), dtype=complex)
            for a in range(Q):
                for b in range(Q):
                    bell = np.eye(Q) @ (np.linalg.matrix_power(shift, a)
                                        @ np.linalg.matrix_power(clock, b)).T / np.sqrt(Q)
                    uncorrected = (bell.conj() @ resource).T
                    correction = (np.linalg.matrix_power(shift, a)
                                  @ np.linalg.matrix_power(clock, -b)).conj().T
                    kraus = correction @ uncorrected
                    choi_vector = kraus.T.reshape(-1) / np.sqrt(Q)
                    maximum = max(maximum, max_error(np.outer(choi_vector, choi_vector.conj()), ideal_density))
                    normalization += kraus.conj().T @ kraus
            completeness = max(completeness, max_error(normalization, np.eye(Q)))
    record(checks, "qudit teleportation: all corrected Bell Kraus Choi matrices", maximum,
           resource_labels=25, measurement_outcomes_per_label=25)
    record(checks, "qudit teleportation: complete Bell instruments", completeness)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional JSON result path")
    args = parser.parse_args()
    checks = []
    raw = parity_resources(checks)
    baseline, linear = deterministic_resources(checks)
    rho_plus = (PHI + 4 * R) / 5
    vpp, vpm, vmp = np.kron(rho_plus, rho_plus), np.kron(rho_plus, R), np.kron(R, rho_plus)
    for law, resource in raw.items():
        scored, _ = twirl(resource)
        reconstructed = 5 * vpp + 32 * scored - 8 * vpm - 4 * vmp
        record(checks, f"{law}: full 625 by 625 extent-49 identity", max_error(reconstructed, TARGET),
               coefficient_extent=49, signed_atom_trace=float(np.trace(scored).real))
    kappa = 1 / np.sqrt(5)
    coefficient = 32 / (1 + kappa)
    reconstructed = 9 * vpp - (4 + coefficient / 2) * (vpm + vmp) + coefficient * baseline
    record(checks, "direct proposed upper: full 625 by 625 identity", max_error(reconstructed, TARGET),
           coefficient_extent=float(97 - 16 * np.sqrt(5)))
    reconstructed = 15 * vpp + 10 * linear - 12 * (vpm + vmp)
    record(checks, "direct linear resource: full 625 by 625 extent-49 identity",
           max_error(reconstructed, TARGET), coefficient_extent=49)
    teleportation_checks(checks)
    report = {"passed": all(c["passed"] for c in checks), "dimension": Q,
              "numpy_version": np.__version__, "checks": checks,
              "scope": "Finite branch, completeness, resource identity and teleportation checks; the analytical witness proves universal optimality and closure."}
    output = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    print(output, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
