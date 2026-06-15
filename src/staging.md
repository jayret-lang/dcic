---
title: Staging
section_number: 24
source_file: staging.html
prev: partial-domains.html
up: booklet_advanced.html
next: factoring-numbers.html
---

## Staging {#staging}

### Problem Definition {#Problem-Definition}

Earlier, we saw a detailed development of binary trees representing ancestry
[[Creating a Datatype for Ancestor Trees](trees.html##ancestor-tree)]. In what follows we don’t need a lot of detail, so
we will give ourselves a simplified version of essentially the same data definition:

```pyret
data ABT:
  | unknown
  | person(name :: String, bm :: ABT, bf :: ABT)
end
```
We can then write functions over such as this:

```pyret
fun abt-size(p :: ABT):
  doc: "Compute the number of known people in the ancestor tree"
  cases (ABT) p:
    | unknown => 0
    | person(n, p1, p2) => 1 + abt-size(p1) + abt-size(p2)
  end
end
```

Now let’s think about a slightly different function:
`how-many-named`{.pyret}, which tells us how many people in a family have
a particular name. Not only can more than one person have the same
name, in some cultures it’s not uncommon to use the same name
across generations, either in successive generations or skipping one.

::: {.do-now}
What is the contract for `how-many-named`{.pyret}? The contract for this function
will be crucial, so make sure you do this step!
:::

Here is one meaningful contract:

```pyret
how-many-named :: ABT, String -> Number
```
It takes a tree in which to search, a name to search for, and returns a count.

::: {.do-now}
Define `how-many-named`{.pyret}.
:::

### Initial Solution {#Initial-Solution}

Presumably you ended up with something like this:

```pyret
fun how-many-named(p, looking-for):
  cases (ABT) p:
    | unknown => 0
    | person(n, p1, p2) =>
      if n == looking-for:
        1 + how-many-named(p1, looking-for) + how-many-named(p2, looking-for)
      else:
        how-many-named(p1, looking-for) + how-many-named(p2, looking-for)
      end
  end
end
```
Let’s say you have defined this person:

```pyret
p =
  person("A",
    person("B",
      person("A", unknown, unknown),
      person("C",
        person("A", unknown, unknown),
        person("B", unknown, unknown))),
    person("C", unknown, unknown))
```
With that, we can write a test like

```pyret
check:
  how-many-named(p, "A") is 3
end
```

### Refactoring {#Refactoring}

Now let’s apply some transformations, sometimes called code refactorings,
to this function.

First, notice the repeated expression. What the whole conditional is
essentially saying is that we want to know how much this person is contributing
to the overall count; the rest of the count stays the same regardless.

One way to make this more explicit is to (perhaps surprisingly)
rewrite the `else`{.pyret} to make explicit that a person with a
different name contributes `0`{.pyret} to the count:

```pyret
fun how-many-named(p, looking-for):
  cases (ABT) p:
    | unknown => 0
    | person(n, p1, p2) =>
      if n == looking-for:
        1 + how-many-named(p1, looking-for) + how-many-named(p2, looking-for)
      else:
        0 + how-many-named(p1, looking-for) + how-many-named(p2, looking-for)
      end
  end
end
```
The reason for this somewhat odd rewrite is that it makes clear what
is common and what is different. What is common is looking in the two
parents. What changes is how much this person contributes, and only
that depends on the conditional. We can therefore express this
more concisely (and, if we know how to read such code,
more meaningfully) as the following instead:

```pyret
fun how-many-named(p, looking-for):
  cases (ABT) p:
    | unknown => 0
    | person(n, p1, p2) =>
      (if n == looking-for: 1 else: 0 end)
      +
      how-many-named(p1, looking-for) +
      how-many-named(p2, looking-for)
  end
end
```
If you have prior programming experience, this may look a bit odd to you, but
`if`{.pyret} is in fact an expression, which has a value; in this case the value
is either `0`{.pyret} or `1`{.pyret}. This value can then be used in an addition.

Now let’s look at this code even more closely. Notice something interesting. We
keep passing two parameters to `how-many-named`{.pyret}; however, only one of
those parameters (`p`{.pyret}) is actually changing. The name we are
looking for does not change, as we would expect: we are looking for the same
name in the entire tree. How can we reflect this in the code?

First, we’ll do something that looks a little useless, but it’s also an
innocent change, so it shouldn’t irk us too much: we’ll change the order of the
arguments. That is, our contract changes from

```pyret
how-many-named :: ABT, String -> Number
```
to

```pyret
how-many-named :: String, ABT -> Number
```
so the function correspondingly changes to

```pyret
fun how-many-named(looking-for, p):
  cases (ABT) p:
    | unknown => 0
    | person(n, p1, p2) =>
      (if n == looking-for: 1 else: 0 end)
      +
      how-many-named(p1, looking-for) +
      how-many-named(p2, looking-for)
  end
end
```

What we have now done is put the “constant” argument first, and the
“varying” argument second.

::: {.do-now}
Try this and make sure it works!
:::

It doesn’t! We have to change more than
just the function header: we have to also change how it’s called. Keep
in mind it’s called twice within the function body itself, and also
from the examples. Therefore, the function as a whole reads:

```pyret
fun how-many-named(looking-for, p):
  cases (ABT) p:
    | unknown => 0
    | person(n, p1, p2) =>
      (if n == looking-for: 1 else: 0 end)
      +
      how-many-named(looking-for, p1) +
      how-many-named(looking-for, p2)
  end
end
```
and the example reads `how-many-named("A", p)`{.pyret}
instead.

### Separating Parameters {#Separating-Parameters}

This sets us up for the next stage. The parameters of functions are meant to
indicate what might vary in a function. Because the name we’re looking for is a
constant once we initially have it, we’d like the actual search function to
take only one argument: where in the tree we’re searching.

That is, we want the search function’s
contract to be `(ABT -> Number)`{.pyret}. To achieve that, we need another
function that will take the `String`{.pyret} part.
Thus, the contract has to become

```pyret
how-many-named :: String -> (ABT -> Number)
```
where `how-many-named`{.pyret} consumes a name and returns a function that will
consume the actual tree to check.

This suggests the following function body:

```pyret
fun how-many-named(looking-for):
  lam(p :: ABT) -> Number:
    cases (ABT) p:
      | unknown => 0
      | person(n, p1, p2) =>
        (if n == looking-for: 1 else: 0 end)
        +
        how-many-named(looking-for, p1) +
        how-many-named(looking-for, p2)
    end
  end
end
```
However, this function body is not okay: the Pyret type-checker will give us
type errors. That’s because `how-many-named`{.pyret} takes one parameter, not two,
as in the two recursive calls.

How do we fix this? Remember, the whole point of this change is we don’t want
to change the name, only the tree. That means we want to recur on the inner
function. We currently can’t do this because it doesn’t have a name! So we have
to give it a name and recur on it:

```pyret
fun how-many-named(looking-for):
  fun search-in(p :: ABT) -> Number:
    cases (ABT) p:
      | unknown => 0
      | person(n, p1, p2) =>
        (if n == looking-for: 1 else: 0 end)
        +
        search-in(p1) +
        search-in(p2)
    end
  end
end
```
This now lets us recur on just the part that should vary, leaving the name
we’re looking for unchanged (and hence, fixed for the duration of the
search).

::: {.do-now}
Try the above and make sure it works.
:::

It still doesn’t: the above body has a syntax error! This is because `how-many-named`{.pyret}
does not actually return any kind of value.

What should it return? Once we provide the function with a name, we should get
back a function that searches for that name in a tree. But we already
have exactly such a function: `search-in`{.pyret}. Therefore,
`how-many-named`{.pyret} should return just … `search-in`{.pyret}.

```pyret
fun how-many-named(looking-for):
  fun search-in(p :: ABT) -> Number:
    cases (ABT) p:
      | unknown => 0
      | person(n, p1, p2) =>
        (if n == looking-for: 1 else: 0 end)
        +
        search-in(p1) +
        search-in(p2)
    end
  end

  search-in
end
```

This still won’t work, because we haven’t changed the example. Let’s
update that: how do we use `how-many-named`{.pyret}? We have to call it
with a name (like `"A"`{.pyret}); this returns a function—the
one bound to `search-in`{.pyret}—which expects a ancestor tree. Doing
so should return a count. Thus, the example should be rewritten as

```pyret
how-many-As = how-many-named("A")
how-many-As(p) is 3
```
This is an instructive way to write the example. We can, however, also
write it more concisely. Notice that `how-many-named("A")`{.pyret}
returns a function, and the way we apply a function to arguments is
`(…)`{.pyret}. Thus, we can also write this as:

```pyret
how-many-named("A")(p) is 3
```

### Context {#Context}

The transformation we just applied is generally called currying, in honor
of Haskell Curry, who was one of the early people to describe it, though it was
earlier discovered by Moses Schönfinkel and even earlier by Gottlob Frege. The
particular use of currying here, where we move more “static” arguments
earlier and more “dynamic” ones later, and split on the static-dynamic
divide, is called staging. It’s a very useful programming technique, and
furthermore, one that enables some compilers to produce more time-efficient
programs.

Even more subtly but importantly, the staged computation tells a different
story than the unstaged one, and we can read this off just from the contract:

```pyret
how-many-named :: String, ABT -> Number
how-many-named :: String -> (ABT -> Number)
```
The first one says the string could co-vary with the person. The second one
rules out that interpretation.

::: {.do-now}
Is the former useful? When might we have the name also changing?
:::

Imagine a slightly different problem: we want to know how often a child has the
same name as a parent. Then, as we traverse the tree, as the name of the person
(potentially) keeps changing, the name we’re looking for in the parent also
changes.

::: {.exercise}
Write this function.
:::

In contrast, the staged type rules out that interpretation and that
behavior. In that way, it sends a signal to the reader about how the
computation might behave just from the type. In the same way, the unstaged type
can be read as giving the reader a hint that the behavior could depend on both
parameters changing, therefore accommodating a much broader range of behaviors
(e.g., checking for parent-child or grandparent-child name reuse).

There’s another very nice example of staging here:
[A Little Calculus](func-as-data.html##fd-calculus).

Finally, it’s worth knowing that some languages, like Haskell and
OCaml, do this transformation automatically. In fact, they don’t even
have multiple-parameter functions: what look like multiple arguments
are actually a sequence of staged functions. This can, in extremis,
lead to a very elegant and powerful programming style. Pyret chose to
not do this because, while this is a powerful tool in the hands of
advanced programmers, for less experienced programmers, finding out
about a mismatch in the number of parameters and arguments is very
useful.
