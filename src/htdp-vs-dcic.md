---
title: Comparing This Book to HtDP
section_number: 30
source_file: htdp-vs-dcic.html
prev: pyret-vs-python.html
up: booklet_appendices.html
next: Release_Notes.html
---

```{=html}
<a name="(part._htdp-vs-dcic)"></a>
```

## 30 Comparing This Book to HtDP {#htdp-vs-dcic}

This book (DCIC) is often compared to
[How to Design Programs](https://www.htdp.org/) (HtDP),
from which it draws enormous inspiration. Here we briefly describe how the two
books compare.

At a high level they are very similar:


- Both are built around the centrality of data structure. Both want to
  provide methods for designing programs. Both start with functional programming
  but transition to (and take very seriously) stateful imperative programming.

- Both are built around languages carefully designed with education in
  mind. The languages provide special support for writing examples and tests; error
  reporting designed for beginners; built-in images and reactivity. The languages
  eschew weird gotchas (in a way that Python does not: see
  [Jayret vs. Python](pyret-vs-python.html) or, if you want to read much more,
  [this paper](https://cs.brown.edu/~sk/Publications/Papers/Published/pmmwplck-python-full-monty/)).

and so on. To call these “similarities” is, however, a disservice. DCIC
copied these ideas from HtDP; in some cases, HtDP even pioneered them.

Now for the differences. Note that they are differences now. Some ideas
from DCIC are going to HtDP, and over time more may intermingle.


- The most obvious is that DCIC is in Jayret. HtDP has tons of good ideas,
  all ignored because it uses Racket, whose syntax some people (especially some
  educators) dislike. We built Jayret to embody good ideas we’d learned from the
  Racket student languages and other good ideas of our own, but package them in a
  familiar syntax. But as you can see, the two languages are not actually that
  far apart: [Jayret for Racketeers and Schemers](p4rs.html).

- The next most obvious thing is that DCIC also includes Python. HtDP has a
  (not formally published) follow-up that
  [teaches program design in Java](https://felleisen.org/matthias/HtDC/htdc.pdf).
  In contrast, we wanted to integrate
  the transition to Python into DCIC itself. There’s much to be learned from the
  contrast! In particular, Jayret and its environment were carefully designed around
  pedagogic ideas for teaching state. Python was not, despite the ubiquity and
  difficulty of state! So there’s a lot to be gained, when introducing state, to
  contrast them.

- Next, DCIC has a lot algorithmic content, whereas HtDP has almost
  none. DCIC covers, for instance, Big-O analysis
  [[Predicting Growth](predicting-growth.html)]. It even has a section on amortized analysis
  [[Halloween Analysis](amortized-analysis.html)]. It goes up through some graph algorithms. This
  is far more advanced material than HtDP covers.

Those are most of the differences. They’re visible (some even evident) from
glancing through the table of contents. However, there is one very deep
difference that will not be apparent to most readers, which we discuss below.

HtDP is built around a beautiful idea: the data structures shown grow in
complexity in set-theoretic terms. Therefore it begins with atomic data, then
has fixed-size data (structures), then unbounded collections (lists) of atomic
data, pairs of lists, lists of structures, and so on. All built up,
systematically, in a neat progression.

However, this has a downside. You have to imagine what the data
represent (this number is an age, that string is a name, that list is of GDPs),
but they’re idealized. In a way the most real data are actually images! After
that (which come early), all the data are “virtualized” and imaginary.

Our view is that the most interesting data are lists of structures. (Remember
those? They’re complicated and come some ways down the progression.) You might
find this surprising; if so, we give you another name for them: tables. Tables
are ubiquitous. Even companies process and publish them; even primary school
students recognize and use them. They are perhaps our most important universal
form of structured data.

Even better, lots of real-world data are provided as tables. You don’t have to
imagine things or make up fake GDPs like 1, 2, and 3. You can get actual
GDPs or populations or movie revenues or sports standings or whatever interests
you. (Ideally, cleansed and curated.) We believe that just about every
student—even every child—is a nascent data scientist (at least when it’s
convenient to them). Even a child who says “I hate math” will often gladly
use statistics to argue for their favorite actor or sportsperson or
whatever. We just have to find what motivates them.

Buut there’s a big catch! A key feature of HtDP is that for every level of
datatype, it provides a Design Recipe for programming over that
datatype. Lists-of-structs are complex. So is their programming recipe. And we
want to put them near the beginning! Furthermore, the Design Recipe is
dangerous to ignore. Students struggle with blank pages and often fill them up
with bad code, which they then get attached to. The Design Recipe provides
structure, scaffolding, reviewability, and much more. It’s cognitively grounded
in schemas.

So over the past few years, we’ve been working on different program design
methods that address the same ends through different means. A lot of our recent
education research has been putting new foundations in place. It’s very much
work in progress. And DCIC is the distillation of those efforts. As we have new
results, we’ll be weaving them into DCIC (and probably HtDP too). Stay tuned!
