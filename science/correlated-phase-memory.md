# Correlated five-level phase memories

[Science guide](README.md) · [Causal model](model.md) · [Independent qubit dephasing](dephasing-memory.md)

For two ordered five-dimensional identity wires and one persistent five-level memory per laboratory, the two specified joint phase channels have the same exact bounded-score signed extent:

```math
\boxed{\Gamma_L=\Gamma_C=49.}
```

The proposed cubic upper bound $`97-16\sqrt5\approx61.2229`$ is valid but nonoptimal. A complete reflection-parity instrument attains 49 without revealing the phase error. The result concerns the strict sequential cutting model below; it does not identify the channels as operationally equivalent for other tasks.

## Model and inherited results

Alice receives the first unknown input and Bob releases its output before the gap. The second unknown input arrives only after the gap. Released outputs and external references cannot serve as private storage. There is no initial spatial entanglement or quantum communication. Within slots, local instruments, transient ancillas and classical communication are unrestricted. Only one five-dimensional private quantum register per laboratory crosses the gap.

Let $`Z|j\rangle=\omega^j|j\rangle`$, $`\omega=e^{2\pi i/5}`$. Conditional on every permitted pre-gap classical history, the one prescribed joint noise use is

```math
\mathcal N_f(\rho)=\frac15\sum_{x\in\mathbb F_5}
(Z^x\otimes Z^{f(x)})\rho(Z^x\otimes Z^{f(x)})^\dagger,
\quad f(x)=x\text{ or }x^3.
```

The hidden draw is fresh and independent of those histories, and its flags and environment are inaccessible. Each marginal channel completely dephases its memory, but the joint channel has correlated errors. The theorem for independent qubit dephasing cannot be substituted for this joint model.

An allowed atom is $`\mathcal F=\sum_h s_h\mathcal C_h`$, where the physical causal instrument is complete and $`|s_h|\le1`$. Every branch retains its physical probability. Extent is the infimum of $`\sum_k|a_k|`$ over exact open-process identities $`\mathcal I^{(2)}=\sum_k a_k\mathcal F_k`$. Finite-round protocols and their operational closure are included.

