# From a single cut to quantum memory

Suppose a quantum computation must be run in two laboratories that can exchange classical messages but have no quantum link or shared entangled state. An operation in the desired computation transfers a qubit between them. Circuit cutting replaces that transfer by physical local experiments and combines their final data with signed weights.

One cut is already a quantum-information problem. Several cuts introduce a second question: can a laboratory preserve a coherent alternative from an earlier cut until a later one? This explanation develops that connection through the [settled 30-milestone map](milestones.md). The [Watrous bridge](anchor.md) supplies the textbook pointers and notation conventions. Exact definitions and proofs remain in the linked scientific pages.

## 1. A physical experiment and its signed weight

**Background connection: M01–M09.** A density operator describes a physical quantum state. A completely positive, trace-preserving channel describes an operation when all its outcomes are retained. An instrument keeps the outcomes separate: its positive branches add to the complete channel, and the trace of a branch is its actual probability. A rare successful outcome therefore cannot be supplied for free as a normalized deterministic operation.

For a target process $`\mathcal T`$, a signed decomposition has the form

```math
\mathcal T=\sum_\ell a_\ell\mathcal F_\ell,
\qquad \Gamma=\sum_\ell|a_\ell|.
```

Each $`\mathcal F_\ell`$ comes from a complete physical instrument with a classical score between minus one and one. Its physical outcomes occur with ordinary nonnegative probabilities. Negative numbers enter the classical reconstruction. The scored map itself can fail to be a channel; this is compatible with each underlying experiment being physical.

