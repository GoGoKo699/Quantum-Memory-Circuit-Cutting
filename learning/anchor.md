# Watrous: the source-to-project bridge

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. Its [author page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the author's manuscript and [errata](https://cs.uwaterloo.ca/~watrous/TQI/TQI.errata.pdf). The pointers below were checked on **25 October 2026** against the **standard-layout individual chapter PDFs**. Page numbers refer to the numbers printed on those pages; a PDF link's `#page=` fragment instead counts pages within that chapter file. The author manuscript and the published book have different typo histories, as the errata explain.

Use this page alongside the [worked explanation](tutorial.md) and [30-milestone map](milestones.md). Watrous supplies a common mathematical language. The project's causal resource restrictions, constructions and converse arguments have their own homes in the [scientific account](../science/README.md).

## 1. A focused source map

| Topic | Verified location in the anchor | Connection to the project |
|---|---|---|
| Density operators and states | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=18), §1.1.2, p.18, Eq.(1.97); [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=5), §2.1.2, p.62, Definition 2.5 | Physical states and positive branch operators |
| Partial trace and vectorization | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=22), §1.1.2, pp.22–24, Eqs.(1.119)–(1.134) | Register order and Choi calculations |
| Schmidt decomposition and matrix norms | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=31), §1.1.3, p.31, Eqs.(1.162)–(1.164); pp.32–33, Eqs.(1.165)–(1.175) | Pure-edge coefficients, trace norm and Hölder bounds |
| Channels, complete positivity and trace preservation | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=16), §2.2.1, p.73, Definition 2.13; §2.2.2, Theorem 2.22, p.82, and Theorem 2.26, p.87 | Operations valid on entangled inputs; Kraus representations |
| Choi representation | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=21), §2.2.2, p.78, Eqs.(2.64)–(2.66) | The normalization and permutation translated below |
| Measurements and instruments | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=44), §2.3.1, p.101, Definition 2.34 and Eq.(2.201); [§2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=55), pp.112–113, Eqs.(2.258)–(2.262) | Born probabilities; a physical record with a quantum output |
| Classical registers and dephasing | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=37), §2.2.3, pp.94–96, Eqs.(2.162)–(2.170) | Persistent classical history and the complete-dephasing endpoint |
| Completely bounded trace norm | [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=47), §3.3.2, p.170, Definition 3.43 and Eq.(3.256); Theorem 3.46, p.173 | One-slot universal error with an arbitrary reference |
| Separable states | [Chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf#page=2), §6.1.1, p.311, Definitions 6.1–6.2; Proposition 6.5, p.313 | Positive product decompositions across a specified division |
| Separable maps, Choi grouping and LOCC | [Chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf#page=16), §6.1.2, Definition 6.17, p.325; Proposition 6.22, p.328; Definition 6.25, pp.330–331; Proposition 6.26, p.332 | Local instruments and classical communication; grouping each party's input reference with its output |
| Teleportation | [Chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf#page=50), §6.3.1, Scenario 6.46, pp.359–360; Theorem 6.47, pp.360–361; Corollary 6.49, pp.364–365 | Converting a resource identity into an operation on an unknown input |
| Entanglement-breaking channels | [Chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf#page=75), §6.4, Exercise 6.1, p.384, Eqs.(6.433)–(6.434) | The measure-and-prepare form of a complete memory break |
| A convex-roof example | [Chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf#page=76), §6.4, Exercise 6.3, p.385, Eqs.(6.437)–(6.438) | Preparation for the distinct concurrence roofs used in the noisy-memory proof |

The relevant subsection titles are §2.3.1, “Two equivalent definitions of measurements”; §2.3.2, “Basic notions concerning measurements”; §6.1.1, “Separable operators and states”; and §6.1.2, “Separable maps and the LOCC paradigm.” Instruments occur inside §2.3.2. The entanglement-breaking characterization is assigned as **Exercise 6.1**. Neither that exercise nor the convex-roof exercise should be cited as a numbered theorem proved in the book.

## 2. Translating the Choi convention

Three choices must be kept separate: matrix vectorization, tensor-factor order, and normalization. Watrous writes $`A^*`$ for the adjoint; this repository usually writes $`A^\dagger`$. The transpose $`A^{\mathsf T}`$ and entrywise conjugate $`\overline A`$ are different operations. In the book, $`\Phi`$ often denotes a channel; here $`\Phi_d`$ denotes a normalized maximally entangled **state operator**.

### A single input

Let $`A:X\to Y`$, with input dimension $`d=\dim X`$, and fix the bases used by the Choi construction. In the convention of Chapter 1,

```math
\mathrm{vec}_{\mathrm W}(A)
=\sum_{y,x} A_{yx}\lvert y\rangle_Y\otimes\lvert x\rangle_X.
```

For a map $`\mathcal E:L(X)\to L(Y)`$, Watrous's Choi operator is in output–input order and uses an unnormalized entangled vector. The project's Bell-probe state uses reference–output order:

```math
\begin{aligned}
J_{\mathrm W}(\mathcal E)
&=\sum_{x,x'}\mathcal E(\lvert x\rangle\langle x'\rvert)
       \otimes\lvert x\rangle\langle x'\rvert,\\
\lvert\Phi_d\rangle_{RX}
&=\frac1{\sqrt d}\sum_x\lvert x\rangle_R\lvert x\rangle_X,\\
J_{\mathrm{repo}}(\mathcal E)
&=(\mathrm{id}_R\otimes\mathcal E)
   (\lvert\Phi_d\rangle\langle\Phi_d\rvert).
\end{aligned}
```

Let $`S:Y\otimes X\to X\otimes Y`$ exchange the factors, identifying the second factor of $`J_{\mathrm W}`$ with the reference $`R`$. Direct substitution gives

```math
\boxed{J_{\mathrm{repo}}(\mathcal E)
=\frac{S J_{\mathrm W}(\mathcal E)S^\dagger}{d}.}
```

For equal factor spaces, this is $`J_{\mathrm{repo}}=(\mathrm{SWAP}\,J_{\mathrm W}\,\mathrm{SWAP})/d`$. No partial transpose is part of this translation. In particular, a trace-preserving map satisfies

```math
\mathrm{Tr}J_{\mathrm W}=d,\qquad
\mathrm{Tr}J_{\mathrm{repo}}=1,\qquad
\mathrm{Tr}_Y J_{\mathrm{repo}}=I_R/d.
```

A unitary $`U`$ therefore has the project's normalized Choi vector

```math
\lvert J(U)\rangle
=(I_R\otimes U)\lvert\Phi_d\rangle
=\frac{S\mathrm{vec}_{\mathrm W}(U)}{\sqrt d}.
```

For a qubit wire, $`d=2`$. For a two-qubit gate, the **total input dimension is $`d=4`$**. After that gate's Choi state is formed, its factors are regrouped as Alice's reference and output versus Bob's reference and output. Regrouping is a permutation, so it introduces no further numerical factor. Proposition 6.22 makes the analogous laboratory grouping explicit in the book's ordering. The book's natural representation $`K(\mathcal E)`$ is a different matrix representation from $`J_{\mathrm W}(\mathcal E)`$.

### Several ordered slots

The Bell tester in [the model](../science/model.md#normalized-choi-tests-and-lower-bounds) delivers a fresh half-pair at each actual input time. If those inputs have dimensions $`d_1,\ldots,d_m`$, set

```math
D_{\mathrm{in}}=\prod_{j=1}^m d_j.
```

For a conventional unnormalized comb Choi operator $`C_{\mathrm{unnorm}}`$, the same translation is

```math
J_{\mathrm{repo}}(\mathcal C)
=\frac{P C_{\mathrm{unnorm}}P^\dagger}{D_{\mathrm{in}}},
```

where $`P`$ puts the named registers into the order used in the particular proof. This is a product of **input normalization factors**, including for a process with memory. It does not assert that the process or its Choi operator factors over time. The ideal independent-slot target does factor. Thus $`m`$ qubit wire slots use $`D_{\mathrm{in}}=2^m`$, while $`m`$ two-qubit gate slots use $`D_{\mathrm{in}}=4^m`$.

Comb causality and allowable interleavings require the additional research framework identified in Section 5 below. A physical slot cannot be moved earlier merely because its tensor factor can be moved on paper.

## 3. From physical instruments to signed atoms

The instrument language in Chapter 2 gives a family of completely positive branches whose sum is a channel. In the project, a complete causal instrument $`\{\mathcal C_h\}_h`$ is paired with a classical score $`s_h\in[-1,1]`$:

```math
\mathcal F=\sum_h s_h\mathcal C_h.
```

The underlying experiment is physical. Its scored linear map $`\mathcal F`$ can fail to be completely positive or trace preserving. On the project's normalized Bell tester, write

```math
p_h=\mathrm{Tr}J(\mathcal C_h),\qquad
\sum_h p_h=1.
```

These are probabilities **for this tester**. If $`p_h>0`$, the conditional state is $`J(\mathcal C_h)/p_h`$. Keeping $`p_h`$ is what lets a branchwise witness bound pass to a whole scored experiment. If each branch obeys

```math
\left|\mathrm{Tr}\bigl[WJ(\mathcal C_h)\bigr]\right|\leq p_h,
```

then

```math
\left|\mathrm{Tr}\bigl[WJ(\mathcal F)\bigr]\right|
\leq\sum_h |s_h|p_h\leq1.
```

This calculation explains why freely supplying a normalized successful postselection branch would change the model. It also explains why a complete instrument, including all its outcomes, is the unit of the resource accounting.

Two further distinctions are needed for the project:

- **Spatial separability does not specify temporal memory.** Alice may hold entanglement among her own registers from different slots while remaining unentangled with Bob. A complete local memory break imposes an additional restriction. The branch factorization over coherence epochs is proved in [reset schedules](../science/reset-schedules.md); it does not follow from the word “LOCC” alone.
- **An instrument is more general than a randomized product channel.** Example 6.21, pp.326–327, helps locate this distinction in the anchor. In the gate construction, retaining and jointly scoring private outcomes is essential; no communication between laboratories is needed during its quantum execution. The exact atom convention is fixed by [the model](../science/model.md#signed-instruments-and-the-cost-being-minimized).

The book's Definition 6.25 uses finite LOCC protocols. The project's converse extends to limits of those protocols by continuity of its finite-dimensional witness functionals; that limiting statement is part of the project's argument.

### Teleportation conventions

The teleportation section provides the mechanism for consuming an entangled resource at an input's arrival time. The project's resource expansions then supply a signed identity to which that mechanism is applied linearly. Book and project Bell-outcome labels need not coincide.

The useful algebraic check is

```math
(M\otimes I)\lvert\Phi_d\rangle
=(I\otimes M^{\mathsf T})\lvert\Phi_d\rangle.
```

It involves a transpose. For example, the project defines its qubit Bell basis using $`\lvert\beta_a\rangle=(I\otimes\overline{\sigma_a})\lvert\Phi_2\rangle`$. The conjugation matters for $`\sigma_y`$. The pair-dependent scores in [gate cuts](../science/gate-cuts.md) must be derived with that convention; ordinary teleportation by itself does not establish their signs. The [gate checks](../verification/README.md) explicitly test those local Kraus identities and signed reconstructions.

## 4. Norms and the factor of two

Watrous's completely bounded trace norm in Definition 3.43 is the one-slot **diamond norm** used here. The project separately defines its operational error as half a norm:

```math
\epsilon_{\mathrm{str}}
=\tfrac12\lVert\widetilde{\mathcal T}-\mathcal T\rVert_{\mathrm{str}}.
```

For one slot, $`\lVert\cdot\rVert_{\mathrm{str}}=\lVert\cdot\rVert_\diamond`$. For several ordered slots, the supremum includes causal intervening operations and retained references. That strategy-norm extension is supplied by the research literature, not by relabeling Chapter 3's one-channel norm.

Since the normalized Bell experiment is one allowed tester,

```math
\tfrac12\lVert
J(\widetilde{\mathcal T})-J(\mathcal T)
\rVert_1\leq\epsilon_{\mathrm{str}}.
```

A small error for that one tester does not establish a small universal strategy error. Likewise, numerical agreement of selected final expectation values does not prove equality of open processes. Exact Choi-operator equality can establish the corresponding linear identity; the construction must additionally respect the causal resource constraints.

An observable taking values in $`[-1,1]`$ has expectation error bounded by the **full** output trace norm, hence by $`2\epsilon_{\mathrm{str}}`$. A probability-valued event admits the half-norm bound when the tested difference has trace zero. The distinction is used in [precision and calibration](../science/precision-calibration.md), including when the signed reconstruction is not completely positive.

## 5. Where the anchor stops and the research begins

The following are primary research ingredients or project derivations. They are **not additional educational anchors**.

| Ingredient | Source and role |
|---|---|
| Signed circuit cutting and collective wire factors | [Brenner, Piveteau and Sutter](https://arxiv.org/abs/2302.03366) supply the collective wire optimum; [Harrow and Lowe](https://arxiv.org/abs/2403.01018) supply low-ancilla interference constructions. The book's channel language does not supply a QPD optimization theorem. |
| Pure-state robustness and edge extent | [Vidal and Tarrach](https://arxiv.org/abs/quant-ph/9806094) supply the robustness result underlying the single-edge Schmidt-coefficient cost. The [forest argument](../science/forest-witness.md) establishes the additional product-over-vertices inequality needed here. |
| General two-qubit gates and KAK coefficients | The collective gate upper construction is inherited from [Schmitt, Piveteau and Sutter, Theorem 6.4](https://arxiv.org/html/2312.11638v4). KAK reduction and this cutting theorem are research inputs to [gate cuts](../science/gate-cuts.md). |
| Instruments with scored classical records | [Piveteau, Schmitt and Sutter](https://arxiv.org/abs/2503.22384) provide the circuit-cutting side-information framework. The project's bounded-score and private-record interface is stated in [the model](../science/model.md). |
| Ordered quantum processes and their distinguishability | [Chiribella, D'Ariano and Perinotti](https://arxiv.org/abs/0904.4483) supply the comb framework; [Gutoski](https://arxiv.org/abs/1008.4636) supplies strategy distinguishability. These address the sequential interface beyond a single channel. |
| Concurrence, assistance and local filters | [Wootters](https://arxiv.org/abs/quant-ph/9709029), [Laustsen, Verstraete and van Enk](https://arxiv.org/abs/quant-ph/0206192), and [Verstraete, Dehaene and De Moor](https://arxiv.org/abs/quant-ph/0011111) supply these specialized tools. Exercise 6.3 is a precursor about entanglement of formation; it does not provide these concurrence formulas. |
| Exact resource restrictions and their consequences | [Reset schedules](../science/reset-schedules.md), [dephasing memory](../science/dephasing-memory.md), and [precision and calibration](../science/precision-calibration.md) derive the common-refinement law, the specified two-slot noisy-memory law, and their stated robustness consequences. Those claims depend on the explicit port, storage and environment assumptions. |

The [related-work account](../references/related-work.md) gives the fuller attribution and model comparisons. The [verification guide](../verification/README.md) separates reproducible finite checks from the analytical proofs. The next step through the common learning route is the [milestone map](milestones.md), with the [worked explanation](tutorial.md) connecting its definitions to concrete cutting experiments.
