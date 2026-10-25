# Causal cutting with quantum memory

## The operational question

Collective circuit cutting can use quantum correlations between operations that occur at different times. Such a protocol must preserve those correlations in a physical memory. This project asks how the best signed simulation changes when that memory is completely reset at prescribed times, or when a single stored qubit dephases between two operations.

The object being simulated is an **open, ordered sequence of quantum operations**. Its inputs may be entangled with inaccessible references, and an external experiment may insert arbitrary causal operations between successive slots. Reproducing this open process is stronger than reproducing a known circuit's final expectation value. It makes the memory resource independent of a particular input or observable.

The connection between circuit cutting, signed local operations, and entanglement robustness follows the frameworks of [Brenner, Piveteau and Sutter](https://arxiv.org/abs/2302.03366), [Schmitt, Piveteau and Sutter](https://arxiv.org/abs/2312.11638), and [Harrow and Lowe](https://arxiv.org/abs/2403.01018). The additional resource constraints here concern what quantum information can persist between the actual operation slots.

## Laboratories, ports and time

There are two laboratories, Alice and Bob, with slots numbered $j=1,\ldots,n$. Slot boundaries are part of the interface, not an optimization variable.

- In a **wire slot**, a $d_j$-dimensional input is delivered to its sender, and the ideal operation transfers that state to the receiver. The main examples use Alice-to-Bob qubit wires. Directions may also be specified separately for each slot.
- In a **gate slot**, one qubit input is delivered to each laboratory, and the ideal operation is a specified two-qubit unitary $U_j$. Each laboratory returns its own output.
- The input for slot $j+1$ is inaccessible to the cutter until slot $j$ has ended and the intervening memory break or noise channel has acted.
- Every slot output is released before the next slot. Released outputs and external references cannot be borrowed as private storage. If a device retains access to a data qubit across a gap, that qubit counts as quantum memory.

The external tester accesses the prescribed quantum ports and its own records; it does not receive the private sampled decomposition index or the simulator's internal instrument records. Adapting to those private labels defines a different interface.

The cutter can prepare private resources in advance from known gate descriptions and classical random labels. It cannot prepare, inspect or process an actual future input before its release time. An external tester can keep earlier outputs and use them to prepare later inputs; the cutter's identity must hold for every such causal tester.

This interface models an online subroutine or a modular cutting rule. It does not impose a memory lower bound on a known closed circuit whose data can be jointly manipulated before the nominal cuts. In particular, two gates that cancel in a known circuit need not have the cost of two universal open slots.

## Free operations and charged storage

Within each slot the laboratories may use arbitrary local quantum instruments, arbitrary finite transient ancillas, classical randomness, and two-way classical communication. The classical controller and classical records may persist indefinitely. Initial spatial entanglement, a quantum link between laboratories, and an accessible coherent noise environment are not free resources.

All private quantum systems that carry information across a slot gap and can be accessed by the cutter at a later stage count as memory, regardless of whether they are called ancillas, data, ports or environmental modes. Temporarily isolating a register does not remove it from this accounting. Fresh ancillary systems are prepared locally using the allowed operations; a reservoir of quantum-correlated future ancillas is charged persistent storage. Transient workspace and persistent workspace are distinct resources. A result using one persistent qubit is not a claim that the entire physical circuit has width one.

The results apply to finite-round local-operations-and-classical-communication protocols. Their lower bounds also hold for limits of such protocols, by continuity of the finite-dimensional witness functionals. No restriction on the amount of classical communication is used in the converses.

### Prescribed complete memory breaks

Each laboratory has a prescribed partition of the slot sequence into consecutive **coherence epochs**. Within an epoch its quantum memory dimension is unrestricted. At every boundary the channel acting on its entire persistent quantum register is entanglement breaking. It can be written as a measurement followed by preparation, possibly conditioned on the surviving classical record.

Each break is a genuine local entanglement-breaking connection conditional on the available earlier classical history, with no accessible environmental extension. An entanglement-breaking marginal of a correlated joint noise process is not sufficient: information retained elsewhere could reveal an error and restore the supposedly broken coherence.

Thus no quantum information about the earlier epoch survives the boundary in the cutter. The two laboratories' boundaries need not coincide. Define $\mathcal I$ to be their common refinement: an interval ends whenever either laboratory has a boundary. For a wire interval,

```math
D_I=\prod_{j\in I}d_j.
```

The prescribed breaks cannot be postponed, skipped, or bypassed through an uncharged register. Outcome-dependent schedules require a different optimization problem.

### One dephasing qubit across a gap

The noisy-memory theorem has two qubit-wire slots. At most one qubit persists at each laboratory, and the gap applies

```math
\mathcal D_\eta(\rho)
=\frac{1+\eta}{2}\rho+\frac{1-\eta}{2}Z\rho Z,
\qquad 0\leq\eta\leq1.
```

Conditional on every allowed **pre-gap** classical history, the physical noise is the product channel $\mathcal D_{\eta_A}\otimes\mathcal D_{\eta_B}$. Its error flags are inaccessible. Later postselection may correlate posterior errors; no posterior-independence assumption is made. All other local operations in this theorem are ideal. This is a specified one-use noise model, not a characterization from marginal coherence times alone.

## Signed instruments and the cost being minimized

Let $\{\mathcal C_h\}_h$ be a physical causal instrument implementing the allowed local operations and memory constraints. Here $h$ includes the simulator's accessible classical history, and summing over $h$ gives a deterministic physical process. A scored atom is the linear map

```math
\mathcal F=\sum_h s_h\mathcal C_h,
\qquad s_h\in[-1,1].
```

The scores use simulator records. They retain the physical probability of every outcome, including an unsuccessful postselection event. A normalized successful branch supplied for free is not an allowed atom. Scores are not allowed to depend on uncharged measurements of the tester's input, reference, or final observable.

The scored map itself need not be completely positive or trace preserving. This convention is necessary for general gate cutting: signed sums of product trace-preserving channels alone remain nonsignalling and cannot reproduce a signalling gate such as CNOT. Physical output deadlines constrain the underlying instrument; a final classical sign may be applied retrospectively to a sample.

For the ideal open process $\mathcal T$, define the **signed extent**

```math
\Gamma_{\mathfrak M}(\mathcal T)
=\inf\left\{\sum_\ell |a_\ell|:
\mathcal T=\sum_\ell a_\ell\mathcal F_\ell,
\ \mathcal F_\ell\text{ allowed by }\mathfrak M\right\}.
```

The model $\mathfrak M$ specifies the port schedule and either the reset partitions or the noisy memories. Equality means equality of the open process, hence of every result obtained by connecting any causal tester. Classical mixtures and randomized bounded scores are included in the allowed atoms.

The exact target is deterministic, so $\Gamma\geq1$. No claim is made that this extent equals the best sample complexity among all biased, nonlinear, learned, or observable-specific estimators.

## Normalized Choi tests and lower bounds

For every slot input, prepare a maximally entangled state between that input and a retained reference. Keep the outputs without feeding them back. This is an allowed tester. Use normalized Bell states, so the Choi operator of every deterministic physical process has trace one. For a physical instrument,

```math
J(\mathcal C_h)\succeq0,
\qquad \sum_h\operatorname{Tr}J(\mathcal C_h)=1.
```

The ideal wire stream has Choi state $\bigotimes_j\Phi_{d_j}$, with

```math
\Phi_d=|\Phi_d\rangle\langle\Phi_d|,
\qquad |\Phi_d\rangle=d^{-1/2}\sum_{x=0}^{d-1}|x,x\rangle.
```

The ideal gate stream has Choi state $\bigotimes_j|J(U_j)\rangle\langle J(U_j)|$. In its spatial partition, each laboratory owns its local input reference and local output for each slot.

If a Hermitian operator $W$ obeys

```math
\left|\operatorname{Tr}\!\left[WJ(\mathcal F)\right]\right|\leq1
```

for every allowed scored atom, then every exact decomposition satisfies $\Gamma\geq\operatorname{Tr}[WJ(\mathcal T)]$. The factorization proofs refine accessible local histories while respecting the memory channel. A hidden entanglement-breaking reset outcome may be exposed for a lower bound, since granting that classical information enlarges the model. Exposing an unflagged dephasing error would instead remove a charged resource restriction and invalidate the noisy-memory cone used here.

## Exact statements and where they are proved

| Setting | Exact signed extent | Canonical account |
|---|---|---|
| Ordered identity wires with prescribed complete memory breaks | $\prod_{I\in\mathcal I}(2D_I-1)$ | [Reset schedules](reset-schedules.md) and [wire construction](wire-construction.md) |
| Ordered two-qubit gates with the same breaks | $\prod_{I\in\mathcal I}(2\prod_{j\in I}\chi_j-1)$ | [Gate cuts](gate-cuts.md) |
| Two qubit wires with independent single-qubit dephasing memories | $5+4/(1+\eta_A\eta_B)$ | [Dephasing memory](dephasing-memory.md) |

Here $\chi_j=(\sum_\alpha|u_{j\alpha}|)^2$, where $u_{j\alpha}$ are normalized KAK coefficients of the two-qubit gate. The upper bounds for unrestricted collective cutting use established constructions; their attribution and operational comparison are given in [related work](../references/related-work.md).

The mathematical connection is an exact [pure-edge forest witness](forest-witness.md). The physical interpretation, scheduling examples, and charged resources are developed in [resource interpretation](resource-interpretation.md). Approximation and calibration have their own statements in [precision and calibration](precision-calibration.md); they do not silently enlarge the exact theorems.
