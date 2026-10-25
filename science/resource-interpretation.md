# Memory timing, noise and the cost of reconstruction

## What the memory preserves

Collective cutting uses coherent alternatives associated with several operation slots. In the wire construction, each physical sample contains a locally prepared two-string superposition. A single qubit keeps track of the two alternatives while their resource qubits are emitted in order. The laboratories share classical labels and communicate teleportation outcomes; they never share a physical entangled resource across the laboratory boundary.

The useful correlations therefore persist **in time within each laboratory**. Increasing the dimension of a local memory is unnecessary for the optimal wire construction, but destroying its correlations with the past changes which collective decompositions are possible. The [reset theorem](reset-schedules.md) gives a converse against every allowed adaptive implementation, not just that particular two-string construction.

This distinction explains the connection to established optimal collective cuts. [Brenner, Piveteau and Sutter](https://arxiv.org/abs/2302.03366) obtain the unrestricted wire cost, and [Harrow and Lowe](https://arxiv.org/abs/2403.01018) provide constant-ancilla coherent constructions. The contribution of the reset analysis is to determine the exact cost after specified temporal coherence opportunities are removed.

## A complete scheduling example

Take six ordered qubit-wire slots. Suppose Alice's epochs are $`[1,2,3]\mid[4,5,6]`$ and Bob's are $`[1,2]\mid[3,4,5]\mid[6]`$. Their common intervals have lengths $`2,1,2,1`$. The exact extent is

```math
\Gamma=7\cdot3\cdot7\cdot3=441.
```

| Coherence schedule for six wires | Common interval lengths | Exact extent |
|---|---|---:|
| No intermediate breaks at either laboratory | 6 | 127 |
| Aligned three-slot epochs | 3, 3 | 225 |
| The asynchronous epochs above | 2, 1, 2, 1 | 441 |
| A break at every gap on at least one side | 1, 1, 1, 1, 1, 1 | 729 |

These are different allowed memory schedules for the same universal input/output interface. Classical communication is unlimited in every row. The asynchronous cost cannot be reduced by putting more quantum storage inside the individual epochs: the forest witness already permits arbitrary local dimension there.

The epoch-overlap graph is the mathematical reason. An epoch at Alice can overlap several epochs at Bob, and conversely. Because both partitions consist of consecutive time intervals, each new overlap introduces at least one new epoch vertex. The graph has no cycle. Its [witness norm](forest-witness.md) forces the common-interval factors to multiply, even when a vertex entangles all its incident local registers.

## Synchronization at a fixed lifetime budget

Let $`n`$ be even and allow a maximum uninterrupted epoch of two slots at each laboratory. Aligned boundaries give common intervals of length two. Shifting one laboratory's boundaries by one slot gives a break at every gap; the first and last epochs may be shorter.

```math
\Gamma_{\mathrm{aligned}}=7^{n/2},
\qquad
\Gamma_{\mathrm{staggered}}=3^n,
\qquad
\frac{\Gamma_{\mathrm{staggered}}}{\Gamma_{\mathrm{aligned}}}
=\left(\frac97\right)^{n/2}.
```

Both schedules obey the same maximum local lifetime budget. Their relative timing produces an exponential ratio in signed extent. The ratio of the corresponding generic squared-extent sampling bounds is $`(9/7)^n`$. Both costs still grow exponentially; this comparison does not establish that a large cut circuit is practical.

The boundaries here are complete information-breaking operations on the entire private memory. A finite physical qubit lifetime alone does not imply such a boundary. For example, transferring a quantum state into a fresh qubit can preserve information beyond the lifetime of one carrier. That transferred state remains charged quantum memory under the model.

## The sharp space distinction for wires

If either laboratory retains only classical information between every pair of slots, the common intervals are singletons, even when the other laboratory has unlimited coherent memory. Consequently,

```math
\Gamma_{\mathrm{one\ side\ classical}}
=\prod_{j=1}^n(2d_j-1).
```

If both laboratories can retain one qubit without an intervening break, the [sequential construction](wire-construction.md) attains the unrestricted value

```math
\Gamma_{\mathrm{one\ qubit\ each}}
=2\prod_{j=1}^n d_j-1.
```

For at least two nontrivial wires, this is a strict improvement. A retained output or input register would count toward the memory on that side. Ancilla-free parallel cutting permits joint operations on all available ports and therefore addresses a different access model; it does not contradict this sequential lower bound.

## Noisy coherence has a continuous value

For two qubit wires, define $`r=\eta_A\eta_B`$ using the independent dephasing parameters in the [noisy-memory theorem](dephasing-memory.md). Then

```math
g(r)=5+\frac4{1+r}.
```

| Surviving joint coherence $`r`$ | Exact two-slot extent $`g(r)`$ |
|---:|---:|
| 0 | 9 |
| $`1/4`$ | $`41/5=8.2`$ |
| $`1/2`$ | $`23/3\approx7.667`$ |
| 1 | 7 |

Every $`r>0`$ improves on independent single-slot cutting. If both laboratories must undergo a complete memory break between successive two-slot blocks and the noise instances are fresh and independent across blocks, the exact extent for $`2m`$ slots is $`g(r)^m`$. A product of the two-slot witnesses proves the converse, as shown in [dephasing memory](dephasing-memory.md). If those block resets are optional, the same expression is an attainable upper bound; it does not determine the unrestricted many-slot optimum with continuously noisy memories.

For stationary exponential dephasing, one may substitute $`\eta_s=\exp(-t/T_{2,s})`$ as a physical model for a gap of duration $`t`$. The exact theorem itself is stated for the channels $`\mathcal D_{\eta_s}`$, without assuming that a measured coherence time certifies stationarity, independence, or the absence of additional gate noise.

In particular, independent marginal calibration is insufficient to certify the product-noise hypothesis. Perfectly correlated unflagged phase flips can leave each memory marginally completely dephased while preserving the joint temporal resource needed for extent seven. The [counterexample](dephasing-memory.md) identifies the relevant joint correlation directly.

## Quantum, classical and precision resources

| Resource | Wire construction inside one common interval | Two-slot dephasing construction |
|---|---|---|
| Persistent private quantum storage | At most one qubit at each laboratory | At most one qubit at each laboratory across the noisy gap |
| Transient quantum workspace | Current input/resource ports and local measurement workspace | Current input/resource ports and local measurement workspace |
| Spatial entanglement or quantum link | None | None |
| Classical information | Two basis-string labels, phases, sampled signs and teleportation outcomes | One of four resource families, local twirl labels, signs and teleportation outcomes |
| Classical label size | $`O(\sum_{j\in I}\log d_j)`$ bits | Constant per two-slot block |
| State preparation | Explicit sequential two-string states; no amplitude-loading oracle | Product local Bell resources, dephasing and finite unitary twirls |
| Classical communication | Standard teleportation outcomes; $`\lceil\log_2(d_j^2)\rceil`$ bits for a fixed-length outcome label on a dimension-$`d_j`$ wire | Two bits per qubit teleportation |
| Precision requirement | Physical implementation and sampling precision | Physical implementation, calibrated dephasing parameters, coupled coefficient rounding and sampling precision |

The number of possible two-string labels is exponential, but a sampled label is generated and processed directly. It does not require storing an exponential table or loading an arbitrary amplitude vector. For qubits, the local sequential state generator uses elementary Clifford operations. General qudit labels require the corresponding controlled basis-state preparation operations; no hardware-independent elementary-gate cost is claimed for arbitrary dimension.

The [general-gate theorem](gate-cuts.md) uses the published protected-resource construction for the sufficiency argument. It permits quantum memory growing with the number of gate slots within a common interval. The optimal extent is proved in that allowed model; a minimum-memory gate implementation is not claimed by that construction.

Calibration is an additional measurement task. The [precision account](precision-calibration.md) provides finite-confidence parameter estimates and propagates their error through the signed reconstruction. It explicitly charges these measurements separately from the circuit-cutting samples.

## From signed extent to a sampling guarantee

For a decomposition with extent $`\Gamma`$, sample term $`\ell`$ with probability $`|a_\ell|/\Gamma`$. Run its physical instrument, record its score $`s_h`$, and obtain a tester outcome $`Y\in[-1,1]`$. The random variable

```math
X=\Gamma\,\operatorname{sgn}(a_\ell)\,s_hY
```

is unbiased for the target expectation when the process identity is exact, and satisfies $`|X|\leq\Gamma`$. Independent repetitions therefore obey the sufficient Hoeffding bound

```math
N\geq\frac{2\Gamma^2}{\epsilon_{\mathrm{stat}}^2}
\log\frac2{\delta_{\mathrm{stat}}}.
```

It gives statistical error at most $`\epsilon_{\mathrm{stat}}`$ with failure probability at most $`\delta_{\mathrm{stat}}`$. A separately controlled calibration or implementation bias adds to the statistical error. This bound does not assert that every estimator needs $`\Gamma^2`$ samples. Variance-aware methods, known observables, circuit structure, or controlled bias can change the sampling problem; [related work](../references/related-work.md) discusses the corresponding literature.

## What the exact frontiers establish

The reset result identifies the optimal universal signed cost from the complete coherence schedule. The noisy two-slot result identifies it from the specified independent memory channels. Their common message is that local storage must be described by its access times and physical transmission of quantum correlations, as well as by its dimension.

These are exact statements within the [causal model](model.md). Complete reset schedules, partial noise, unrestricted many-slot memories, and circuit-specific inference remain distinct resource problems. The constructions and lower bounds provide a controlled way to compare them without exchanging one model's assumptions for another's conclusion.
