---
title: Representing Sets as Lists
section_number: 18.1
source_file: sets-from-lists.html
prev: part_sets.html
up: part_sets.html
next: sets-from-trees.html
---

```{=html}
<a name="(part._sets-from-lists)"></a>
```

### 18.1 Representing Sets as Lists {#sets-from-lists}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-from-lists.html#%28part._.Representation_.Choices%29">18.1.1<span class="hspace"> </span>Representation Choices</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-from-lists.html#%28part._.Time_.Complexity%29">18.1.2<span class="hspace"> </span>Time Complexity</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-from-lists.html#%28part._choosing-set-reps%29">18.1.3<span class="hspace"> </span>Choosing Between Representations</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-from-lists.html#%28part._.Other_.Operations%29">18.1.4<span class="hspace"> </span>Other Operations</a></p></td></tr></table>
```

Earlier [[Sets as Collective Data](Collections_of_Structured_Data.html##sets-as-collections)] we introduced sets. Recall
that the elements of a set have no specific order, and ignore
duplicates.[If these ideas are not familiar, please read
[Sets as Collective Data](Collections_of_Structured_Data.html##sets-as-collections), since they will be important when
discussing the representation of sets.]{.margin-note} At that time we relied on
Jayret’s built-in representation of sets. Now we will discuss how to
build sets for ourselves. In what follows, we will focus only on sets
of numbers.

We will start by discussing how to represent sets using
lists. Intuitively,
using lists to represent sets of data seems problematic,
because lists respect both order and duplication. For
instance,

```jayret
@Check void test() {
    assertEquals([1, 2, 3], [3, 2, 1, 1]);
}
```
fails, but the corresponding sets are equal.

In principle, we want sets to obey the following
interface:[Note that a type called `Set`{.pyret} is already
built into Jayret, so below we will use the name `LSet`{.pyret} for a set
represented as a list.]{.margin-note}
<set-operations> ::=
```jayret
/* contract: mt-set :: Object */;
/* contract: is-in :: Object */;
/* contract: insert :: Object */;
/* contract: union :: Object */;
/* contract: size :: Object */;
/* contract: to-list :: Object */;
```
We may also find it also useful to have functions such as

```jayret
/* contract: insert-many :: Object */;
```
which, combined with `mt-set`{.pyret}, easily gives us a `to-set`{.pyret}
function.

Sets can contain many kinds of values, but not necessarily any kind:
we need to be able to check for two values being equal (which is a
requirement for a set, but not for a list!), which can’t
be done with all values (such as functions). We discuss the nuances of
this elsewhere [[Equality and Ordering](orderability.html##eq-ord)]. For now, we can ignore these
issues by focusing on sets of (non-rough)numbers.

```{=html}
<a name="(part._Representation-Choices)"></a>
```

#### 18.1.1 Representation Choices {#Representation-Choices}

The empty list can stand in for the empty set—

```jayret
type LSet = List;
mt-set = empty;
```
—and we can presumably define `size`{.pyret} as

```jayret
int size(LSet<Object> s) {
    return s.length();
}
```
However, this [☛ reduction](glossary.html#%28elem._glossary-reduction%29) (of sets to lists) can be
dangerous:


1. There is a subtle difference between lists and sets. The list
  
  ```jayret
[1, 1];
  ```
  is not the same as
  
  ```jayret
