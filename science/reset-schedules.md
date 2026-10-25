# Exact cost for asynchronous memory resets

An uninterrupted quantum memory allows several circuit cuts to share one collective decomposition. A complete break on one side might appear less restrictive: the other laboratory could preserve its memory and use classical feedback to connect operations on the two sides of the break. This section proves that such a relay does not improve the universal signed extent. The useful collective intervals are exactly those during which neither laboratory has a break.

The operational definitions, including scored physical instruments and the strict timing of input release and output delivery, are in [Causal cutting with quantum memory](model.md). The mathematical bound is the [pure-edge forest identity](forest-witness.md), and the matching physical protocol is constructed in [Wire construction](wire-construction.md).

## 1. Epochs and the common refinement

Consider $`n`$ ordered identity-wire slots. Slot $`j`$ transfers a $`d_j`$-dimensional state between the two laboratories in a specified direction. The direction may vary with $`j`$. Alice and Bob have partitions $`\mathcal P_A`$ and $`\mathcal P_B`$ into contiguous intervals of slots. Their intervals are called coherence epochs.

Inside each epoch, the private quantum memory may have arbitrary finite dimension. At a boundary of one laboratory's partition, its entire persistent quantum memory passes through an entanglement-breaking channel. Unlimited classical records and two-way classical communication remain available. The definition excludes initial spatial entanglement, a quantum link, and any private quantum system that bypasses the break.

The break is a genuine local measure-and-prepare connection, conditional on the available earlier classical history. An apparently entanglement-breaking marginal is insufficient if an accessible correlated environment or another memory retains a flag that restores the lost coherence. Such a joint process is not the prescribed local break assumed here.

Let $`\mathcal I=\mathcal P_A\wedge\mathcal P_B`$ be the common refinement. Thus an interval of $`\mathcal I`$ ends whenever either laboratory has a boundary. For each $`I\in\mathcal I`$, write

$$
D_I=\prod_{j\in I}d_j,
\qquad
G=\prod_{I\in\mathcal I}(2D_I-1).
$$

**Theorem 1 — Exact common-refinement law.** In the prescribed-reset model,

$$
\boxed{
\Gamma_{\mathcal P_A,\mathcal P_B}(\mathrm{Id}_{\mathrm{stream}})
=\prod_{I\in\mathcal I}(2D_I-1).
}
$$

The converse permits arbitrary quantum memory within each epoch and arbitrary two-way classical feedback. A protocol with one persistent qubit at each laboratory inside each common interval attains the value. Each persistent qubit is returned exactly to a fixed pure state and is decoupled from the data at the end of that interval. Transient input and resource registers are additional physical systems, as detailed in the construction.

## 2. The graph determined by time

Create one vertex for every Alice epoch and one vertex for every Bob epoch. A nonempty intersection of an Alice epoch and a Bob epoch is an edge. Contiguity implies that every such intersection is one interval $`I\in\mathcal I`$. Assign its edge the dimension $`D_I`$.

**Lemma 2 — The overlap graph is a forest.**

**Proof.** Scan the ordered slots. The first overlap starts with two new vertices joined by one edge. When only Alice has a boundary, the next overlap introduces a new Alice vertex and joins it to the current Bob vertex. A Bob-only boundary has the symmetric effect. When both have boundaries, the next overlap introduces two new vertices and starts a new component. Every new edge consequently introduces at least one vertex that has not appeared before. A cycle cannot be created. $`\square`$

The graph can contain a vertex of large degree. Such a vertex represents a long epoch at one laboratory that overlaps many shorter epochs at the other. The proof does not replace that long epoch by independent operations: the corresponding vertex state is allowed to be arbitrarily entangled among all its incident registers.

## 3. Why the physical branches factor over epochs