The strict interface and scored-instrument convention come from [Quantum Memory Circuit Cutting](https://github.com/GoGoKo699/Quantum-Memory-Circuit-Cutting/tree/ef27ad0a327bdd5f9feb7c7570dd887a57843ac1), especially science/model.md and science/wire-construction.md. The phase laws come from [LWE Noise Geometry](https://github.com/GoGoKo699/LWE-Noise-Geometry/tree/e28ac6c911c6f558013a0083b60268cd9174a9b6), especially science/model.md and science/channels.md. The spatial robustness witness, resource-to-teleportation reduction, and classical instrument framework are inherited ingredients; the complete parity construction below is the joint result of this comparison.

## Universal lower bound including filters and closure

Under the normalized Bell-probe tester, the ideal two-wire Choi state is $`\Phi_{25}=\Phi_5\otimes\Phi_5`$, with the spatial grouping $`(R_1R_2):(B_1B_2)`$. Put

```math
W=50\Phi_{25}-I_{625}.
```

For every positive spatially separable operator $`X`$,

```math
0\le\mathrm{Tr}(\Phi_{25}X)\le\frac{\mathrm{Tr}X}{25},
\qquad |\mathrm{Tr}(WX)|\le\mathrm{Tr}X.
```

Every physical outcome Choi operator remains spatially separable: local operations, classical communication, and the shared-random mixture of product phase unitaries preserve this property. Refining histories or mathematically expanding the noise sum does not grant the simulator the hidden error flag. Completeness gives $`\sum_h\mathrm{Tr}J(\mathcal C_h)=1`$, so

```math
|\mathrm{Tr}WJ(\mathcal F)|
\le\sum_h |s_h|\mathrm{Tr}J(\mathcal C_h)\le1.
```

Since $`\mathrm{Tr}(W\Phi_{25})=49`$, both extents are at least 49. This argument includes arbitrary local filtering and adaptive communication, without normalizing successful branches. Continuity of the finite-dimensional witness extends the bound to the operational closure. In particular, no valid universal witness can establish a strict gap once the construction below is available.

## Resource notation

On a single spatial slot pair define

```math
\Phi=\Phi_5,\quad R=\frac{I_{25}-\Phi}{24},\quad
\rho_+=\frac15\Phi+\frac45R,\quad \rho_-=R,
\quad V_{ab}=\rho_a\otimes\rho_b.
```

Both $`\rho_+`$ and $`\rho_-`$ are separable preparations: apply a bilateral isotropic twirl $`U\otimes\overline U`$ to an aligned basis product or an orthogonal basis product, respectively. Twirling each slot independently leaves a four-dimensional operator space spanned by $`\Phi\Phi,\Phi R,R\Phi,RR`$. These twirls can be finite: average over the five-dimensional Weyl and Clifford actions. Weyl averaging removes cross terms in the Bell basis, and the symplectic action is transitive on the 24 nonidentity Bell labels. Equivalently, finite exact quadrature exists for the Haar moment channel.

The first-slot rotations act only on the first emitted resource ports; the second-slot rotations act on the decoded second ports after the noise. Thus they do not conjugate or replace the prescribed memory channel.

## Direct certification of the proposed cubic upper bound

Prepare a rank-two local temporal cat at each laboratory. The first resource labels are 0 and 1. Alice encodes the two alternatives in memory levels 0 and 1; Bob encodes them in levels 0 and 3. After the gap each uses a deterministic basis permutation to map its occupied memory levels to second resource labels 0 and 1. No postselection occurs.

The joint relative phase has mean

```math
\kappa=\frac15\sum_x\omega^{x+3x^3}
=\frac{1+2\omega+2\omega^4}{5}=\frac1{\sqrt5}.
```

After independent slot twirls, the deterministic resource $`E_\kappa`$ has coefficients

```math
E_\kappa=\frac{1+\kappa}{50}\Phi\Phi
+\frac{4-\kappa}{50}(\Phi R+R\Phi)
+\frac{41+\kappa}{50}RR.
```

Its two marginal Bell overlaps are $`1/10`$ and its joint overlap is $`(1+\kappa)/50`$. Substitution in all four sectors proves

```math
\Phi\Phi=9V_{++}
-\left(4+\frac{16}{1+\kappa}\right)(V_{+-}+V_{-+})
+\frac{32}{1+\kappa}E_\kappa.
```

The coefficient extent is

```math
17+\frac{64}{1+\kappa}=97-16\sqrt5.
```

This deterministic resource directly certifies the proposed upper bound. The complete instrument below improves it to the spatial lower bound.

## Complete parity instrument attaining 49

Write

```math
|s_j\rangle=\frac{|j\rangle+|-j\rangle}{\sqrt2},\qquad
|a_j\rangle=\frac{|j\rangle-|-j\rangle}{\sqrt2},\quad j=1,2.
```

Each laboratory prepares its first resource port and memory in

```math
|\psi\rangle=\frac{|1\rangle|s_1\rangle+|2\rangle|s_2\rangle}{\sqrt2}.
```

After the prescribed phase channel, the memory is decoded with two Kraus operators into the second resource port:

```math
K_e=|0\rangle\langle0|+|1\rangle\langle s_1|+|2\rangle\langle s_2|,
\qquad
K_o=|2\rangle\langle a_1|+|1\rangle\langle a_2|.
```

The five vectors $`0,s_1,s_2,a_1,a_2`$ are an orthonormal basis, hence

```math
K_e^\dagger K_e+K_o^\dagger K_o=I_5.
```

These are the two outcomes of a complete physical instrument. All outcomes are retained. Apply score +1 for equal local parity labels and −1 for different labels. This score uses only accessible instrument records.

For $`\theta_x=2\pi x/5`$, the unnormalized local two-time vectors are

```math
|e_x\rangle=\frac{\cos\theta_x|11\rangle+\cos2\theta_x|22\rangle}{\sqrt2},
\qquad
|o_x\rangle=\frac{i(\sin\theta_x|12\rangle+\sin2\theta_x|21\rangle)}{\sqrt2}.
```

The special finite-field fact is $`x^3=\epsilon_x x`$, with $`\epsilon_x\in\{+1,-1\}`$. Therefore $`e_{x^3}=e_x`$ and $`o_{x^3}=\epsilon_xo_x`$. The density operators $`E_x=|e_x\rangle\langle e_x|`$ and $`O_x=|o_x\rangle\langle o_x|`$ are real, and the paired local parity branches are identical for the linear and cubic channels. The signed resource before twirling is

```math
F_{\rm raw}=\frac15\sum_x(E_x-O_x)_A\otimes(E_x-O_x)_B.
```

The shorthand uses a temporal local grouping. To evaluate spatial Bell tests, regroup the ports as $`(A_1B_1)(A_2B_2)`$.

At $`x=0`$ the even/odd probabilities are 1 and 0; at every nonzero $`x`$ they are $`3/8`$ and $`5/8`$. Elementary trigonometric moments give

| Quantity | Exact value |
|---|---:|
| Signed trace $`\mathrm{Tr}F_{\rm raw}`$ | $`1/4`$ |
| First marginal Bell overlap | $`1/20`$ |
| Second marginal Bell overlap | $`1/40`$ |
| Joint Bell overlap | $`1/40`$ |

For detail, the reduced operator of $`E_x-O_x`$ on its first temporal port is one half of $`\mathrm{diag}(\cos2\theta_x,\cos4\theta_x)`$, whose mean squared Hilbert–Schmidt norm is $`1/4`$. Its reduced operator on the second port is diagonal with both entries $`(\cos2\theta_x+\cos4\theta_x)/4`$, whose mean squared norm is $`1/8`$. Divide these by 5 for the marginal Bell overlaps. The joint overlap is $`\mathbb E_x[p_e(x)^2+p_o(x)^2]/25=(5/8)/25`$. The marginal asymmetry matters.

After the independent slot twirls,

```math
F=\frac1{40}\Phi\Phi+\frac1{40}\Phi R+\frac15RR.
```

This is the operator of a scored complete instrument, with trace $`1/4`$. It must not be renormalized into a free successful state. Although this particular twirled signed operator is positive, its physical realization still uses every parity outcome and its sign.

The full operator identity is

```math
\boxed{\Phi\Phi=5V_{++}+32F-8V_{+-}-4V_{-+}.}
```

In the ordered sectors $`(\Phi\Phi,\Phi R,R\Phi,RR)`$, the right side coefficients are

```math
\left(\frac5{25}+\frac{32}{40},
\frac{20}{25}+\frac{32}{40}-\frac85,
\frac{20}{25}-\frac45,
\frac{80}{25}+\frac{32}{5}-\frac{32}{5}-\frac{16}{5}\right)
=(1,0,0,0).
```

The coefficient extent is $`5+32+8+4=49`$. A concrete sampler chooses these four atoms with probabilities $`5/49,32/49,8/49,4/49`$. The final sample is multiplied by 49, the outer coefficient sign, and the internal parity score when using $`F`$.

## Strict streaming implementation and open process equality

At the first slot each laboratory prepares only its first resource port and one memory. Alice Bell-measures the actual first input with her port; Bob applies the generalized Pauli correction and releases the first output. Only the two five-level memories remain across the gap. At the second slot, each decoder emits a second resource port and records its parity; the actual second input is accessed at its release time and teleported in the same way. The parity score can be applied retrospectively after both outputs have been released.

No operation reads the hidden phase draw. The first teleportation measurement and first-port rotations act on tensor factors disjoint from the memory channel and decoder. Commuting these disjoint maps proves equivalence between the simultaneous resource calculation and the physical streaming process, including branch probabilities. This does not move the second input earlier. The slotwise twirled operator is Bell diagonal, so standard slotwise teleportation has its two-slot Choi operator. Applying the full resource identity proves equality for every causal tester, including reference-entangled inputs and adaptive interventions between slots.

The same parity construction works for the linear channel. Together with the universal lower bound this certifies both exact extents. For a second direct linear construction, prepare temporal maximally entangled five-level pairs and reverse Bob's physical memory labels. The local phase vectors are conjugate, so their twirled resource is $`E_L=(\Phi\Phi+24RR)/25`$. The identity $`\Phi\Phi=15V_{++}+10E_L-12V_{+-}-12V_{-+}`$ has extent 49. All decoding is deterministic.

## Scientific consequence and validation

The matched phase channels remain distinct channels and retain their different fixed-source learning behavior from LWE Noise Geometry. Its [operational comparison](https://github.com/GoGoKo699/LWE-Noise-Geometry/blob/main/science/circuit-cutting.md) places this cutting result alongside those distinctions; the present file owns the complete proof. This comparison establishes that their distinction is invisible to this exact two-wire cutting extent once complete scored instruments are allowed. The mechanism uses $`q=5`$ and $`x^3\in\{x,-x\}`$; it is not a statement for all primes, higher-dimensional graph laws, or arbitrary memory tasks.

Restricting the search to deterministic normalized resources or invertible filters would miss the successful instrument. A nonlinear error relation does not imply a strict cutting gap. The lower bound credits the inherited spatial separability argument; the new part is the complete parity instrument and its exact extent-49 identity.

The [finite verification](../verification/correlated_phase_checks.py) contracts the five physical hidden-error branches and both decoder outcomes at each laboratory. It checks instrument completeness, equality of the linear and cubic branch operators, all four moments, the proposed deterministic upper bound, the exact full $`625\times625`$ twirled identity, and the qudit teleportation Kraus identities. Exact moment calculations and the universal witness supply the proof; floating-point agreement is a consistency check.

The external foundations include [Vidal and Tarrach](https://arxiv.org/abs/quant-ph/9806094), [Brenner, Piveteau and Sutter](https://arxiv.org/abs/2302.03366), and the [instrument treatment of Piveteau, Schmitt and Sutter](https://journals.aps.org/prresearch/abstract/10.1103/38mx-36k6). The present finite construction is derived here; no exhaustive priority claim is made.
