# Quantum Memory Circuit Cutting

**Exact circuit-cutting costs under local memory breaks, independent dephasing, and specified correlated phase noise.**

Collective circuit cutting trades quantum resources for signed classical sampling. Its advantage can depend on preserving quantum information between cuts. This repository studies that temporal resource explicitly: which coherences must survive, how two laboratories' reset schedules interact, and what a noisy stored qubit can still accomplish.

The target is an open sequence of wire or gate slots, usable inside an arbitrary causal surrounding computation. Inputs arrive at their assigned slots, outputs leave before the next slot, and every private quantum system retained across a gap counts as memory. The optimized quantity is the **signed extent** $`\Gamma`$: the smallest sum of absolute coefficients in a universal quasiprobability decomposition into allowed physical instruments with bounded classical scores. These conventions are defined in [the operational model](science/model.md).

**Sister connection — [LWE Noise Geometry](https://github.com/GoGoKo699/LWE-Noise-Geometry).** Its linear and cubic $`q=5`$ phase channels give the same exact two-wire cutting extent, $`\Gamma_L=\Gamma_C=49`$, with one persistent five-level memory per laboratory. A complete parity instrument attains the bound despite inaccessible error flags. This repository owns the [full proof and streaming construction](science/correlated-phase-memory.md); the sister repository gives the [channel-to-task comparison](https://github.com/GoGoKo699/LWE-Noise-Geometry/blob/main/science/circuit-cutting.md). Their different channel geometry and fixed-source learning behavior do not imply a strict gap for this cutting task.

## Main results

### 1. The two reset schedules determine a common-refinement law

Let $`\mathcal I`$ be the intervals obtained by cutting the slot sequence whenever either laboratory undergoes a complete entanglement-breaking memory reset. For identity wires of dimensions $`d_j`$, put $`D_I=\prod_{j\in I}d_j`$. Then

```math
\boxed{\Gamma_{\mathrm{reset}}=\prod_{I\in\mathcal I}(2D_I-1).}
```

The lower bound allows arbitrary adaptive classical communication and unrestricted quantum memory inside an epoch. The matching wire construction needs only one persistent qubit per laboratory inside each interval, together with explicitly counted transient systems. It emits its private resource sequentially and returns the branch memory cleanly.

For general two-qubit gate slots, replace $`D_I`$ by $`\prod_{j\in I}\chi_j`$, where $`\chi_j=(\sum_\alpha|u_{j\alpha}|)^2`$ and $`u_{j\alpha}`$ are normalized KAK coefficients. The gate upper construction uses larger, explicitly charged private resource storage; the one-qubit wire statement is not a minimum-memory claim for general gates.

The proof connects causal memory breaks to a forest of local coherence epochs. A product witness has the required bound on a forest, even when each vertex can hold an arbitrary joint quantum state. [Reset theorem and proof](science/reset-schedules.md) · [Forest inequality](science/forest-witness.md) · [Wire implementation](science/wire-construction.md) · [Gate extension](science/gate-cuts.md)

### 2. Two noisy memory qubits have an exact continuous tradeoff

For two qubit-wire slots, allow one persistent qubit at each laboratory and apply independent, unflagged dephasing channels with coherence factors $`\eta_A,\eta_B\in[0,1]`$ across the gap. All other local operations are ideal. Then

```math
\boxed{\Gamma_2(\eta_A,\eta_B)=5+\frac4{1+\eta_A\eta_B}.}
```

The extent runs from nine when either memory completely dephases to seven when both are noiseless. A four-resource construction attains the bound. The converse constrains each local temporal Choi state using concurrence and concurrence of assistance, then bounds every adaptive scored instrument.

The result depends on the actual noise and port schedule: correlated phase errors with the same marginal channels can attain seven even when independent errors require nine. For prescribed two-slot blocks, the exact costs multiply if both laboratories completely reset between blocks and the noise is fresh across blocks. For uninterrupted many-slot noisy memories, the repeated-block protocol is an upper bound. [Complete noisy-memory theorem](science/dephasing-memory.md)

### 3. Linear and cubic phase memories both attain extent 49

For two ordered five-dimensional identity wires, let the gap act on the two local five-level memories by the joint unflagged phase channel

```math
\mathcal N_f(\rho)=\frac15\sum_{x\in\mathbb F_5}
(Z^x\otimes Z^{f(x)})\rho(Z^x\otimes Z^{f(x)})^\dagger,
\qquad f(x)=x\text{ or }x^3.
```

Here $`Z|j\rangle=e^{2\pi i j/5}|j\rangle`$. The two actual input times and output deadlines remain fixed. The hidden draw is independent of every permitted pre-gap classical history, and neither its flag nor its environment is accessible. Each marginal memory channel completely dephases, while the joint errors are correlated. For both choices,

```math
\boxed{\Gamma_L=\Gamma_C=49.}
```

The inherited spatial separability witness supplies the lower bound for arbitrary filtering, complete scored instruments, and their operational closure. A complete reflection-parity instrument supplies the matching upper bound. Its scored operator has trace $`1/4`$: all physical outcomes are charged, and this operator is not renormalized into a free successful state. The cubic upper bound $`97-16\sqrt5`$ is also certified, but is nonoptimal. This joint five-level model is separate from the independent-qubit theorem above. [Correlated phase-memory proof](science/correlated-phase-memory.md)

### 4. Approximation and calibration are accounted for separately

Witness spectral ranges give lower bounds for approximate universal signed decompositions. They preserve an exponential separation between aligned and staggered reset schedules at fixed sufficiently small strategy error.

For the noisy two-slot construction, using nominal $`r_0`$ instead of actual $`r=\eta_A\eta_B`$ gives exact full strategy error $`|r-r_0|/(1+r_0)`$. The miscalibrated reconstruction is not completely positive, so errors over repeated blocks require an explicit signed-process calculation. The account includes that calculation, a charged Ramsey calibration procedure, coefficient rounding, and sufficient execution counts. [Precision and calibration](science/precision-calibration.md)

## Read the scientific account

Start with the [science reading map](science/README.md). For a compact physical interpretation, see [memory alignment, examples and resource accounting](science/resource-interpretation.md). The [related-work comparison](references/related-work.md) and [primary-source bibliography](references/references.bib) distinguish inherited constructions from the constrained-memory claims proved here.

In particular, collective wire cutting, low-ancilla interference constructions, and collective two-qubit gate cutting have established antecedents. The unrestricted upper constructions are attributed to Brenner–Piveteau–Sutter, Harrow–Lowe, and Schmitt–Piveteau–Sutter, as appropriate. The memory-constrained results include the reset and independent-dephasing frontiers. The joint result with LWE Noise Geometry adds the complete parity construction and exact extent-49 identity; its phase laws and channel distinctions come from that sister repository.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source bridge](learning/anchor.md) identifies the useful sections, translates the book's Choi and norm conventions, and separates textbook foundations from the project's additional research arguments.

