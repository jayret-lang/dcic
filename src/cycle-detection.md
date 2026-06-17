---
title: Detecting Cycles
section_number: 21
source_file: cycle-detection.html
prev: rec-from-mut.html
up: booklet_advanced.html
next: avoid-recomp.html
---

## 21 Detecting Cycles {#cycle-detection}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="cycle-detection.html#%28part._.A_.Running_.Example%29">21.1<span class="hspace"> </span>A Running Example</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="cycle-detection.html#%28part._.Types%29">21.2<span class="hspace"> </span>Types</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="cycle-detection.html#%28part._.A_.First_.Checker%29">21.3<span class="hspace"> </span>A First Checker</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="cycle-detection.html#%28part._cyc-det-comp%29">21.4<span class="hspace"> </span>Complexity</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="cycle-detection.html#%28part._.A_.Fabulous_.Improvement%29">21.5<span class="hspace"> </span>A Fabulous Improvement</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="cycle-detection.html#%28part._.Testing%29">21.6<span class="hspace"> </span>Testing</a></p></td></tr></table>
```

### 21.1 A Running Example {#A-Running-Example}

As you may have noticed, Jayret will check for and print cycles. For instance,

```jayret
import lists as L
data Pair {
}
p0 = p(0, 0);
p1 = p(1, 1);
p2 = p(2, 3);
p3 = p(3, 4);
p2 ! {tl p3 }
p3 ! {tl p2 }
p4 = p(4, p3);
p5 = p(5, p4);
p6 = p(6, "dummy");
p6 ! {tl p6 }
```

::: {.do-now}
Sketch out the above pairs to make sure you see all the cycles.
:::

So we have two that participate in no cyclic behavior (`p0`{.pyret} and
`p1`{.pyret}), two (`p2`{.pyret} and `p3`{.pyret} that are mutually-cyclic, one
(`p6`{.pyret}) that is a self-cycle, and two (`p4`{.pyret} and `p5`{.pyret})
that lead to a cycle.

### 21.2 Types {#Types}

As an aside, imagine we try to type-check this program. We have to
provide a type for `tl`{.pyret}, but it’s not clear what this can be:
sometimes it’s a `Number`{.pyret}, and other times it’s a
`Pair`{.pyret}. However, we might observe that if our goal is to
create cyclic data, then we want `tl`{.pyret} to refer to a `Pair`{.pyret}
or to nothing at all. That suggests that a useful type is:

```jayret
data Pair {
}
```
so that we can write

```jayret
p0 = p(0, none);
p1 = p(1, none);
p2 = p(2, none);
p3 = p(3, none);
p2 ! {tl some(p3) }
p3 ! {tl some(p2) }
p4 = p(4, some(p3));
p5 = p(5, some(p4));
p6 = p(6, none);
p6 ! {tl some(p6) }
```
This works, but we have to deal with the `Option`{.pyret}
everywhere. Since our goal is to focus on cycles, and this would
become unwieldy, we ignore the typed version from now on.

### 21.3 A First Checker {#A-First-Checker}

Okay, back to the untyped version.

So let’s try to figure out whether, given a Pair, it leads to a cycle. What should the type be?

```jayret
/* contract: cc :: Object */;
```
where `cc`{.pyret} stands for “check cycle”.

Critically, it’s important that this be a total function: i.e., it always terminates.

So let’s write the most obvious solution:

```jayret
Object cc(e) {
    Object loop(cur, hist) {
        return if (is-p(cur)) {
            return if (L.member-identical(hist, cur)) {
                return true;
            } else {
                return loop(cur ! tl, link(cur, hist));
            }
        } else {
            return false;
        }
    }
    return loop(e, empty);
}
```
First of all, does this even terminate? It could take a while to visit
all the nodes, but a cycle demands that somewhere, we revisit a node
we saw before. Since we track that, we can’t not terminate. Therefore,
termination is guaranteed, and the function is total. Indeed, all
these tests pass:

```jayret
@Check void test() {
    assertEquals(cc(p0), false);
    assertEquals(cc(p1), false);
    assertEquals(cc(p2), true);
    assertEquals(cc(p3), true);
    assertEquals(cc(p4), true);
    assertEquals(cc(p5), true);
    assertEquals(cc(p6), true);
}
```

As another aside, observe that we could have written these tests instead like

```jayret
@Check void test() {
    assertViolates(p0, cc);
    assertSatisfies(p2, cc);
}
```
which would be more concise, but that would also be misleading: it
would suggest that `cc`{.pyret} is a desirable property, so `p2`{.pyret} is
a “good” instance and `p0`{.pyret} is a “bad” one. However, `cc`{.pyret}
is not a judgment of quality—its two responses have equal
weight—so this would be confusing to a later reader.

### 21.4 Complexity {#cyc-det-comp}

Now that we have determined that it terminates, we can ask for its
time and space complexity. First we have to decide what we are even
computing the complexity over. If the sequence is finite, then the
size is clearly the size of the sequence. But if it’s infinite, we
don’t want to traverse the “whole thing”: rather, we mean its finite
part (excluding any repetition). So the meaningful measure in either
case is the number of `p`{.pyret} nodes, i.e., the finite size. It may
just be that some of these lead back to themselves, so that a naïve
traversal will go on forever.

Okay, so we visit each node once. We keep track of all the nodes just
in case we double back over, either until we run out of nodes or we
repeat one. Therefore, the space complexity is linear in the length of
the sum of the prefix (from the starting node) and the cycle. The time
complexity is that but also, at each point, we have to check
membership, so it’s quadratic in the length of that prefix +
cycle. So: linear space, quadratic time, in the size of the prefix +
cycle.

Now, some degree of linear behavior is unavoidable: we clearly have to
keep going until we run out or hit a cycle, so for detecting the cycle
having something be linear in the size of the prefix (get it out of
the way) + length of the cycle (find the cycle) seems essential. But
can we improve on this complexity? It seems unlikely: by definition,
how can we check for a cycle if we don’t remember everything we’ve
seen?

Our first hunch might be, “Maybe there’s another space-time
tradeoff!” But it’s not so clear here. Our space is linear and time
quadratic, so we may think we can flip those around. But the time
can’t be less than the space! If, for instance, we had linear time and
quadratic space, that wouldn’t make sense, because we’d need at least
quadratic time just to fill the space. So that’s not going to work so
well.

Instead, the best way to improve seems to have a better lookup data
structure. We’d still take linear space—as we said, linear was
unavoidable (and we can’t just be linear in the size of the cycle,
because the whole point is we don’t even know we have a cycle, much
less which parts are prefix and which parts cycle)—and the time
complexity would hopefully reduce from quadratic to
linear-times-something-sublinear.

### 21.5 A Fabulous Improvement {#A-Fabulous-Improvement}

It turns out we can do a lot better! It’s called the tortoise-and-hare
algorithm.

We start off with two references into the sequence, one called the
tortoise and the other the hare.

At each step, the tortoise tries to advance by one node. If it cannot,
we’ve run out of sequence, and we’re done. The hare, being a hare and
not a tortoise, tries to advance by two nodes. Again, if it cannot,
we’ve run out of sequence, and we’re done. Otherwise both advance, and
check if they’re at the same place. If they are, because they started
out being at distinct nodes, we’ve found a cycle! If they are not,
then we iterate.

Why does this even work? In the finite case it’s clear, because the
hare will run out of next nodes. We only have to think about the
infinite case. There, in general, we have this kind of situation:

![](cycle-rho.png)

There is some prefix of nodes, followed by a cycle. Now, we don’t know
how long the prefix is, so we don’t know how far ahead of the tortoise
the hare is. Nevertheless, there is some first point at which the
tortoise enters the cycle. (There must be, because the tortoise always
makes progress, and the prefix can only be finite.) From this point
on, we know that on each step, the relative speed of the two animals
is 1. That means the hare “gains” 1 on the tortoise every step. We
can see that eventually, the hare must catch up with the
tortoise—or, alternatively, that the tortoise catches up with the
hare!

Now let’s analyze this. The tortoise will get caught by the time it
has completed one loop of the cycle. Because the tortoise moves one
step at a time, the total time is the length of the prefix + length of
the loop. In terms of space, however, we no longer need any history at
all; we only need the current positions of the tortoise and
hare. Therefore, our time complexity is linear, but the space
complexity is now significantly smaller: down to constant!

Here is the code:

```jayret
Object th(e) {
    Object loop(tt, hr) {
        return if (tt <=> hr) {
            return true;
        } else {
            return if (is-p(tt) && is-p(hr)) {
                new-tt = tt ! tl;
                int-hr = hr ! tl;
                return if (is-p(int-hr)) {
                    new-hr = int-hr ! tl;
                    return loop(new-tt, new-hr);
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
    }
    return loop(e, e ! tl);
}
```

### 21.6 Testing {#Testing}

While it might be tempting to write tests like

```jayret
@Check void test() {
    assertEquals(cc(p0), false);
    assertEquals(cc(p2), true);
}
```
(i.e., the same as before, but with `cc`{.pyret} replaced by `ph`{.pyret}), we should instead write them as follows:

```jayret
@Check void test() {
    assertEquals(cc(p0), th(p0));
    assertEquals(cc(p1), th(p1));
    assertEquals(cc(p2), th(p2));
    assertEquals(cc(p3), th(p3));
    assertEquals(cc(p4), th(p4));
    assertEquals(cc(p5), th(p5));
    assertEquals(cc(p6), th(p6));
}
```

This confers two advantages. First, if we change the example, we don’t
have to update two tests, only one. But the much more important reason
is that we intend for `pr`{.pyret} to be an optimized version of
`cc`{.pyret}. That is, we expect the two to produce the same result. We
can think of `cc`{.pyret} as our clear, reference implementation. That
is, this is another instance of model-based testing.

As an aside, this algorithm is not exactly what Jayret does, because we
need to check for arbitrary graph-ness, not just cycles. It’s also
complicated due to user-defined functions, etc.
