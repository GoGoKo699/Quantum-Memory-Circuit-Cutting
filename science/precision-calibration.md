# Universal approximation, calibration and statistical precision

This page separates three quantities: the extent of an exact or approximate universal signed process decomposition, systematic error from using an imperfect memory calibration, and the number of repeated measurements sufficient for a specified estimator. Their assumptions and conclusions differ.

The port schedule, private simulator records and bounded-score atoms are those in the [causal model](model.md). The exact two-slot construction and witness are proved in [Dephasing memory](dephasing-memory.md). Every bound below concerns those interfaces; no claim is made about arbitrary learned or observable-specific circuit-knitting algorithms.

## 1. Error convention

For a Hermiticity-preserving difference of two ordered processes, define the operational strategy norm by

```math
\|\Delta\|_{\mathrm{str}}
=\sup_{\mathsf T}\|\mathsf T[\Delta]\|_1,
\tag{P1}
```

where $\mathsf T$ ranges over deterministic causal testers with arbitrary retained quantum references, and its final output is a Hermitian operator. The normalization is the one that reduces to the diamond norm for a one-slot map. The general strategy distinguishability formalism is developed in [Gutoski](https://arxiv.org/abs/1008.4636).

Write

```math
\epsilon_{\mathrm{str}}=\frac12\|\widetilde{\mathcal T}-\mathcal T\|_{\mathrm{str}}.
\tag{P2}
```

The independent, temporally delivered Bell-probe experiment is one permitted tester. Its output is the normalized Choi operator, so

```math
\frac12\|J(\widetilde{\mathcal T})-J(\mathcal T)\|_1
\leq\epsilon_{\mathrm{str}}.
\tag{P3}
```

The converse implication is not asserted for general processes.

A final observable with outcomes in $[-1,1]$ has absolute expectation-value error at most the **full** norm in (P1), hence at most $2\epsilon_{\mathrm{str}}$. For a probability-valued event, the sharper half-norm bound holds when the difference has zero trace after the tester. This distinction matters for the calibration formulas below.

The reconstructed signed process can be Hermiticity preserving without being completely positive. Equations (P1)–(P3) still apply to that linear difference. Complete positivity and contraction properties must not be silently assigned to a miscalibrated signed reconstruction.

## 2. Approximation bounds from witness spectral ranges

Let $W$ be a valid extent witness: $|\operatorname{Tr}[WJ(\mathcal F)]|\leq1$ for every allowed scored atom. Put $J_0=J(\mathcal T)$, $G=\operatorname{Tr}(WJ_0)$, and let $\widetilde J$ be the reconstructed Choi operator. Any decomposition producing $\widetilde J$ has extent at least $\operatorname{Tr}(W\widetilde J)$.

Suppose first that $\operatorname{Tr}\widetilde J=\operatorname{Tr}J_0=1$. Exact deterministic trace normalization of the reconstructed process is sufficient; the argument itself needs only this Bell-test trace equality. For $E=\widetilde J-J_0$, $\operatorname{Tr}E=0$, so

```math
\begin{aligned}
|\operatorname{Tr}(WE)|
&=\left|\operatorname{Tr}\left[
\left(W-\frac{\lambda_{\max}+\lambda_{\min}}2I\right)E\right]\right|\\
&\leq\frac{\lambda_{\max}-\lambda_{\min}}2\|E\|_1.
\end{aligned}
\tag{P4}
```

Consequently, if (P2) is at most $\epsilon$,

```math
\Gamma(\widetilde{\mathcal T})
\geq G-(\lambda_{\max}-\lambda_{\min})\epsilon.
\tag{P5}
```

A trace-one reconstructed Choi operator also implies $\Gamma\geq1$, because every scored atom has absolute Choi trace at most one. These are lower bounds, not a claim to know the entire optimal approximation frontier.

Without exact trace equality, centering the witness in (P4) is unjustified. The always valid estimate is

```math
\Gamma(\widetilde{\mathcal T})
\geq G-2\|W\|_\infty\epsilon.
\tag{P6}
```

### 2.1 Identity wires with complete memory breaks

For the common refinement $\mathcal I$ of the two reset schedules, discard trivial intervals of dimension one and define

```math
D_I=\prod_{j\in I}d_j,\qquad
c_I=2D_I-1,\qquad
G=\prod_{I\in\mathcal I}c_I,\qquad
c_{\min}=\min_{I\in\mathcal I}c_I.
\tag{P7}
```

The [forest witness](forest-witness.md) is

```math
W_{\mathrm{forest}}=\bigotimes_{I\in\mathcal I}(2D_I\Phi_{D_I}-I).
\tag{P8}
```

Each nontrivial factor has eigenvalues $c_I$ and $-1$. Therefore

```math
\lambda_{\max}=G,\qquad
\lambda_{\min}=-G/c_{\min},\qquad
\|W_{\mathrm{forest}}\|_\infty=G.
\tag{P9}
```

For the minimum eigenvalue, selecting the negative eigenvalue on one factor with the smallest $c_I$ gives $-G/c_{\min}$. Selecting negative eigenvalues on additional factors divides its magnitude by additional factors at least one and cannot make it more negative.

The trace-preserving approximate extent obeys

```math
\boxed{\Gamma_\epsilon^{\mathrm{TP}}
\geq\max\left\{1,
G\left[1-\left(1+\frac1{c_{\min}}\right)\epsilon\right]
\right\}.}
\tag{P10}
```

For general signed approximants without exact trace normalization,

```math
\boxed{\Gamma_\epsilon
\geq\max\{0,\,G(1-2\epsilon)\}.}
\tag{P11}
```

If no nontrivial interval remains, the exact target is free and the trace-one lower bound is simply one.

These bounds preserve the memory-alignment separation at fixed sufficiently small universal error. For example, aligned two-slot qubit epochs have an exact construction of extent $7^{n/2}$. A one-slot staggered schedule has $G=3^n$, $c_{\min}=3$, and any trace-normalized reconstruction with error $\epsilon<3/4$ has extent at least $(1-4\epsilon/3)3^n$. The ratio to the aligned exact construction remains exponential in $n$. This is a statement about universal signed extent; it is not a measurement lower bound for all algorithms.

The special spectral form in (P9) belongs to maximally entangled wire edges. It must not be replaced by the target expectation of an arbitrary pure gate-Choi edge without checking the witness spectrum.

### 2.2 The noisy two-slot witness

For $r=\eta_A\eta_B$, the witness from the dephasing theorem is

```math
Q_r=\frac{W_1W_2+r(W_1+W_2-I)}{1+r},
\qquad W_i=4\Phi_i-I.
\tag{P12}
```

Its spectrum is explicit:

| Sector | Eigenvalue | Multiplicity |
|---|---:|---:|
| $\Phi_1\Phi_2$ | $g_r=(9+5r)/(1+r)$ | 1 |
| Exactly one $\Phi_i$ | $(r-3)/(1+r)$ | 6 |
| Neither $\Phi_i$ | $(1-3r)/(1+r)$ | 9 |

For $0\leq r\leq1$, the middle row is the minimum. The spectral midpoint is exactly three, and

```math
\lambda_{\max}-\lambda_{\min}
=\frac{4(3+r)}{1+r},
\qquad \|Q_r\|_\infty=g_r.
\tag{P13}
```

Thus

```math
\boxed{\Gamma_{2,\epsilon}^{\mathrm{TP}}(\eta_A,\eta_B)
\geq\max\left\{1,
\frac{9+5r}{1+r}-\frac{4(3+r)}{1+r}\epsilon
\right\}.}
\tag{P14}
```

Without exact trace normalization the valid bound is

```math
\Gamma_{2,\epsilon}\geq\max\{0,\,g_r(1-2\epsilon)\}.
\tag{P15}
```

Only the zero-error endpoint of (P14) is established to be tight by the four-resource theorem. This page does not claim an optimal biased approximation protocol attaining its entire straight-line bound.

### 2.3 Prescribed noisy blocks with complete resets at both sides

Under the imposed-reset and fresh-noise assumptions of [the exact block corollary](dephasing-memory.md#exact-product-law-when-both-resets-are-imposed), define

```math
G_{\mathrm{blocks}}=\prod_b g_{r_b},
\qquad
\kappa_{\max}=\max_b\frac{3-r_b}{9+5r_b}.
\tag{P15a}
```

The product witness $\bigotimes_b Q_{r_b}$ is valid for this reset-constrained class. Its largest and smallest eigenvalues are $G_{\mathrm{blocks}}$ and $-G_{\mathrm{blocks}}\kappa_{\max}$: the most negative product selects the negative eigenvalue in one block with the largest negative-to-positive magnitude ratio. Hence a trace-one approximation with half strategy error at most $\epsilon$ satisfies

```math
\Gamma_{\mathrm{blocks},\epsilon}^{\mathrm{TP}}
\geq\max\{1,\,
G_{\mathrm{blocks}}[1-(1+\kappa_{\max})\epsilon]\}.
\tag{P15b}
```

Without exact trace normalization, the bound is $G_{\mathrm{blocks}}(1-2\epsilon)$, truncated at zero. These statements require the imposed resets at both laboratories; the product witness has not been proved valid for uninterrupted many-slot noisy memories.

## 3. Exact bias from nominal versus actual dephasing

Let $r_0\in[0,1]$ be the nominal parameter used to choose the four-resource coefficients, while the actual independent memory channels have product $r\in[0,1]$. Assume for this calculation that all other preparations, rotations, measurements and communications are ideal.

Use the physical resources $V_{++},V_{+-},V_{-+},E_r$ defined in the dephasing theorem, but the nominal coefficients

```math
3,\quad -a_0,\quad-a_0,\quad b_0,
\qquad a_0=\frac{2+r_0}{1+r_0},\quad b_0=\frac2{1+r_0}.
\tag{P16}
```

The implemented signed Choi operator is

```math
\widetilde J_{r_0;r}
=3V_{++}-a_0(V_{+-}+V_{-+})+b_0E_r.
\tag{P17}
```

Since $E_r=I_{16}/16+(1+2r)W_1W_2/144$, its exact deviation from the ideal is

```math
\boxed{\widetilde J_{r_0;r}
=\Phi_1\Phi_2+\frac{r-r_0}{36(1+r_0)}W_1W_2.}
\tag{P18}
```

Define the dimensionless calibration mismatch

```math
d=\frac{r-r_0}{1+r_0}.
\tag{P19}
```

The reconstruction retains exact deterministic trace normalization. Indeed all four physical atoms are causal trace-preserving processes and the coefficients still sum to one. It is Hermiticity preserving. It is **not completely positive for any $d\neq0$**: the Choi coefficients in the product Bell basis are

| Pauli error label | Reconstructed coefficient for each label | Number of labels |
|---|---:|---:|
| $(I,I)$ | $1+d/4$ | 1 |
| Exactly one nonidentity Pauli | $-d/12$ | 6 |
| Two nonidentity Paulis | $d/36$ | 9 |

For $d>0$ the second row is negative; for $d<0$ the third row is negative. For the permitted actual and nominal parameters, $-1/2\leq d\leq1$, so the first row remains positive.

### 3.1 The calibration strategy norm is exact

Let $\Lambda_+$ and $\Lambda_-$ be the one-slot Pauli channels with normalized Choi states $\rho_+$ and $\rho_-$. Their difference $\Xi=\Lambda_+-\Lambda_-$ has Pauli coefficients

```math
(1/2,-1/6,-1/6,-1/6),
\qquad J(\Xi)=W/6.
\tag{P20}
```

Thus the two-slot error is the ordered product

```math
\widetilde{\mathcal I}_{r_0;r}^{(2)}-\mathcal I^{(2)}
=d\,\Xi\otimes\Xi.
\tag{P21}
```

More generally, a real signed combination of Pauli paths

```math
\Delta=\sum_{\boldsymbol\alpha}q_{\boldsymbol\alpha}
 \mathcal P_{\boldsymbol\alpha}
```

has strategy norm exactly $\sum_{\boldsymbol\alpha}|q_{\boldsymbol\alpha}|$. The triangle inequality proves the upper bound, since every fixed Pauli path is a physical deterministic causal process of norm one. Independent Bell probes yield mutually orthogonal product Bell states for these paths, attaining the same trace norm. This proof includes arbitrary external adaptive testers; it does not rely on multiplying one-slot channel norms across unknown interleavings.

Applying this observation to (P21) gives

```math
\boxed{\|\widetilde{\mathcal I}_{r_0;r}^{(2)}-\mathcal I^{(2)}\|_{\mathrm{str}}
=\frac{|r-r_0|}{1+r_0}=|d|.}
\tag{P22}
```

The half strategy distance is $|d|/2$. The worst-case bias for an observable in $[-1,1]$ is $|d|$, and a Bell-probe measurement with signs matching the error coefficients attains it. For a probability-valued event the maximum bias is $|d|/2$.

Consequently, a certified interval $|r-r_0|\leq\delta_r$ gives a bounded-observable bias at most $\delta_r/(1+r_0)$. No unknown multiplicative amplification by the QPD extent is needed for this particular scalar mismatch: (P18) has computed the cancellations exactly.

## 4. Repeating calibrated blocks

Consider the explicit implementation that resets both memories after each pair of slots and uses the four-resource construction independently in each of $m$ blocks. There may be arbitrary external quantum operations and reference systems connecting the exposed blocks. The formulas below analyze this chosen construction; they make no claim that the unrestricted optimum for $2m$ slots is the product of the two-slot optima.

For block $j$, write

```math
d_j=\frac{r_j-r_{0,j}}{1+r_{0,j}},
\quad p_j=1+d_j/4,
\quad L_j=1+d_j/4+3|d_j|/4.
\tag{P23}
```

Here $p_j$ is the coefficient of the identity Pauli path and $L_j$ is the sum of absolute values of all coefficients in that block. Independence of the physical block construction gives product coefficients over its complete Pauli paths. Set

```math
P=\prod_{j=1}^m p_j,\qquad L=\prod_{j=1}^m L_j.
```

The all-identity path has coefficient $P$, while the sum of absolute values of all other path coefficients is $L-P$. The Pauli-path argument from Section 3.1 therefore gives the exact full strategy error

```math
\boxed{\|\widetilde{\mathcal I}_{\mathrm{blocks}}-\mathcal I^{(2m)}\|_{\mathrm{str}}
=|P-1|+L-P.}
\tag{P24}
```

For identical $d$, this is

```math
\begin{cases}
(1+d)^m-1,&d\geq0,\\[2mm]
(1+|d|/2)^m+1-2(1-|d|/4)^m,&d\leq0.
\end{cases}
\tag{P25}
```

Both expressions are $m|d|+O(m^2d^2)$ when $m|d|$ is small. A simple bound convenient for error budgets is

```math
\boxed{\|\widetilde{\mathcal I}_{\mathrm{blocks}}-\mathcal I^{(2m)}\|_{\mathrm{str}}
\leq\prod_{j=1}^m(1+|d_j|)-1.}
\tag{P26}
```

One proof expands the product of ideal blocks plus their signed errors and bounds each term by its Pauli coefficient norm. In particular, if $|d_j|\leq\delta$, the full norm is at most $(1+\delta)^m-1$. The half strategy distance is half of (P24) or (P26).

Using a bound of just $\sum_j|d_j|$ for arbitrary $m$ would be unjustified: the miscalibrated blocks are not completely positive, and the usual contractivity argument for physical channels is unavailable. The higher-order terms in (P26) account for this.

To guarantee bounded-observable calibration bias at most $\epsilon_{\mathrm{bias}}$, it suffices to require

```math
|d_j|\leq\delta_*:=(1+\epsilon_{\mathrm{bias}})^{1/m}-1
\quad\text{for every block.}
\tag{P27}
```

For fixed small $\epsilon_{\mathrm{bias}}$, this asks for a parameter error of order $\epsilon_{\mathrm{bias}}/m$, not a constant error independent of the number of blocks.

## 5. A charged calibration procedure

Assume the specified independent dephasing channels are stationary over both calibration and execution, with the same gap duration and control conditions. All preparations and measurements used for calibration are ideal in this model.

For each laboratory $s\in\{A,B\}$, prepare $|+\rangle$, apply its actual memory-gap channel, and measure $X$. The result $X_{s,k}\in\{-1,1\}$ has mean $\eta_s$. From $N_s$ independent uses form the sample mean and clip it to $[0,1]$, obtaining $\widehat\eta_s$. Clipping cannot increase the distance to an actual $\eta_s\in[0,1]$.

[Hoeffding's inequality](https://doi.org/10.1080/01621459.1963.10500830) gives

```math
\Pr\{|\widehat\eta_s-\eta_s|>\zeta_s\}
\leq2\exp(-N_s\zeta_s^2/2).
\tag{P28}
```

Thus the sufficient sample counts

```math
\boxed{N_s\geq\frac{2}{\zeta_s^2}\log\frac4{\alpha_{\mathrm{cal}}}}
\tag{P29}
```

ensure both calibration errors are within their specified tolerances with probability at least $1-\alpha_{\mathrm{cal}}$. The charged resources are $N_A+N_B$ uses of the actual memory-gap channels, the corresponding preparations and measurements, and storage of their classical outcomes or running averages. If both laboratories calibrate simultaneously, the number of parallel trials can be the larger of $N_A,N_B$, but both sets of memory uses are still consumed.

Set

```math
r_0=\widehat\eta_A\widehat\eta_B.
```

Because all four factors are in $[0,1]$,

```math
|r-r_0|
\leq |\eta_A-\widehat\eta_A|+|\eta_B-\widehat\eta_B|
\leq\zeta_A+\zeta_B.
\tag{P30}
```

Therefore one block has bounded-observable calibration bias at most

```math
\frac{\zeta_A+\zeta_B}{1+r_0}
\tag{P31}
```

on the successful calibration event. For $m$ identical stationary blocks, the same calibrated parameters can be reused. A conservative choice independent of the observed denominator is

```math
\zeta_A=\zeta_B=\delta_*/2,
\qquad \delta_*=(1+\epsilon_{\mathrm{bias}})^{1/m}-1.
\tag{P32}
```

Then (P27) holds, and the sufficient total calibration uses scale as

```math
N_A+N_B
=O\!\left(m^2\epsilon_{\mathrm{bias}}^{-2}
\log(1/\alpha_{\mathrm{cal}})\right)
\tag{P33}
```

for fixed small bias budget. This is a constructive upper bound for this calibration method, not an optimal calibration lower bound. If parameters drift by block, stationarity cannot be used to reuse this one estimate; corresponding parameter intervals must instead hold for every executed block.

Marginal Ramsey calibration establishes the two coherence factors within the assumed channel family. It does **not** certify independent noise, an inaccessible environment, correct port timing or absence of other noise components. The correlated-phase example in [Dephasing memory, Section 6](dephasing-memory.md#6-endpoints-repeated-blocks-and-scope-tests) has identical marginal complete-dephasing calibrations but a different circuit-cutting extent. Those physical assumptions must be validated separately if they are to be inferred from an experiment.

## 6. Sampling precision after calibration

Condition on the calibration record and freeze the nominal coefficients. For one block sample the four physical atoms with probabilities proportional to

```math
(3,a_0,a_0,b_0),
\qquad \Gamma_0=3+2a_0+b_0=5+\frac4{1+r_0}.
\tag{P34}
```

Multiply the final bounded measurement result by the selected coefficient's sign and by $\Gamma_0$. For $m$ independently sampled blocks, use the product of their signs and

```math
G_0=\prod_{j=1}^m\left(5+\frac4{1+r_{0,j}}\right).
\tag{P35}
```

The single-shot estimator $Y$ always satisfies $|Y|\leq G_0$, even when the physical memory calibration is wrong. Its mean is the signed reconstructed expectation, rather than necessarily the target expectation.

For $N_{\mathrm{exec}}$ fresh independent complete executions,

```math
\Pr\{|\overline Y-\mathbb EY|>\epsilon_{\mathrm{stat}}\mid
\text{calibration record}\}
\leq2\exp\left[-\frac{N_{\mathrm{exec}}\epsilon_{\mathrm{stat}}^2}{2G_0^2}\right].
\tag{P36}
```

A sufficient execution count is

```math
\boxed{N_{\mathrm{exec}}\geq
\frac{2G_0^2}{\epsilon_{\mathrm{stat}}^2}
\log\frac2{\alpha_{\mathrm{stat}}}.}
\tag{P37}
```

Using (P27)–(P32), a union bound yields the explicit end-to-end guarantee

```math
|\overline Y-\mu_{\mathrm{target}}|
\leq\epsilon_{\mathrm{bias}}+\epsilon_{\mathrm{stat}}
```

with probability at least $1-\alpha_{\mathrm{cal}}-\alpha_{\mathrm{stat}}$. Calibration uses (P29) are charged **in addition** to the complete circuit executions (P37). The execution confidence bound is conditional on the frozen calibration choices, so its validity does not require pretending the estimated coefficients were known beforehand.

These counts are sufficient for this specified bounded estimator. They need not be optimal for a particular observable or promise. The distinction between extent and actual variance is discussed in [Harrow and Lowe, Section 2.2](https://arxiv.org/abs/2403.01018); tomography-based circuit families can behave differently, as shown by [Harada et al.](https://arxiv.org/abs/2512.19623).

## 7. Coefficient precision and other implementation errors

### Coupled coefficient rounding preserves normalization

The coefficients can be parameterized by one number,

```math
b_0=\frac2{1+r_0},\qquad a_0=1+b_0/2,
\qquad 3-2a_0+b_0=1.
\tag{P38}
```

If finite precision requires rounding, choose a representable $\widehat b\in[1,2]$ and define $\widehat a=1+\widehat b/2$ with the same exact rational representation. Then the signed coefficient sum remains exactly one. The effective nominal parameter is

```math
\widehat r_0=2/\widehat b-1,
```

and all of Section 3 applies with that parameter. Equivalently, the mismatch is

```math
d=\widehat b(1+r)/2-1.
\tag{P39}
```

An additional coefficient error $|\widehat b-b_0|\leq\zeta_b$ changes $d$ by at most $\zeta_b(1+r)/2\leq\zeta_b$. This supplies a direct precision budget. Independently rounding all four weights need not preserve the trace equality required for the sharper approximation bounds.

Exact rational weights also avoid assuming an infinite-precision classical sampler. If $\widehat b=p/q$ with positive integers $p,q$, the four sampling probabilities are proportional to the integer weights $(6q,2q+p,2q+p,2p)$. Draw a uniform integer from a set of size $M=10q+4p$ and select the corresponding interval. A fair-bit rejection sampler uses fewer than $2\lceil\log_2M\rceil$ random bits on average. The empirical Ramsey means, their clipped product, and the coefficients obtained from them can all be stored as exact rationals. This charges finite classical arithmetic and randomness without introducing an additional quantum precision assumption.

### Errors outside the scalar dephasing model

Let $\mathcal F_{k,r}$ denote the four actual-dephasing atoms analyzed in Section 3, and let $\widehat{\mathcal F}_k$ include additional preparation, measurement, twirl or control error. If certified full strategy-norm bounds are

```math
\|\widehat{\mathcal F}_k-\mathcal F_{k,r}\|_{\mathrm{str}}
\leq e_k,
```

then the additional signed-process error is bounded by

```math
\left\|\sum_k c_{k,0}
(\widehat{\mathcal F}_k-\mathcal F_{k,r})\right\|_{\mathrm{str}}
\leq\sum_k|c_{k,0}|e_k.
\tag{P40}
```

This is an assumption-to-error conversion, not a claim that such norm certificates follow from marginal calibration or average gate fidelity.

### Composition lemma for general Hermiticity-preserving block errors

The product error bound also holds beyond the Pauli family, provided the complete implementation is a chronological composition of the specified block processes. An arbitrary external tester may retain quantum memory and operate between every exposed slot. Hidden apparatus environments shared between blocks are not part of this blockwise-composition assumption; bounds on isolated block marginals alone would not describe such an implementation.

Taking the trace norm of a tester's final Hermitian output is equivalent to optimizing its final two-outcome signed measurement, so (P1) equals the operational strategy norm used by [Gutoski, Theorem 3(1), Section 4](https://arxiv.org/pdf/1008.4636). That theorem characterizes its Hermitian unit ball: $\|X\|_{\mathrm{str}}\leq1$ if and only if $X=\mathcal S_+-\mathcal S_-$, where $\{\mathcal S_+,\mathcal S_-\}$ is a two-outcome physical measuring strategy and its sum is deterministic. His matrix representation uses unnormalized Choi operators; the statement here is about the corresponding processes and hence uses the same operational norm without an additional dimension factor.

For block processes $X_j$ with $\|X_j\|_{\mathrm{str}}\leq b_j$, apply this characterization to $X_j/b_j$ (zero-norm blocks are zero). Run the resulting physical block instruments successively, keep their outcome bits private, and assign the final score equal to the product of their $\pm1$ scores. This is a physical causal instrument with a score of absolute value one. Against any external tester, its signed output has trace norm at most the sum of its positive branch traces, which is one. Thus, denoting chronological concatenation by $\boxtimes$,

```math
\|X_1\boxtimes\cdots\boxtimes X_m\|_{\mathrm{str}}
\leq\prod_{j=1}^m b_j.
\tag{P41}
```

These auxiliary instrument realizations need not obey the cutting resource restrictions: they are used solely to prove an operational norm inequality, not to construct a free cutting protocol.

Now write each reconstructed block as $\widetilde{\mathcal T}_j=\mathcal T_j+\Delta_j$, with deterministic physical target $\mathcal T_j$ and $\|\Delta_j\|_{\mathrm{str}}\leq b_j$. Expand the chronological product and remove its all-target term. Every nonempty subset $S$ of error blocks contributes a term bounded by $\prod_{j\in S}b_j$ through (P41), since $\|\mathcal T_j\|_{\mathrm{str}}=1$. Summing gives

```math
\left\|\mathop{\boxtimes}_{j=1}^m\widetilde{\mathcal T}_j
-\mathop{\boxtimes}_{j=1}^m\mathcal T_j\right\|_{\mathrm{str}}
\leq\sum_{\varnothing\neq S\subseteq\{1,\ldots,m\}}
\prod_{j\in S}b_j
=\prod_{j=1}^m(1+b_j)-1.
\tag{P42}
```

The $b_j$ may include both calibration and implementation contributions such as (P40). This argument covers nonphysical intermediate reconstructions through the strategy-norm unit-ball theorem; it does not invoke CPTP contractivity for those reconstructions. The direct Pauli-path proofs and exact formulas (P22)–(P26) remain valid independently of this general composition lemma.

The error budget is consequently explicit: parameter estimation controls (P22), prescribed block repetition controls (P26), additional atom errors enter through (P40), and independent sampling controls (P37). None of these statements extends the exact two-slot optimum to arbitrary correlated memory noise or unrestricted many-slot simulation.