[1];
  ```
  because the first list has length two whereas the second has length
  one. Treated as a set, however, the two are the same: they both have
  size one. Thus, our implementation of `size`{.pyret} above is incorrect
  if we don’t take into account duplicates (either during insertion or
  while computing the size).
2. We might falsely make assumptions about the order in which
  elements are retrieved from the set due to the ordering guaranteed
  provided by the underlying list representation. This might hide bugs
  that we don’t discover until we change the representation.

3. We might have chosen a set representation because we didn’t need
  to care about order, and expected lots of duplicate items. A list
  representation might store all the duplicates, resulting in
  significantly more memory use (and slower programs) than we expected.

To avoid these perils, we have to be precise about how we’re going to
use lists to represent sets. One key question (but not the only one,
as we’ll soon see [[Choosing Between Representations](sets-from-lists.html##choosing-set-reps)]) is what to do about duplicates. One
possibility is for `insert`{.pyret} to check whether an element is
already in the set and, if so, leave the representation unchanged;
this incurs a cost during insertion but avoids unnecessary duplication
and lets us use `length`{.pyret} to implement `size`{.pyret}. The other
option is to define `insert`{.pyret} as `link`{.pyret}—literally,

```jayret
insert = link;
```
—and have some other procedure perform the filtering of duplicates.

```{=html}
<a name="(part._Time-Complexity)"></a>
```

#### 18.1.2 Time Complexity {#Time-Complexity}

What is the complexity of this representation of sets? Let’s consider
just `insert`{.pyret}, `is-in`{.pyret}, and `size`{.pyret}.
Suppose the size of the set is \(k\) (where, to avoid ambiguity,
we let \(k\) represent the number of distinct elements).
The complexity of these operations depends on whether or not we store
duplicates:


- If we don’t store duplicates, then `size`{.pyret} is simply
  `length`{.pyret}, which takes time linear in \(k\). Similarly,
  `is-in`{.pyret} only needs to traverse the list once to determine whether
  or not an element is present, which also takes time linear in
  \(k\). But `insert`{.pyret} needs to check whether an element is
  already present, which takes time linear in \(k\), followed by
  at most a constant-time operation (`link`{.pyret}).

- If we do store duplicates, then `insert`{.pyret} is constant
  time: it simply `link`{.pyret}s on the new element without regard to
  whether it already is in the set representation. `is-in`{.pyret}
  traverses the list once, but the number of elements it needs to visit
  could be significantly greater than \(k\), depending on how many
  duplicates have been added. Finally, `size`{.pyret} needs to check
  whether or not each element is duplicated before counting it.

::: {.do-now}
What is the time complexity of `size`{.pyret} if the list has duplicates?
:::

One implementation of `size`{.pyret} is

```jayret
int size(LSet<Object> s) {
    return switch (s) {
        case Empty: yield 0;
        case Link(f, r): yield if (r.member(f)) {
            return size(r);
        } else {
            return 1 + size(r);
        };
    }
}
```

Let’s now compute the complexity of the body of the function, assuming
the number of distinct elements in `s`{.pyret} is \(k\) but the
actual number of elements in `s`{.pyret} is \(d\), where
\(d \geq k\). To compute the time to run `size`{.pyret} on \(d\)
elements, \(T(d)\), we should determine the number of operations in
each question and answer. The first question has a constant number of
operations,
and the first answer also a constant. The second question also has
a constant number of
operations. Its answer is a conditional, whose first question
(`r.member(f)`{.pyret} needs to traverse the entire list, and hence has
\(O([k \rightarrow d])\) operations. If it succeeds, we recur on something of size
\(T(d-1)\); else we do the same but perform a constant more operations.
Thus \(T(0)\) is a constant, while the recurrence (in big-Oh terms) is
\begin{equation*}T(d) = d + T(d-1)\end{equation*}Thus \(T \in O([d \rightarrow d^2])\).
Note that this is quadratic in the number of elements in the
list, which may be much bigger than the size of the
set.

```{=html}
<a name="(part._choosing-set-reps)"></a>
```

#### 18.1.3 Choosing Between Representations {#choosing-set-reps}

Now that we have two representations with different complexities, it’s
worth thinking about how to choose between them. To do so, let’s build
up the following table. The table distinguishes between the
interface (the set) and the implementation (the list),
because—owing to duplicates in the representation—these two may
not be the same. In the table we’ll consider just two of the most
common operations, insertion and membership checking:

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p> </p></td><td><p><span class="hspace">  </span></p></td><td colspan="3"><p><span style="font-weight: bold">With Duplicates</span></p></td><td><p><span class="hspace">  </span></p></td><td colspan="3"><p><span style="font-weight: bold">Without Duplicates</span></p></td></tr><tr><td><p> </p></td><td><p><span class="hspace">  </span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">insert</code></span></p></td><td><p><span class="hspace">  </span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">is-in</code></span></p></td><td><p><span class="hspace">  </span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">insert</code></span></p></td><td><p><span class="hspace">  </span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">is-in</code></span></p></td></tr><tr><td><p><span style="font-weight: bold">Size of Set</span></p></td><td><p><span class="hspace">  </span></p></td><td><p>constant</p></td><td><p><span class="hspace">  </span></p></td><td><p>linear</p></td><td><p><span class="hspace">  </span></p></td><td><p>linear</p></td><td><p><span class="hspace">  </span></p></td><td><p>linear</p></td></tr><tr><td><p><span style="font-weight: bold">Size of List</span></p></td><td><p><span class="hspace">  </span></p></td><td><p>constant</p></td><td><p><span class="hspace">  </span></p></td><td><p>linear</p></td><td><p><span class="hspace">  </span></p></td><td><p>linear</p></td><td><p><span class="hspace">  </span></p></td><td><p>linear</p></td></tr></table>
```
A naive reading of this would suggest that the representation with
duplicates is better because it’s sometimes constant and sometimes
linear, whereas the version without duplicates is always
linear. However, this masks a very important distinction: what the
linear means. When there are no duplicates, the size of the list is
the same as the size of the set. However, with duplicates, the size
of the list can be arbitrarily larger than that of the set!