The following argument establishes the bridge from a causal circuit to the graph. Quantum combs provide the standard representation of networks with ordered input and output ports; see [Chiribella, D'Ariano, and Perinotti](https://arxiv.org/abs/0904.4483). Only the normalized Choi experiment and a direct circuit factorization are needed here.

Prepare a normalized maximally entangled pair for every slot input. Release its input half at the required slot, retain its reference, and retain every returned output without feeding it back. This is a valid causal tester. Denote the resulting normalized Choi operator of a physical instrument branch by $`J(\mathcal C_h)`$. Determinism of the sum of the branches gives

$$
J(\mathcal C_h)\geq0,
\qquad
\sum_h\mathrm{Tr}J(\mathcal C_h)=1.
$$

The references and outputs belonging to a laboratory during one epoch form that epoch's vertex space. A wire contributes its sender's input reference and its receiver's output to the two endpoints of its edge. Reversing the wire direction changes these port names but leaves the bipartite maximally entangled target unchanged.

**Proposition 3 — Refined-branch factorization.** For every allowed finite-round physical instrument, there is a refinement $`t`$ of its classical branches such that

$$
J(\mathcal C_h)
=\sum_{t:\,h(t)=h}
p_t\bigotimes_{v\in V}\rho_{v,t},
\qquad p_t\geq0,
\qquad \sum_t p_t=1,
$$

where every $`\rho_{v,t}`$ is a normalized positive operator on one epoch's Choi registers.

**Proof.** Include the shared random seed, all local instrument outcomes, and all exchanged classical messages in a complete transcript. Condition on that transcript. The local operations are now fixed linear maps; their choices can depend on the transcript, but the classical messages themselves are fixed labels rather than quantum connections.

An entanglement-breaking channel on the entire memory has a measure-and-prepare representation

$$
\mathcal E(X)=\sum_z\mathrm{Tr}(E_zX)\,\tau_z,
\qquad E_z\geq0,
\qquad \sum_zE_z=I.
$$

This characterization is established in [Horodecki, Shor, and Ruskai](https://arxiv.org/abs/quant-ph/0302031). Spectrally decompose each $`E_z`$ and $`\tau_z`$. The resulting Kraus operators can be chosen rank one,

$$
K_{zab}=\sqrt{e_{za}t_{zb}}\,
|u_{zb}\rangle\langle v_{za}|.
$$

Refine the transcript by these Kraus labels, even if they are physically hidden. For a converse it is legitimate to expose this information: doing so grants additional classical information and cannot make the allowed simulation class smaller.

With one rank-one Kraus operator fixed at a boundary, the earlier memory is contracted with a fixed bra and the later epoch begins with a fixed ket. No quantum index remains connecting those epochs. There is also no quantum index connecting Alice to Bob, because the laboratories share neither an initial entangled state nor a quantum communication channel. Refine any other discarded local environment into Kraus labels and include terminal memory-discard labels. Every quantum component of the conditioned circuit now lies wholly inside one epoch.

The strict port schedule matters at this step. A future input has never been accessible in an earlier epoch, and a released output cannot be operated on in a later epoch. Thus no input or output register supplies an additional quantum connection between epoch components. The Choi tester's reference halves are retained externally and never touched by the cutter.

Vectorizing the fixed component maps gives a product of positive Choi operators,

$$
J_t=\bigotimes_v Q_{v,t},
\qquad Q_{v,t}\geq0.
$$

Scalar probabilities from classical choices and the normalization of the Bell inputs can be included in these factors. Set $`p_t=\mathrm{Tr}J_t`$. For a nonzero branch, divide each factor by its trace to obtain $`J_t=p_t\bigotimes_v\rho_{v,t}`$. Branches with $`p_t=0`$ can be omitted. Summing all refined branches reproduces the physical deterministic Choi operator, so $`\sum_t p_t=1`$. $`\square`$

This is a separability statement about the normalized Choi test, not a claim that the entire experiment becomes independent across epochs. The external tester can correlate actual inputs in a general experiment. The particular independent-Bell-input tester suffices for the lower bound because the cutting identity is required to hold for every tester.

Arbitrary two-way feedback is included: conditioning on the full transcript changes the $`Q_{v,t}`$ but does not restore a quantum connection across a rank-one boundary. The same witness bound holds for limits of finite-round protocols by continuity on the fixed finite-dimensional port space.

## 4. Scored atoms retain physical branch probabilities

A scored atom has the form

$$
\mathcal F=\sum_h s_h\mathcal C_h,
\qquad |s_h|\leq1.
$$

Proposition 3 gives

$$
J(\mathcal F)
=\sum_t s_{h(t)}p_t\bigotimes_v\rho_{v,t}.
$$

The normalized successful branch of a postselection cannot be inserted without its success probability: the factor $`p_t`$ is part of the physical Choi operator. This is why the converse remains valid even when a protocol uses rare outcomes or postpones its scoring until the final record is available.

For each common interval, let $`\Phi_{D_I}`$ be its maximally entangled edge state and define

$$
W_I=2D_I\Phi_{D_I}-I,
\qquad W=\bigotimes_{I\in\mathcal I}W_I.
$$

The forest witness gives $`|\mathrm{Tr}[W\bigotimes_v\rho_{v,t}]|\leq1`$. Consequently

$$
|\mathrm{Tr}[WJ(\mathcal F)]|
\leq\sum_t|s_{h(t)}|p_t
\leq1.
$$

The ideal open wire process has Choi state $`\bigotimes_j\Phi_{d_j}`$. Regrouping slots within a common interval identifies $`\bigotimes_{j\in I}\Phi_{d_j}`$ with $`\Phi_{D_I}`$. Hence

$$
\mathrm{Tr}[WJ(\mathrm{Id}_{\mathrm{stream}})]
=\prod_{I\in\mathcal I}(2D_I-1)=G.
$$

Applying the witness to any exact signed decomposition proves $`\Gamma\geq G`$.

## 5. Attainment and the role of synchronized coherence

For each common interval $`I`$, the [causal wire protocol](wire-construction.md) attains extent $`2D_I-1`$ with one persistent qubit in each laboratory. It emits and uses each local resource port only when the corresponding slot arrives. Earlier outputs have already been returned, and future data inputs are never accessed. Its memory returns clean at the interval's end.

Execute these protocols independently for the different common intervals. Each interval is contained in one epoch at both laboratories, so all its persistent memory is permitted by the schedule. At a common boundary, the laboratory without a prescribed reset may voluntarily discard its now-unneeded memory. Coefficients multiply, and so do their absolute sums. The resulting extent is $`G`$, completing the proof of Theorem 1. $`\square`$

The factor $`2D_I-1`$ is the established collective wire-cutting optimum; see [Brenner, Piveteau, and Sutter](https://arxiv.org/abs/2302.03366). The exact reset theorem combines that attainable factor with a converse for arbitrary asynchronous schedules and unrestricted within-epoch memory. Independent batching by itself would establish only the upper bound.

### One-sided loss of memory

If either laboratory has a boundary at every slot gap, every common interval is a singleton. Therefore

$$
\Gamma=\prod_{j=1}^n(2d_j-1),
$$

even if the other laboratory has arbitrarily large coherent memory throughout all $`n`$ slots. For qubit wires this is $`3^n`$.

If neither side has a boundary, there is one common interval. Writing $`D=\prod_jd_j`$ gives

$$
\Gamma=2D-1.
$$

For qubit wires, one persistent qubit at each side therefore attains $`2^{n+1}-1`$, while complete loss of persistent coherence on either side gives $`3^n`$. These are statements about the specified streaming interface, not a general quantum-memory capacity bound.

### An exponential synchronization penalty

Let $`n`$ be even. Suppose Alice's epochs are $`(1,2),(3,4),\ldots`$. If Bob uses the same partition, every common interval has two qubit slots and

$$
\Gamma_{\mathrm{aligned}}=7^{n/2}.
$$

If Bob's partition is shifted by one slot, with singleton intervals at the two ends, then a boundary occurs on one side at every gap. Every common interval is a singleton and

$$
\Gamma_{\mathrm{staggered}}=3^n,
\qquad
\frac{\Gamma_{\mathrm{staggered}}}{\Gamma_{\mathrm{aligned}}}
=\left(\frac97\right)^{n/2}.
$$

Both laboratories have maximum epoch length two in both cases. Their relative reset timing changes the extent exponentially. In the standard bounded-weight Monte Carlo estimate, the corresponding squared-extent overhead ratio is $`(9/7)^n`$; this is not a sample lower bound for arbitrary algorithms.

For a finite example, take six qubit slots with Alice epochs $`(1,2,3),(4,5,6)`$ and Bob epochs $`(1,2),(3,4,5),(6)`$. The common interval lengths are $`2,1,2,1`$, giving $`\Gamma=7\cdot3\cdot7\cdot3=441`$. Aligned length-three epochs give $`15^2=225`$, uninterrupted coherence gives $`127`$, and singleton epochs give $`729`$.

## 6. Precision and scope

The exact exponential distinction survives a fixed small approximation error within the same universal QPD class. With half strategy-distance error at most $`\epsilon`$, the unconditional witness bound is $`\Gamma\geq(1-2\epsilon)G`$. If the approximating Choi operator also has trace one, the sharper bound is

$$
\Gamma\geq G\left[1-\left(1+\frac1{c_{\min}}\right)\epsilon\right],
\qquad c_{\min}=\min_{I\in\mathcal I}(2D_I-1).
$$

The norm conventions, trace-normalization requirement, and proof are given in [Precision and calibration](precision-calibration.md).

The reset law concerns prescribed complete entanglement-breaking boundaries of all private quantum storage. A bound only on the number of stored qubits, an average coherence time, or partial dephasing does not imply this law. The separately specified [two-slot dephasing model](dephasing-memory.md) has its own attainable set and exact cost. For gate slots, the same factorization and forest proof apply, but the edge entanglement is determined by the normalized KAK coefficients; the resulting formula is proved in [Gate cuts](gate-cuts.md).
