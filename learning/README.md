# Learning Quantum Memory Circuit Cutting

The learning route connects familiar quantum channels and entanglement to a temporal resource question: **what must a circuit cutter keep coherent between successive operations?** It follows the project's exact assumptions, constructions and converses, including the conditions under which a different answer becomes possible.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Use the [source bridge](anchor.md) for verified section pointers, notation translation and the distinction between textbook foundations and project-specific arguments. The book is a focused reference alongside the explanations; reading it cover to cover is unnecessary.

## Three complementary entrypoints

| Read | Purpose |
|---|---|
| [From a single cut to quantum memory](tutorial.md) | A connected explanation with small worked examples, from signed weights and Bell probes to reset alignment, noisy memory and calibration. |
| [The 30-milestone map](milestones.md) | The common understanding targets, their dependencies, conceptual connections and exact scientific sources. |
| [The Watrous source bridge](anchor.md) | Relevant parts of the one anchor, the Choi-normalization translation, and the additional ingredients supplied by the project and its primary research citations. |

## How the map builds the story

The **12 background/preliminaries milestones** assemble a common language for states, channels, instruments, entanglement, norms and signed simulation. Their endpoint is the complete causal resource model. The **18 narrative/innovation milestones** develop two distinct converse mechanisms, their matching constructions, and the consequences for precision and physical resources. This allocation gives each proof mechanism room while keeping the prerequisites tied to the actual scientific question.

| Milestones | Connection developed |
|---|---|
| M01–M05 | From measured states and physical branches to a correctly normalized Choi test |
| M06–M12 | From local operations and witnesses to the complete causal cutting model |
| M13–M19 | From a single pure edge to forests, online resource generation and the reset law |
| M20–M21 | From gate Choi entanglement to the attributed collective gate construction and its reset extension |
| M22–M25 | From four physical resources and temporal filtering to the exact noisy-memory law and its boundaries |
| M26–M29 | From witness spectra to approximation, calibration, signed error composition and sampling |
| M30 | The complete scientific account, its evidence, resource meaning and scope |

The map is defined by the project and is the same for every reader. A reader may use the source bridge or a scientific proof whenever a concept needs more detail. The [science reading map](../science/README.md) gives the direct specialist route; its topic pages remain the authoritative homes of the exact statements and proofs.

## A useful first comparison

Two independent qubit cuts have signed extent nine. With one noiseless persistent qubit at each laboratory, a collective online construction attains seven. If either laboratory undergoes a genuine complete memory break between those two slots, the optimum returns to nine. Partial independent dephasing gives an exact value between these endpoints.

Understanding why all three statements can hold together is the opening thread of the [worked explanation](tutorial.md). The answer uses physical input and output deadlines, the quantum information that actually crosses the gap, and the distinction between a real experimental run and its signed classical weight.

[Repository overview](../README.md) · [Scientific account](../science/README.md) · [Verification guide](../verification/README.md)
