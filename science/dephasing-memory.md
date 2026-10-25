# Two sequential wire cuts with dephasing memories

## 1. Exact result and causal interface

Use the strict port and scored-instrument conventions of the [causal model](model.md). Consider two ordered qubit identity slots from Alice to Bob. The apparatus has one persistent qubit at each laboratory, and those qubits undergo the channels

```math
\mathcal D_\eta(X)
=\frac{1+\eta}{2}X+\frac{1-\eta}{2}ZXZ,
\qquad 0\leq\eta\leq1,
\tag{D1}
```

between the slots. Write $`\eta_A,\eta_B`$ for the two coherence factors and $`r=\eta_A\eta_B`$. The optimum signed bounded-score extent is

```math
\boxed{\Gamma_2(\eta_A,\eta_B)
=\frac{9+5r}{1+r}=5+\frac4{1+r}.}
\tag{D2}
```

The result includes arbitrary local instruments, classical communication in either direction, shared classical randomness, local filtering, and outcome-dependent scores. It requires the following physical interface.

| Stage | Available quantum systems and required action |
|---|---|
| First slot | Alice receives the first input. The apparatus must deliver Bob's first output before the memory gap. |
| Gap | At most one cutter-accessible qubit remains at each side. Their prescribed noise use is $`\mathcal D_{\eta_A}\otimes\mathcal D_{\eta_B}`$. |
| Second slot | Only after the gap does Alice receive the second input. Bob then delivers the second output. |

All accessible quantum degrees of freedom count toward the memory bound, including retained data qubits, resource ports, environments and purportedly temporary ancillas. Transient ancillas inside a slot are unrestricted, but none may bypass the gap. A released output cannot be borrowed back by the apparatus. An external tester may retain that output and use it to prepare a later input; that is a permitted causal use of the exposed ports.

The physical noise channel is a product conditional on each permitted **pre-gap** classical history, with the same fixed parameters in (D1). The error labels and their environments are inaccessible. The channel is one prescribed use: inserting an additional noiseless storage system or accessing its internal environment is outside the model. Later conditioning on measurement records need not leave the hidden error variables statistically independent. The proof below works with those records and does not assume posterior independence.

There is no initial shared spatial entanglement and no quantum communication between the laboratories. All source inputs arrive through the stated ports. The apparatus's random choices and internal instrument records are private; they may control its operations and its final score, but are not additional control inputs exposed to the unknown external tester.

For clarity, a free scored atom has the form

```math
\mathcal F=\sum_h s_h\mathcal E_h,
\qquad |s_h|\leq1,
\tag{D3}
```

where $`\{\mathcal E_h\}_h`$ is a complete physical causal instrument obeying the resource restrictions. A signed decomposition of the ideal two-slot comb $`\mathcal I^{(2)}`$ is

```math
\mathcal I^{(2)}=\sum_k c_k\mathcal F_k,
\qquad \Gamma=\sum_k|c_k|.
\tag{D4}
```

