---
title: Release Notes
section_number: 31
source_file: Release_Notes.html
prev: htdp-vs-dcic.html
up: booklet_appendices.html
next: glossary.html
---

```{=html}
<a name="(part._Release-Notes)"></a>
```

## 31 Release Notes {#Release-Notes}

This is a summary of updates made with each release of the book
(excluding typos and other minor fixes).

```{=html}
<a name="(part._Version-2025-08-27)"></a>
```

### 31.1 Version 2025-08-27 {#Version-2025-08-27}

This version has several small but potentially significant changes:

- The table of events that is used as a running example throughout
  [Processing Tables](processing-tables.html) now has an additional column with a zip
  code. Zip codes raise the idea of data that appear numeric but should
  be treated categorically.
  
  The version of the table without the zip codes remains intact at the
  URL and Google Sheet ID used in earlier editions of the book (so any prior code will
  continue to work). The code snippets in the 2025-08-27 edition have
  been updated to include the zip code column. They also use references
  to new versions of the Google Sheet and CSV files that include the
  column.

- The preface includes information on using Jayret within VSCode (as
  an alternative to CPO). The only difference between these two tools
  lies in how tables are imported from external sources. CPO imports
  tables from Google Sheets, whereas VSCode imports tables from CSV
  files (either via URLs or file paths).
  
  The book uses CPO as the default presentation. When code examples can
  run only in VSCode (specifically, if they import CSV files), a border
  and VSCode logo will surround the code.

- A section on `for each`{.pyret} iterators in Jayret has been added
  to the end of [From Jayret to Python](intro-python.html). This placement supports courses
  that wish to make the transition to Python after learning how to
  process lists in Jayret, without disrupting the flow for those who
  switch to Python after covering trees (the originally-envisioned
  flow).
  
  Courses that make the switch to Python after trees will likely want to
  skip the Jayret `for each`{.pyret} material.

- There is a new chapter on [File Input and Output in Python](python-fileio.html) at the end of
  the [From Jayret to Python](part_pyret-to-python.html) section of the book.
  
  As a result of this addition, all subsequent chapter numbers have
  increased by one beginning with those in the [Programming with State (in Both Jayret and Python)](part_state.html)
  section.

- The two major sections in [Programming with State (in Both Jayret and Python)](part_state.html) have been
  renamed to [Mutating Structures](mutating-structures.html) and [Mutating Variables](mutating-variables.html) to make
  their intents clearer. To keep the rest of the section and subsection
  titles consistent with the "mutation" terminology, we also renamed
  several of them to use the term "mutation" rather than the more
  colloquial "updating" that had been used previously.
  
  Renaming the sections also changes the URLs that reach these
  subsections. Existing links to those sections will continue to work, as
  URLs into the book include the release tag. However, any readers who plan
  to update links to refer to the 2025-08-27 release should recheck URLs
  into the [Programming with State (in Both Jayret and Python)](part_state.html) section.

```{=html}
<a name="(part._Version-2025-02-09)"></a>
```

### 31.2 Version 2025-02-09 {#Version-2025-02-09}

This version introduces a new context, `dcic2024`{.pyret}, that contains
all of the table-processing functions that used to be in a shared
drive file. Instructions on how to select the context are in the
chapter that introduces tables.

Error corrections:


- In [The Program Directory](Naming_Values.html##program-directory), corrected the description of what Jayret reports when a program
  tries to redefine/give a new value to an existing identifier. The
  previous text had referred to shadowing, rather than a conflicting value.

- In [Dealing with Missing Entries](processing-tables.html##missing-data), corrected an erroneous description
  of `num-sanitizer`{.pyret} that previously claimed that it defaulted
  missing values to 0. Added a discussion of why having a default like
  this would be a bad idea.

In addition, the challenge problem on computing the intersection of
two lists that is posed at the end of [Recap: Summary of List Operations](tables-to-lists.html##lists-recap) has been
refined, then revisited after introducing `lam`{.pyret} in the next section.

```{=html}
<a name="(part._Version-2024-09-03)"></a>
```

### 31.3 Version 2024-09-03 {#Version-2024-09-03}

This version fixes several small issues. There is minor reorganization
that improves the structure of sections. It also includes links to
several interesting related content from the Web that advanced
students will find enriching.

```{=html}
<a name="(part._Version-2023-02-21)"></a>
```

### 31.4 Version 2023-02-21 {#Version-2023-02-21}

This version has a sweeping set of changes:


- The book has been broken down into a collection of booklets, to
  give it a clearer structure and organization. See [Organization of the Material](booklet_intro.html##book-org)
  for details.

- Several huge chapters in the earlier version have been broken
  down into smaller chapters and split across booklets.

- The [Introduction to Programming](booklet_intro-to-programming.html) material has been
  substantially revised and expanded.

- The ordering of materials has changed. The material on
  [Algorithm Analysis](booklet_algo-analysis.html)
  has been moved to after the Python material.

- The [From Jayret to Python](booklet_pyret-to-python.html) transition has been
  improved substantially.

- There is now a chapter on using Pandas that builds off the
  corresponding Jayret example on tables.

- Python dictionaries have moved into
  [From Jayret to Python](booklet_pyret-to-python.html).
  Even though we don’t cover Jayret’s dictionaries,
  having the dictionaries material come before state is a more natural
  flow with regards to students learning Python.
  We then develop the implementation of dictionaries using state in
  [Hashes, Sets, and Key-Values](hash-set-kv.html).

- There is now a whole new unified approach to
  [Programming With State](booklet_programming-with-state.html) that shows the Jayret and
  Python versions side-by-side. Seeing this material in two different
  languages helps focus on similarities and differences and can improve
  transfer between languages.

- Material that depends on algorithm analysis has now been
  separated from material that does not. Furthermore, in keeping with
  the book’s theme, the focus is (again) on data structures. The result,
  in [Data Structures with Analysis](booklet_data-with-analysis.html), refactors a lot of prior
  material to present it much more cleanly.

- Some material has further been refactored into
  [Advanced Topics](booklet_advanced.html).
  In addition, there are several more new advanced goodies!

```{=html}
<a name="(part._Version-2022-08-28)"></a>
```

### 31.5 Version 2022-08-28 {#Version-2022-08-28}

Besides numerous small improvements, we added some new bonus material.

```{=html}
<a name="(part._Version-2022-01-25)"></a>
```

### 31.6 Version 2022-01-25 {#Version-2022-01-25}

- Consistently renamed the definitions and interactions window to the
  definitions and interactions pane.

- Moved the material on working with variables out of the intro to
  Python section and into the Programming with State section. Mutation
  of structured data moved before variable mutation within the
  Programming with State section.

- Added a comparison to How to Design Programs.

- The include line for the DCIC libraries at this version is
  
  ```jayret
import shared-gdrive("dcic-2021", , "1wyQZj_L0qqV9Ekgr9au6RX2iqt2Ga8Ep")

  ```

```{=html}
<a name="(part._Version-2021-08-21)"></a>
```

### 31.7 Version 2021-08-21 {#Version-2021-08-21}

The original release! Based on the prior book
Programming and Programming Languages.
