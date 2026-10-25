# Relation to existing circuit-cutting and quantum-information results

Primary sources and publication metadata were checked on **25 October 2026**. The bibliography is in [references.bib](references.bib). A journal publication year can differ from the first arXiv posting; both are recorded when that distinction matters. This account identifies the results and models on which the project builds. A literature search cannot certify priority or the absence of another proof.

## The operational question

The project asks how the exact quasiprobability extent changes when a simulator must respect a prescribed pattern of **local quantum memory continuity**. The target is a sequence of universal wire or gate slots. Each output is released before the next input is supplied; the simulator must work inside arbitrary causal surrounding computations, including computations with retained quantum references. Between slots, classical history can remain available, while specified local boundaries destroy all persistent quantum memory. The signed atoms come from complete physical instruments with scores of absolute value at most one. See [the model](../science/model.md).

For wire dimensions `d_j`, let the common refinement of Alice's and Bob's coherence epochs have intervals `I_k`, and set `D_k = product_{j in I_k} d_j`. The reset theorem gives

```math
\gamma_{\mathrm{reset}}=\prod_k(2D_k-1).
```

The unrestricted collective factor `2D-1`, the benefit of grouping cuts, teleportation-based reductions, and low-ancilla interference constructions all have substantial prior literature. The result developed here is the matching converse for the restricted set of **causal protocols with two potentially different local reset schedules**, together with the exact two-slot law for a specified noisy one-qubit memory model. These statements concern the QPD extent in the defined model, not an unrestricted sample-complexity optimum.

## Closest circuit-cutting results

