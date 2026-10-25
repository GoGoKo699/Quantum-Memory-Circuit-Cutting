# Thirty milestones: from quantum operations to memory-constrained cutting

This map follows the scientific dependencies of the project. Its sole educational anchor is **John Watrous, _The Theory of Quantum Information_ (2018)**. The [anchor guide](anchor.md) records the selected sections, author-hosted chapter PDFs, and the translation from the book's unnormalized Choi operators to this repository's normalized convention. Page numbers below are printed book pages.

| Phase | Milestones | Scientific role |
|---|---|---|
| Background/preliminaries | M01–M12 | Build the state, channel, instrument, and norm language, then combine it into the fully specified causal interface. |
| Narrative/innovation | M13–M30 | Assemble the forest and noisy-memory converses, their physical constructions, and the approximation, calibration, and resource consequences. |

The 12/18 allocation reflects the two distinct converse mechanisms. Complete resets produce separability over coherence epochs; unflagged dephasing instead imposes a temporal-state constraint. Both require an attainable causal construction, and their experimental interpretation additionally requires separate approximation and calibration arguments. M12 closes the background phase by integrating its ingredients into one model. M30 closes the second phase by relating the exact results, physical resources, attribution, and scope.

The anchor supplies foundations. The ordered-comb interface, signed-QPD definitions, forest identity, concurrence-roof argument, KAK cutting construction, and calibration formulas are supplied by the canonical scientific pages and their primary research references. In particular, a pointer to textbook Schmidt decomposition does not attribute KAK decomposition to that section, and a pointer to quantum instruments does not attribute the concurrence formulas to Watrous.

Each dependency refers to an earlier milestone. The targets identify the conceptual connections needed for the complete scientific story; specialist proofs and implementation details remain in the linked canonical sources.

## Phase I — Background/preliminaries

### M01

**States and measured outcomes**

**Central question.** How does a quantum-state description determine the probabilities and averages of measured outcomes?

**Understanding target.** Interpret a density operator as a positive, trace-one description of a preparation, and relate measurement probabilities to traces of positive operators. Distinguish a coherent superposition from a classical mixture and distinguish an observable's outcome from its expectation.

**Dependencies and story role.** No earlier milestone. This establishes the local objects that later become input states, memory states, Choi operators, and bounded experimental outcomes.

**Conceptual connection.** The final cutting estimator averages classical outcomes, but the state that generates those probabilities must retain its quantum coherences until the physical operations have occurred.

