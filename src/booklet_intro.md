---
title: Introduction
section_number: I
source_file: booklet_intro.html
prev: index.html
up: index.html
next: booklet_intro-to-programming.html
---

## I Introduction {#booklet-intro}

## 1 Overview {#Overview}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.What_.This_.Book_is_.About%29">1.1<span class="hspace"> </span>What This Book is About</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.The_.Values_.That_.Drive_.This_.Book%29">1.2<span class="hspace"> </span>The Values That Drive This Book</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.Our_.Perspective_on_.Data%29">1.3<span class="hspace"> </span>Our Perspective on Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.What_.Makes_.This_.Book_.Unique%29">1.4<span class="hspace"> </span>What Makes This Book Unique</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.Who_.This_.Book_is_.For%29">1.5<span class="hspace"> </span>Who This Book is For</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._book-style%29">1.6<span class="hspace"> </span>The Structure of This Book</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._book-org%29">1.7<span class="hspace"> </span>Organization of the Material</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.Our_.Programming_.Language_.Choice%29">1.8<span class="hspace"> </span>Our Programming Language Choice</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.Programming_.Tools%29">1.9<span class="hspace"> </span>Programming Tools</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.Sending_.Us_.Feedback__.Errors__and_.Comments%29">1.10<span class="hspace"> </span>Sending Us Feedback, Errors, and Comments</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="booklet_intro.html#%28part._.Staying_.Up-.To-.Date%29">1.11<span class="hspace"> </span>Staying Up-To-Date</a></p></td></tr></table>
```

### 1.1 What This Book is About {#What-This-Book-is-About}

This book is an introduction to computer science. It will teach you to program,
and do so in ways that are of practical value and importance. However, it will
also go beyond programming to computer science, a rich, deep, fascinating, and
beautiful intellectual discipline. You will learn many useful things that you
can apply right away, but we will also show you some of what lies beneath and
beyond.

Most of all, we want to give you ways of thinking about solving problems
using computation. Some of these ways are technical methods, such as working
from data and examples to construct solutions to problems. Others are
scientific methods, such as ways of making sure that programs are reliable and
do what they claim. Finally, some are social, thinking about the impacts that
programs have on people.

### 1.2 The Values That Drive This Book {#The-Values-That-Drive-This-Book}

Our perspective is guided by our decades of experience as software developers,
researchers, and educators. This has instilled in us the following beliefs:


- Software is not written only to be run. It must also be written to be
  read and maintained by others. Often, that “other” person is you, six months
  later, who has forgotten what they did and why.
- Programmers are responsible for their software
  meeting its desired goals and being reliable. This is
  reflected in a variety of disciplines inside computer science, such as testing
  and verification.
- Programs ought to be be amenable to prediction. We need to know, as much
  as possible, before a program runs, how it will behave. This behavior includes
  not only technical characteristics such as running time, space, power, and so
  on, but also social impacts, benefits, and harms. Programmers have been
  notoriously poor at thinking about the latter.

### 1.3 Our Perspective on Data {#Our-Perspective-on-Data}

These concerns intersect with our belief about how computer science has evolved
as a discipline. It is a truism that we live in a world awash with data, but
what consequence does that have?

At a computational level, data have had a profound effect. Traditionally, the
only way to make a program better was to improve the program directly,
which often meant making it more complicated and impacting the values we
discuss above. But there are classes of programs for which there is another method: simply give the
same program more or better data, and the program can improve. These
data-driven programs lie at the heart of many innovations we see around
us.

In addition to this technical effect, data can have a profound pedagogic
impact, too. Most introductory programming is plagued by artificial data
that have no real meaning, interest, or consequence (and often, artificial
problems to accompany them). With real data, learners can personalize their
education, focusing on problems they find meaningful, enriching, or just plain
fun—asking and answering questions they find worthwhile. Indeed, from this
perspective, programs interrogate data: that is, programs are tools
for answering questions. In turn, the emphasis on real data and real questions
enables us to discuss the social impacts of computing.

These phenomena have given rise to whole new areas of study, typically
called data science. However, typical data science curricula also have many
limitations. They pay little attention to what we know about the difficulties
of learning to program. They have little emphasis on software reliability. And
they fail to recognize that their data are often quite limited in their
structure. These limitations, where data science typically ends, are where
computer science begins. In particular, the structure of data serve as a point
of departure for thinking about and achieving some of the values above—performance, reliability, and predictability—using the many tools of computer
science.

### 1.4 What Makes This Book Unique {#What-Makes-This-Book-Unique}

First, we propose a new perspective on structuring computing curricula,
which we call data centricity.[For more about this, read
[our essay](https://cs.brown.edu/~sk/Publications/Papers/Published/kf-data-centric/).]{.margin-note}
We view a data-centric curriculum as


data centric = data science + data structures

in that order: we begin with ideas from data science, before shifting to
classical ideas from data structures and the rest of computer science. This
book lays out this vision concretely and in detail.

Second, computing education talks a great deal about
notional machines—abstractions of program behavior meant to help
students understand how programs work—but few curricula actually use one. We
take notional machines seriously, developing a sequence of them and weaving
them through the curriculum. This ties to our belief that programs are not only
objects that run, but also objects that we reason about.

Third, we weave content on socially-responsible computing into the
text. Unlike other efforts that focus on exposing students to ethics
or the pitfalls of technology in general, we aim to show students how
the constructs and concepts that they are turning into code
right now can lead to adverse impacts unless used with
care. In keeping with our focus on testing and concrete examples, we
introduce several topics by getting students to think about
assumptions at the level of concrete data. This material is called out
explicitly throughout the book.

Finally, this book is deeply informed by recent and ongoing research
results. Our choices of material, order of presentation, programming methods,
and more are driven by what we know from the research literature. In many
cases, we ourselves are the ones doing the research, so the curriculum and
research live in a symbiotic relationship. You can find our papers
(some with each other, others not)
[on](https://cs.brown.edu/~kfisler/Pubs/index.html)
[our](https://cs.brown.edu/~sk/Publications/Papers/Published/)
[respective](https://www.ccs.neu.edu/home/blerner/papers.html)
[pages](https://jpolitz.github.io).

### 1.5 Who This Book is For {#Who-This-Book-is-For}

This book is written primarily for students who are in the early stages of
computing education at the tertiary level (college or university). However,
many—especially the earlier—parts of it are also suitable for secondary
education (in the USA, for instance, roughly grades 6–12, or ages
12–18). Indeed, we see a natural continuum between secondary and tertiary
education, and think this book can serve as a useful bridge between the two.

### 1.6 The Structure of This Book {#book-style}

Unlike some other textbooks, this one does not follow a top-down
narrative. Rather it has the flow of a conversation, with
backtracking. We will often build up programs incrementally, just as
a pair of programmers would. We will include mistakes, not because we
don’t know better, but because this is the best way for you
to learn. Including mistakes makes it impossible for you to read
passively: you must instead engage with the material, because you can
never be sure of the veracity of what you’re reading.

At the end, you’ll always get to the right answer. However, this
non-linear path is more frustrating in the short term (you will often
be tempted to say, “Just tell me the answer, already!”), and it
makes the book a poor reference guide (you can’t open up to a random
page and be sure what it says is correct). However, that feeling of
frustration is the sensation of learning. We don’t know of a way
around it.

We use visual formatting to highlight some of these points. Thus,
in several places you will encounter this:

::: {.exercise}
This is an exercise. Do try it.
:::

This is a traditional textbook exercise. It’s something you need to
do on your own. If you’re using this book as part of a course, this
may very well have been assigned as homework. In contrast, you will
also find exercise-like questions that look like this:

::: {.do-now}
There’s an activity here! Do you see it?
:::

When you get to one of these, stop. Read, think, and formulate
an answer before you proceed. You must do this because this is
actually an exercise, but the answer is already in the
book—most often in the text immediately following (i.e., in the part
you’re reading right now)—or is something you can determine for
yourself by running a program. If you just read on, you’ll see the
answer without having thought about it (or not see it at all, if the
instructions are to run a program), so you will get to neither (a)
test your knowledge, nor (b) improve your intuitions. In other words,
these are additional, explicit attempts to encourage active learning.
Ultimately, however, we can only encourage it; it’s up to you to
practice it.

Specific strategies for program design and development get highlighted
in boxes that look like this:

::: {.strategy}
here’s a summary of how to do something.
:::

Finally, we also call out content on socially-responsible computing
with visually distinctive regions like this:

::: {.responsible-cs}
Here are social pitfalls from using
material naively.
:::

### 1.7 Organization of the Material {#book-org}

Because this book covers what would be considered multiple semesters
worth of material at the tertiary level in the USA, we have divided it
into seven main booklets. Later booklets depend on some earlier ones,
but the earlier ones can be treated as a stand-alone book that arrives
at a satisfying ending for a student or course that does not proceed
further.

1. [Introduction to Programming](booklet_intro-to-programming.html):
  An introduction to programming for beginners that teaches programming
  and rudimentary data analysis. It introduces core programming concepts
  through composing images and processing tables, before covering lists
  and trees. The notional machine throughout this section is based on
  substitution.
  
  Dependencies: None!
2. [From Jayret to Python](booklet_pyret-to-python.html):
  Students learn to transfer their knowledge from Jayret to
  Python, highlighting similarities and differences between the
  languages and their traditional programming styles
  (“paradigms”). Students are also introduced to Pandas, as a
  real-world table-processing system.
  
  Dependencies: [Introduction to Programming](booklet_intro-to-programming.html).
3. [Programming With State](booklet_programming-with-state.html):
  Students learn the subtleties of state and aliasing. Much of the
  coverage is in both Python and Jayret. This contrast lets students
  understand how multiple languages can approach the same topic; the
  ways in which the underlying ideas are actually the same; but also
  some key differences that provide insight. The notional machine grows
  to cover state and aliasing by separating the naming environment (here
  called the directory) from a heap of structured data values.
  
  Dependencies: [Introduction to Programming](booklet_intro-to-programming.html) is
  essential. [From Jayret to Python](booklet_pyret-to-python.html) is helpful to follow
  the Python portions of this booklet, but a student can
  do the Jayret parts without having seen Python.
4. [Algorithm Analysis](booklet_algo-analysis.html):
  Students are introduced to multiple techniques for analyzing
  algorithms.
  
  Dependencies: [Introduction to Programming](booklet_intro-to-programming.html). There is
  no dependency on state.
5. [Data Structures with Analysis](booklet_data-with-analysis.html):
  Students are introduced to more advanced data structures through a
  lens of algorithm analysis, which motivates their revision and
  variation.
  
  Dependencies: [Introduction to Programming](booklet_intro-to-programming.html) and
  [Algorithm Analysis](booklet_algo-analysis.html) are essential
  everywhere. [Programming With State](booklet_programming-with-state.html) is necessary for
  some material.
6. [Advanced Topics](booklet_advanced.html):
  Students cover a grab-bag of interesting computer science
  topics in program design and algorithmic programming. Relative to the
  other material, this content is either more subtle, more advanced, or
  less essential in a mainstream course.
  
  Dependencies: All the material depends on
  [Introduction to Programming](booklet_intro-to-programming.html). Some material depends on
  [Algorithm Analysis](booklet_algo-analysis.html) and/or
  [Programming With State](booklet_programming-with-state.html).
7. [Interactive Programs](booklet_interaction.html):
  Students can write interactive programs with relatively few dependencies!
  
  Dependencies: [Introduction to Programming](booklet_intro-to-programming.html).

This decomposition into booklets allows flexibility in offering
several different kinds of courses at very different levels of
sophistication. For instance, we already offer two very different
courses by remixing this material, which others could follow:


- An introductory course can use
  [Introduction to Programming](booklet_intro-to-programming.html),
  [From Jayret to Python](booklet_pyret-to-python.html),
  and [Programming With State](booklet_programming-with-state.html)
  to
  cover the data-centric view of computer science and leaving students
  with basic skills in Python. This corresponds to
  [CSCI 0111](https://cs.brown.edu/courses/csci0111/)
  at Brown University.
- A more advanced course can start with
  [Introduction to Programming](booklet_intro-to-programming.html),
  then do
  [Algorithm Analysis](booklet_algo-analysis.html) (perhaps in increments),
  followed by
  [Data Structures with Analysis](booklet_data-with-analysis.html),
  before returning to
  [Programming With State](booklet_programming-with-state.html),
  while interspersing content from
  [Advanced Topics](booklet_advanced.html). This corresponds to
  [CSCI 0190](https://cs.brown.edu/courses/csci0190/)
  at Brown University.

The course pages archive all prior instances of the
courses, which include all the assignments and related materials. Readers are
welcome to use these in their own courses.

Many of these courses will have entering students who have programmed with state
before (in Python, Java, Scratch, or other languages). In our experience, most
of these students have been given either vastly incomplete, or outright
misleading, explanations of and metaphors for state (e.g., “a variable is a
box”). Thus, they have a poor understanding of it beyond the absolute basics,
especially when they get to important topics like aliasing. As a result, many
of these students have found it both novel and insightful to properly
understand how state really works through our notional machine. For that
reason, we recommend going through that material slowly and carefully.

We of course invite readers to create their own mashups of the
chapters within the sections. We would love to hear about others’ designs.

### 1.8 Our Programming Language Choice {#Our-Programming-Language-Choice}

If we wanted to get rich, we’d have written this book entirely in Python. As of
this writing, Python is enjoying its instructional-use heyday (just like Java
before it, C++ before that, C before that, Pascal earlier, and so on).
And there are, indeed, many attractive aspects of Python, not least its presence
next to bullet points on job listings. However, we’ve been [repeatedly frustrated by Python](pyret-vs-python.html) as an entrypoint into
learning programming.

As a result, this book features two programming languages. It starts with a
language, called
[Jayret](https://jayret-lang.github.io/),
that we designed to address our needs and frustrations. It has been expressly
designed for the style of programming in this book, so the two can grow in
harmony. It draws on Python, but also on many other excellent programming
languages. Beginning programmers can therefore rest in the knowledge they are
being cared for, while programmers with past acquaintance of the language
menagerie, from serpents to dromedaries, should find Jayret familiar and
comfortable.

Then, recognizing the value of Python both as a standard language of
communication and for its extensive libraries, the [Programming with State (in Both Jayret and Python)](part_state.html) part
of this book explicitly covers Python. Rather than starting from scratch in
Python, we present a systematic and gradual transition to it from the earlier
material. We believe this will make you learn general programming better than
if you had seen only one programming language. However, we believe this will
help you understand Python better, too: just like you learn to appreciate your
own language, country, or culture better once you’ve stepped outside and been
exposed to other ones.

### 1.9 Programming Tools {#Programming-Tools}

[CPO](https://jayret-lang.github.io/code/) (an abbreviation of
jayret-lang.github.io/code) is our default programming environment for Jayret.
It runs entirely in the browser and uses Google Drive
for authentication and file storage.

Jayret support is also available for VSCode. To install it, visit
[https://code.visualstudio.com](https://code.visualstudio.com).
Once you have installed it, click the Extensions tab on the left and
search for Jayret. You should install the "Jayret Interactive Editor for VSCode".

CPO and VSCode differ only in their support for loading spreadsheet
data. CPO is designed to work with Google Sheets, while VSCode does
not support Google Sheets, and instead expects students to load data from
local CSV files. Unless the book says otherwise, all code can be run in
either tool, and the interface for editing and interacting with programs
is the same. If there are differences, the book will present both
versions. In such cases, code that could run only in VSCode will be
labeled with the VSCode icon, as follows:

::: {.vscode-note}
```jayret
import csv

