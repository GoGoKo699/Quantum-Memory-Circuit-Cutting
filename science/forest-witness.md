# A separable norm identity on forests

The reset-schedule theorem rests on a distinction between two kinds of correlation. A laboratory may maintain arbitrary quantum correlations among the ports belonging to one uninterrupted coherence epoch. Across an entanglement-breaking boundary, only a classical record survives. The resulting Choi operators are therefore separable over epochs, although a single epoch can contain many entangled port registers. The theorem below bounds precisely this larger class of local correlations.

For a forest whose edges carry pure bipartite states, the optimal signed decomposition into states that are fully separable over the vertices has a product formula. The single-edge factor is the familiar pure-state standard-robustness factor. The forest argument shows why joint operations on several incident registers cannot improve the product when the vertex graph has no cycle. The connection to standard robustness uses the convention introduced by [Vidal and Tarrach](https://arxiv.org/abs/quant-ph/9806094).

## 1. States and the decomposition norm

Let $`G=(V,E)`$ be a finite undirected forest. For each edge $`e=\{v,w\}`$, give its two endpoints finite-dimensional spaces $`\mathcal H_{v,e}`$ and $`\mathcal H_{w,e}`$. The complete space of vertex $`v`$ is

$$
\mathcal H_v=\bigotimes_{e\ni v}\mathcal H_{v,e}.
$$

An individual vertex state may be entangled among all its incident registers. Full separability refers only to the partition into the spaces $`\mathcal H_v`$:

$$
\operatorname{Sep}(V)
=\operatorname{conv}\left\{\bigotimes_{v\in V}\rho_v:
\rho_v\geq0,\ \operatorname{Tr}\rho_v=1\right\}.
$$

For a density operator $`\rho`$, define its signed separable extent by

$$
\Gamma_{\operatorname{Sep}(V)}(\rho)
=\inf\left\{\sum_\ell|a_\ell|:
\rho=\sum_\ell a_\ell\sigma_\ell,
\quad a_\ell\in\mathbb R,
\quad \sigma_\ell\in\operatorname{Sep}(V)\right\}.
$$

Each edge has a normalized pure state with Schmidt decomposition

$$
|\psi_e\rangle
=\sum_{i=1}^{r_e}s_{e i}
|a_{e i}\rangle|b_{e i}\rangle,
\qquad s_{e i}>0,
\qquad \sum_i s_{e i}^{2}=1.
$$

The endpoint dimensions may exceed $`r_e`$. Define

$$
S_e=\sum_i s_{e i},
\qquad g_e=2S_e^2-1,
\qquad
\rho_G=\bigotimes_{e\in E}|\psi_e\rangle\langle\psi_e|.
$$

The tensor factors of $`\rho_G`$ are regrouped by vertices when evaluating separability.

**Theorem 1 — Pure-edge forest identity.** For every such forest,

$$
\boxed{
\Gamma_{\operatorname{Sep}(V)}(\rho_G)
=\prod_{e\in E}g_e
=\prod_{e\in E}\left[2\left(\sum_i s_{e i}\right)^2-1\right].
}
$$

An empty product equals one. Product states on any additional isolated vertex do not change the value.

## 2. A contraction bound for one edge

Introduce the unnormalized vector on the Schmidt support,

$$
|\Omega_e\rangle
=\sum_{i=1}^{r_e}|a_{e i}\rangle|b_{e i}\rangle,
\qquad
W_e=2|\Omega_e\rangle\langle\Omega_e|-I.
$$

The identity acts on the full endpoint space, including directions outside the Schmidt support. This choice is necessary when the local Choi space is larger than the operator Schmidt rank of a gate.

**Lemma 2 — Leaf contraction.** Let $`R`$ be any Hermitian operator on one endpoint of an edge, and define

$$
M=\operatorname{Tr}_{v,e}[(R\otimes I)W_e].
$$

Then $`M`$ is Hermitian and

$$
\|M\|_\infty\leq\|R\|_1.
$$

**Proof.** Fix a unit vector $`|z\rangle`$ at the other endpoint and set

$$
|\widetilde z\rangle
=\sum_{i=1}^{r_e}\langle z|b_{e i}\rangle|a_{e i}\rangle.
$$

Orthonormality gives $`\|\widetilde z\|\leq1`$. Direct contraction yields

$$
\langle z|M|z\rangle
=\operatorname{Tr}\left[
R\left(2|\widetilde z\rangle\langle\widetilde z|-I\right)
\right].
$$

The operator in parentheses has eigenvalue $`2\|\widetilde z\|^2-1`$ in the direction of $`\widetilde z`$ and eigenvalue $`-1`$ on its orthogonal complement. Its operator norm is at most one. Trace-norm duality therefore gives

$$
|\langle z|M|z\rangle|\leq\|R\|_1.
$$

The expression is real for every $`z`$, so $`M`$ is Hermitian, and taking the supremum proves the claim. Equivalently, Hermiticity follows from cyclicity of the partial trace with respect to operators on the traced subsystem. $`\square`$

If the Schmidt support fills both endpoint spaces and corresponding Schmidt bases are identified, the contraction has the particularly simple form

$$
M=2R^{\mathsf T}-\operatorname{Tr}(R)I.
$$

For eigenvalues $`r_i`$ of $`R`$, the required estimate is then

$$
\left|2r_i-\sum_jr_j\right|
=\left|r_i-\sum_{j\ne i}r_j\right|
\leq\sum_j|r_j|.
$$

The proof needs the bound for all Hermitian $`R`$, rather than only positive $`R`$, because eliminating an earlier leaf can produce a signed operator at its neighbor.

**Lemma 3 — Absorbing a message.** If $`M`$ is Hermitian on $`\mathcal K`$ and $`S`$ is Hermitian on $`\mathcal K\otimes\mathcal L`$, then

$$
R'=\operatorname{Tr}_{\mathcal K}[(M\otimes I)S]
$$

is Hermitian and satisfies

$$
\|R'\|_1\leq\|M\|_\infty\|S\|_1.
$$

**Proof.** For any Hermitian $`H`$ on $`\mathcal L`$ with $`\|H\|_\infty\leq1`$,

$$
|\operatorname{Tr}(HR')|
=|\operatorname{Tr}[(M\otimes H)S]|
\leq\|M\otimes H\|_\infty\|S\|_1
\leq\|M\|_\infty\|S\|_1.
$$

Taking the dual supremum gives the result. Partial-trace cyclicity gives Hermiticity. $`\square`$

## 3. The forest witness

Define

$$
W_G=\bigotimes_{e\in E}W_e.
$$

**Lemma 4 — Product-vertex bound.** For any normalized vertex density operators,

$$
\left|\operatorname{Tr}\left[
W_G\bigotimes_{v\in V}\rho_v
\right]\right|\leq1.
$$

**Proof.** Work first on a connected tree. Initially assign the Hermitian operator $`R_v=\rho_v`$ to every vertex, so $`\|R_v\|_1=1`$. Choose a leaf $`v`$, with neighbor $`w`$ and edge $`e`$. Contract $`R_v`$ through $`W_e`$ to obtain a Hermitian operator $`M`$ on the corresponding register of $`w`$. Lemma 2 gives $`\|M\|_\infty\leq1`$. Absorb $`M`$ into $`R_w`$ and trace that register. Lemma 3 gives a new Hermitian operator on the remaining registers of $`w`$ with trace norm at most one.

The scalar tensor contraction is unchanged. Removing $`v`$ and $`e`$ leaves a smaller tree with the same invariant. Continue until one vertex remains. The final contraction is its trace, whose absolute value is at most its trace norm and hence at most one. A forest is a disjoint union of trees, and its contractions multiply. $`\square`$

Convexity extends the bound to every $`\sigma\in\operatorname{Sep}(V)`$. The target expectation is

$$
\operatorname{Tr}(W_G\rho_G)
=\prod_e\langle\psi_e|W_e|\psi_e\rangle
=\prod_e(2S_e^2-1),
$$

because $`\langle\Omega_e|\psi_e\rangle=S_e`$. Therefore every signed separable decomposition obeys

$$
\prod_e g_e
=\sum_\ell a_\ell\operatorname{Tr}(W_G\sigma_\ell)
\leq\sum_\ell|a_\ell|.
$$

This proves the lower bound in Theorem 1.

## 4. A matching finite decomposition

It is enough to construct a single-edge decomposition. Suppress the edge label. For $`i<j`$, define on the first endpoint

$$
X_{ij}^{A}=|a_i\rangle\langle a_j|+|a_j\rangle\langle a_i|,
\qquad
Y_{ij}^{A}=-i|a_i\rangle\langle a_j|+i|a_j\rangle\langle a_i|,
$$

and define $`X_{ij}^{B},Y_{ij}^{B}`$ in the corresponding $`b`$ basis. Then

$$
|\psi\rangle\langle\psi|
=\sum_i s_i^2
|a_i\rangle\langle a_i|\otimes|b_i\rangle\langle b_i|
 +\frac12\sum_{i<j}s_i s_j
\left(X_{ij}^{A}\otimes X_{ij}^{B}
-Y_{ij}^{A}\otimes Y_{ij}^{B}\right).
$$

Each $`X`$ is a difference of the two normalized projectors onto

$$
|x_{ij}^{\pm}\rangle
=\frac{|a_i\rangle\pm|a_j\rangle}{\sqrt2},
$$

and each $`Y`$ is a difference of the projectors onto

$$
|y_{ij}^{\pm}\rangle
=\frac{|a_i\rangle\pm i|a_j\rangle}{\sqrt2}.
$$

The same identities hold at the second endpoint. Consequently each pair $`i<j`$ contributes eight signed product density operators, each with coefficient magnitude $`s_i s_j/2`$. The total coefficient extent is

$$
\sum_i s_i^2+4\sum_{i<j}s_i s_j
=2\left(\sum_i s_i\right)^2-1.
$$

Tensor these decompositions over edges. Each resulting term is a product of endpoint density operators. Group all factors incident on a common vertex; this produces a normalized state at that vertex. The overall term is therefore fully separable over vertices, and its extent is the product of the single-edge extents. This proves the upper bound and completes Theorem 1. $`\square`$

The proof also identifies the exact relation with standard robustness. If

$$
R_{\operatorname{Sep}(V)}(\rho)
=\inf\left\{t\geq0:
\rho=(1+t)\sigma_+-t\sigma_-,
\quad \sigma_\pm\in\operatorname{Sep}(V)\right\},
$$

then collecting the positive and negative terms of any decomposition, and using $`\operatorname{Tr}\rho=1`$, gives

$$
\Gamma_{\operatorname{Sep}(V)}(\rho)=1+2R_{\operatorname{Sep}(V)}(\rho).
$$

Both the positive and the negative normalized states must be separable. Replacing the negative state by an arbitrary density operator defines a different robustness and is not the norm evaluated here.

## 5. Why a cycle changes the problem

The leaf argument cannot be extended to arbitrary graphs. Consider a four-cycle with a qubit at each edge endpoint, so every vertex contains two qubits. Place a Bell state between those two local qubits at each vertex. Their tensor product $`\sigma`$ is fully separable over the four vertices. For each edge let $`\Phi_e`$ be the normalized Bell projector and set $`W_e=4\Phi_e-I`$.

A computational-basis contraction gives

$$
\operatorname{Tr}\left[\sigma\prod_{e\in S}\Phi_e\right]
=4^{-|S|}
\quad\text{for every proper subset }S\subsetneq E,
$$

whereas projecting all four edges closes the loop and gives $`4^{-3}`$. Expanding the four witness factors therefore yields

$$
\operatorname{Tr}(W_G\sigma)
=\sum_{k=0}^{3}\binom4k(-1)^{4-k}+4^4\,4^{-3}
=-1+4=3.
$$

Thus $`W_G`$ is not bounded by one on product-vertex states for this cycle. This calculation does not establish the optimal decomposition norm on cyclic graphs; it establishes the precise boundary of the forest witness used here.

The temporal overlap graph in [Reset schedules](reset-schedules.md) is always a forest, which is why this obstruction does not arise in the circuit-cutting theorem. The [wire construction](wire-construction.md) realizes its maximally entangled edge decomposition causally, and [Gate cuts](gate-cuts.md) applies the arbitrary-Schmidt version to normalized two-qubit-unitary Choi states.
