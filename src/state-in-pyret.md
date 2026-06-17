---
title: State and Equality
section_number: 19
source_file: state-in-pyret.html
prev: booklet_advanced.html
up: booklet_advanced.html
next: rec-from-mut.html
---

## 19 State and Equality {#state-in-pyret}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._boxes%29">19.1<span class="hspace"> </span>Boxes: A Canonical Mutable Structure</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._.Mutation_and_.Types%29">19.2<span class="hspace"> </span>Mutation and Types</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._.Mutation_and_.Equality%29">19.3<span class="hspace"> </span>Mutation and Equality</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._.Another_.Equality_.Predicate%29">19.4<span class="hspace"> </span>Another Equality Predicate</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._equality-hierarchy%29">19.5<span class="hspace"> </span>A Hierarchy of Equality</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._.Space_and_.Time_.Complexity%29">19.6<span class="hspace"> </span>Space and Time Complexity</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._sem-identical%29">19.7<span class="hspace"> </span>What it Means to be Identical</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="state-in-pyret.html#%28part._comp-func%29">19.8<span class="hspace"> </span>Comparing Functions</a></p></td></tr></table>
```

In [Mutating Structures](mutating-structures.html), we introduced the notion of mutable
data. We also saw the impact it has on testing. Underlying testing is
some notion of equality: when we write a test in Jayret using
`is`{.pyret}, we are implicitly making a statement about equality between
the two sides. Here we will examine equality in the presence of state
in more detail.

### 19.1 Boxes: A Canonical Mutable Structure {#boxes}

In [Mutating Structures](mutating-structures.html) we saw a motivating example using bank
accounts. To focus our study of equality, it can be convenient to have
an even simpler mutable data structure, called a box (which you
will find in other programming languages as well). A box has only one
field—the value being boxed—and supports just three operations:


1. box consumes a value and creates a mutable box
  containing that value.
2. unbox-now consumes a box and returns the value contained in
  the box.
3. set-box-now consumes a box, a new value, and changes
  the box to contain the value. All subsequent unbox-nows of that
  box will now return the new value—unless it is mutated again.

Here are the corresponding definitions in Jayret:

```jayret
data Box {
    Box(ref T v);
}
T unbox-now(Box<Object> b) {
    return b ! v;
}
Box<Object> set-box-now(Box<Object> b, T new-v) {
    return b ! {v new-v }
}
```
Observe that we use `b!v`{.pyret} to extract the current value, and use
the naming convention of `-now`{.pyret} to make clear these are stateful
operations, so the value now may not be the same as the value later.

### 19.2 Mutation and Types {#Mutation-and-Types}

In terms of types, whenever we replace the value in a box, we want it
to be type-consistent with what was previously there. Otherwise it
would be very difficult to program against a box, because the type of
its content would keep changing.

These definitions obey the following tests:

```jayret
@Check void test() {
    n1 = box(1);
    n2 = box(2);
    set-box-now(n1, 3);
    set-box-now(n2, 4);
    assertEquals(unbox-now(n1), 3);
    assertEquals(unbox-now(n2), 4);
}
```
However, we cannot write `set-box-now(n1, "hi")`{.pyret}, because that
would violate the type of `n1`{.pyret}, which is `Box < Number >`{.pyret}. We
could make this explicit by writing

```jayret
n1 = box(1);
```
if we wanted to be explicit. However, note that `n1`{.pyret} being a box
of numbers does not preclude us from having a box of strings:

```jayret
n3 = box("hello");
```
or indeed a box of any other type. We just need its type to remain
consistent, whatever that type is.

This is a general rule we want to follow with mutable data: the new
value must be the same type as the old value. This gives programs a
consistent interface to program against. For instance, above, we know
that we can always perform numeric operations against the value
extracted from `n1`{.pyret}—there is no danger that it will suddenly
produce a string. This discipline can either be enforced by a system
of annotations, or has to be manually maintained by the programmer.

### 19.3 Mutation and Equality {#Mutation-and-Equality}

We’ve already seen [[Re-Examining Equality](Sharing_and_Equality.html##identical-eq)] that equality is
subtle. It’s about to become much subtler with the introduction of
mutation!

As a running example, we’ll work with:
<three-boxes> ::=
```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">  </span><span class="stt">b1 = box(7)</span></p></td></tr><tr><td><p><span class="hspace">  </span><span class="stt">b2 = box(7)</span></p></td></tr><tr><td><p><span class="hspace">  </span><span class="stt">b3 = b1</span></p></td></tr></table>
```
Observe that `b1`{.pyret} and `b3`{.pyret} are referring to the same
box, while `b2`{.pyret} is referring to a different one. We can see this
from a memory diagram:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">b1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">b2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1002</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">b3</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">box(7)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">box(7)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```