```
:::

We do not recommend any
particular Python environment. Any Python editor that allows you to
use pytest and load external data files should work fine.

### 1.10 Sending Us Feedback, Errors, and Comments {#Sending-Us-Feedback-Errors-and-Comments}

As you work through the book, you may spot typos, notice points
where we could have been clearer, or have a suggestion for a future
release. You can pass these along to us by filing an issue on our
[public GitHub site](https://github.com/data-centric-computing/dcic-public). Thanks in advance!

### 1.11 Staying Up-To-Date {#Staying-Up-To-Date}

You can subscribe to our very-low-volume mailing list,
[dcic-notifications](https://groups.google.com/g/dcic-notifications).

## 2 Acknowledgments {#Acknowledgments}

This book has benefited from the attention of many.

Special thanks to the students at Brown University, who have been
drafted into acting as a crucible for every iteration of this
book. They have supported it with unusual grace, creating a welcoming
and rewarding environment for pedagogic effort. Thanks also to our
academic homes—Brown, Northeastern, and UC San Diego—for comfort
and encouragement.

The following people have helpfully provided information on typos and other infelicities:


Abhabongse Janthong,
Alex Hayworth, Alex Kleiman,
Athyuttam Eleti,
Benjamin S. Shapiro,
Cheng Xie,
Daniel Cai,
Danil Braun,
Dave Lee,
David Cooper, Doug Kearns, Ebube Chuba,
Egg (on discord), Evelyn Mitchell, frodokomodo (on github),
Laura Pozzi, Gavin Sinclair,
Ggbb (from Discord), Graeme McCutcheon, Gregor Grasselli, gregshubert (on github), Harrison Pincket,
Igor Moreno Santos,
Iuliu Balibanu,
Joann Ordille, Jason Bennett,
Jeremy Siek,
jiad (from Discord),
Jonathan Zhou,
John (Spike) Hughes,
Jon Sailor,
Jonathan Zhou, Josh Paley,
Kelechi Ukadike,
Kendrick Cole,
Kishore Vancheeshwaran, Laura Pozzi, Marc Smith,
Mark Smucker,
Mehmet Fatih Köksal, Michael Morehouse, Noah Tye,
Oyendrila Dobe, Rafał Gwoździński,
rawalplawit (on github), Raymond Plante,
Ricardo Vela, Samuel Ainsworth,
Samuel Kortchmar,
timotree (on github), Yukai Chou,
Zach Amiton.

The following have done the same, but in much greater quantity or depth:


Dorai Sitaram,
John Palmer,
Kartik Singhal,
Kenichi Asai,
Lev Litichevskiy.

Even amongst the problem-spotters, one is hors catégorie:


Sorawee Porncharoenwase.

Daniel Patterson has helped us think about where to switch
between Jayret and Python, while also helping with content on using
Jayret with VSCode.

This book is completely dependent on Jayret, and thus on the
[many people](https://jayret-lang.github.io/crew/) who have
created and sustained it.

We thank
[Matthew Butterick](https://practicaltypography.com/)
for his help with book styling (though the ultimate style is ours, so don’t blame him!).

Many, many years ago, Alejandro Schäffer introduced SK to the idea of
nature as a fat-fingered typist. Alejandro’s fingerprints are over
many parts of this book, even if he wouldn’t
necessarily approve of what has come of his patient instruction.

We are deeply inspired by the work and ideas of
Matthias Felleisen, Matthew Flatt, and Robby Findler.
Matthias, in particular, inspired our ideas on program design. Even where we
disagree, he continues to engage with and challenge our ideas in ways that
force us to grow and improve. Our work is better than it would be in
incalculable ways due to his influence.

The chapter on [Interactive Games as Reactive Systems](games-reactive.html) is translated from
[How to Design Worlds](https://world.cs.brown.edu/),
and owes thanks to all the people acknowledged there.

This book is written in
[Scribble](https://docs.racket-lang.org/scribble/),
the authoring tool of choice for the discerning programmer.

We thank
[cloudconvert](https://cloudconvert.com/)
for their free conversion tools.
