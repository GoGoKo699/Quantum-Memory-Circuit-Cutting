# A causal construction with one persistent qubit

This section gives an explicit protocol for one uninterrupted interval of wire cuts. It attains signed extent $2D-1$, where $D$ is the product of the wire dimensions, while retaining only one private qubit at each laboratory between slots. It prepares each resource port just before that port is needed and returns the persistent qubit exactly clean. The construction therefore supplies the attainable side of the [common-refinement theorem](reset-schedules.md).

The collective extent is the known wire-cutting value of [Brenner, Piveteau, and Sutter](https://arxiv.org/abs/2302.03366). Its realization through coherent superpositions of two product alternatives is closely related to the pairwise coherent-LCU techniques of [Harrow and Lowe](https://arxiv.org/abs/2403.01018). The account here makes the input-release times, persistent storage, sampling procedure, and clean return explicit.

## 1. The resource identity

Consider an interval of $m$ slots, with dimensions $d_1,\ldots,d_m$, and write

$$
D=\prod_{j=1}^m d_j.
$$

A basis label is a string $x=(x_1,\ldots,x_m)$ with $0\leq x_j<d_j$. Under this product-basis identification,

$$
|\Phi_D\rangle
=\frac1{\sqrt D}\sum_x |x\rangle_A|x\rangle_B,
\qquad
\Phi_D=\bigotimes_{j=1}^m\Phi_{d_j}.
$$

The subscripts $A,B$ here label local resource ports. They do not presume that the physical protocol can prepare an entangled state between the laboratories. Instead, the entangled operator will be expressed as a signed sum of local resource states.

For an unordered pair $x<y$, define

$$
X_{xy}=|x\rangle\langle y|+|y\rangle\langle x|,
\qquad
Y_{xy}=-i|x\rangle\langle y|+i|y\rangle\langle x|.
$$

Expanding the matrix elements of $\Phi_D$ gives

$$
\Phi_D
=\frac1D\sum_x|x\rangle\langle x|\otimes|x\rangle\langle x|
+\frac1{2D}\sum_{x<y}
\left(X_{xy}\otimes X_{xy}-Y_{xy}\otimes Y_{xy}\right).
$$

Let $P_{xy,X}^{s}$ and $P_{xy,Y}^{s}$, for $s\in\{+1,-1\}$, be the projectors onto

$$
|c_{xy,X}^{s}\rangle
=\frac{|x\rangle+s|y\rangle}{\sqrt2},
\qquad
|c_{xy,Y}^{s}\rangle
=\frac{|x\rangle+i s|y\rangle}{\sqrt2}.
$$

Then $X_{xy}=P_{xy,X}^{+}-P_{xy,X}^{-}$ and $Y_{xy}=P_{xy,Y}^{+}-P_{xy,Y}^{-}$. Each pair contributes eight normalized product density operators. The coefficient of $P_{xy,X}^{s}\otimes P_{xy,X}^{t}$ is $st/(2D)$, and the coefficient of $P_{xy,Y}^{s}\otimes P_{xy,Y}^{t}$ is $-st/(2D)$. The diagonal terms have coefficient $1/D$.

The total coefficient extent is consequently

$$
\Gamma
=D\frac1D+\binom D2\frac8{2D}
=2D-1.
$$

Every sampled term is a product state across Alice and Bob. Its correlations between different slots are local quantum correlations, which are exactly the resource supplied by the persistent memories.

## 2. Sampling without enumerating the decomposition

The decomposition contains quadratically many terms in $D$, but a sample has a short classical description. The following procedure samples each term with probability equal to its coefficient magnitude divided by $\Gamma$.

1. With probability $1/\Gamma$, draw a uniform label $x$ and select $|x\rangle_A|x\rangle_B$, with positive sign.
2. Otherwise draw a uniform unordered distinct pair $\{x,y\}$, choose $X$ or $Y$ uniformly, and choose $s,t\in\{+1,-1\}$ independently and uniformly. Prepare the corresponding local cat states. The sign is $st$ for $X$ and $-st$ for $Y$.

For an off-diagonal term the probability is

$$
\frac{2D-2}{2D-1}\,
\frac1{\binom D2}\,\frac12\,\frac14
=\frac1{2D\Gamma},
$$

as required. Two independent uniform labels, conditioned on being different, give a uniform unordered pair; the expected number of trials is $1/(1-1/D)\leq2$ for $D\geq2$.

For qubit wires, a label consists of $m$ classical bits. The sample uses $O(m)$ random bits in expectation and $O(m)$ classical storage for the two labels and phase choices. A rational branch probability such as $1/(2^{m+1}-1)$ can be sampled by ordinary uniform-integer rejection using $O(m)$ bits. No exponentially long coefficient table, amplitude-loading oracle, or quantum-addressed memory is required. For nonbinary dimensions, the labels use $\sum_j\lceil\log_2d_j\rceil$ bits and can be sampled one symbol at a time.

The initial label may be shared classically before the interval begins. Teleportation outcomes are communicated as the slots occur. The final bounded experimental outcome is multiplied by the sampled sign and $\Gamma$.

## 3. Generating a local cat state online

It remains to prepare

$$
|c_{xy}^{\zeta}\rangle
=\frac{|x\rangle+\zeta|y\rangle}{\sqrt2},
\qquad \zeta\in\{1,-1,i,-i\},
$$

one output register at a time. Let $f$ and $\ell$ be the first and last positions where $x$ and $y$ differ. Use one persistent qubit $M$, initially $|0\rangle$.

Before slot $f$, emit the fixed symbols $x_j=y_j$ without coupling them to $M$. At slot $f$, prepare

$$
\frac{|0\rangle_M+\zeta|1\rangle_M}{\sqrt2}.
$$

For each $f\leq j<\ell$, initialize a fresh output register in $|x_j\rangle$ and apply a memory-controlled permutation that sends $|x_j\rangle$ to $|y_j\rangle$ on the $M=1$ branch. If the two symbols agree, this operation is the identity. The emitted prefix is now coherently correlated with the binary branch held by $M$.

At the last differing position, initialize the output register and apply an isometry satisfying

$$
|0\rangle_M|0\rangle_{R_\ell}
\longmapsto |0\rangle_M|x_\ell\rangle_{R_\ell},
$$

$$
|1\rangle_M|0\rangle_{R_\ell}
\longmapsto |0\rangle_M|y_\ell\rangle_{R_\ell}.
$$

The two output states are orthogonal because $x_\ell\ne y_\ell$, so this isometry extends to a local unitary. One implementation first emits the two controlled symbols and then flips $M$ conditioned on the output symbol being $y_\ell$. The memory is now exactly $|0\rangle$. All later symbols are fixed and can be emitted independently.

For qubits, the final transfer is a SWAP between the memory and a fresh output qubit, followed by a known bit flip if needed. Intermediate emission uses controlled bit flips. The four allowed phases use only Hadamard and phase gates. The resource-generation circuit therefore has $O(m)$ local Clifford gates for qubit wires.

**Clean-return property.** The final isometry maps the entire two-dimensional input space of $M$ into $|0\rangle_M\otimes\operatorname{span}\{|x_\ell\rangle,|y_\ell\rangle\}$. Therefore it resets $M$ to a fixed pure state for every joint state of $M$ and any reference system. This remains true if earlier emitted ports have already been measured, corrected, or coupled to external data, and also after conditioning on any earlier instrument outcomes. Clean return does not rely on preserving an unmeasured cat state until the interval ends.

If $f=\ell$, the same preparation and transfer occur in one slot. If the sampled resource is a basis string, no coherent branch memory is needed at all.

## 4. Using each emitted port

At slot $j$, each laboratory emits one local resource register. The designated sender receives the actual input for that slot, performs the usual generalized Bell measurement on the input and its local resource register, and sends the outcome to the receiver. The receiver applies the corresponding generalized Pauli correction to its emitted resource register and releases that register as the slot output. For qubits, this uses two classical bits per teleportation, in addition to the shared initial sample description.

There is no physical quantum link between the laboratories. In each sampled run the two local resource states are unentangled with one another. Their signed average supplies the ideal resource operator only at the level of the final estimator.

The procedure respects the strict interface:

- Each actual input is accessed only at its own slot.
- The corrected output is delivered before the next input is released.
- Only the two private branch qubits survive between slots.
- Previously emitted outputs are not retained as private workspace.

The sender needs, at a given qubit slot, its incoming data qubit, one transient resource qubit, and its persistent branch qubit. The receiver needs its emitted resource/output qubit and its persistent branch qubit. If the wire direction changes, the laboratories exchange these roles. This is a constant persistent-memory statement, with the transient systems explicitly present.

## 5. Equality as an open quantum process

Two facts establish correctness for arbitrary external references and adaptive intervening operations.

First, imagine that all local resource ports of a sampled product state $\rho_\lambda$ were prepared before the first slot. Standard slot-by-slot teleportation defines a process $\mathcal T_{\rho_\lambda}$ that is linear in this initial resource operator. For the ideal resource,

$$
\mathcal T_{\Phi_D}
=\mathcal T_{\bigotimes_j\Phi_{d_j}}
=\mathrm{Id}_{\mathrm{stream}},
$$

including when each input is entangled with an external reference or is produced adaptively from earlier outputs. Applying the resource identity gives

$$
\sum_\lambda a_\lambda\mathcal T_{\rho_\lambda}
=\mathcal T_{\sum_\lambda a_\lambda\rho_\lambda}
=\mathrm{Id}_{\mathrm{stream}}.
$$

The hypothetical entangled state $\Phi_D$ is used only in this linear identity. It is not supplied to any physical run.

Second, the online generator implements exactly the same process as preparing each sampled local resource in advance. Its later emission isometries act on the private memory and fresh resource ports. Earlier Bell measurements, Pauli corrections, and external interventions act on already emitted ports and data. These operations act on disjoint tensor factors and commute, even when those factors are entangled. Moving each later emission isometry past the earlier port operations therefore transforms the advance-preparation circuit into the online circuit without changing its branch probabilities or conditional outputs.

This establishes equality as an open comb, rather than only equality of a final state for a chosen input. The generator never requires access to an actual future data input. Its exact clean-return property permits independent repetition at successive common-refinement intervals.

## 6. A finite memoryless qubit protocol

For one qubit, the extent-three result also has a direct measure-and-prepare interpretation. Choose one of the Pauli bases uniformly. Measure the input in that basis and prepare either the measured eigenstate or its opposite. Let the two resulting channels be $\mathcal E_+$ and $\mathcal E_-$. Writing $\mathcal D(\rho)=I\operatorname{Tr}(\rho)/2$, their Bloch-vector actions give

$$
\mathcal E_+=\frac{\mathrm{Id}+2\mathcal D}{3},
\qquad
\mathcal E_-=\frac{4\mathcal D-\mathrm{Id}}{3}.
$$

Both are physical entanglement-breaking channels, and

$$
\mathrm{Id}=2\mathcal E_+-\mathcal E_-.
$$

The extent is three and no quantum system survives a slot gap. Applying this independently gives $3^n$. The [reset converse](reset-schedules.md) proves that this independent cost is optimal whenever either laboratory loses all persistent coherence at every gap, regardless of the other laboratory's memory.

The constructive contrast is therefore precise: one persistent binary branch at both laboratories suffices to correlate the cuts throughout an uninterrupted interval, while any complete break at either endpoint separates the useful collective intervals.
