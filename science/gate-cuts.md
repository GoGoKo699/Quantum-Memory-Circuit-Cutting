# Two-qubit gate cuts under prescribed memory breaks

The reset-schedule law extends from identity wires to arbitrary two-qubit unitary slots. The factor assigned to an interval is determined by the operator Schmidt coefficients of its gates. The normalized Choi convention is essential: a two-qubit gate has a four-dimensional local reference-output space, but its Schmidt rank can be smaller than four.

The unrestricted black-box gate-cutting optimum and the virtual-resource construction are due to [Schmitt, Piveteau, and Sutter, Theorems 6.2 and 6.4](https://arxiv.org/html/2312.11638v4). Their signed-instrument convention is given in Definition 2.2. This section reconstructs the upper bound in the strict slot interface and combines it with the epoch factorization and forest converse. The result concerns universal open gate slots; a known circuit containing cancellations or additional structure can have a smaller circuit-specific cost.

## 1. Normalized KAK coefficients

At slot $j$, one input qubit arrives at each laboratory. The desired operation is the known two-qubit unitary

$$
U_j=(V_{A,j}\otimes V_{B,j})
\left(\sum_{\alpha=0}^3u_{j\alpha}\,
\sigma_\alpha\otimes\sigma_\alpha\right)
(W_{A,j}\otimes W_{B,j}),
$$

where $\sigma_0=I$ and $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices. The KAK coefficients are normalized by

$$
\sum_{\alpha=0}^3|u_{j\alpha}|^2=1.
$$

Define

$$
\chi_j=\left(\sum_{\alpha=0}^3|u_{j\alpha}|\right)^2,
\qquad 1\leq\chi_j\leq4.
$$

Outer one-qubit unitaries are free local operations and can be executed at the actual slot. They do not change $\chi_j$.

For a single-qubit operator $L$, write

$$
|L\rangle\!\rangle=(I\otimes L)|\Phi_2\rangle.
$$

If $L$ is unitary, this vector has norm one. In particular,

$$
\langle\!\langle L|M\rangle\!\rangle
=\frac12\operatorname{Tr}(L^\dagger M).
$$

The normalized gate Choi vector is

$$
|J(U_j)\rangle
=\sum_\alpha u_{j\alpha}
|V_{A,j}\sigma_\alpha W_{A,j}\rangle\!\rangle_A
\otimes
|V_{B,j}\sigma_\alpha W_{B,j}\rangle\!\rangle_B.
$$

The local vectors in either sum are orthonormal, since the Pauli operators are orthonormal in the normalized Hilbert--Schmidt inner product. Absorbing the phase of each nonzero coefficient into one local vector gives a Schmidt decomposition with coefficients $|u_{j\alpha}|$. There is no additional factor of two in these normalized Choi Schmidt coefficients.

## 2. Exact theorem

Use the [operational model](model.md), with prescribed Alice and Bob coherence-epoch partitions $\mathcal P_A,\mathcal P_B$. Every actual future input is inaccessible until its own slot, and each current output must be released before the next slot. At a prescribed boundary, all private persistent quantum memory of that laboratory undergoes an entanglement-breaking channel. Memory dimension within epochs is unrestricted.

Let $\mathcal I$ be the common refinement of the two partitions. Set

$$
\chi_I=\prod_{j\in I}\chi_j.
$$

**Theorem 1 — Gate common-refinement law.** The optimal signed extent for the ordered gate process is

$$
\boxed{
\Gamma_{\mathcal P_A,\mathcal P_B}(U_1,\ldots,U_n)
=\prod_{I\in\mathcal I}(2\chi_I-1).
}
$$

The lower bound permits arbitrary local instruments, shared randomness, and two-way classical communication. The upper bound uses local operations and bounded classical scores, with a shared initial sample label; no communication between laboratories during the quantum execution is needed. Its private resource storage is charged and survives only within a common interval.

### Lower bound

The epoch-overlap graph is a forest by Lemma 2 of [Reset schedules](reset-schedules.md). Proposition 3 there applies also to gate slots: each epoch's local Choi registers now contain both the local input references and the local outputs. After refining the physical branches, the Choi operator is a nonnegative mixture of products over epoch vertices, with total trace weight one. Bounded outcome-dependent scores preserve the unit witness bound.

The target Choi state is

$$
J(\mathcal T)=\bigotimes_{j=1}^n
|J(U_j)\rangle\langle J(U_j)|.
$$

The edge corresponding to $I$ carries the product of the gate Choi states in that interval. Its Schmidt coefficients are the nonzero products

$$
s_{I,\boldsymbol\alpha}
=\prod_{j\in I}|u_{j\alpha_j}|.
$$

They obey $\sum_{\boldsymbol\alpha}s_{I,\boldsymbol\alpha}^2=1$ and

$$
\left(\sum_{\boldsymbol\alpha}s_{I,\boldsymbol\alpha}\right)^2
=\prod_{j\in I}\left(\sum_{\alpha_j}|u_{j\alpha_j}|\right)^2
=\chi_I.
$$

Apply the arbitrary-Schmidt-support witness of [Theorem 1 in Forest witness](forest-witness.md) to these pure edges. It has absolute expectation at most one on every scored physical atom, while its target expectation is $\prod_I(2\chi_I-1)$. The signed-decomposition triangle inequality proves the lower bound.

This use of the full endpoint space matters for gates of Schmidt rank one or two. The edge witness is $2|\Omega_I\rangle\langle\Omega_I|-I$ on the entire local Choi spaces, where $|\Omega_I\rangle$ sums only over the actual Schmidt support. The forest contraction proof does not presume that this support fills those spaces.

## 3. One uninterrupted interval: virtual resources

We now prove the matching upper bound for an interval of $m$ gates. Relabel its slots $1,\ldots,m$ and temporarily omit the outer local KAK unitaries, which will be restored at each slot.

Let $\boldsymbol k=(k_1,\ldots,k_m)$ be a Pauli-label string and define

$$
w_{\boldsymbol k}=\prod_{j=1}^m u_{j k_j},
\qquad
s_{\boldsymbol k}=|w_{\boldsymbol k}|,
\qquad
\theta_{\boldsymbol k}=\arg w_{\boldsymbol k}.
$$

Zero coefficients can be omitted. Introduce two private resource qubits $R_{L,j},S_{L,j}$ per slot and per laboratory $L\in\{A,B\}$. The local Bell-basis vectors are

$$
|\boldsymbol k\rangle\!\rangle_L
=\bigotimes_{j=1}^m|\sigma_{k_j}\rangle\!\rangle_{R_{L,j}S_{L,j}}.
$$

The formal parallel Choi vector of the KAK cores is

$$
|\Psi\rangle
=\sum_{\boldsymbol k}w_{\boldsymbol k}
|\boldsymbol k\rangle\!\rangle_A
|\boldsymbol k\rangle\!\rangle_B.
$$

Set

$$
|a_{\boldsymbol k}\rangle
=e^{i\theta_{\boldsymbol k}}|\boldsymbol k\rangle\!\rangle_A,
\qquad
|b_{\boldsymbol k}\rangle
=|\boldsymbol k\rangle\!\rangle_B.
$$

These are orthonormal families, and $|\Psi\rangle=\sum_{\boldsymbol k}s_{\boldsymbol k}|a_{\boldsymbol k}\rangle|b_{\boldsymbol k}\rangle$ is its Schmidt form. The finite decomposition proved in [Forest witness, Section 4](forest-witness.md) expresses $|\Psi\rangle\langle\Psi|$ as diagonal product states plus eight signed local cat products for every unordered distinct pair $\{\boldsymbol k,\boldsymbol l\}$. Its extent is

$$
\sum_{\boldsymbol k}s_{\boldsymbol k}^2
+4\sum_{\boldsymbol k<\boldsymbol l}s_{\boldsymbol k}s_{\boldsymbol l}
=2\left(\sum_{\boldsymbol k}s_{\boldsymbol k}\right)^2-1
=2\chi_I-1.
$$

Every term is a physical product state across the laboratories. It can be prepared before the interval's first actual input arrives, using only the specified gate descriptions and a sampled classical label. This preparation is of private virtual resources, not of future data inputs.

For non-Clifford gates, ordinary gate teleportation with this formal Choi state would generally require nonlocal corrections. The next step is therefore essential: the simulator knows which diagonal or pair contribution it sampled and can correct Pauli commutation factors by a bounded final score.

## 4. The local teleportation identity

For a Pauli label $a$, choose the Bell vector on an incoming qubit $Q$ and a resource-input qubit $R$ as

$$
|\beta_a\rangle_{QR}
=(I\otimes\sigma_a^*)|\Phi_2\rangle_{QR}.
$$

With resource $|P\rangle\!\rangle_{RS}$, contraction gives

$$
(\langle\beta_a|_{QR}\otimes I_S)
\left(|\varphi\rangle_Q\otimes|P\rangle\!\rangle_{RS}\right)
=\frac12P\sigma_a|\varphi\rangle_S.
$$

After applying $\sigma_a$ to the output, a Pauli $P=\sigma_k$ satisfies

$$
\sigma_aP\sigma_a=f(a,k)P,
\qquad f(a,k)\in\{+1,-1\}.
$$

Consequently, for a resource matrix unit $|\sigma_k\rangle\!\rangle\langle\!\langle\sigma_l|$, the conditional corrected map on an arbitrary input operator $X$ is

$$
X\longmapsto
\frac14 f(a,k)f(a,l)\,
\sigma_kX\sigma_l^\dagger.
$$

The identity also holds when $X$ acts jointly on an inaccessible reference: the Pauli operators then act only on the local input factor. It is an operator identity, not an assumption about pure or uncorrelated data.

At gate slot $j$, Alice and Bob perform this local Bell measurement separately, with outcomes $a_j,b_j$, and apply their local Pauli corrections before returning the outputs. For a fixed pair of multi-indices, define the classical sign

$$
h_{\boldsymbol k\boldsymbol l}(\boldsymbol a,\boldsymbol b)
=\prod_{j=1}^m
f(a_j,k_j)f(a_j,l_j)
f(b_j,k_j)f(b_j,l_j).
$$

Its absolute value is one. If $\boldsymbol k=\boldsymbol l$, it is identically one.

## 5. Why pair-dependent scoring reconstructs the gates

Consider one off-diagonal pair. Its eight resource terms sum to

$$
R_{\boldsymbol k\boldsymbol l}
=s_{\boldsymbol k}s_{\boldsymbol l}
\left(
|a_{\boldsymbol k}b_{\boldsymbol k}\rangle
\langle a_{\boldsymbol l}b_{\boldsymbol l}|
+|a_{\boldsymbol l}b_{\boldsymbol l}\rangle
\langle a_{\boldsymbol k}b_{\boldsymbol k}|
\right).
$$

Assign the same score $h_{\boldsymbol k\boldsymbol l}$ to all eight underlying physical resource terms. Their positive diagonal pieces cancel in the signed sum separately for every Bell-outcome string. Thus the calculation can be performed on $R_{\boldsymbol k\boldsymbol l}$ itself. Each of its two matrix units accumulates the same commutation sign $h_{\boldsymbol k\boldsymbol l}$. Multiplication by that sign cancels it exactly.

After cancellation, a fixed Bell-outcome string contributes the intended left-right Pauli-path map with scalar factor $16^{-m}$, since each slot contains two local Bell contractions. Summing over the $16^m$ possible Bell-outcome strings restores that path map with unit coefficient. This is a linear-map normalization; the probabilities of the outcomes in a physical sampled run need not be uniform. The diagonal resource terms require no extra score and reconstruct the diagonal paths in the same way.

This argument continues to hold with arbitrary causal operations between the slots. Insert their Kraus operators between the successive Pauli factors in each left-right path. The local teleportation identity pulls out exactly the same scalar commutation sign at each slot, independent of those Kraus operators. An external reference can be included among their registers, and adaptive outcomes can be kept in classical registers. The only necessary information boundary is the one in the [model](model.md): the external tester acts on the ports, not on the cutter's private sample label or Bell records.

Summing all diagonal and off-diagonal path contributions yields the expansion of the target sequence of KAK cores, with coefficient $w_{\boldsymbol k}w_{\boldsymbol l}^*$ for each pair of paths. Restoring $W_{A,j},W_{B,j}$ immediately before the local teleportation step and $V_{A,j},V_{B,j}$ immediately after its output correction reconstructs every original $U_j$ at its actual slot.

For each sampled local resource, the underlying procedure is a physical causal instrument. Its score is bounded by one. The exterior coefficients are exactly those of the finite resource decomposition, so their absolute sum remains $2\chi_I-1$. This proves the uninterrupted-interval upper bound without assuming that a non-Clifford gate can be teleported with ordinary physical local corrections alone.

## 6. Storage, preparation, and sampling

The explicit implementation above uses two private resource qubits per gate at each laboratory, or four per gate across both laboratories. The actual input qubits are additional transient systems. At each slot, $R_{L,j}$ is measured with the incoming data, while $S_{L,j}$ becomes the released output. Only unused future resources remain private. At the end of the interval all resource ports have been consumed or released, and any remaining local workspace can be discarded.

A local cat between two product Bell-basis strings can be prepared from the two classical label strings: prepare their two-term superposition in a computational basis and apply a fixed local Bell-basis transform to each pair of qubits. The binary-branch construction in [Wire construction](wire-construction.md) performs this preparation with a transient branch qubit and $O(m)$ local operations. The relative phase on Alice's branch includes $\theta_{\boldsymbol l}-\theta_{\boldsymbol k}$; it is computed from the known KAK coefficients. The branch qubit can be returned clean before the first data input arrives. This gives an explicit finite preparation route without a state-loading oracle.

The coefficient distribution also has a short sampler. Put

$$
S_j=\sum_\alpha|u_{j\alpha}|,
\qquad
q_{j\alpha}=\frac{|u_{j\alpha}|}{S_j},
\qquad
S=\prod_jS_j=\sqrt{\chi_I}.
$$

The diagonal terms have total weight one; conditioned on that part of the sampling distribution, draw $\boldsymbol k$ independently with probabilities $|u_{jk_j}|^2$. The off-diagonal terms have total weight $2(\chi_I-1)$; conditioned on that part, draw an unordered distinct pair with probability

$$
\frac{2s_{\boldsymbol k}s_{\boldsymbol l}}{\chi_I-1},
$$

and choose a common $X$ or $Y$ cat axis and two independent signs according to the eight-term decomposition. The outer branch probabilities are these total weights divided by $2\chi_I-1$.

To draw the distinct pair without enumerating $4^m$ strings or relying on repeated trials when the gates are weak, define

$$
c_j=\sum_\alpha q_{j\alpha}^2,
\qquad
T_j=\prod_{t=j}^m c_t,
\qquad T_{m+1}=1.
$$

Draw an ordered pair of strings from the product distribution $q\otimes q$, conditioned on the strings differing. Before their first differing position, the conditional probability of labels $\alpha,\beta$ at position $j$ is

$$
\frac{q_{j\alpha}q_{j\beta}
\left(1-\mathbf 1_{\alpha=\beta}T_{j+1}\right)}{1-T_j}.
$$

After a difference has occurred, draw the remaining labels independently. The denominator is nonzero whenever this conditioned state is reached. Forgetting the order gives the required unordered distribution. If $\chi_I=1$, no off-diagonal branch is present. There are only sixteen candidate label pairs per position, so the sampler needs $O(m)$ elementary probability updates and $O(m)$ storage given the KAK coefficients. Numerical arithmetic and rotation synthesis must, as usual, be performed at the precision required by the desired implementation accuracy.

These storage counts are sufficient resources for the exact upper bound. They are not a minimum-memory theorem for general gate sequences. The one-persistent-qubit result stated for identity wires is a separate, more tightly accounted construction.

## 7. Completing the reset theorem

Run the uninterrupted-interval protocol independently on every $I\in\mathcal I$. Its resources are prepared after the interval begins and consumed before it ends. Because $I$ lies in a single epoch at both laboratories, no required private quantum resource crosses a prescribed break. At a boundary where only one side is forced to reset, the other side may voluntarily discard its no-longer-needed resources.

The interval extents multiply, giving $\prod_I(2\chi_I-1)$ and matching the lower bound. This completes Theorem 1. $\square$

For CNOT, $\chi_j=2$, so its gate-slot reset law has the same factors as the qubit-wire law. For SWAP, $\chi_j=4$. A product unitary has $\chi_j=1$ and contributes no additional extent. For the entangling family $\exp(-i\theta Z\otimes Z)$,

$$
\chi_j=(|\cos\theta|+|\sin\theta|)^2
=1+|\sin2\theta|,
$$

which also displays the continuous weak-interaction limit of the exact formula.

The gate result is exact. The simple relative-error witness estimate for maximally entangled wire edges cannot be copied unchanged to general gates: a gate edge's witness spectral norm depends on its Schmidt rank, while its target expectation depends on $\chi_I$. Approximation claims must use the appropriate norm and spectrum, as discussed in [Precision and calibration](precision-calibration.md). The prescribed-reset theorem likewise does not describe arbitrary partial noise or a generic memory-size constraint.
