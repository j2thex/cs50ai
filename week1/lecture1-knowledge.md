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
⍺ ⊨ β
In every model where ⍺ is true, β is also true.


### Inference
the process of deriving new sentences from existing sentences.

Example:
P: All men are mortal.
Q: Socrates is a man.
R: Socrates is mortal.

P ∧(and) not Q → R

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

## Conjunctive Normal Form (CNF)

A sentence is in CNF if it is a conjunction of clauses, where each clause is a disjunction of literals.

Conversion to CNF
• Eliminate biconditionals
• turn (a <-> B) into (a → B) ^ (B → a)
• Eliminate implications
• turn (a → B) into ¬a v B
• Move ¬ inwards using De Morgan's Laws
• e.g. turn ¬(an B) into ¬a v ¬B
• Use distributive law to distribute v wherever possible

P ∧ Q -> R
¬(P ∧ Q) v R
(¬P ^ ¬Q) v R
(¬P v R) ^ (¬Q v R) # Conjunctive Normal Form

## Inference by Resolution

Proof by contradiction:
• To determine if KB = a:
• Check if (KB ^ ¬a) is a contradiction?
• If so, then KB= a.
• Otherwise, no entailment.

 Does (A v B) ^ (-B v C) ^ (-C) entail A?
 (A v B) ^ (-B v C) ^ (-C) ^ (-A)
 
 # First order logic

 ## Constant Symbol 
Minerva 
Pomona 
Horace 
Gilderoy
Gryffindor
Hufflepuff
Ravenclaw
Slytherin

## Predicate Symbol
Person
House
Belongs To  

## Existential Quantification

∀x. Person(x) → (∃y. House(y) ^ Belongs To(x, y))

## Universal Quantification

∃x. Person(x) → (∀y. House(y) ^ Belongs To(x, y))

## Quantifier Negation

¬∀x. P(x) ≡ ∃x. ¬P(x)
¬∃x. P(x) ≡ ∀x. ¬P(x)