The optimum is the infimum of this quantity. Equality means equality against every causal external tester, including one with entangled inputs, retained reference systems and arbitrary operations between slots. A postselected branch is charged with its physical success probability through (D3); its normalized successful output is not a free deterministic atom. The instrument formulation is consistent with the general treatment of classical side information in [Piveteau, Schmitt and Sutter](https://arxiv.org/abs/2503.22384).

Finite-round protocols with finite outcomes suffice for the upper construction. The lower bound also applies to their operational closure: it is a continuous linear witness bound, and hence survives limits of such protocols.

## 2. Four physical resources and their full matrix identity

### 2.1 Notation and single-slot states

Use normalized Choi states. Set

```math
|\Phi\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\quad \Phi=|\Phi\rangle\langle\Phi|,
\quad R=\frac{I_4-\Phi}{3},
\quad W=4\Phi-I_4.
\tag{D5}
```

In the computational basis $`(00,01,10,11)`$,

```math
\Phi=\frac12
\begin{pmatrix}
1&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&1
\end{pmatrix},
\qquad
W=\begin{pmatrix}
1&0&0&2\\0&-1&0&0\\0&0&-1&0\\2&0&0&1
\end{pmatrix}.
\tag{D6}
```

Define two separable single-slot resource states,

```math
\rho_+=\frac12\Phi+\frac12R
=\frac16\begin{pmatrix}
2&0&0&1\\0&1&0&0\\0&0&1&0\\1&0&0&2
\end{pmatrix},
\tag{D7}
```

```math
\rho_-=R
=\frac16\begin{pmatrix}
1&0&0&-1\\0&2&0&0\\0&0&2&0\\-1&0&0&1
\end{pmatrix}.
\tag{D8}
```

Their separability and preparation are explicit. Apply the bilateral isotropic twirl

```math
\mathcal T(X)=\mathbb E_U
 (U\otimes\overline U)X(U\otimes\overline U)^\dagger
\tag{D9}
```

to $`|00\rangle\langle00|`$ for $`\rho_+`$, or to $`|01\rangle\langle01|`$ for $`\rho_-`$. It requires a shared classical choice of $`U`$, not shared quantum entanglement. The uniform single-qubit Clifford ensemble is a finite exact unitary 2-design and implements this twirl; see [Dankert et al.](https://arxiv.org/abs/quant-ph/0606161).

On the two spatial slot pairs, ordered as $`(A_1B_1)(A_2B_2)`$, take

```math
V_{++}=\rho_+\otimes\rho_+,
\quad V_{+-}=\rho_+\otimes\rho_-,
\quad V_{-+}=\rho_-\otimes\rho_+.
\tag{D10}
```

These three resources need no persistent quantum memory.

### 2.2 The resource that uses the memories

At a single laboratory, prepare a Bell pair between its first resource port and its memory. Release or consume the first port, apply (D1) to the memory, and use that memory as its second resource port. The resulting two-time local state is

```math
\chi_\eta
=\frac12\begin{pmatrix}
1&0&0&\eta\\0&0&0&0\\0&0&0&0\\\eta&0&0&1
\end{pmatrix}.
\tag{D11}
```

Let $`E_r`$ be the product $`(\chi_{\eta_A})_{A_1A_2}\otimes (\chi_{\eta_B})_{B_1B_2}`$, reordered into slot pairs, followed by an independent twirl (D9) on each pair. Although each local state can be entangled between its two times, the joint resource is separable between Alice and Bob. The twirls preserve that spatial separability.

The full normalized density matrix has either of the equivalent forms

```math
\begin{aligned}
E_r={}&\frac{1+r}{8}\Phi\otimes\Phi
+\frac{1-r}{8}(\Phi\otimes R+R\otimes\Phi)
+\frac{5+r}{8}R\otimes R\\
={}&\frac{I_{16}}{16}+\frac{1+2r}{144}W\otimes W.
\end{aligned}
\tag{D12}
```

For an explicit $`16\times16`$ block matrix, put $`k=1+2r`$. Each displayed entry below is a $`4\times4`$ block, with $`W`$ specified in (D6):

```math
E_r=\frac1{144}
\begin{pmatrix}
9I_4+kW&0&0&2kW\\
0&9I_4-kW&0&0\\
0&0&9I_4-kW&0\\
2kW&0&0&9I_4+kW
\end{pmatrix}.
\tag{D13}
```

To derive (D12), first note that every local one-qubit marginal of $`\chi_\eta`$ is maximally mixed. Consequently each spatial Bell fidelity is $`1/4`$. The joint Bell fidelity is

```math
\operatorname{Tr}[(\Phi_{A_1B_1}\otimes\Phi_{A_2B_2})
 (\chi_{\eta_A}\otimes\chi_{\eta_B})]
=\frac14\operatorname{Tr}(\chi_{\eta_A}\chi_{\eta_B}^{T})
=\frac{1+r}{8}.
\tag{D14}
```

The pairwise twirl makes the state uniform on each of the four orthogonal sectors $`\Phi\Phi,\Phi(I-\Phi),(I-\Phi)\Phi,(I-\Phi)(I-\Phi)`$. Their probabilities are therefore $`(1+r)/8,(1-r)/8,(1-r)/8,(5+r)/8`$, which proves the stated full matrix expression.

### 2.3 Exact decomposition

With

```math
a_r=\frac{2+r}{1+r},\qquad b_r=\frac2{1+r},
\tag{D15}
```

the identity is

```math
\boxed{\Phi\otimes\Phi
=3V_{++}-a_rV_{+-}-a_rV_{-+}+b_rE_r.}
\tag{D16}
```

This is a density-matrix identity, not only an agreement of selected expectation values. For example, substitution of (D7), (D8) and (D12) gives the following coefficients in the four linearly independent sector states:

| Sector state | Coefficient in the right side of (D16) |
|---|---:|
| $`\Phi\otimes\Phi`$ | $`3/4+b_r(1+r)/8=1`$ |
| $`\Phi\otimes R`$ | $`3/4-a_r/2+b_r(1-r)/8=0`$ |
| $`R\otimes\Phi`$ | $`3/4-a_r/2+b_r(1-r)/8=0`$ |
| $`R\otimes R`$ | $`3/4-a_r+b_r(5+r)/8=0`$ |

The signed coefficients sum to one, and their absolute sum is

```math
3+2a_r+b_r=\frac{9+5r}{1+r}.
\tag{D17}
```

The four resources in (D16) are coarse-grained physical preparations. The finite random choices inside their twirls are part of those preparations, rather than additional signed coefficients.

## 3. Streaming teleportation and universal comb equality

For each slot, use its resource qubits for standard teleportation: Alice Bell-measures the received input with her resource port, sends the two classical outcome bits, and Bob applies the appropriate Pauli correction before releasing the output. The relation between an arbitrary teleportation resource and the resulting Pauli channel is established in [Bowen and Bose](https://arxiv.org/abs/quant-ph/0107132); the correlated multi-use version is explicit in [Caruso, Giovannetti and Palma](https://arxiv.org/abs/0906.0506).

Here it can also be checked directly. Let $`\Phi_\alpha=(I\otimes P_\alpha)\Phi(I\otimes P_\alpha)^\dagger`$, for $`P_\alpha\in\{I,X,Y,Z\}`$. A resource diagonal as

```math
\Omega=\sum_{\alpha,\beta}p_{\alpha\beta}
 \Phi_\alpha\otimes\Phi_\beta
\tag{D18}
```

implements a causal two-slot comb: sample $`(\alpha,\beta)`$ from this distribution, apply $`P_\alpha`$ to the first transmitted input, and apply $`P_\beta`$ to the second. Its normalized comb Choi state is exactly $`\Omega`$. An external tester may adapt its second input to the first output; each fixed Pauli path remains a well-defined causal operation, so linearity proves the same identity for that tester. Averaging (D18) does not assume independent or product input states.

All four states in (D16) are diagonal in the product Bell basis. Applying slotwise teleportation to (D16) therefore gives (D4) for the full comb. The target resource $`\Phi\otimes\Phi`$ gives two identity slots.

The memory resource does not need to exist as four simultaneously stored qubits. In its streaming implementation:

1. Each laboratory locally prepares its first resource port entangled with its one memory qubit.
2. Both apply their first-slot twirl rotations to those first ports. Alice performs the first teleportation measurement; Bob corrects and releases the first output.
3. Only the two prescribed memory qubits persist through the gap and undergo (D1).
4. The second-slot twirl rotations are applied to the memories after the gap. The second input now arrives, and the second teleportation is completed.

The rotations for both slots can be sampled beforehand as classical information. A first-port teleportation instrument acts on systems disjoint from the later memory noise and later local resource rotations. Those operations commute as linear maps, so moving the second resource preparation through the first-port operations gives exactly the simultaneous-resource description used to prove (D16). This argument does not move the second input backward in time.

There is one stored qubit per side across the gap. The peak transient width is larger: Alice's first teleportation can involve an incoming qubit, a resource port and the memory. Equation (D2) concerns persistent memory, rather than that peak width.

## 4. Temporal state constraint for arbitrary instruments

The lower bound will use a necessary constraint on the local two-time states generated by the noisy memory. It does not assert that this constraint completely characterizes all physically realizable states.

For a normalized pure two-qubit state with coefficient matrix $`\Psi`$, define

```math
C(|\psi\rangle)=2|\det\Psi|.
\tag{D19}
```

For mixed states, use its convex and concave roofs,

```math
C(\rho)=\inf_{\rho=\sum_jp_j\psi_j}\sum_jp_jC(\psi_j),
\qquad
C_a(\rho)=\sup_{\rho=\sum_jp_j\psi_j}\sum_jp_jC(\psi_j).
\tag{D20}
```

These are concurrence and concurrence of assistance. Their established two-qubit treatment appears in [Wootters](https://arxiv.org/abs/quant-ph/9709029) and [Laustsen, Verstraete and van Enk](https://arxiv.org/abs/quant-ph/0206192). Only the roof definitions and elementary properties proved here are needed.

### Lemma 1: the dephased Bell state has a fixed roof ratio

```math
C(\chi_\eta)=\eta,\qquad C_a(\chi_\eta)=1.
\tag{D21}
```

**Proof.** Every pure vector in any decomposition of $`\chi_\eta`$ lies in $`\operatorname{span}\{|00\rangle,|11\rangle\}`$, since the density matrix has no support outside it. For a vector $`\alpha|00\rangle+\beta|11\rangle`$, the concurrence is $`2|\alpha\beta|`$. The triangle inequality applied to the $`00,11`$ matrix element gives an average concurrence at least $`\eta`$. Choose $`\theta\in[0,\pi/4]`$ with $`\sin2\theta=\eta`$. The equal mixture of

```math
\cos\theta|00\rangle+\sin\theta|11\rangle,
\qquad
\sin\theta|00\rangle+\cos\theta|11\rangle
```

is $`\chi_\eta`$, and both vectors have concurrence $`\eta`$, attaining the lower bound. Conversely, $`\chi_\eta`$ is the mixture of $`\Phi^+`$ and $`\Phi^-`$ with weights $`(1+\eta)/2`$ and $`(1-\eta)/2`$. Both are maximally entangled, so the assisted roof equals its maximum possible value one. $`\square`$

### Lemma 2: both roofs scale identically under local filtering

For invertible $`2\times2`$ matrices $`A,B`$, let

```math
\rho'=\frac{(A\otimes B)\rho(A\otimes B)^\dagger}{p},
\quad p=\operatorname{Tr}[(A\otimes B)\rho(A\otimes B)^\dagger]>0.
```

Then

```math
C(\rho')=\frac{|\det A\det B|}{p}C(\rho),
\qquad
C_a(\rho')=\frac{|\det A\det B|}{p}C_a(\rho).
\tag{D22}
```

**Proof.** For a pure coefficient matrix, filtering changes $`\Psi`$ to $`A\Psi B^T`$. Its determinant acquires the factor $`\det A\det B`$. Mapping a pure ensemble through the filter changes the probability of each component by its success probability; in the average concurrence this cancels that component's normalization. The entire average is multiplied by $`|\det A\det B|/p`$. Invertibility gives a bijection between the input and output ensembles, so both the infimum and supremum scale by the same factor. If either matrix is rank one, its output has one local system in a fixed one-dimensional support, and both roofs vanish. Zero-probability branches may be omitted. This also agrees with the established concurrence filtering law in [Verstraete, Dehaene and De Moor, Theorem 1](https://arxiv.org/abs/quant-ph/0011111). $`\square`$

### Lemma 3: every local two-time branch belongs to a concurrence cone

Define the convex set

```math
\mathcal K_\eta
=\{\rho\geq0:\operatorname{Tr}\rho=1,
\ C(\rho)\leq\eta C_a(\rho)\}.
\tag{D23}
```

Every normalized local two-time Choi factor generated through the prescribed memory use belongs to $`\mathcal K_\eta`$.

**Proof.** Any pure state on a first emitted qubit and the incoming memory is $`(A\otimes I)|\Phi\rangle`$ for a $`2\times2`$ matrix $`A`$, with its normalization absorbed in $`A`$. A post-gap, single-Kraus operation from the memory to the second emitted qubit is another $`2\times2`$ matrix $`B`$. The resulting unnormalized state is

```math
(A\otimes B)\chi_\eta(A\otimes B)^\dagger.
\tag{D24}
```

Lemmas 1 and 2 prove its normalized version satisfies (D23).

This preparation description applies directly to Bob's two outputs. For Alice, use independent normalized Bell probes $`\Phi_{R_1I_1}`$ and $`\Phi_{R_2I_2}`$, delivering $`I_j`$ only in slot $`j`$ and keeping $`R_j`$ inaccessible to the apparatus. The first operation prepares a state on $`R_1M_A`$. A refined terminal operation in slot two is a bra $`\langle v|_{M_AI_2}`$, after expanding any discarded final output in a basis. Contracting it with the second Bell probe induces

```math
B_{i m}=\frac{v_{m i}^*}{\sqrt2}
\tag{D25}
```

from $`M_A`$ to $`R_2`$. Thus Alice's local reference state has the same form (D24).

Mixed initial states, unobserved local Kraus outcomes and discarded transient systems give positive mixtures of these filtered states. The roof definition makes $`C`$ convex and $`C_a`$ concave. Consequently a mixture of states satisfying $`C\leq\eta C_a`$ also satisfies that inequality. These refinements are of local operation environments only. Refining the inaccessible dephasing environment into its $`I`$ and $`Z`$ error labels would violate the model and would invalidate (D23). $`\square`$

The late release of $`I_2`$ and early release of $`B_1`$ are exactly what force the local two-time correlations through the memory use. Abstract causality of an input-output map, without these availability constraints, does not supply Lemma 3.

## 5. A witness bounded on every scored protocol

### Lemma 4: two elementary Bloch inequalities

Write a two-qubit state as

```math
\sigma=\frac14\left[I\otimes I+
\sum_i a_i\sigma_i\otimes I+
\sum_i b_iI\otimes\sigma_i+
\sum_{i,j}T_{ij}\sigma_i\otimes\sigma_j\right].
\tag{D26}
```

For any normalized two-qubit states $`\sigma,\tau`$,

```math
T_\sigma:T_\tau\leq1+2C(\sigma)C(\tau),
\tag{D27}
```

```math
|a_\sigma|,|b_\sigma|
\leq\sqrt{1-C_a(\sigma)^2}.
\tag{D28}
```

**Proof.** A pure state's correlation matrix has singular values $`(1,C,C)`$, as follows by writing its Schmidt form. The matrix trace inequality therefore bounds the correlation-matrix inner product of two pure states by $`1+2C_\sigma C_\tau`$. Expand the two mixed states into independent ensembles attaining, or approaching, their convex roofs. Bilinearity gives (D27). No equal-concurrence ensemble assumption is needed.

For each pure state in an ensemble, $`C(\psi_j)^2+|a_j|^2=1`$. The vectors $`(C(\psi_j),a_j)`$ have unit Euclidean norm, so their convex average has norm at most one. It follows that $`(\sum_jp_jC(\psi_j))^2+|a_\sigma|^2\leq1`$. Maximizing the average concurrence gives (D28), and the second marginal is identical. $`\square`$

For $`\sigma\in\mathcal K_{\eta_A}`$, $`\tau\in\mathcal K_{\eta_B}`$, let $`x=C_a(\sigma)`$, $`y=C_a(\tau)`$. Equations (D27) and (D28) imply

```math
\begin{aligned}
F_r(\sigma,\tau)
&:=T_\sigma:T_\tau+r(a_\sigma\cdot a_\tau+b_\sigma\cdot b_\tau)\\
&\leq1+2rxy+2r\sqrt{(1-x^2)(1-y^2)}\\
&\leq1+2r.
\end{aligned}
\tag{D29}
```

The last inequality is Cauchy-Schwarz for the unit vectors $`(x,\sqrt{1-x^2})`$ and $`(y,\sqrt{1-y^2})`$.

The lower bound needs no cone restriction. With the spin-flipped state $`\widetilde\tau=(Y\otimes Y)\tau^*(Y\otimes Y)`$, direct expansion gives

```math
F_r(\sigma,\tau)
=2(1+r)\operatorname{Tr}(\sigma\tau)
+2(1-r)\operatorname{Tr}(\sigma\widetilde\tau)-1
\geq-1.
\tag{D30}
```

Both traces are nonnegative, and $`0\leq r\leq1`$.

### The dual witness

On the two spatial reference-output pairs set

```math
Q_r=\frac{W_1W_2+r(W_1+W_2-I)}{1+r}.
\tag{D31}
```

For a spatial product state $`\sigma_{R_1R_2}\otimes\tau_{B_1B_2}`$, use

```math
W=\sum_{i=x,y,z}\sigma_i\otimes\sigma_i^T.
```

The expectations of $`W_1,W_2,W_1W_2`$ are respectively
$`a_\sigma\cdot a_{\tau^T}`$, $`b_\sigma\cdot b_{\tau^T}`$, and $`T_\sigma:T_{\tau^T}`$. Full transposition preserves both concurrence roofs. Therefore (D29) and (D30) give

```math
\left|\operatorname{Tr}[Q_r(\sigma\otimes\tau)]\right|
=\left|\frac{F_r(\sigma,\tau^T)-r}{1+r}\right|
\leq1.
\tag{D32}
```

### Adaptive histories and normalization

Apply an arbitrary allowed physical instrument to the independent, temporally delivered Bell probes. Condition on a complete classical history, including the initial shared random choice, and refine local Kraus outcomes where necessary. Once that history is fixed, all local control choices are fixed. The unnormalized positive Choi contribution factors spatially as

```math
J_h=p_h\,\sigma_h\otimes\tau_h,
\quad p_h\geq0,
\quad \sigma_h\in\mathcal K_{\eta_A},
\quad \tau_h\in\mathcal K_{\eta_B}.
\tag{D33}
```

This factorization retains each dephasing channel as a complete, unflagged channel. It uses the product physical noise specified before the gap. It does not condition on its hidden Kraus labels. Classical feedback only selects the two local maps associated with a fixed history; it does not create a quantum connection between them. A coarse accepted event can sum several such products and correlate error posteriors, which is why the argument is applied before coarse-graining.

Because the Bell probes are normalized and the physical instrument is complete,

```math
\sum_h p_h=1.
\tag{D34}
```

For a scored atom (D3), equations (D32)–(D34) yield

```math
\left|\operatorname{Tr}[Q_rJ(\mathcal F)]\right|
\leq\sum_h |s_h|p_h\leq1.
\tag{D35}
```

This proves the bound even for arbitrary adaptive classical communication and bounded postselection scores. The score cannot depend on an external tester's private measurement result: that would change the universal comb interface.

The ideal comb has normalized Choi state $`J_0=\Phi\otimes\Phi`$. Thus

```math
\operatorname{Tr}(Q_rJ_0)=\frac{9+5r}{1+r}.
\tag{D36}
```

Apply (D35) to every atom in (D4) and use the triangle inequality. It proves the lower bound in (D2), which is attained by the streaming construction (D16).

## 6. Endpoints, repeated blocks and scope tests

At $`r=0`$, $`Q_0=W_1W_2`$ and $`\Gamma_2=9`$. Complete dephasing at either laboratory removes the useful local temporal entanglement, regardless of the other laboratory's noiseless qubit. At $`r=1`$,

```math
Q_1=8\Phi\otimes\Phi-I,
\qquad \Gamma_2=7,
```

which is the ordinary dimension-four spatial separability witness. The unrestricted noiseless extent and teleportation-based wire-cutting background are treated in [Brenner, Piveteau and Sutter](https://arxiv.org/abs/2302.03366), while constant local control ancillas also occur in [Harrow and Lowe](https://arxiv.org/abs/2403.01018).

For $`m`$ independent two-slot blocks, resetting both memories after each block and applying (D16) independently gives extent

```math
\left(5+\frac4{1+r}\right)^m<9^m\qquad(r>0).
\tag{D37}
```

This is an upper bound for the unrestricted $`2m`$-slot problem. It is not an assertion that unrestricted many-slot optima multiply. Calibration and statistical error accounting for this particular repeated-block construction are given in [Precision and calibration](precision-calibration.md).

### Exact product law when both resets are imposed

There is a stronger conclusion for a different, explicitly restricted model. Suppose both laboratories are required to undergo complete entanglement-breaking resets between prescribed two-slot blocks. Within block $`b`$, each side has its one prescribed memory qubit and dephasing parameter $`\eta_{s,b}`$, as above. Require fresh noise instances across blocks, as well as the conditional product noise between the two laboratories inside each block. Then

```math
\boxed{\Gamma_{\mathrm{reset\ blocks}}
=\prod_{b=1}^m\left(5+\frac4{1+\eta_{A,b}\eta_{B,b}}\right).}
\tag{D37a}
```

For the converse, refine the measurement and preparation outcomes in each entanglement-breaking reset, granting their classical records if necessary. This enlarges the allowed operations and is legitimate for a lower bound. After conditioning on a full history, the normalized Bell-test Choi contribution factors over local block vertices. No system coherence crosses a reset, and freshness leaves the dephasing channels in the separate block factors. Within every block, the two local factors satisfy Lemma 3. The tensor product of that block's witness $`Q_{r_b}`$ therefore has absolute expectation at most one on a normalized full-history product. Summing the positive history probabilities and bounded scores gives the same bound for every physical atom. Its target expectation is the product in (D37a). Independent block constructions attain it.

The dephasing environments remain unrefined in this argument. System resets alone do not imply fresh environmental noise; hidden phase errors reused across blocks would not satisfy the stated noise model. The exact product law (D37a) must therefore be distinguished from the upper bound (D37) for memories that may remain coherent across arbitrarily many slots.

### Correlated noise: the same marginal channels can have a different optimum

Replace the product memory noise by a common random phase flip,

```math
\mathcal N(X)=\tfrac12X+
\tfrac12(Z_A\otimes Z_B)X(Z_A\otimes Z_B).
\tag{D38}
```

Each marginal channel is complete dephasing. Starting from a local temporal Bell pair at each laboratory gives

```math
\tfrac12(\Phi^+_{A_1A_2}\otimes\Phi^+_{B_1B_2})
+\tfrac12(\Phi^-_{A_1A_2}\otimes\Phi^-_{B_1B_2}).
\tag{D39}
```

The phase errors agree. After the bilateral slot twirls, this is exactly $`E_1`$, not $`E_0`$: its local correlation-tensor overlap is three. Consequently (D16) with $`r=1`$ achieves extent seven even though both marginal coherence factors are zero. The spatial witness $`Q_1`$ bounds every spatially separable scored branch by one, proving seven is optimal in this example.

Thus independent complete dephasing gives nine, while the correlated noise (D38) gives seven with the same marginal channels. Individual-memory calibration does not establish the product-noise assumption. Access to phase-error flags would also change the answer, since it would permit correction of the memory errors.

### Early second input: abstract causal channels do not enforce memory use

Keep $`\eta_A=0`$, $`\eta_B=1`$, but give Alice both source inputs before the gap. She can perform both of her resource-side teleportation measurements before the gap and retain only their classical outcomes. Bob uses his noiseless qubit to hold the second resource output. This implements the four resources in (D16) with $`r=1`$, so the extent is seven rather than the nine predicted for the strict interface.

More explicitly, for the $`E_1`$ atom Alice prepares a local Bell pair on her two resource ports, twirls them, and Bell-measures each against its already available input. She has no quantum system left to protect during the gap. Bob prepares his local Bell pair, releases and corrects its first port, and stores its second port until the second output time. The product resources are simpler versions of the same schedule. Their averaged maps remain correlated Pauli combs, so the counterexample need not introduce signaling from a later input to an earlier output at the abstract map level. It violates the physical input-availability condition instead.

The spatial lower bound seven again proves optimality in this relaxed example. Similarly, allowing Bob to retain the first output until after the gap removes the reason his two-time resource must pass through his prescribed memory. Both port-release conditions are substantive assumptions.

## 7. Precision of the claim

Equation (D2) is exact for universal, unbiased, signed bounded-score simulation in the stated resource class. It is not a lower bound on the number of shots needed by every possible estimator, and $`\Gamma_2^2`$ is only the usual bounded-range sampling upper-bound factor. Learning an observable-specific cut, exploiting a promised circuit family or accepting controlled bias changes the estimation problem. [Harrow and Lowe, Section 2.2](https://arxiv.org/abs/2403.01018) distinguish extent from actual variance, and [Harada et al.](https://arxiv.org/abs/2512.19623) give tomography-based examples with polynomial measurement scaling for promised tree structures.

No characterization of arbitrary memory channels, correlated environments or the unrestricted optimum for all numbers of noisy slots is implied. The concurrence-cone argument and the four-resource construction establish precisely the two-slot theorem above.
