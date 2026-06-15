---
title: Sets as a Case Study
section_number: 18.6
source_file: dcic_orig_sets-case-study.html
prev: orderability.html
up: part_sets.html
next: booklet_advanced.html
---

### Sets as a Case Study {#sets-case-study}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-case-study.html#%28part._.Nature_of_the_.Data%29">18.6.1<span class="hspace"> </span>Nature of the Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-case-study.html#%28part._.Nature_of_the_.Operations%29">18.6.2<span class="hspace"> </span>Nature of the Operations</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-case-study.html#%28part._.Nature_of_the_.Guarantee%29">18.6.3<span class="hspace"> </span>Nature of the Guarantee</a></p></td></tr></table>
```

We have spent a lot of time on sets. That is not only because they are
useful in their own right, but also because they offer a window into a
variety of possible designs. In particular, they illustrate several
tradeoffs that we can make in the design of data structures, based on
our needs.

There are several dimensions along which we can divide our designs.

#### Nature of the Data {#Nature-of-the-Data}

If the data cannot even be comparable for quality, then we can’t
construct sets out of them, because equality is central to the
definition of a set.

If the data can be compared for equality but not for ordering, then we
can only construct list-sets [[Representing Sets as Lists](sets-from-lists.html)], with their
linear-time complexity. However, if we can hash the
values [[Converting Values to Ordered Values](orderability.html##hashing-values)], then we can construct trees
[[Making Sets Grow on Trees](sets-from-trees.html)] and hashtables
[[Sets from Hashing and Arrays](hash-set-kv.html##hash-tables)]. Trees give us logarithmic complexity for the
most expensive atomic operations, while hashtables give us
constant-to-linear complexity.

#### Nature of the Operations {#Nature-of-the-Operations}

Another dimension of variation is the collection of operations we
need. We began with a fairly ambitious, but standard, collection of
operations [[<set-operations>](sets-from-lists.html#%28elem._set-operations%29)], but gradually ignored many of
them. In particular, some interpretations of sets, like
[Union-Find](union-find.html), achieve excellent complexity at the cost of
most of these operations. [Bloom Filters](hash-set-kv.html##bloom-filters) provide
another instance of this. There is a general computer science
principle at work here: the fewer operations we need to support, the
better we can (sometimes) make the complexity of the remaining ones.

#### Nature of the Guarantee {#Nature-of-the-Guarantee}

Most subtly, there was another distinction: whether or not we needed
reliable results. Most of our set representations are
reliable. However, we also saw one situation
[[Bloom Filters](hash-set-kv.html##bloom-filters)] where we intentionally abandoned complete
reliability, replacing it with a statistical guarantee. In return,
this gave us (potentially) much higher performance.

Thus, sets provide a useful microcosm of computer science itself.