| Source | Established result relevant here | Relation to this project |
|---|---|---|
| [Piveteau and Sutter, *Circuit knitting with classical communication*](https://arxiv.org/abs/2205.00016), IEEE TIT 70, 2734–2745 (2024), first posted 2022; `PiveteauSutter2024` | Collective simulation of nonlocal gates can be cheaper than independently cutting each gate; classical communication improves the collective CNOT construction. | Establishes the collective-cutting phenomenon. The present resource restriction is which local coherences survive between prescribed slots. |
| [Brenner, Piveteau, and Sutter, *Optimal wire cutting with classical communication*](https://arxiv.org/html/2302.03366v1), IEEE TIT 71, 7742–7752 (2025), first posted 2023; `BrennerPiveteauSutter2025` | The optimal collective extent for `n` qubit wires with classical communication is `2^(n+1)-1`. Section 4.3 extends the construction to arbitrary cut positions using ancillary resources. | Supplies the collective wire optimum and teleportation perspective. Prescribed local resets restrict the admissible simulator, so their unrestricted optimum is a lower baseline and an achievable factor inside each common interval. |
| [Harada, Wada, and Yamamoto, *Doubly optimal parallel wire cutting without ancilla qubits*](https://arxiv.org/abs/2303.07340), PRX Quantum 5, 040308 (2024); `HaradaWadaYamamoto2024` | Uses mutually unbiased bases to achieve optimal sampling overhead and decomposition-channel count for parallel wire cuts without ancillary qubits. | Simultaneous access to all input qubits differs from strict input arrival and output release. “No ancilla” for a parallel channel does not imply “no persistent quantum memory” for its online implementation. |
| [Harrow and Lowe, *Optimal quantum circuit cuts with application to clustered Hamiltonian simulation*](https://arxiv.org/pdf/2403.01018), PRX Quantum 6, 010316 (2025); `HarrowLowe2025` | Theorem 1.2 and Sections 3.3–3.4 give product-extent and double-Hadamard-test constructions with one ancillary qubit per laboratory. Their Choi-state expansion uses coherent pairs of local terms. | The two-string resource expansion and low-memory implementation build on this established interference mechanism. The reset-schedule converse is a separate issue. Their Section 4 also distinguishes actual estimator variance from a generic squared-extent bound. |
| [Schmitt, Piveteau, and Sutter, *Cutting circuits with multiple two-qubit unitaries*](https://arxiv.org/html/2312.11638v4), Quantum 9, 1634 (2025); `SchmittPiveteauSutter2025` | For two-qubit gates with normalized KAK coefficients `u_(j,alpha)`, the optimal collective extent is `2 product_j (sum_alpha |u_(j,alpha)|)^2 - 1`. Theorem 6.4 covers unknown interleaving channels. | **The arbitrary two-qubit gate upper construction is inherited from Theorem 6.4.** Applying it inside each common epoch interval supplies the upper bound; the forest argument supplies the reset-constrained lower bound. |
| [Piveteau, Schmitt, and Sutter, *Circuit cutting with classical side information*](https://arxiv.org/abs/2503.22384), Physical Review Research 7, 033063 (2025); `PiveteauSchmittSutter2025` | Formalizes classical side information through quantum instruments and derives lower bounds that account for it. | Motivates keeping measurement records and signed branch scores explicit. A restriction to deterministic product channels would describe a different, inadequate gate-cutting model. Our witnesses are evaluated on complete scored instruments. |

The one-qubit wire construction in [wire-construction.md](../science/wire-construction.md) exposes an implementation detail relevant to this resource accounting: a coherent superposition of two classical strings can be emitted sequentially, and the final differing symbol transfers the memory into the output and returns the memory to a fixed pure state. This is consistent with the general relation between sequential ancilla generation and matrix-product states established by [Schön et al.](https://arxiv.org/abs/quant-ph/0501096) (`SchonEtAl2005`). Neither bond-two sequential generation nor the unrestricted collective optimum is presented as a new resource principle.

The gate construction quoted above uses four additional ancilla qubits per gate in the black-box realization described by Schmitt, Piveteau, and Sutter. The project allows the required memory within an epoch for that extension. The one-qubit-per-party wire upper bound is **not** asserted for arbitrary two-qubit gates, and the wire precision calibration is not asserted as a general gate precision theorem.

## What the forest argument adds

The single-edge pure-state cost is inherited from robustness of entanglement. For Schmidt coefficients `s_i`, [Vidal and Tarrach](https://arxiv.org/abs/quant-ph/9806094) (`VidalTarrach1999`) give the pure-state robustness underlying the signed extent

```math
g=2\left(\sum_i s_i\right)^2-1.
```

The point requiring an additional argument is how these edge costs combine when a laboratory may retain joint quantum states across several slots inside one epoch. Tensoring edge witnesses does not automatically preserve a bound against arbitrary states at the incident vertices. The [forest lemma](../science/forest-witness.md) proves the needed product-over-vertex bound by eliminating leaves. It covers unequal endpoint dimensions and proper Schmidt supports. An explicit four-cycle of local Bell pairs gives witness value `3`, showing why this particular argument requires acyclicity.

The overlap graph of two interval partitions is a forest. Refining the simulator's classical histories and the measure-and-prepare components at entanglement-breaking boundaries turns each branch into a positive product over epoch vertices. This connects the forest inequality to a causal protocol restriction. It is this connection that yields dependence on the **common refinement**, rather than on either party's lifetime alone. See [reset-schedules.md](../science/reset-schedules.md).

The surrounding mathematical language is established. The measure-and-prepare characterization of entanglement-breaking channels is treated by [Horodecki, Shor, and Ruskai](https://arxiv.org/abs/quant-ph/0302031) (`HorodeckiShorRuskai2003`). [Chiribella, D'Ariano, and Perinotti](https://arxiv.org/abs/0904.4483) (`ChiribellaEtAl2009`) develop quantum combs and the link product for composing memory channels. [Gutoski](https://arxiv.org/abs/1008.4636) (`Gutoski2012`) develops the strategy distinguishability norm. These justify framing correctness against arbitrary causal testers and using a strategy-level approximation criterion. The project specializes these tools to its reset and bounded-score atom sets.

## Noisy temporal memory and shared spatial entanglement

[Bechtold et al., *Joint wire cutting with non-maximally entangled states*](https://arxiv.org/html/2406.13315v1) (`BechtoldEtAl2025`) derive optimal overheads with supplied entangled resources and constructive optimal decompositions for pure non-maximally entangled states. They also discuss arbitrary cut positions and composite resource states. [Hu, Liu, and Wu, *Entanglement-assisted circuit knitting*](https://arxiv.org/html/2510.26789v3) (`HuLiuWu2026`, version 3, April 2026) develop a more general resource-assisted QPD framework, including black-box quantum combs and probabilistic entanglement supply. Both are close conceptual precedents for trading a physical resource against signed sampling overhead.

Their assisting resource is **entanglement shared between the laboratories**. The noisy-memory theorem here starts with no such entanglement. Each laboratory has at most one persistent qubit across a single gap, and those two local memories undergo independent, unflagged dephasing. Transient quantum systems cannot bypass the gap, the next input has not yet arrived, and the noise environment is inaccessible. Under these conditions, [dephasing-memory.md](../science/dephasing-memory.md) establishes

```math
\Gamma_2=5+\frac{4}{1+\eta_A\eta_B}.
```

The upper construction uses local temporal states, followed by spatial twirling and slotwise teleportation. The lower bound must control all admissible filtering and adaptive classical communication, not only that construction. Its ingredients include the convex-roof concurrence of [Wootters](https://arxiv.org/abs/quant-ph/9709029) (`Wootters1998`), the concurrence-of-assistance framework of [Laustsen, Verstraete, and van Enk](https://arxiv.org/abs/quant-ph/0206192) (`LaustsenEtAl2003`), and local-filter covariance as developed by [Verstraete, Dehaene, and De Moor](https://arxiv.org/abs/quant-ph/0011111) (`VerstraeteEtAl2001`). The project derives the dephasing-compatible inequality `C <= eta C_a` and the resulting two-slot witness within its stated causal model.

The physical distinctions matter. Giving the simulator a dephasing error flag, access to the environment, a second coherent storage system, or the second input before the gap changes the free set. The theorem does not characterize those alternatives. Mandatory complete resets at both laboratories between noisy blocks yield the stated exact block product corollary. For uninterrupted many-slot memories, repeating the two-slot protocol gives an upper bound; exact general noisy-memory multiplicativity is not claimed.

## Recent work and the scope of a sampling statement

The following 2026 sources address adjacent questions. Their distinctions are relevant even when their circuits or resource formulas have a similar appearance.

| Primary source and status | Relevant finding or question | Scope distinction |
|---|---|---|
| [Hart, *Optimal two-qubit gate-cutting cost and measures of nonlocality*](https://arxiv.org/html/2609.30141v1), September 2026 preprint; `Hart2026` | Starts from the known two-qubit optimal cost and derives sharp relations to entangling power, gate typicality, operator entanglement, Schmidt strength, and maximum product-input concurrence. | Relating a gate's Schmidt spectrum to cost is distinct from restricting a simulator's temporal memory. This project does not claim the single-gate formula or its Rényi-1/2 interpretation. |
| [Gragera Garces, Drăgoi, and Pira, *Entanglement geometry separates circuit cutting, classical hardness, and trainability*](https://arxiv.org/abs/2607.17872), July 2026 preprint; `GrageraGarcesEtAl2026` | Its public abstract studies circuit families with controlled seam bond dimension and the relation among cutting overhead, classical simulation, and trainability. | A known restricted circuit family can have small effective cut dimension. The present target is a universal slot process that must accept arbitrary external quantum inputs. The comparison here is limited to the publicly retrieved abstract. |
| [Harada, Wada, Yamamoto, and Endo, *Learning enables exponential-to-polynomial sampling overhead scaling in quantum divide-and-conquer for tree-structured circuits*](https://arxiv.org/html/2512.19623v2), June 2026 preprint revision; `HaradaEtAl2026` | Learns effective observables and uses controlled bias to achieve measurement cost `O-tilde(d^3 K^3 / epsilon^2)` for finite rooted trees, including learning cost; also proves a separation from prespecified learning-free wire cuts. | Its tree is a circuit-fragment structure and its task is observable-specific estimation. The forest here is a graph of local coherence epochs, used to bound a universal linear QPD. Observable learning changes the task and estimator class. |

These comparisons prevent an overinterpretation of the extent. Sampling a decomposition with total absolute weight `gamma` gives a bounded-range Monte Carlo cost proportional to `gamma^2` at fixed accuracy, by [Hoeffding's inequality](https://doi.org/10.1080/01621459.1963.10500830) (`Hoeffding1963`). It does not follow that every estimator of every fixed observable requires that many measurements. Circuit-specific simplifications, direct variance bounds, tomography, adaptive estimation, and controlled bias can change that question. Harrow and Lowe's time-like-cut analysis already illustrates that the variance can yield a better sample bound than the generic squared-extent estimate.

The [precision result](../science/precision-calibration.md) is correspondingly a robustness statement for normalized approximate signed combs in the stated strategy-distance convention. It bounds how much the QPD extent can fall at a fixed approximation error. It is not a universal minimax measurement lower bound.

## Attribution map

| Component used in this repository | Attribution |
|---|---|
| Single-edge pure-state robustness and its Schmidt-coefficient formula | Vidal–Tarrach |
| Collective wire-cut value and teleportation reduction | Brenner–Piveteau–Sutter and the preceding collective-cutting literature |
| Parallel ancilla-free cutting | Harada–Wada–Yamamoto |
| Paired local coherences and low-ancilla interference constructions | Harrow–Lowe; the explicit sequential wire resource implementation is given here |
| General two-qubit gate upper bound with unknown interleavings | Schmitt–Piveteau–Sutter, Theorem 6.4 |
| Classical record and signed-instrument treatment | Circuit-cutting side-information framework of Piveteau–Schmitt–Sutter |
| Combs and strategy norms | Chiribella–D'Ariano–Perinotti; Gutoski |
| Concurrence, assistance, and filtering ingredients | Wootters; Laustsen–Verstraete–van Enk; Verstraete–Dehaene–De Moor |
| Exact common-refinement reset law, its forest converse, and specified two-slot dephasing law | Derived in this repository, under the explicit model assumptions |

The last row identifies the mathematical claims to assess in this project. It does not turn the search record into a proof of novelty, and it does not transfer the claims to broader models than those stated in the scientific notes.