The [30-milestone map](learning/milestones.md) follows the complete scientific story: **12 background/preliminaries milestones** assemble the operational framework, and **18 narrative/innovation milestones** connect the two converse mechanisms, matching constructions, precision analysis and physical interpretation. Every milestone includes a central question, an understanding target, earlier dependencies, a conceptual connection and source pointers.

Start with [From a single cut to quantum memory](learning/tutorial.md) for a worked explanation of the costs three, seven and nine, reset alignment, independent dephasing, and the complete parity experiment attaining 49. The [learning entrypoint](learning/README.md) connects this explanation, the source bridge and the map. The [LLM reading guide](llms.txt) provides direct routes for study, theorem inspection and reproduction.

## Reproduce the finite checks

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py --output verification/results.json
python verification/correlated_phase_checks.py
```

The [verification guide](verification/README.md) explains the fixed-seed checks of resource identities, witness bounds, reset graphs, genuinely online teleportation, non-Clifford gate reconstruction, noisy filters, and calibration formulas. The recorded [results](verification/results.json) accompany the code. Finite numerical checks support the algebra and implementation; the universal optimality statements rest on the analytical proofs in `science/`.

## Scope

The exact theorems concern universal bounded-score signed simulation with the stated resource and timing constraints. The standard estimator has a sufficient sampling bound proportional to $`\Gamma^2`$, but this is not a universal measurement lower bound for every fixed observable, learned estimator, or promised circuit family. The approximate witness bounds are not complete optimal tradeoff curves. Arbitrary noisy memories and the unrestricted many-slot noisy optimum remain outside the established results.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT License](LICENSE).
