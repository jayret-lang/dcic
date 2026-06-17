---
title: Recursion and Cycles from Mutation
section_number: 20
source_file: rec-from-mut.html
prev: state-in-pyret.html
up: booklet_advanced.html
next: cycle-detection.html
---

## 20 Recursion and Cycles from Mutation {#rec-from-mut}

Earlier [[From Acyclicity to Cycles](Sharing_and_Equality.html##acyc-to-cyc)], we saw the difficulty of
constructing cyclic data, and saw how we could address this problem
using state [[Cyclic Data](unified-cyclic-data.html)]. Let us now return to the
earlier example of creating a cyclic list of alternating colors. We
had tried to write:

```jayret
web-colors = link("white", link("grey", web-colors));
```
which, as we noted, does not pass muster because `web-colors`{.pyret} is
not bound on the right of the `=`{.pyret}. (Why not? Because otherwise,
if we try to substitute `web-colors`{.pyret} on the right, we would end
up in an infinite regress.)

Something about this should make you a little suspicious: we have been
able to write recursive functions all the time, without
difficulty. Why are they different? For two reasons:


- The first reason is the fact that we’re defining a
  function. A function’s body is not evaluated right away—only
  when we apply it—so the language can wait for the body to finish
  being defined. (We’ll see what this might mean in a moment.)
- The second reason isn’t actually a reason: function definitions
  actually are special. But we are about to expose what’s so special
  about them—it’s the use of a box! [[Boxes: A Canonical Mutable Structure](state-in-pyret.html##boxes)]—so that any
  definition can avail of it.

Returning to our example above, recall that we can’t make up our list
using `link`{.pyret}s, because we want the list to never
terminate. Therefore, let us first define a new datatype to hold an
cyclic list:

```jayret
data Pair {
}
```
You should think of this as analogous to a list, where `hd`{.pyret} is
the first element and `tl`{.pyret} is the rest.

Observe that we have carefully avoided writing type definitions for
the fields; we will instead try to figure them out as we go
along. Also, however, this definition as written cannot work.

::: {.do-now}
Do you see why not?
:::

Let’s decompose the intended infinite list into two pieces: lists that
begin with white and ones that begin with grey. What follows white? A
grey list. What follows grey? A white list. It is clear we can’t write
down these two definitions because one of them must precede the other,
but each one depends on the other. (This is the same problem as trying
to write a single definition above.)

### 20.1 Partial Definitions {#Partial-Definitions}

What we need to instead do is to partially define each list,
and then complete the definition using the other one. However,
that is impossible using the above definition, because we cannot
change anything once it is constructed. Instead, therefore, we need:

```jayret
data Pair {
}
```
Note that this datatype lacks a base case, which should remind you of
definitions we saw in [Streams From Functions](func-as-data.html##streams-from-funs).

Using this, we can define:

```jayret
white-pair = p("white", "dummy");
grey-pair = p("grey", "dummy");
```
Each of these definitions is quite useless by itself, but they each
represent what we want, and they have a mutable field for the
rest, currently holding a dummy value. Therefore, it’s clear what we
must do next: update the mutable field.

```jayret
white-pair ! {tl grey-pair }
grey-pair ! {tl white-pair }
```
Because we have ordained that our colors must alternate beginning with
white, this rounds up our definition:

```jayret
web-colors = white-pair;
```
If we ask Jayret to inspect the value of `web-colors`{.pyret}, we notice
that it employs an algorithm to prevent traversing infinite
objects. You can learn more about how that works separately
[[Detecting Cycles](cycle-detection.html)].

We can define a helper function, `take`{.pyret}, a variation of
which we saw for streams [[Streams From Functions](func-as-data.html##streams-from-funs)], to inspect a
finite prefix of an infinite list:

```jayret
List ctake(int n, Pair il) {
    return if (n == 0) {
        return empty;
    } else {
        return link(il.hd, ctake(n - 1, il ! tl));
    }
}
```
such that:

```jayret
@Check void test() {
    assertEquals(ctake(4, web-colors), ["white", "grey", "white", "grey"]);
}
```

### 20.2 Recursive Functions {#rec-for-recursive}

Based on this, we can now understand recursive functions. Consider a
very simple example, such as this:

```jayret
Object sum(n) {
    return if (n > 0) {
        return n + sum(n - 1);
    } else {
        return 0;
    }
}
```
We might like to think this is equivalent to:

```jayret
sum = (n) -> if (n > 0) {
    return n + sum(n - 1);
} else {
    return 0;
}
```
but if you enter this, Jayret will complain that `sum`{.pyret} is not
bound. We must instead write

```jayret
rec sum = (n) -> if (n > 0) {
    return n + sum(n - 1);
} else {
    return 0;
}
```
What do you think `rec`{.pyret} does? It binds `sum`{.pyret} to a box
initially containing a dummy value; it then defines the function in
an environment where the name is bound, unboxing the use of the name;
and finally, it replaces the box’s content with the defined function,
following the same pattern we saw earlier for `web-colors`{.pyret}.

### 20.3 Premature Evaluation {#premature-eval}

Observe that the above description reveals that there is a time
between the creation of the name and the assignment of a value to
it. Can this intermediate state be observed? It sure can!

There are generally three solutions to this problem:


1. Make sure the value is sufficiently obscure so that it can never
  be used in a meaningful context. This means values like 0 are
  especially bad, and indeed most common datatypes should be
  shunned. Indeed, there is no value already in use that can be used
  here that might not be confusing in some context.
2. The language might create a new type of value just for use
  here. For instance, imagine this definition of `CList`{.pyret}:
  
  ```jayret
data CList {
    Undef;
    Clink(v, ref r);
}
  ```
  `undef`{.pyret} appears to be a “base case”, thus
  making `CList`{.pyret} very similar to `List`{.pyret}. In truth, however,
  the `undef`{.pyret} is present only until the first mutation happens,
  after which it will never again be present: the intent is that
  `r`{.pyret} only contain a reference to other `clink`{.pyret}s.
  
  The `undef`{.pyret} value can now be used by the language to check for
  premature uses of a cyclic list. However, while this is
  technically feasible, it imposes a run-time penalty. Therefore, this
  check is usually only performed by languages focused on teaching;
  professional programmers are assumed to be able to manage the
  consequences of such premature use by themselves.
3. Allow the recursion constructor to be used only in the case of
  binding functions, and then make sure that the right-hand side of the
  binding is syntactically a function. This solution precludes some
  reasonable programs, but is certainly safe.

### 20.4 Cyclic Lists Versus Streams {#Cyclic-Lists-Versus-Streams}

The color list example above is, as we have noted, very reminiscent of
stream examples. What is the relationship between the two ways of
defining infinite data?

Cyclic lists have on their side simplicity. The pattern of definition
used above can actually be encapsulated into a language construct,
so programmers do not
need to wrestle with mutable fields (as above) or thunks (as streams
demand). This simplicity, however, comes at a price: cyclic lists can
only represent strictly repeating data, i.e., you cannot define
`nats`{.pyret} or `fibs`{.pyret} as cyclic lists. In contrast, the function
abstraction in a stream makes it generative: each invocation
can create a truly novel datum (such as the next natural or Fibonacci
number). Therefore, it is straightforward to implement cyclic lists as
streams, but not vice versa.