To execute the decomposition, draw label $`\ell`$ with probability $`|a_\ell|/\Gamma`$. Run its instrument and multiply a final bounded measurement outcome by the coefficient sign, the instrument score, and $`\Gamma`$. The average reproduces the target expectation. The internal label and instrument records remain private to the cutter; the external quantum computation uses the declared ports. These are the conventions of [the causal model](../science/model.md#signed-instruments-and-the-cost-being-minimized).

The magnitude $`\Gamma`$ controls a general bound on this estimator's fluctuations. It does not determine the minimum measurements for every task that might exploit a known observable or a special circuit family.

## 2. Why a single qubit cut has extent three

**Connections: M05–M10 and M13.** The Choi test probes a channel with half of an entangled state and retains the other half as a reference. It turns a statement about an unknown input into a statement about correlations with that reference. For the ideal qubit transfer, the normalized Choi state is

```math
\Phi=|\Phi^+\rangle\langle\Phi^+|,
\qquad |\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

The reference stays on the input side, while the ideal output belongs on the receiving side. Without a quantum link or shared spatial entanglement, a physical local protocol produces a separable state across this division. Its overlap with $`\Phi`$ is at most one half. Therefore

```math
W=4\Phi-I_4
```

has expectation between minus one and one on every separable state, but expectation three on the ideal Choi state. Retaining physical branch probabilities and bounded scores preserves the same absolute bound. Applying $`W`$ to a signed decomposition gives

```math
3=\mathrm{Tr}(W\Phi)
\leq\sum_\ell|a_\ell|=\Gamma.
```

This is a witness lower bound: it applies to every allowed decomposition, not only to a selected construction.

The bound is attained. Let $`R=(I_4-\Phi)/3`$, and define two separable states

```math
\rho_+=\tfrac12\Phi+\tfrac12R,
\qquad \rho_-=R.
```

They obey $`\Phi=2\rho_+-\rho_-`$. They can be prepared with local states and shared classical random rotations; the finite construction is described in [Dephasing memory, Section 2](../science/dephasing-memory.md#2-four-physical-resources-and-their-full-matrix-identity). Teleportation with each resource gives a physical local cutting channel. For example, if $`\mathcal R(X)=\mathrm{Tr}(X)I_2/2`$ is complete replacement by the maximally mixed state, these two channels are

```math
\mathcal E_+=\frac{\mathrm{id}+2\mathcal R}{3},
\qquad
\mathcal E_-=\frac{4\mathcal R-\mathrm{id}}{3},
\qquad
\mathrm{id}=2\mathcal E_+-\mathcal E_-.
```

The minus sign in the formula for $`\mathcal E_-`$ does not mean it is unphysical: its Choi state is the positive separable state $`\rho_-`$. The outer decomposition has weights two and minus one, hence extent three. One samples its two channels with probabilities two thirds and one third, and weights their outcomes by plus three and minus three.

The normalized Choi convention matters throughout this argument. The [source bridge](anchor.md) explains how the book's unnormalized channel matrix is reordered and divided by the input dimension to obtain the project convention.

## 3. Two operations make memory visible

**Connections: M10–M12 and M18–M19.** Cutting two qubit wires independently multiplies their extents: $`3\times3=9`$. An uninterrupted collective construction instead treats the two wires' formal Choi state as a dimension-four maximally entangled state, whose optimal separable signed extent is $`2\times4-1=7`$. This collective value belongs to the established wire-cutting literature, as explained in [related work](../references/related-work.md#closest-circuit-cutting-results).

A parallel resource identity alone does not explain how to run the protocol at two different times. Here, the first output must leave before the second input arrives. A future input cannot be borrowed early, and a released output cannot be retained as private storage.

The [online construction](../science/wire-construction.md) resolves this by sampling a pair of classical basis strings. At each laboratory it prepares a superposition of those two alternatives and emits their resource symbols in order. A single persistent qubit carries the binary branch while later symbols remain to be emitted. At the final differing symbol, an isometry transfers the branch into that emitted symbol and returns the private memory to a fixed pure state. Earlier outputs may already have interacted with an external reference; the cleanup is an operator identity and remains valid in that situation.

Each resource port is then consumed by teleportation at the actual slot. A physical sample uses no entanglement shared between laboratories. Its useful coherence lies between different times inside each laboratory. The strings need only linear classical storage for qubit wires and can be sampled without an exponentially large table.

If either laboratory undergoes a genuine entanglement-breaking reset of its entire private memory at the gap, this temporal connection is severed. The exact optimum becomes nine, even if the other laboratory has unlimited memory. Increasing storage within the surviving epochs cannot repair the missing connection.

## 4. From one memory break to a complete schedule

**Connections: M13–M19.** For one pure bipartite edge with Schmidt coefficients $`s_i`$, the optimal signed extent is

```math
g=2\left(\sum_i s_i\right)^2-1.
```

For a maximally entangled edge of dimension $`D`$, all $`D`$ coefficients equal $`1/\sqrt D`$, giving $`g=2D-1`$. The single-edge formula and its robustness interpretation are established ingredients. The [forest proof](../science/forest-witness.md) addresses how such factors combine when one vertex can hold a joint state of several incident registers.

Associate a vertex with each uninterrupted local coherence epoch. An interval where an Alice epoch overlaps a Bob epoch becomes an edge. Two partitions of a line produce a forest: moving forward to a new overlap always introduces at least one new epoch vertex. A leaf can therefore be removed without encountering a cycle.

For the converse, first refine a complete physical history, including the measurement-and-preparation components of each genuine entanglement-breaking reset. Each branch factors positively over the epoch vertices, and the weights sum to one. Joint processing inside an epoch remains allowed. The forest witness is bounded by eliminating leaves while preserving a trace-norm bound on the remaining Hermitian operators. Its target expectation is the product of the edge factors. The matching construction runs separately on each common interval.

Consequently, if $`\mathcal I`$ contains the intervals ending whenever either laboratory resets,

```math
\Gamma_{\mathrm{reset}}
=\prod_{I\in\mathcal I}(2D_I-1),
\qquad D_I=\prod_{j\in I}d_j.
```

The two schedules must be combined before evaluating the cost. For six qubit slots, consider the following example.

| Schedule | Alice's epochs | Bob's epochs | Common interval lengths | Extent |
|---|---|---|---|---:|
| Aligned | 12 / 34 / 56 | 12 / 34 / 56 | 2, 2, 2 | 343 |
| Staggered | 12 / 34 / 56 | 1 / 23 / 45 / 6 | 1, 1, 1, 1, 1, 1 | 729 |

Here `12` means slots 1 and 2 belong to the same epoch; a slash marks a reset. Both laboratories have a maximum uninterrupted epoch of two slots in either schedule. Alignment changes the collective opportunities. The [resource interpretation](../science/resource-interpretation.md#synchronization-at-a-fixed-lifetime-budget) gives the exponential ratio for longer streams.

The forest property is essential to this proof. The same product witness takes value three on a four-cycle of suitable local Bell states, exceeding its required unit bound. The project supplies that counterexample rather than extending the tree argument to arbitrary graphs.

## 5. What changes for gate cuts

**Connections: M20–M21.** A two-qubit unitary has input and output registers at both laboratories. Its normalized Choi vector can be written in local orthonormal operator bases, with Schmidt coefficients given by the absolute values of its normalized KAK coefficients $`u_{j\alpha}`$. Define

```math
\chi_j=\left(\sum_\alpha|u_{j\alpha}|\right)^2.
```

For one common interval, the Schmidt sums multiply and give factor $`2\prod_{j\in I}\chi_j-1`$. The forest converse then gives the exact gate reset law. A product gate has $`\chi=1`$, CNOT has $`\chi=2`$, and SWAP has $`\chi=4`$.

Attainment requires a further ingredient. Teleporting a non-Clifford gate does not generally leave corrections that can all be executed locally. The construction attributed to Schmitt–Piveteau–Sutter uses a sampled pair of local resource alternatives and an outcome-dependent sign. The same sign is assigned to all resource terms associated with that pair; unwanted contributions cancel separately for each Bell record, while the desired commutation signs cancel in the score. The [gate page](../science/gate-cuts.md) proves the identity with arbitrary operations between the slots.

The actual output qubits still leave on time. The final classical sample can be signed after later measurement records become available. Protected resource qubits for later slots are charged quantum storage. This general gate construction establishes the exact extent with its stated sufficient workspace; it does not establish the one-persistent-qubit storage bound of the wire construction.

## 6. Partial memory noise needs a different converse

**Connections: M11 and M22–M25.** Complete resets split epochs. Partial dephasing instead weakens the coherence inside a local temporal state. The noisy theorem allows one persistent qubit per laboratory between two wire slots and applies independent channels

```math
\mathcal D_\eta(\rho)
=\frac{1+\eta}{2}\rho+\frac{1-\eta}{2}Z\rho Z.
```

The parameter $`\eta=1`$ means no dephasing, and $`\eta=0`$ means complete dephasing. The error flags remain inaccessible. These assumptions describe the actual gap channel conditional on the available pre-gap classical history, rather than only its observed marginals.

A local Bell pair whose second half crosses the noisy gap has coherence $`\eta`$. Local operations before and after the gap act as filters on its two-time state. The concurrence $`C`$ is the minimum average pure-state concurrence over decompositions of a mixed state, while concurrence of assistance $`C_a`$ is the maximum such average. The project proves that the allowed local temporal states satisfy

```math
C(\sigma)\leq\eta\,C_a(\sigma).
```

Both roofs acquire the same factor under invertible local filtering, singular filters remove the relevant entanglement, and mixtures preserve this inequality. These facts give a restriction on all allowed temporal states, including states selected by adaptive classical histories. Exposing the hidden noise labels would destroy this restriction and change the model.

With $`r=\eta_A\eta_B`$ and the one-wire witnesses $`W_i=4\Phi_i-I`$, the dual operator

```math
Q_r=\frac{W_1W_2+r(W_1+W_2-I)}{1+r}
```

is bounded by one on every allowed scored atom. Its ideal value is $`5+4/(1+r)`$. A four-resource identity attains this value, giving the [exact two-slot law](../science/dephasing-memory.md).

For example, if both memories have $`\eta=1/2`$, then $`r=1/4`$ and $`\Gamma_2=41/5=8.2`$. Any nonzero product coherence helps compared with the value nine of independent single cuts, within this specified noise model.

Two boundaries clarify the physics. Perfectly correlated phase flips can give the same completely dephased marginal memories as independent noise, yet attain extent seven. Giving Alice the actual second input before the gap can also avoid the prescribed temporal resource restriction. The [counterexamples](../science/dephasing-memory.md#6-endpoints-repeated-blocks-and-scope-tests) show why joint noise and actual port availability belong in the theorem statement.

For many prescribed two-slot blocks, the exact factors multiply when both laboratories completely reset between blocks and the noise instances are fresh across blocks. If a cutter may retain coherence continuously across those boundaries, the product construction remains an upper bound; its optimality has not been established.

## 7. Approximation, calibration and sampling have different roles

**Connections: M26–M29.** An approximate universal decomposition is assessed against every causal tester, including one retaining quantum references. The strategy norm measures the largest trace-norm difference in such an experiment. This project defines its approximation parameter as **half** that norm. A bounded observable with outcomes in $`[-1,1]`$ can have bias as large as the full norm.

An extent witness converts a trace-distance error into a lower bound on the remaining extent. If the reconstructed Choi operator has exactly the same trace as the target, the witness can be centered by a scalar identity. Its spectral range, rather than twice its operator norm, then controls the bound. This is the source of the sharper trace-normalized approximation statements in [Precision and calibration](../science/precision-calibration.md#2-approximation-bounds-from-witness-spectral-ranges). They are lower bounds; the full approximate optima are not claimed known.

Calibration asks a separate implementation question. Suppose the two-slot coefficients use a nominal product parameter $`r_0`$, while the actual independent memory channels have product $`r`$. The reconstructed Choi operator is exactly

```math
\widetilde J
=\Phi_1\Phi_2+\frac{r-r_0}{36(1+r_0)}W_1W_2,
```

and its full strategy error is $`|r-r_0|/(1+r_0)`$. A nonzero mismatch gives negative Choi eigenvalues. Each run remains physical, but its signed average is no longer a physical channel. Consequently, error propagation cannot be justified by simply assigning channel contractivity to that average.

The project instead computes the exact signed Pauli-path coefficients of repeated blocks. It also proves a general product error bound for genuine blockwise process composition using the strategy-norm unit ball. Hidden environments connecting blocks require a different model from isolated block marginals.

Finally, uncertainty in calibration and fluctuations in execution consume different samples. Ramsey measurements estimate the two local coherence factors within the assumed channel family. The [charged calibration procedure](../science/precision-calibration.md#5-a-charged-calibration-procedure) propagates their finite-confidence error, accounts for coefficient precision, then gives a separate number of circuit executions for the final estimator. Marginal Ramsey measurements alone do not establish that the two memories' noise is independent.

## 8. Putting the result together

**Connection: M30.** The reset theorem determines the exact universal signed cost from two complete coherence schedules. The noisy two-slot theorem determines it from two specified independent local memory channels. Both connect a physical temporal resource to an attainable signed extent, with a converse covering arbitrary allowed adaptive instruments.

The construction and the lower bound have different jobs. A resource identity, sampler and causal implementation establish an attainable cost. A witness valid on the entire allowed class establishes that no smaller extent is possible in that model. The [finite verification suite](../verification/README.md) checks identities, examples and nontrivial causal executions; the analytical proofs establish the universal statements.

The resulting scope is precise. Persistent quantum storage includes data or ancillary systems retained across a gap. Genuine local entanglement-breaking connections differ from noisy marginals with recoverable information elsewhere. The general gate construction has its own workspace count. The noisy product theorem requires its imposed resets and fresh environments. A universal extent bound does not rule out lower measurement costs for a learned observable or a promised circuit family.

Use the [scientific reading map](../science/README.md) to follow the complete proofs, the [source bridge](anchor.md) for the textbook-to-project translation, and the [30 milestones](milestones.md) to connect the components into the whole account.
