# Focused verification

This directory contains finite matrix and state-vector checks of the identities and model boundaries used in the scientific notes. The analytical arguments in `../science/` establish the general results. Passing this suite does not prove an optimization over every adaptive LOCC protocol.

## Reproduce

Use Python 3.10 or later and NumPy `>=1.26,<3`. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py --output verification/results.json
```

The checked-in report was generated with **Python 3.12.14 and NumPy 2.3.5**. There is no network access, optimization solver, or optional plotting dependency in the checks. The random seed is **20261025** (and seed + 1 for local filter examples). Random inputs are reproducible coverage of specified finite cases, not an optimization or a proof by sampling. Last floating-point digits can vary with NumPy and the linear algebra backend; compare the assertions and tolerances, not JSON byte equality. Run ordinary Python, without the `-O` option that disables assertions.

## What is checked

| Check | Finite coverage | Expected outcome |
|---|---|---|
| Pure-edge resource identity | Schmidt ranks 1, 2, and 3; rectangular endpoint dimensions; nontrivial local bases | Product-state expansion reconstructs the edge state with extent `2 (sum s_i)^2 - 1` |
| Forest witness | A path, a three-leaf star, and a disconnected forest; 64 seeded product-over-vertex states each; explicit saturating states | Absolute witness expectation at most 1 in the tested cases; the target gives the product of edge extents |
| Forest boundary | A four-cycle with a Bell state at every vertex | Witness value **3**, demonstrating that the proposed bound cannot be extended to cycles unchanged |
| Epoch overlap graph | All **1,365** pairs of partitions for one through six slots | Every overlap graph is acyclic; common intervals are exactly the union of the two sets of boundaries |
| Wire resource QPD | All terms for one through four qubits: 10, 52, 232, 976 terms | Extents **3, 7, 15, 31**; complete density matrices agree |
| Sequential cat generation | All unordered two-string pairs and four phases for one through four qubits: 4, 24, 112, 480 cats | Correct state and zero amplitude for memory state `1` |
| Causal two-slot tester | All 52 resource atoms and all 16 teleportation-outcome branches per atom | Full output state agrees with ideal wires; both local memories end in `0` in every branch |
| Noisy two-slot identity and dual | Six pairs of dephasing parameters, including both endpoints | Exact resource identity, coefficient sum 1, extent `5 + 4/(1 + eta_A eta_B)`, and atom witness values `[1,-1,-1,1]` |
| Noisy local-filter cases | 45 filters per side for each parameter pair, hence **12,150** filter pairs; identity, singular, nearly singular, and seeded complex filters | Tested normalized local states satisfy `C <= eta C_a`; tested product states obey the dual bound |
| Noise-access boundary | Conditional local Bell states at complete dephasing, as could be available with an accessible error flag | The unflagged-noise witness has value **3**; environmental information changes the admissible resource set |
| Precision calibration | Five small products of interval witnesses | Largest eigenvalue `G`, smallest `-G/c_min`, and the claimed trace-distance spectral calibration |
| Actual versus nominal dephasing | Five pairs of actual and nominal product parameters, including both extreme mismatch signs and exact calibration | Signed reconstruction error `d W_1 W_2 / 36`, correct eigenvalues, trace one, full Choi trace error `|d|`, and a negative eigenvalue at every tested nonzero mismatch |
| Repeated miscalibrated blocks | Three four-block examples; all 65,536 Pauli paths in each, with positive, negative, and mixed mismatches | Exact coefficient error `|P-1| + L-P`, the two equal-parameter formulas, and the product upper bound |
| Gate Bell conventions and signs | All 16 Pauli/Bell Kraus cases; all 256 resource/input matrix-unit cases | The conjugated Bell convention gives corrected Kraus operator `f(a,k) sigma_k / 2` and the stated matrix-unit sign |
| Physical one-gate reconstruction | A generic rank-four non-Clifford KAK core with noncommuting local outer rotations; all 52 resource terms and 16 Bell records per term | Correct normalized gate Choi matrix and extent **2.77618736868338**; every underlying local instrument is complete |
| Two-gate causal intervention | Two distinct rank-four KAK cores, with local outer rotations; amplitude damping, a rotation, and CNOT between the slots; 976 resource terms and 256 Bell records per term | Correct normalized composite Choi matrix and extent **7.17756908581050** |

The causal tester is stronger than preparing an entire resource state and only checking it at the end. It emits the first local resource qubits, completes first-slot teleportation, lets the external tester entangle the released output with a newly prepared second input and rotate that input, then emits the second resource qubits and completes second-slot teleportation. Future ports are represented as untouched zero placeholders until their release time. A retained reference is entangled with the first input. The full final density matrix is compared, including the reference. This checks one nontrivial adaptive composition and the memory cleanup under its measurement back-action; it does not replace the general comb identity.

The gate checks are also available separately:

```bash
python verification/gate_checks.py
```

They inspect the pair-dependent scoring in [Gate cuts](../science/gate-cuts.md). The one-gate calculation directly contracts each physical Bell vector and sums the weighted Kraus Choi matrices. It verifies all local instrument completeness relations. Omitting the pair score produces a maximum matrix error of approximately **0.0762**, so the example tests the non-Clifford correction rather than a case where ordinary local teleportation corrections suffice. For two slots, each physical cat product has four coherent Pauli-path alternatives. The code sums the signs over all 256 Bell records into a four-by-four matrix and then forms the complete Choi sum. The factor `16^-2` comes from squared Kraus amplitudes; outcome probabilities remain in the Kraus operators and are never replaced by uniform probabilities. An inaccessible reference is included by comparing normalized Choi matrices. This is one specified interslot tester, not a numerical proof for every causal tester.

## Numerical accuracy and limitations

The algebra and state-vector assertions use absolute tolerance `2e-11`. In the recorded run, wire and noisy-memory resource reconstruction residuals are below `4e-16`; the gate reconstruction residuals are below `2e-15`. The tested final wire-memory-one amplitudes are exactly zero in floating-point arithmetic. The two-qubit concurrence formulas involve square roots of near-zero eigenvalues; their inequality uses tolerance `2e-7` for singular and nearly singular filters. The recorded maximum positive residual is below `3e-9`. That separate tolerance is not used for the resource identities or the direct witness bounds.

The spectral calibration constructs density matrices that attain the trace-norm dual bound. These matrices are not claimed to be valid approximate causal combs; the check establishes the constants in the spectral estimate, not attainability of the operational approximation tradeoff.

The miscalibration checks deliberately allow the reconstructed signed operator to have negative eigenvalues. They therefore test the algebra behind the error estimate without treating that reconstruction as a physical channel. Enumerating Pauli coefficient paths checks the proposed norm formula numerically; the analytical Bell-probe and triangle-inequality arguments are still needed to identify that coefficient norm with the strategy norm for every causal tester. No statistical calibration experiment is simulated, and the suite does not establish the assumptions of stationarity or independent unflagged noise from measured data.

The suite does not establish universal protocol optimality, exact multiplicativity for more than two noisy slots, a general lower bound on measurement counts, or the applicability of the model to hardware with additional coherent storage or accessible noise environments. It does not simulate laboratory noise outside the specified dephasing channels. Those distinctions are part of the model and the scope of the theorems.
