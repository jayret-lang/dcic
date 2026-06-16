---
title: Glossary
section_number: 32
source_file: glossary.html
prev: Release_Notes.html
up: booklet_appendices.html
---

## 32 Glossary {#glossary}

☞ bandwidth

The bandwidth between two network nodes is
the quantity of data that can be transferred in a unit of time between
the nodes.

☞ cache

A cache is an instance of a
[☛ space-time tradeoff](glossary.html#%28elem._glossary-space-time._tradeoff%29): it trades space for time by
using the space to avoid recomputing an answer. The act of using a
cache is called caching. The word “cache” is often used
loosely; we use it only for information that can be perfectly
reconstructed even if it were lost: this enables a program that needs
to reverse the trade—i.e., use less space in return for more
time—to do so safely, knowing it will lose no information and thus
not sacrifice correctness.

☞ coinduction

Coinduction is a proof principle for
mathematical structures that are equipped with methods of observation
rather than of construction. Conversely, functions over inductive data
take them apart; functions over coinductive data construct them. The
[classic tutorial](http://www.cs.ru.nl/~bart/PAPERS/JR.pdf)
on the topic will be useful to mathematically sophisticated readers.

☞ idempotence

An idempotent operator is one whose repeated
application to any value in its domain yields the same result as a
single application (note that this implies the range is a subset of
the domain). Thus, a function \(f\) is idempotent if, for all \(x\) in
its domain, \(f(f(x)) = f(x)\) (and by induction this holds for
additional applications of \(f\)).

☞ invariants

Invariants are assertions about programs
that are intended to always be true (“in-vary-ant”—never
varying). For instance, a sorting routine may have as an invariant
that the list it returns is sorted.

☞ latency

The latency between two network nodes is the
time it takes for packets to go between the nodes.

☞ metasyntactic variable

A metasyntactic variable is
one that lives outside the language, and ranges over a fragment of
syntax. For instance, if we write “for expressions `e1`{.pyret} and
`e2`{.pyret}, the sum `e1 + e2`{.pyret}”, we do not mean the programmer
literally wrote “`e1`{.pyret}” in the program; rather we are using
`e1`{.pyret} to refer to whatever the programmer might write on the left
of the addition sign. Therefore, `e1`{.pyret} is metasyntax.

☞ packed representation

At the machine level, a packed
representation is one that ignores traditional alignment boundaries
(in older or smaller machines, bytes; on most contemporary machines,
words) to let multiple values fit inside or even spill over the
boundary.

For instance, say we wish to store a vector of four values, each of
which represents one of four options. A traditional representation
would store one value per alignment boundary, thereby consuming four
units of memory. A packed representation would recognize that each
value requires two bits, and four of them can fit into eight bits, so
a single byte can hold all four values. Suppose instead we wished to
store four values representing five options each, therefore requiring
three bits for each value. A byte- or word-aligned representation
would not fundamentally change, but the packed representation would
use two bytes to store the twelve bits, even permitting the third
value’s three bits to be split across a byte boundary.

Of course, packed representations have a cost. Extracting the values
requires more careful and complex operations. Thus, they represent a
classic [☛ space-time tradeoff](glossary.html#%28elem._glossary-space-time._tradeoff%29): using more time to
shrink space consumption. More subtly, packed representations can
confound certain run-time systems that may have expected data to be
aligned.

☞ parsing

Parsing is, very broadly speaking, the act of
converting content in one kind of structured input into content in
another. The structures could be very similar, but usually they are
quite different. Often, the input format is simple while the output
format is expected to capture rich information about the
content of the input. For instance, the input might be a linear
sequence of characters on an input stream, and the output might be
expected to be rich and tree-structured according to some datatype:
most program and natural-language parsers are faced with this task.

☞ reduction

Reduction is a relationship between a pair
of situations—problems, functions, data structures, etc.—where one
is defined in terms of the other. A reduction R is a
function from situations of the form P to ones of the form
Q if, for every instance of P, R
can construct an instance of Q such that it preserves
the meaning of P. Note that the converse strictly does not
need to hold.

☞ space-time tradeoff

Suppose you have an expensive
computation that always produces the same answer for a given set of
inputs. Once you have computed the answer once, you now have a choice:
store the answer so that you can simply look it up when you need it
again, or throw it away and re-compute it the next time. The former
uses more space, but saves time; the latter uses less space, but
consumes more time. This, at its heart, is the space-time
tradeoff. Memoization [[Avoiding Recomputation by Remembering Answers](avoid-recomp.html)] and using a [☛ cache](glossary.html#%28elem._glossary-cache%29)
are both instances of it.

☞ type variable

Type variables are identifiers in the
type language that (usually) range over actual types.

☞ wire format

A notation used to transmit data across,
as opposed to within, a closed platform (such as a virtual
machine). These are usually expected to be relatively simple because
they must be implemented in many languages and on weak processes. They
are also expected to be unambiguous to aid simple, fast, and
correct parsing. Popular examples include XML, JSON, and
s-expressions.