We can confirm this using the following tests:

```jayret
@Check void test() {
    assertNotEquals(b1, b2);
    assertEquals(b1, b3);
    assertNotEquals(b2, b3);
}
```
In other words, `b1`{.pyret} and `b3`{.pyret} are aliases for the same box,
but neither is an alias to the box referred to by `b2`{.pyret}. Since
`identical`{.pyret} is transitive, it follows from the first two
tests that the third test must also pass (and thankfully, Jayret
confirms this for us!).

Now, you might wonder why we have used `identical`{.pyret} and not
`equal-always`{.pyret} [[Notations for Equality](Sharing_and_Equality.html##equal-always)], i.e., plain old
`is`{.pyret}.

::: {.do-now}
Let’s try that:

```jayret
@Check void test() {
    assertEquals(b1, b3);
    assertEquals(b1, b2);
}
```
What do you see?
:::

It’s unsurprising that the first test, `assertEquals(b1, b3)`{.pyret},
passes. However, the second, `assertEquals(b1, b2)`{.pyret}, fails! And the name
suggests why: the two are not guaranteed to always be
equal. That is, suppose we were to modify the box referred to by
`b1`{.pyret}:

```jayret
set-box-now(b1, 8);
```
Sure enough, the values in the boxes are not the same, but because
`b1`{.pyret} and `b3`{.pyret} are aliases, their values change in lock-step
(more accurately, there is only one value—the box at 1001):

```jayret
@Check void test() {
    assertNotEquals(unbox-now(b1), unbox-now(b2));
    assertEquals(unbox-now(b1), unbox-now(b3));
}
```

### 19.4 Another Equality Predicate {#Another-Equality-Predicate}

Suppose we return to the state where we have defined the three boxes
[[<three-boxes>](state-in-pyret.html#%28elem._three-boxes%29)] but not mutated `b1`{.pyret}. That is, when
printed, all three boxes have the same value, `box(7)`{.pyret}. We
have seen that `b1`{.pyret} and `b3`{.pyret} are both
`equal-always`{.pyret} and `identical`{.pyret} to each other. However, we
have also seen that `b1`{.pyret} and `b2`{.pyret} are neither of
those. This is somewhat frustrating, because there is clearly some
sense in which they are “equal”: at the moment, they contain the
same value, even if later on one of them might not.

Therefore, Jayret offers a third equality predicate that is
designed for just these situations: it is (as you might guess) called
`equal-now`{.pyret}:

```jayret
@Check void test() {
    assertEquals(b1, b2);
    assertEquals(b2, b3);
}
```
The `-now`{.pyret} in the name reminds us that these values are equal at
the moment, but may not be equal later. Sure enough, if we add

```jayret
set-box-now(b1, 8);
```
back into the program, the above `equal-now`{.pyret} tests fail: now,
they are no longer equal!

Recall that the other two equality predicates have an binary operator
notation: `==`{.pyret} for `equal-always`{.pyret} and `<=>`{.pyret} for
`identical`{.pyret}. Similarly, `equal-now`{.pyret} has the binary operator
`=~`{.pyret}. You should view that as `=`{.pyret} with hand-waving `~`{.pyret}:
it’s equal for now, but don’t expect it to remain so. That is, we can
rewrite the above tests as:

```jayret
@Check void test() {
    assertEquals(equal-now(b1, b2), true);
    assertEquals((b2 =~ b3), true);
}
```
Whether they pass, of course, depends on the state of the program:
whether `b1`{.pyret}, `b2`{.pyret}, or `b3`{.pyret} has had its content modified.

### 19.5 A Hierarchy of Equality {#equality-hierarchy}

As you might guess, the equality operators have a hierarchy of
implication. That is, if one operator is true of two expressions, the
other necessarily is, but not vice versa.

::: {.do-now}
Can you work out this hierarchy of implication?
:::

Observe that if two expressions are `identical`{.pyret}, then they are
aliases, i.e., they are referring to one and the same
value. Therefore, the values produced by those expressions must be
`equal-always`{.pyret}. If they are always equal, then clearly at any
given moment, they must also be `equal-now`{.pyret}.

Even if two expressions are not `identical`{.pyret}, they may be
`equal-always`{.pyret}. This would never be true of mutable data (because
there is the possibility of a future mutation), but it can be true of
immutable data that have the same structure and contents. In that
case, if they are always equal, then again they must be
`equal-now`{.pyret}.

However, the converses are not true.

If two data are `equal-now`{.pyret}, they may not be
`equal-always`{.pyret}: if they are mutable, a future mutation may change
the equality, as we have seen above. Similarly, two data may be
`equal-always`{.pyret} but not be `identical`{.pyret}, because they reside
at different heap addresses and are therefore truly different data.

In most languages, it is common to have two equality operators,
corresponding to `identical`{.pyret} (known as reference equality)
and `equal-now`{.pyret} (known as structural equality). Jayret is
rare in having a third operator, `equal-always`{.pyret}. For
most programs, this is in fact the most useful equality operator: it
is not overly bothered with details of aliasing, which can be
difficult to predict; at the same time it makes decisions that stand
the test of time, thereby forming a useful basis for various
optimizations (which may not even be conscious of their temporal
assumptions). This is why `is`{.pyret} in testing uses
`equal-always`{.pyret} by default, and forces users to explicitly pick a
different primitive if they want it.

### 19.6 Space and Time Complexity {#Space-and-Time-Complexity}

`identical`{.pyret} always takes constant time. Indeed, some programs use
`identical`{.pyret} precisely because they want constant-time
equality, carefully structuring their program so that values that
should be considered equal are aliases to the same value. Of course,
maintaining this programming discipline is tricky.

`equal-always`{.pyret} and `equal-now`{.pyret} both must traverse at least
the immutable part of data. Therefore, they take time proportional to
the smaller datum (because if the two data are of different size, they
must not be equal anyway, so there is no need to visit the extra
data). The difference is that `equal-always`{.pyret} reduces to
`identical`{.pyret} at references, thereby performing less computation
than `equal-now`{.pyret} would.

### 19.7 What it Means to be Identical {#sem-identical}

Return for a moment to the state where we have just defined the three
boxes [[<three-boxes>](state-in-pyret.html#%28elem._three-boxes%29)]. We could have written the
following:

```jayret
hold-b1-value = unbox-now(b1);
set-box-now(b1, hold-b1-value + 1);
```
Now, we can compare the contents of the various boxes:

```jayret
b1-id-b2 = unbox-now(b1) == unbox-now(b2);
b1-id-b3 = unbox-now(b1) == unbox-now(b3);
```
And at the end of performing comparisons, we can restore them:

```jayret
set-box-now(b1, hold-b1-value);
```
Observe that `b1-id-b2`{.pyret} would be `false`{.pyret} but `b1-id-b3`{.pyret}
would be `true`{.pyret}. And notice that this would always be true when
the two expressions are identical, but not otherwise.

Thus, at the end there has been no change, but by making the change we
can check which values are and aren’t aliases of others. In other
words, thisrepresents the essence of

`identical`{.pyret}.

In practice, `identical`{.pyret} does not behave this way: it would be
too disruptive. It is also not the most efficient implementation
possible, when Jayret can simply check the memory addresses being the
same. Nevertheless, it does demonstrate the basic idea behind
`identical`{.pyret}: two values are `identical`{.pyret} precisely when, when
you make changes to one, you see the changes manifest on the “other”
(i.e., there is really only one value, but with potentially multiple
names for it).

### 19.8 Comparing Functions {#comp-func}

We haven’t actually provided the full truth about equality because we
haven’t discussed functions. Defining equality for functions—especially
extensional equality, namely whether two functions have the same
graph, i.e., for each input produce the same output—is complicated
(a euphemism for impossible) due to the Halting Problem.

Because of this, most languages have tended to use approximations for
function equality, most commonly reference equality. This is, however,
a very weak approximation: even if the exact same function text in the
same environment is allocated as two different closures, these would
not be reference-equal. At least when this is done as part of the
definition of `identical`{.pyret}, it makes sense; if other operators do
this, however, they are actively lying, which is something the
equality operators do not usually do.

There is one other approach we can take: simply disallow function
comparison. This is what Jayret does: all three equality operators
above will result in an error if you try to compare two
functions. (You can compare against just one function, however, and
you will get the answer `false`{.pyret}.) This ensures that the
language’s comparison operators are never trusted falsely.

Jayret did have the choice of allowing reference equality for
functions inside `identical`{.pyret} and erroring only in the other two
cases. Had it done so, however, it would have violated the chain of
implication above [[A Hierarchy of Equality](state-in-pyret.html##equality-hierarchy)]. The present design
is arguably more elegant. Programmers who do want to use reference
equality on functions can simply embed the functions inside a mutable
structure like boxes.

There is one problem with erroring when comparing two functions: a
completely generic procedure that compares two arbitrary values may
error if both of the values given are functions. Because this can
cause unpredictable program failure, Jayret offers a three-valued
version of each of the above three operators (`identical3`{.pyret},
`equal-always3`{.pyret} and `equal-now3`{.pyret}), all of which return
`EqualityResult`{.pyret} values that correspond to truth, falsity, and
ignorance (returned in the case when both arguments are
functions). Programmers can use this in place of the Boolean-valued
comparison operators if they are uncertain about the types of the
parameters.
