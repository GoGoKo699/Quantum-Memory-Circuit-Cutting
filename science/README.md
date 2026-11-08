# Scientific reading map

The scientific account is organized by the question each page answers. The [operational model](model.md) fixes the meaning of every theorem: open causal slots, prescribed input and output availability, charged quantum storage, and complete physical instruments carrying bounded classical scores.

## A route through the results

| Page | Main question and result | Dependencies |
|---|---|---|
| [Causal model](model.md) | What is being simulated, which resources are allowed, and what does signed extent measure? | Quantum channels, instruments and normalized Choi operators |
| [Forest witness](forest-witness.md) | When can pure-edge entanglement witnesses be multiplied despite joint states at graph vertices? A leaf-contraction argument proves the exact pure-edge extent on forests. | Schmidt decomposition and trace-norm duality |
| [Reset schedules](reset-schedules.md) | How do two different local reset schedules determine the optimum? Their common refinement gives the exact wire product law. | Causal model, forest witness |
| [Wire construction](wire-construction.md) | How is each collective wire factor attained online with one persistent qubit at each side? Two-string resources are emitted sequentially and consumed by teleportation. | Pure-edge decomposition, teleportation |
| [Gate cuts](gate-cuts.md) | How does the reset law extend to arbitrary two-qubit unitaries? KAK coefficients set each interval factor; pair-dependent bounded scores resolve the teleportation signs. | Forest witness, reset factorization, operator Schmidt decomposition |
| [Dephasing memory](dephasing-memory.md) | What is the exact value of two independent, unflagged noisy memory qubits? A physical four-resource construction and a temporal-concurrence witness match. | Causal model, two-qubit states, teleportation |
| [Correlated phase memory](correlated-phase-memory.md) | Do the linear and cubic joint $`q=5`$ phase channels have different two-wire costs? Both attain extent 49 through a complete parity instrument, matching the spatial witness. | Causal model, scored instruments, spatial separability, teleportation |
| [Precision and calibration](precision-calibration.md) | What survives approximation, and what bias arises from imperfect calibration? Witness spectra, exact Pauli-path errors and charged statistical procedures give separate answers. | Reset and noisy-memory witnesses |
| [Resource interpretation](resource-interpretation.md) | What do the formulas imply for scheduling, storage and execution cost? Examples separate memory alignment, persistent width, transient width and sampling. | The main theorem statements |

For the shortest route to the physical result, read **model → resource interpretation → reset schedules → dephasing memory**. For the proof route, read **model → forest witness → reset schedules → wire construction → gate cuts**, then the noisy-memory and precision pages. The [related-work comparison](../references/related-work.md) explains where the established collective-cutting constructions enter both routes.

For a guided conceptual route, use the [worked explanation](../learning/tutorial.md), the [30-milestone map](../learning/milestones.md), and the [Watrous source bridge](../learning/anchor.md). The scientific pages below remain the canonical statements and proofs.

## Proof structure

The reset results have two independent halves. The converse turns complete local memory breaks into a product over coherence-epoch vertices, then uses the forest witness. The achievable construction operates separately inside each common interval, respects the actual port deadlines, and consumes its private quantum resources before the interval ends. Equality follows by matching their extents.

The noisy result uses a different restriction. An unflagged dephasing environment cannot be refined into accessible error labels. Instead, the local temporal Choi states obey a concurrence inequality that survives filtering and mixtures. A witness bounded on that cone controls all scored adaptive protocols, and the explicit resource identity reaches its target value.

The [joint phase comparison](correlated-phase-memory.md) changes the noise model and local dimension. It uses the linear and cubic channels of [LWE Noise Geometry](https://github.com/GoGoKo699/LWE-Noise-Geometry), whose [operational comparison](https://github.com/GoGoKo699/LWE-Noise-Geometry/blob/main/science/circuit-cutting.md) explains the consequence for its channel distinctions. Here the inherited spatial witness gives49 for either joint channel. A complete parity instrument attains it because $`x^3\in\{x,-x\}`$ over $`\mathbb F_5`$. Its signed resource has trace $`1/4`$, with every outcome retained. The proof does not transfer the independent-qubit concurrence cone to correlated noise or expose hidden phase flags.

The approximation statements use those established witnesses. The calibration calculation analyzes an actual implementation with mismatched coefficients. A signed reconstruction can have negative Choi eigenvalues, so its propagation is derived directly rather than assigned physical-channel contraction properties.

## Evidence and boundaries

The [verification code](../verification/verify.py) checks finite identities and examples, including an online tester that interacts between resource emissions. Its [guide](../verification/README.md) identifies what each check establishes. It does not replace the general proofs or test every allowed adaptive protocol.

The exact results apply to the stated universal process task. Observable-specific learning, nonuniversal circuit promises, a different joint noise environment, uncharged stored data, early future inputs and delayed output release can change the answer. Counterexamples and explicit boundaries are part of the relevant scientific pages. The correlated phase result is for the two stated $`q=5`$ channels; it asserts no general equivalence of those channels or their learning tasks. Repeated independent-noise two-slot optima multiply as an exact theorem only with the imposed complete resets and fresh noise specified there.

[Repository overview](../README.md) · [Primary bibliography](../references/references.bib)