**Sources.** [Watrous](anchor.md), §1.1.2, density operators, p.18, and Definition 2.5, p.62; §2.3.1, Definition 2.34 and Born-rule equation (2.201), p.101. Project: [normalized Choi tests](../science/model.md#normalized-choi-tests-and-lower-bounds) and [bounded sampling outcomes](../science/precision-calibration.md#6-sampling-precision-after-calibration).

### M02

**Composite systems, references, and Schmidt correlations**

**Central question.** What changes when a local system is part of a larger correlated quantum state?

**Understanding target.** Use tensor products and partial traces to distinguish a joint state from its local marginals. Interpret a Schmidt decomposition and a Bell pair, and explain why a channel must be tested with an external reference rather than only on isolated inputs.

**Dependencies and story role.** M01. This expands the description from one local preparation to the correlations on which both constructions and converses depend.

**Conceptual connection.** The same mathematics describes spatial Alice–Bob entanglement in a target Choi state and temporal correlations among several ports inside one laboratory. Their physical resource roles differ.

**Sources.** [Watrous](anchor.md), §1.1.2, tensor-product operator notation, and §1.1.3, Schmidt decomposition, p.31, equations (1.162)–(1.164). Project: [pure-edge states and vertex spaces](../science/forest-witness.md#1-states-and-the-decomposition-norm) and [external references in the interface](../science/model.md#laboratories-ports-and-time).

### M03

**Channels, Kraus maps, and hidden environments**

**Central question.** What makes a quantum operation valid even when its input is entangled with an inaccessible reference?

**Understanding target.** Distinguish positivity from complete positivity and explain trace preservation, Kraus representations, and a dilation using an environment. Identify the difference between an inaccessible environment and an additional coherent system that the apparatus can later access.

**Dependencies and story role.** M01–M02. This gives the physical transformation language needed before introducing measurement branches or memory noise.

**Conceptual connection.** The memory theorems constrain complete physical operations. Treating an accessible environmental register as absent can change the allowed memory resource and invalidate a converse.

**Sources.** [Watrous](anchor.md), Definition 2.13, p.73; Theorem 2.22, completely positive representations, p.82; Theorem 2.26, trace preservation, p.87. Project: [free operations and charged storage](../science/model.md#free-operations-and-charged-storage).

### M04

**Instruments and physical branch probabilities**

**Central question.** How can a protocol retain measurement outcomes without treating a rare successful branch as a free deterministic operation?

**Understanding target.** Describe an instrument as completely positive branches whose sum is a physical deterministic operation. Keep a branch's trace as its probability, distinguish its unnormalized output from its conditioned state, and understand a bounded score attached to the final classical record.

**Dependencies and story role.** M03. This extends a single channel to adaptive experiments while retaining the normalization needed by the lower bounds.

**Conceptual connection.** Refinement of a classical history can simplify a proof, but it never removes the physical probability of that history. This controls arbitrary postselection in the scored-atom model.

**Sources.** [Watrous](anchor.md), §2.3.2, pp.112–113, equations (2.258)–(2.262). Project: [signed instruments](../science/model.md#signed-instruments-and-the-cost-being-minimized) and [physical branch weights](../science/reset-schedules.md#4-scored-atoms-retain-physical-branch-probabilities).

### M05

**Normalized Choi operators**

**Central question.** How can an operation be represented by an operator without losing its input dimension, register order, or branch normalization?

**Understanding target.** Relate vectorization and Bell-input tests to a Choi representation. Translate the book's output–input, unnormalized convention by the appropriate register permutation and division by the full input dimension. A deterministic repository Choi operator has trace one; instrument-branch traces sum to one. A two-qubit gate has input dimension four.

**Dependencies and story role.** M02–M04. This turns the physical operation model into the state geometry used by the witnesses.

**Conceptual connection.** A normalized Choi test is an allowed experiment. Its positive branch weights provide a lower-bound certificate even when the final signed reconstruction is not a physical state.

**Sources.** [Watrous](anchor.md), §1.1.2, vectorization, pp.23–24; §2.2.2, Choi representation, p.78, equations (2.64)–(2.66); Proposition 6.22, register regrouping, p.328. Project: [normalized Choi tests](../science/model.md#normalized-choi-tests-and-lower-bounds) and [gate normalization](../science/gate-cuts.md#1-normalized-kak-coefficients).

### M06

**Separability and local operations with classical communication**

**Central question.** Which correlations can local operations and shared classical records create across the laboratory boundary?

**Understanding target.** Distinguish product states, mixtures of product states, and entangled states for a specified partition. Understand that each laboratory may entangle its own registers while a refined branch of the independent local Bell-probe experiment is spatially a product. Recognize the inclusion of finite-round LOCC in separable operations without identifying those two sets.

**Dependencies and story role.** M02–M03 and M05. This establishes the spatial restriction from which the epoch and noisy-state lower bounds are built.

**Conceptual connection.** Separability depends on the partition. A product over coherence epochs permits arbitrary quantum correlations among all registers inside one epoch.

**Sources.** [Watrous](anchor.md), §6.1.1, Definition 6.1, p.311; §6.1.2, Definitions 6.17 and 6.20, pp.325–326, Definition 6.25, pp.330–331, and Proposition 6.26, p.332. Project: [vertex separability](../science/forest-witness.md#1-states-and-the-decomposition-norm) and [adaptive-history normalization](../science/dephasing-memory.md#adaptive-histories-and-normalization).

### M07

**Genuine entanglement-breaking connections**

**Central question.** When does a memory operation actually sever all quantum correlations with the earlier epoch?

**Understanding target.** Relate an entanglement-breaking channel to a measurement followed by preparation and to a rank-one Kraus refinement. Explain why the break must act on the entire charged memory and why an entanglement-breaking marginal is insufficient when another accessible system retains an error flag.

**Dependencies and story role.** M03–M04 and M06. This identifies the exact physical property that will permit an epoch factorization.

**Conceptual connection.** A complete local break and unflagged partial dephasing impose different restrictions. Exposing a measure-and-prepare reset record can enlarge the reset model harmlessly for a converse; exposing a hidden phase-error flag changes the noisy-memory resource.

**Sources.** [Watrous](anchor.md), Exercise 6.1, p.384, the entanglement-breaking/measure-and-prepare equivalence, with the channel foundations in Theorem 2.22. Project: [complete memory breaks](../science/model.md#prescribed-complete-memory-breaks) and [rank-one boundary refinement](../science/reset-schedules.md#3-why-the-physical-branches-factor-over-epochs). The book locator is an exercise; the needed characterization and proof use are made explicit in the project.

### M08

**Norm duality and witnesses**

**Central question.** How can one Hermitian operator bound every allowed signed reconstruction?

**Understanding target.** Interpret trace norm and operator norm, their duality, and the inequality bounding a trace pairing by the product of the norms. Distinguish a witness bounded on an allowed set from an operator bounded on all states, and relate the witness's target value to a decomposition lower bound.

**Dependencies and story role.** M01–M02, M05–M06. This supplies the common mathematical tool for the forest converse, the noisy converse, and their approximation bounds.

**Conceptual connection.** A useful witness need not have operator norm one. It must have absolute expectation at most one on every allowed scored atom.

**Sources.** [Watrous](anchor.md), §1.1.3, Schatten norms and duality, pp.32–33, equations (1.165)–(1.175). Project: [the witness criterion](../science/model.md#normalized-choi-tests-and-lower-bounds) and [one-edge contraction bounds](../science/forest-witness.md#2-a-contraction-bound-for-one-edge).

### M09

**Signed extent and bounded scores**

**Central question.** What is optimized by a quasiprobability decomposition, and how does that differ from a physical random mixture?

**Understanding target.** Read the extent as the sum of absolute exterior coefficients and explain sampling proportional to those magnitudes. Distinguish the physical instrument from its possibly nonpositive scored map. Relate the extent to a bounded-range estimator while recognizing that its square is a generic sufficient sampling factor, not a lower bound for every estimator.

**Dependencies and story role.** M04–M05 and M08. This combines physical branch normalization with the mathematical quantity studied throughout the project.

**Conceptual connection.** Outcome-dependent signs enlarge the linear simulation class without adding an uncharged quantum operation or normalizing away an unlikely outcome.

**Sources.** [Watrous](anchor.md), §2.3.2 and §1.1.3 supply instrument and norm foundations. Signed-QPD extent is introduced in the project: [cost definition](../science/model.md#signed-instruments-and-the-cost-being-minimized) and [extent versus sampling](../science/resource-interpretation.md#from-signed-extent-to-a-sampling-guarantee).

### M10

**Teleportation as a linear resource transformation**

**Central question.** How does a Bell resource, local measurement, and classical correction implement a wire?

**Understanding target.** Follow standard teleportation through its Bell outcome and correction, including an input entangled with a reference. Explain the linear dependence on the resource operator and why a signed identity among resources gives a signed identity among the resulting processes.

**Dependencies and story role.** M02–M03 and M05–M06. This connects state decompositions to a physical operation that can meet an output deadline.

**Conceptual connection.** An ideal entangled resource can appear in an algebraic proof even though every executed term is spatially separable. The signed average, rather than a supplied entangled pair, reconstructs the desired wire.

**Sources.** [Watrous](anchor.md), §6.3.1, Scenario 6.46 and Theorem 6.47, pp.359–361. Project: [resource-port use](../science/wire-construction.md#4-using-each-emitted-port) and [open-process equality](../science/wire-construction.md#5-equality-as-an-open-quantum-process).

### M11

**Dephasing, filters, and convex and concave roofs**

**Central question.** How can local noise and filtering constrain temporal entanglement without making every branch separable?

**Understanding target.** Describe the unflagged dephasing channel and its local two-time Bell state. Interpret a filter as a probability-bearing local operation. Understand the definitions of pure-state concurrence, its minimum-average convex roof, and its maximum-average assisted roof, without assuming that an arbitrary ensemble realizes either extremum.

**Dependencies and story role.** M02–M04 and M06. This introduces the state descriptors needed for the noisy converse, while reserving the dephasing-specific inequality for its own proof.

**Conceptual connection.** The reset proof uses exact separability after a break. Partial dephasing requires a quantitative constraint that remains valid after filtering and mixtures.

**Sources.** [Watrous](anchor.md), Theorem 2.22 and §2.3.2 provide the channel and filtering foundations; §2.2.3, pp.94–96, treats complete dephasing and classical registers; Exercise 6.3, p.385, supplies the related convex-roof definition of entanglement of formation. **Concurrence and its two roof definitions are supplied by the project's research account**, not attributed to those textbook sections: [temporal state definitions and filtering](../science/dephasing-memory.md#4-temporal-state-constraint-for-arbitrary-instruments).

### M12

**The complete strict-port resource model**

**Central question.** What process must the simulator reproduce, and which systems may carry quantum information between its slots?

**Understanding target.** Combine input-release times, output deadlines, private instrument records, external references, charged persistent storage, and free classical communication into one interface. Distinguish prescribed complete resets from the independently dephasing one-qubit model. Explain why a universal open-process identity is stronger than reproducing one known circuit's final output.

**Dependencies and story role.** M05, M07, M09–M11. This closes the background phase by integrating its local state and operation concepts into the exact task.

**Conceptual connection.** The lower bounds require physical availability constraints, not merely an abstract no-future-signalling property. Early inputs, retained outputs, or quantum-correlated future ancillas can bypass the intended memory restriction.

**Sources.** [Watrous](anchor.md), §2.3.2, Definition 6.25, and §3.3.2 provide instruments, local protocols, and reference-assisted channel testing. The multi-slot extension and timing restrictions are supplied by [the causal model](../science/model.md) and [scope counterexamples](../science/dephasing-memory.md#6-endpoints-repeated-blocks-and-scope-tests).

## Phase II — Narrative/innovation

### M13

**Single-edge cost and two-component cat states**

**Central question.** What determines the signed separable cost of one pure entangled edge?

**Understanding target.** Connect Schmidt coefficients $`s_i`$ to the factor $`2(\sum_i s_i)^2-1`$. Understand how the Schmidt-support witness supplies the lower bound and how the diagonal terms plus eight signed cat products per pair attain it. Distinguish standard robustness, whose negative part is also separable, from generalized robustness.

**Dependencies and story role.** M02, M06, M08–M09. This provides the local building block before examining whether its cost can multiply on a network.

**Conceptual connection.** The single-edge factor is an established ingredient. The project's additional problem is whether joint correlations inside epoch vertices can lower the cost of several edges.

**Sources.** [Watrous](anchor.md), §1.1.3, Schmidt decomposition, and Definition 6.1 supply the foundations. Project: [pure-edge statement](../science/forest-witness.md#1-states-and-the-decomposition-norm) and [matching cat decomposition and robustness convention](../science/forest-witness.md#4-a-matching-finite-decomposition).

### M14

**Hermitian leaf contraction**

**Central question.** Why can a leaf of the graph be removed without increasing the bound passed to its neighbor?

**Understanding target.** Explain the trace-norm-to-operator-norm contraction through $`2|\Omega\rangle\langle\Omega|-I`$, including a proper Schmidt support. Track why the remaining message may be Hermitian but nonpositive, and why the next contraction must therefore use trace-norm duality rather than a probability argument.

**Dependencies and story role.** M08 and M13. This isolates the local mathematical mechanism that makes the forest converse possible.

**Conceptual connection.** A bound proved only for positive intermediate states would not justify repeated elimination. The Hermitian invariant carries the proof through the whole tree.

**Sources.** [Watrous](anchor.md), §1.1.3, pp.32–33, on Schatten duality. Project: [Lemmas 2 and 3, leaf contraction and message absorption](../science/forest-witness.md#2-a-contraction-bound-for-one-edge).

### M15

**The forest product identity and its cycle obstruction**

**Central question.** When do single-edge signed costs multiply despite arbitrary quantum correlations inside each vertex?

**Understanding target.** Assemble leaf contraction into the product-vertex witness bound, combine it with the tensor-product upper decomposition, and obtain the exact pure-edge forest identity. Explain why the four-cycle product of local Bell states gives witness value three and prevents an unrestricted graph claim.

**Dependencies and story role.** M13–M14. This closes the mathematical network argument before the graph is tied to physical reset schedules.

**Conceptual connection.** The decisive restriction is acyclicity of the vertex graph, not a prohibition on entanglement among registers within a vertex.

**Sources.** [Watrous](anchor.md), §1.1.3 and Definition 6.1 supply norm and separability foundations. The forest result is proved in [the forest witness](../science/forest-witness.md#3-the-forest-witness), with its [cycle obstruction](../science/forest-witness.md#5-why-a-cycle-changes-the-problem).

### M16

**Epoch-overlap forests**

**Central question.** Which graph is imposed by two different partitions of one ordered slot sequence?

**Understanding target.** Construct one vertex per local coherence epoch and one edge per nonempty Alice–Bob overlap. Explain why scanning contiguous time intervals always introduces a new vertex at a new edge, and identify the common-refinement dimensions $`D_I`$.

**Dependencies and story role.** M07, M12, M15. This connects the mathematical forest hypothesis to the physical time ordering.

**Conceptual connection.** A long epoch may overlap many short epochs at the other laboratory. The resulting high-degree vertex still permits unrestricted local quantum correlations, so the graph construction does not assume independent batching.

**Sources.** [Watrous](anchor.md), Definition 6.1 supplies the product-over-vertices language. The interval-graph argument is project-supplied: [epochs and common refinement](../science/reset-schedules.md#1-epochs-and-the-common-refinement) and [Lemma 2](../science/reset-schedules.md#2-the-graph-determined-by-time).

### M17

**Refined causal-branch factorization**

**Central question.** Why does every allowed reset-constrained instrument produce a normalized mixture of epoch-product Choi operators?

**Understanding target.** Condition on a full classical transcript, refine genuine EB boundaries to rank-one Kraus operators, and identify the disconnected quantum components. Retain every positive branch probability and prove their sum is one. Explain how strict port availability removes additional quantum connections between epochs.

**Dependencies and story role.** M04–M05, M07, M09, M12, M16. This converts the physical resource constraint into the separability condition required by the forest witness.

**Conceptual connection.** Classical feedback changes conditioned local factors without restoring a severed quantum index. The same refinement must not expose inaccessible phase-error labels in the later noisy-memory proof.

**Sources.** [Watrous](anchor.md), Theorem 2.22, §2.3.2, and Exercise 6.1. Project: [Proposition 3 and its proof](../science/reset-schedules.md#3-why-the-physical-branches-factor-over-epochs) and [bounded scores with physical weights](../science/reset-schedules.md#4-scored-atoms-retain-physical-branch-probabilities).

### M18

**Streamed wire resources and clean return**

**Central question.** How can one persistent qubit emit a collective resource while every wire output meets its deadline?

**Understanding target.** Follow a sampled two-string superposition through controlled emission and the final differing symbol. Explain why the final isometry returns the memory exactly clean even after earlier resource ports have been used. Account for the classical label sampler, transient input/resource registers, and slotwise teleportation.

**Dependencies and story role.** M10, M12–M13. This gives the causal upper construction needed to turn the reset lower bound into an equality.

**Conceptual connection.** Exponentially many possible decomposition labels do not require an exponentially stored table. One persistent branch qubit is sufficient, but the full circuit width also contains transient data and resource ports.

**Sources.** [Watrous](anchor.md), §6.3.1, Scenario 6.46 and Theorem 6.47. Project: [implicit sampling](../science/wire-construction.md#2-sampling-without-enumerating-the-decomposition), [online generation and clean return](../science/wire-construction.md#3-generating-a-local-cat-state-online), and [open-process equality](../science/wire-construction.md#5-equality-as-an-open-quantum-process).

### M19

**The exact reset law and synchronization**

**Central question.** Which uninterrupted intervals actually determine the optimal universal wire-cutting extent?

**Understanding target.** Match the epoch-forest converse with the streamed construction to obtain $`\Gamma=\prod_I(2D_I-1)`$. Explain the one-sided memoryless limit and the exponential aligned-versus-staggered separation at the same maximum local epoch length.

**Dependencies and story role.** M15–M18. This integrates the mathematical and physical reset arguments into their principal operational consequence.

**Conceptual connection.** Memory retained only at the opposite laboratory cannot relay the collective advantage across a genuine complete break. Synchronization changes the common refinement even when the individual lifetime budgets are unchanged.

**Sources.** [Watrous](anchor.md), Definition 6.1 and §6.3.1 provide the separability and teleportation foundations. Project: [Theorem 1](../science/reset-schedules.md#1-epochs-and-the-common-refinement), [attainment and synchronization](../science/reset-schedules.md#5-attainment-and-the-role-of-synchronized-coherence), and [the six-wire example](../science/resource-interpretation.md#a-complete-scheduling-example).

### M20

**Normalized KAK Choi entanglement**

**Central question.** How does a two-qubit gate's operator structure determine the entanglement of its normalized Choi state?

**Understanding target.** Relate normalized KAK coefficients $`u_{j\alpha}`$ to Choi Schmidt coefficients $`|u_{j\alpha}|`$ and define $`\chi_j=(\sum_\alpha|u_{j\alpha}|)^2`$. Keep the four-dimensional gate input normalization separate from the two-dimensional local vectorization normalization, and recognize that the local Schmidt support can be proper.

**Dependencies and story role.** M02, M05, M13. This identifies the correct edge factors for replacing identity wires by general gate slots.

**Conceptual connection.** The same forest witness applies to nonmaximally entangled pure edges, but its spectral norm need not equal its target expectation.

**Sources.** [Watrous](anchor.md), §1.1.2, vectorization, and §1.1.3, Schmidt decomposition, supply the foundations. **KAK decomposition and its cutting application are research-level ingredients supplied by** [normalized KAK coefficients](../science/gate-cuts.md#1-normalized-kak-coefficients) and the primary sources cited there.

### M21

**The attributed gate upper and reset extension**

**Central question.** How can the optimal collective gate factor be attained causally when ordinary non-Clifford teleportation would need different corrections?

**Understanding target.** Follow the Schmitt–Piveteau–Sutter virtual-resource construction and the bounded pair-dependent Pauli signs. Explain why all eight resource terms of a pair share the same score, how each output is delivered on time, and how the forest lower bound gives $`\prod_I(2\prod_{j\in I}\chi_j-1)`$.

**Dependencies and story role.** M09–M10, M12, M15, M17, M20. This completes the gate extension while preserving the attribution of its unrestricted upper construction.

**Conceptual connection.** A final signed estimator can correct a linear interference contribution without supplying a nonlocal physical correction. The published protected-resource storage is sufficient; no minimum-memory claim for arbitrary gates follows.

**Sources.** [Watrous](anchor.md), §2.3.2, §6.3.1, and Proposition 6.22 provide instruments, teleportation, and Choi regrouping. Project: [gate theorem](../science/gate-cuts.md#2-exact-theorem), [pair-dependent scoring](../science/gate-cuts.md#5-why-pair-dependent-scoring-reconstructs-the-gates), and [charged storage](../science/gate-cuts.md#6-storage-preparation-and-sampling).

### M22

**Four physical resources for noisy memories**

**Central question.** What physical construction improves two-slot cutting whenever both local memories retain some dephasing coherence?

**Understanding target.** Identify the three memoryless resource families and the locally temporal, spatially separable memory resource $`E_r`$, with $`r=\eta_A\eta_B`$. Understand the finite bilateral twirls, the complete signed matrix identity, and its streaming teleportation implementation through the actual noisy gap.

**Dependencies and story role.** M10–M12. This begins the second result family with an attainable construction rather than assuming that its cost is already optimal.

**Conceptual connection.** The useful entanglement is between two times inside each laboratory. Shared spatial entanglement is absent, and the product-noise assumption is a physical condition rather than a consequence of marginal calibration.

**Sources.** [Watrous](anchor.md), Theorem 2.22 and §6.3.1 provide channel and teleportation foundations. Project: [four resources and exact identity](../science/dephasing-memory.md#2-four-physical-resources-and-their-full-matrix-identity) and [streaming implementation](../science/dephasing-memory.md#3-streaming-teleportation-and-universal-comb-equality).

### M23

**The dephasing-compatible temporal cone**

**Central question.** Which necessary state constraint survives every allowed filter, mixture, and adaptive local operation through the noisy memory?

**Understanding target.** Explain the inequality $`C(\rho)\leq\eta C_a(\rho)`$, starting from the dephased Bell state and the common determinant scaling of the two roofs under a local filter. Use convexity and concavity to retain the inequality under mixtures, and connect both laboratories' temporal Choi factors to filtered states of this form.

**Dependencies and story role.** M04–M05, M11–M12, M22. This supplies the local geometric restriction for the noisy converse.

**Conceptual connection.** The cone is a necessary constraint, not a claimed complete characterization of all reachable temporal states. Its derivation keeps the dephasing environment unflagged.

**Sources.** [Watrous](anchor.md), §2.3.2 and Theorem 2.22 provide the filtering framework. The concurrence-roof facts and dephasing constraint are proved in [temporal-state Lemmas 1–3](../science/dephasing-memory.md#4-temporal-state-constraint-for-arbitrary-instruments).

### M24

**The noisy witness and exact two-slot cost**

**Central question.** Why can no allowed adaptive instrument beat the four-resource noisy construction?

**Understanding target.** Relate the temporal cones to the Bloch-correlation inequalities and the witness $`Q_r`$. Explain how full-history factorization, positive branch probabilities, and bounded scores extend the witness bound to every permitted protocol. Match its target value with the upper construction to obtain $`5+4/(1+r)`$.

**Dependencies and story role.** M08–M09, M17, M22–M23. This closes the noisy lower-bound argument and establishes its equality with the physical upper bound.

**Conceptual connection.** The endpoints are nine for complete dephasing on either side and seven for two noiseless memories. Every positive $`r`$ improves the exact two-slot extent, with no claim about arbitrary many-slot noisy memories.

**Sources.** [Watrous](anchor.md), §1.1.3, §2.3.2, and Definition 6.1 supply norm, instrument, and spatial-product foundations. Project: [the noisy witness and history normalization](../science/dephasing-memory.md#5-a-witness-bounded-on-every-scored-protocol).

### M25

**Noise and availability counterexamples; block scope**

**Central question.** Which physical changes preserve an exact product theorem, and which change the allowed simulation problem?

**Understanding target.** Distinguish mandatory complete resets with fresh noise between blocks from optional independent repetition of a protocol. Explain why common phase errors can give extent seven despite completely dephased marginals, and why early access to the second input invalidates the strict-memory lower bound.

**Dependencies and story role.** M12, M19, M24. This integrates the reset and noisy results through their physical boundaries.

**Conceptual connection.** A marginal channel, an abstract causal map, and a complete physical interface contain different information. Neither local Ramsey data nor a choice to batch two slots establishes all the assumptions of a converse.

**Sources.** [Watrous](anchor.md), Theorem 2.22, Exercise 6.1, and §6.3.1 provide channel, break, and teleportation foundations. Project: [exact reset blocks and counterexamples](../science/dephasing-memory.md#6-endpoints-repeated-blocks-and-scope-tests).

### M26

**Trace-normalized approximation bounds**

**Central question.** How much can a universal approximation reduce the extent certified by an exact witness?

**Understanding target.** Distinguish full strategy norm, half-distance error, and the weaker normalized Choi test. Explain why trace-one reconstruction permits centering a witness by its spectral midpoint, while an unrestricted signed approximant requires the operator-norm bound. Apply the distinction to the wire forest and the noisy two-slot witness without claiming a complete tight approximation frontier.

**Dependencies and story role.** M05, M08, M12, M19, M24. This extends the exact converses to a controlled universal error while keeping normalization visible.

**Conceptual connection.** The wire formula uses maximally entangled edge spectra. Its relative-error expression cannot be transferred to arbitrary KAK gates by substituting only their target expectation.

**Sources.** [Watrous](anchor.md), §1.1.3 and §3.3.2, Definition 3.43 and Theorem 3.46, provide dual norms and reference-assisted channel norms. The multi-slot norm and spectral arguments are in [error conventions](../science/precision-calibration.md#1-error-convention) and [approximation bounds](../science/precision-calibration.md#2-approximation-bounds-from-witness-spectral-ranges).

### M27

**Calibration mismatch and nonphysical reconstructions**

**Central question.** What process is actually reconstructed when nominal coefficients use $`r_0`$ but the memories have parameter $`r`$?

**Understanding target.** Interpret the exact signed Choi error and the mismatch $`d=(r-r_0)/(1+r_0)`$. Explain why trace normalization survives but complete positivity fails for every nonzero mismatch, and why orthogonal Pauli paths give an exact full strategy error $`|d|`$.

**Dependencies and story role.** M09, M22, M26. This replaces a generic error estimate with the exact bias of the specified implementation.

**Conceptual connection.** A bounded observable can have worst-case bias equal to the full norm, while a probability-valued event uses the half norm for this trace-preserving difference. A signed reconstructed operator must not be treated as a physical channel.

**Sources.** [Watrous](anchor.md), §2.2.2 and §3.3.2 provide Choi and norm foundations. Project: [nominal versus actual dephasing](../science/precision-calibration.md#3-exact-bias-from-nominal-versus-actual-dephasing) and [the exact Pauli-path strategy norm](../science/precision-calibration.md#31-the-calibration-strategy-norm-is-exact).

### M28

**Composing signed block errors**

**Central question.** How do calibration and implementation errors accumulate when intermediate reconstructions are not completely positive?

**Understanding target.** Follow product Pauli-path coefficients through repeated blocks and distinguish the exact expression from a first-order estimate. Understand why general Hermiticity-preserving block errors require a strategy-norm composition argument and why the bound contains $`\prod_j(1+b_j)-1`$, including higher-order terms.

**Dependencies and story role.** M12, M25–M27. This connects local error certificates to a full chronological experiment with arbitrary external interventions.

**Conceptual connection.** Contractivity of physical channels cannot simply be assigned to a signed reconstruction. The process decomposition and independence assumptions used for block composition must be stated separately from isolated block marginals.

**Sources.** [Watrous](anchor.md), §3.3.2 supplies the one-slot norm foundation. The multi-slot extension and its research-level unit-ball ingredient are given in [repeated calibrated blocks](../science/precision-calibration.md#4-repeating-calibrated-blocks) and [the general composition lemma](../science/precision-calibration.md#composition-lemma-for-general-hermiticity-preserving-block-errors).

### M29

**Charged calibration, coefficient precision, and sampling**

**Central question.** What resources and assumptions are needed to turn the exact protocol into an end-to-end accuracy guarantee?

**Understanding target.** Account separately for memory-channel uses during Ramsey calibration and complete circuit executions. Freeze coefficients after calibration, allocate bias and statistical tolerances, and preserve trace normalization through coupled finite-precision coefficient choices. Explain why marginal calibration alone does not certify independent noise or correct port timing.

**Dependencies and story role.** M04, M09, M25, M27–M28. This assembles preparation, classical arithmetic, parameter estimation, signed execution, and confidence bounds into one resource account.

**Conceptual connection.** The squared extent supplies a sufficient bounded-estimator sample count. The calibration cost and implementation assumptions remain additional resources, and the resulting guarantee is not an optimality theorem for every estimator.

**Sources.** [Watrous](anchor.md), §2.3.1, Definition 2.34, and §3.3.2 supply measurement and error-norm foundations. Project: [charged calibration](../science/precision-calibration.md#5-a-charged-calibration-procedure), [sampling precision](../science/precision-calibration.md#6-sampling-precision-after-calibration), and [coefficient and implementation precision](../science/precision-calibration.md#7-coefficient-precision-and-other-implementation-errors).

### M30

**Global scientific synthesis and scope**

**Central question.** What do the exact memory frontiers establish, and what conclusions require a different task or a different physical model?

**Understanding target.** Relate the wire common-refinement law, its KAK gate extension, and the specified two-slot dephasing law to their distinct constructions and converses. Separate persistent memory from transient width, memory synchronization from hardware lifetime alone, universal signed extent from observable-specific sampling complexity, and analytical proof from finite verification.

**Dependencies and story role.** M19, M21, M25–M26, M29. This closes the narrative phase by integrating the full result rather than adding another isolated lemma.

**Conceptual connection.** The collective-cutting values, interference primitives, and general-gate upper construction have established antecedents. The scientific contribution lies in the stated constrained frontiers and their complete operational proofs; numerical checks and a literature comparison support their assessment without proving every neighboring claim.

**Sources.** [Watrous](anchor.md), §1.1.3, §3.3.2, Definition 6.1, and §6.3.1 provide the common mathematical and operational foundations. Project: [resource interpretation](../science/resource-interpretation.md#what-the-exact-frontiers-establish), [attribution map](../references/related-work.md#attribution-map), [scientific evidence and boundaries](../science/README.md#evidence-and-boundaries), and [verification guide](../verification/README.md).

[Learning route](README.md) · [Anchor and notation bridge](anchor.md) · [Scientific reading map](../science/README.md)