Based on this, we can draw several lessons:


1. Which representation we choose is a matter of how much
  duplication we expect. If there won’t be many duplicates, then the
  version that stores duplicates pays a small extra price in return for
  some faster operations.

2. Which representation we choose is also a matter of how
  often we expect each operation to be performed. The representation
  without duplication is “in the middle”: everything is roughly equally
  expensive (in the worst case). With duplicates is “at the extremes”:
  very cheap insertion, potentially very expensive membership. But if we
  will mostly only insert without checking membership, and especially if
  we know membership checking will only occur in situations where we’re
  willing to wait, then permitting duplicates may in fact be the smart
  choice. (When might we ever be in such a situation? Suppose your set
  represents a backup data structure; then we add lots of data but very
  rarely—indeed, only in case of some catastrophe—ever need to look
  for things in it.)

3. Another way to cast these insights is that our form of analysis
  is too weak. In situations where the complexity depends so heavily on
  a particular sequence of operations, big-Oh is too loose and we should
  instead study the complexity of specific sequences of operations. We
  will address precisely this question later
  [[Halloween Analysis](amortized-analysis.html)].

Moreover, there is no reason a program should use only one
representation. It could well begin with one representation, then
switch to another as it better understands its workload. The only
thing it would need to do to switch is to convert all existing data
between the representations.

How might this play out above? Observe that data conversion is very
cheap in one direction: since every list without duplicates is
automatically also a list with (potential) duplicates, converting in
that direction is trivial (the representation stays unchanged, only
its interpretation changes). The other direction is harder: we have to
filter duplicates (which takes time quadratic in the number of
elements in the list). Thus, a program can make an initial guess about
its workload and pick a representation accordingly, but maintain
statistics as it runs and, when it finds its assumption is wrong,
switch representations—and can do so as many times as needed.

```{=html}
<a name="(part._Other-Operations)"></a>
```

#### 18.1.4 Other Operations {#Other-Operations}

::: {.exercise}
Implement the remaining operations catalogued above
([<set-operations>](sets-from-lists.html#%28elem._set-operations%29))
under each list representation.
:::

::: {.exercise}
Implement the operation

```jayret
/* contract: remove :: Object */;
```
under each list representation (renaming `Set`{.pyret} appropriately.
What difference do you see?
:::

::: {.do-now}
Suppose you’re asked to extend sets with these operations, as the set
analog of `first`{.pyret} and `rest`{.pyret}:

```jayret
/* contract: one :: Object */;
/* contract: others :: Object */;
```
You should refuse to do so! Do you see why?
:::

With lists the “first” element is well-defined, whereas sets are
defined to have no ordering. Indeed, just to make sure users of your
sets don’t accidentally assume anything about your implementation
(e.g., if you implement `one`{.pyret} using `first`{.pyret}, they may notice
that `one`{.pyret} always returns the element most recently added to the
list), you really ought to return a random element of the set on each
invocation.

Unfortunately, returning a random element means the above interface is
unusable. Suppose `s`{.pyret} is bound to a set containing `1`{.pyret},
`2`{.pyret}, and `3`{.pyret}. Say the first time `one(s)`{.pyret} is invoked
it returns `2`{.pyret}, and the second time `1`{.pyret}. (This already
means `one`{.pyret} is not a function.)
The third time it may again return `2`{.pyret}. Thus
`others`{.pyret} has to remember which element was returned the last time
`one`{.pyret} was called, and return the set sans that element. Suppose
we now invoke `one`{.pyret} on the result of calling `others`{.pyret}. That
means we might have a situation where `one(s)`{.pyret} produces the same
result as `one(others(s))`{.pyret}.

::: {.exercise}
Why is it unreasonable for `one(s)`{.pyret} to produce the same
result as `one(others(s))`{.pyret}?
:::

::: {.exercise}
Suppose you wanted to extend sets with a `subset`{.pyret} operation that
partitioned the set according to some condition. What would its type
be?
:::

::: {.exercise}
The types we have written above are not as crisp as they could
be. Define a `has-no-duplicates`{.pyret} predicate, refine the relevant
types with it, and check that the functions really do satisfy this
criterion.
:::
