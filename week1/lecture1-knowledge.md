# Knowledge representation

## Propositional logic

And (∧), Or (∨), Not (¬), Implies (→), Biconditional (↔)

[logicalconnectives](./logicalcons.png)

### Not (¬)
Inverts the truth value of the proposition.

| p | ¬p |
|---|----|
| T | F  |
| F | T  |

### And (∧)

| p | q | p ∧ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

### Or (∨)

| p | q | p ∨ q |
|---|---|-------|
| T | T | T     |
| T | F | T     |
| F | T | T     |
| F | F | F     |


### Implication truth table:
if p then q
| p | q | p → q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | T     |
| F | F | T     |

### Biconditional truth table:
p if and only if q
| p | q | p ↔ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | T     |

### Entailment

A sentence is entailed by a set of sentences if it is impossible for the set of sentences to be true and the sentence to be false.

### Inference
the process of deriving new sentences from existing sentences.

Example:
P: All men are mortal.
Q: Socrates is a man.
R: Socrates is mortal.

P ∧ Q → R

P: It is a Tuesday.
Q: It is raining.
R: Harry will go for a walk.


Inference: R is true.
It is a Tuesday and it is not raining, implies that Harry will go for a walk.

### Model Checking

- To determine if KB = a:
- Enumerate all possible models.
- If in every model where KB is true, a is true, then
KB entails a.

KB: (P ∧ ¬Q) → R
Query: R
Table of all possible models:

| P | Q | R | KB | 
|---|---|---|----|
| F | F | F | F  |
| F | F | T | F  |
| F | T | F | F  |
| F | T | T | F  |
| T | F | F | F  |
| T | F | T | T  |
| T | T | F | F  |
| T | T | T | F  |

