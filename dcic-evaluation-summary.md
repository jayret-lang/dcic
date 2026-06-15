# DCIC: Data-Centric Introduction to Computing — Evaluation Summary

> For someone evaluating this as an intro CS/programming textbook at a state college.

---

## Overall Approach

DCIC takes a genuinely novel approach to intro CS by centering the curriculum on **data science first**, then layering classical CS concepts on top. Authored by faculty from Brown, Northeastern, and UC San Diego, it treats pedagogy and software reliability as core values. The language used is **Pyret** (a custom language designed by the authors), transitioning to **Python** partway through.

---

## Structure

The book is organized into **8 modular booklets** that can be mixed and matched:

| Booklet | Topic |
|---------|-------|
| I | Introduction & philosophy |
| II | Introduction to Programming (Ch. 3–8) |
| III | From Pyret to Python |
| IV | Programming With State |
| V | Algorithm Analysis |
| VI | Data Structures with Analysis |
| VII | Advanced Topics |
| VIII | Interactive Programs |

---

## Chapter-by-Chapter Breakdown

### Ch. 3–4: Basic Data & Tabular Data
Students start with **concrete, visual problems** — drawing flags of countries using graphical primitives. This introduces expressions, numbers, strings, and images immediately. Chapter 4 pivots to real data via tables (Google Sheets/CSV): filtering, sorting, adding columns, visualization, and **data cleaning** (missing values, type mismatches) as a first-class concern.

*Pedagogy:* Start with images (visual, motivating) before algorithms; make data feel natural early.

### Ch. 5: Lists
Students extract columns from tables into lists. Structural recursion is introduced via the **design recipe**: write examples → understand structure → write code. Covers `map`, `filter`, `reduce`, and accumulators. Heavy emphasis on writing examples *before* code.

### Ch. 6: Structured Data
Custom data types (records and variants) via concrete problems (e.g., representing quiz questions with multiple types). Students learn to extract fields, test for variants, and process heterogeneous collections.

### Ch. 7: Trees
Genealogy/ancestry data motivates tree representation. Students build traversals incrementally using pattern matching on recursive structure.

### Ch. 8: Bonus / Advanced Foundations
Functions as data, streams, queues, and a substantial section on **testing**: converting examples to automated tests, test oracles, handling failure.

### Ch. 12–13: Programming With State
A standout section. Rather than saying "a variable is a box," DCIC introduces a formal **notional machine** with a *directory* (name-value bindings) and a *heap* (where objects live). Covers mutation, aliasing, equality (value vs. reference), and cyclic data. Contrasts Python and Pyret throughout. Students build a real mental model, not a convenient fiction.

### Ch. 14–15: Algorithm Analysis
Tabular method for measuring work on recursive functions, recurrence relations, Big-O notation, and amortized analysis (with a "Halloween" cost example). Multiple techniques taught, not just cookbook Big-O.

### Ch. 16–18: Data Structures with Analysis
DAGs, graph representations (adjacency list/matrix/edge list), DFS/BFS traversals, weighted graphs, shortest paths, spanning trees, sets (via lists/trees/hashing), AVL rotations, union-find, hash tables with collision handling, and Bloom filters. Concludes with a case study on choosing data structures based on operation frequencies. Unusually thorough for an intro text.

### Ch. 19–26: Advanced Topics
Mutable cells (boxes), equality under mutation, partial functions, exceptions vs. Option types, cycle detection (Floyd's algorithm), memoization, dynamic programming (Levenshtein distance), staging optimization, and loop decomposition.

### Ch. 27: Interactive Programs
Reactive systems for games: state-update functions, rendering, event handling, world-based animation. Built incrementally across 11 versions of an airplane landing game.

---

## Pedagogy & Exercise Design

### Distinctive Features

1. **"Do Now!" vs. "Exercise":** Inline "Do Now!" questions are answered in the next paragraph — forces active reading. Standalone exercises are homework-level with solutions withheld. Prevents passive skimming.

2. **Design Recipe:** Write examples → understand structure → write code. Applied consistently throughout the book for functions, data types, and recursion.

3. **Notional Machines:** Real, formal models of computation that evolve through the book (substitution → heap+directory → extensions for mutation and cycles). Students reason about how programs *actually* work, not just what they produce.

4. **Data-First:** Every CS structure (list, tree, graph) is introduced motivated by a real problem students have already worked on with data.

5. **Testing Culture:** Examples are tests. A dedicated section on test design, oracles, and handling failure.

6. **Socially Responsible Computing:** Ethical pitfalls (bias in data, algorithmic assumptions, data quality) are woven into technical sections where code is being written — not isolated in a separate ethics chapter.

### Exercise Types
- Concrete implementation ("Create the Armenian flag")
- Data exploration and cleaning
- Writing test examples first (test-driven)
- Complexity analysis and recurrence relations
- Conceptual reasoning ("Why does this equality test fail?")
- Comparative analysis ("Compare these two set implementations")

Difficulty spans from beginner (arithmetic expressions) to advanced (memoization, balanced trees, cycle detection).

---

## Language & Tools

- **Pyret:** Custom language designed for this book. Clean syntax, strong error messages, functional style. Not industrially used.
- **Python:** Introduced in Booklet III, then used throughout IV+. Pandas for data tables. The Pyret → Python transition is systematic and helps students learn both by contrast.
- **Environments:** CPO (code.pyret.org) is browser-based with Google Sheets integration — zero setup. VSCode used for local files and Python.

---

## Strengths for State College Adoption

- **Comprehensive:** One book can support multiple course levels, from intro through algorithms/data structures.
- **Motivated:** Every concept arrives because students need it for a problem they care about.
- **Rigorous but Accessible:** Covers Big-O, amortized analysis, tree rotations — grounded in concrete examples, not formalism for its own sake.
- **Active Learning by Design:** "Do Now!" sections, design recipe, and test-driven approach force engagement.
- **Well-Researched Pedagogy:** Authors cite education research. Topic order, language design, and notional machines are empirically motivated choices.
- **Real Data:** Students work with actual datasets (Google Sheets, CSV) from week one.
- **Flexible:** Booklets I+II alone work for a 4-week intro; I+II+V+VI cover a full algorithms course.

---

## Potential Challenges

- **Non-Standard Language:** Pyret lacks industry adoption. Students wanting a Python portfolio must wait for Booklet III. (Mitigated: transition is systematic and conceptual transfer is strong.)
- **Infrastructure Dependency:** Requires Google Sheets access or VSCode. CPO relies on Google auth.
- **Density:** 27 chapters requires instructor-level planning about what to include or skip.
- **Non-Linear Narrative:** Deliberate inclusion of wrong attempts before correct ones forces engagement but may confuse students who skim.
- **Advanced Material:** Ch. 19–26 is genuinely graduate-adjacent in places. Better suited for honors track or second course.

---

## Verdict

**Ideal for:** A college seeking a modern, data-first intro CS curriculum that emphasizes problem-solving, software reliability, and ethical engagement with data. Excellent for a two-course intro sequence or a spring algorithms course.

**Well-suited to:** Courses where you want students to understand not just *how* to code but *why* code works the way it does, and where data comes from.

**Less ideal for:** Programs requiring immediate Python fluency from day one, or students focused on web/mobile development (covered only lightly).

**Bottom line:** DCIC treats students as capable of understanding real computer science. The data-centric approach gives immediate relevance, the pedagogy is carefully researched, and the modular structure gives instructors flexibility. A strong candidate for serious adoption.
