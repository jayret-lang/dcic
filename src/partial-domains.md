---
title: Partial Domains
section_number: 23
source_file: partial-domains.html
prev: avoid-recomp.html
up: booklet_advanced.html
next: staging.html
---

## 23 Partial Domains {#partial-domains}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="partial-domains.html#%28part._pd-sentinel%29">23.1<span class="hspace"> </span>A Non-Solution</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="partial-domains.html#%28part._pd-exceptions%29">23.2<span class="hspace"> </span>Exceptions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="partial-domains.html#%28part._pd-option%29">23.3<span class="hspace"> </span>The Option Type</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="partial-domains.html#%28part._pd-total-dyn%29">23.4<span class="hspace"> </span>Total Domains, Dynamically</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="partial-domains.html#%28part._pd-total-static%29">23.5<span class="hspace"> </span>Total Domains, Statically</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="partial-domains.html#%28part._pd-summary%29">23.6<span class="hspace"> </span>Summary</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="partial-domains.html#%28part._pd-pyret-list-constr%29">23.7<span class="hspace"> </span>A Note on Notation</a></p></td></tr></table>
```

Sometimes, we cannot precisely capture the domain of a function with the
precision we would like. In mathematics, if a function cannot accept all values
in its domain, it is called partial. This is a problem we encounter more
often than we might like in programming, so we need to know how to handle
it. There are actually several programming strategies that we can use, with
different benefits and weaknesses. Here, we will examine some of them.

Consider some functions on lists of numbers, such as computing the median or
the average. In both cases, these functions don’t work on all lists of
numbers: there is no median for the empty list, and we can’t compute its
average either, because there are no elements (so trying to compute the average
would result in a divison-by-zero error). Thus, while it is a convenient
fiction to write

```pyret
average :: List<Number> -> Number
```
it is just that: a (bit of a) fiction. The function is only defined on
non-empty lists.

We will now see how to handle this from a software engineering
perspective. We’ll specifically work through `average`{.pyret} because the function is
simple enough that we can focus on the software structure without getting lost
in the solution details. There are at least four solutions, and one
non-solution.

### 23.1 A Non-Solution {#pd-sentinel}

We will start with a strategy that has often been used by programmers in the
past, but that we reject as a non-solution. This strategy is to make the above
contract absolutely correct by returning a value in the erroneous case;
this value is often called a sentinel. For instance, the sentinel might
be `0`{.pyret}. Here is the full program:

```pyret
type LoN = List<Number>

fun sum(l :: LoN) -> Number:
  fold({(a, b): a + b}, 0, l)
end

avg0 :: LoN -> Number

fun avg0(l):
  cases (List) l:
    | empty => 0
    | link(_, _) =>
      s = sum(l)
      c = l.length()
      s / c
  end
end
```
and here are a few tests:

```pyret
check:
  avg0([list: 1]) is 1
  avg0([list: 1, 2, 3]) is 2
  avg0([list: 1, 2, 3, 10]) is 4
end
```

Is there a test missing here? Yes, for the empty list! Should we add it?

```pyret
check:
  avg0(empty) is 0
end
```
The question is, should we be happy with this “solution”? There are two
problems with it.

First, every single use of `avg0`{.pyret} needs to check for whether it got back
`0`{.pyret} or not. If it did not, then the answer is legitimate, and it can
proceed with the computation. But if it did, then it has to assume that the
input may have been illegitimate, and cannot use the answer.

Second, even that’s not quite true. To understand why, we need to write a few
more tests:

```pyret
check:
  avg0([list: -1, 0, 1]) is 0
  avg0([list: -5, 4, 1]) is 0
end
```
So the problem is that when `avg0`{.pyret} returns `0`{.pyret}, we don’t know whether
that’s a legitimate answer or a “fake” answer that stands for “this
is not a valid input”. So even our strategy of “check everywhere” fails!

Ah, but maybe the problem is the use of `0`{.pyret}! Perhaps we could use a
different number that would work. How about `1`{.pyret}? Or `-1`{.pyret}? The
question is: Is there any number that reasonably can’t be the
average of an actual input? (And in general, for all problems, can you be sure
of this?) Well, of course not.

That’s why this is a non-solution. It has created several problems:


- We can’t tell from the output whether the input was invalid.
- That means every caller needs to check.
- A caller that forgets to check may compute with nonsense.
- Compositionality is ruined: any function passed `average`{.pyret} needs to
  know to check the output (and there is nothing in the contract to warn it!).

Indeed, decades of experience tells us that some of the world’s most
sophisticated programmers have not been able to handle this issue even when it
matters most, resulting in numerous, pernicious security problems. Therefore,
we should now regard this as a flawed approach to software construction, and
never do it ourselves.

Let’s instead look at four actual solutions.

### 23.2 Exceptions {#pd-exceptions}

One technique that many languages, including Pyret, provide is called the
exception. An exception is a special programming construct that
effectively halts the computation because the program cannot figure out how to
continue computing with the data it has. There are more sophisticated forms of
exceptions in some languages, but here we focus simply on using them as a
strategy for handling partiality.

Here is the average program written using an exception (we reuse `sum`{.pyret}
from before):

```pyret
avg1 :: LoN -> Number

fun avg1(l):
  cases (List) l:
    | empty => raise("no average for empty list")
    | link(_, _) =>
      s = sum(l)
      c = l.length()
      s / c
  end
end

check:
  avg1([list: 1]) is 1
  avg1([list: 1, 2, 3]) is 2
  avg1([list: 1, 2, 3, 10]) is 4
end
```
The way `raise`{.pyret} works is that it terminates everything that is waiting to
happen. For instance, if we were to write

```pyret
1 + avg1(empty)
```
the `1 + …`{.pyret} part never happens: the whole computation ends. `raise`{.pyret}
creates exceptions.

Again, we’re missing a test. How do we write it?

```pyret
check:
  avg1(empty) raises "no average for empty list"
end
```
The `raises`{.pyret} form takes a string that it matches against that provided to
`raise`{.pyret}. In act, for convenience, any sub-string of the original string is
permitted: we can, for instance, also write
`check:
  avg1(empty) raises "no average"
  avg1(empty) raises "empty list"
end`{.pyret}

In many programming languages, the use of exceptions is the standard way of
dealing with partiality. It is certainly a pragmatic solution. Observe that we
got to reuse `sum`{.pyret} from earlier; the contract looks clean; and we only
needed to use `raise`{.pyret} at the spot where we didn’t know what to do. What’s
not to like?

There are two main problems with exceptions:


1. In real systems, exceptions halt a program’s execution in unpredictable
  ways. A caller to `avg1`{.pyret} may be half-way through doing something else
  (e.g., it may have opened a file that it intends to close), but the exception
  causes the call to not finish cleanly, causing the remaining computation to not
  run, leaving the system in a messy state.
2. Relatedly, what we presented as a feature should actually be treated as a
  problem: the contract lies! There’s no indication at all in the contract
  that an exception might occur. A programmer has to read the whole
  implementation—which could change at any time—instead of being able to rely
  on its published contract, when the whole point of contracts was that they
  saved us from having to read the whole implementation!

Indeed, some modern programming languages designed for large-scale programming
(such as Go and Rust) no longer have exception constructs. Therefore, you
should not assume that this will continue to be the “standard” way of doing
things in the future.

Observe that there is are two kinds of exceptions that can occur. One is
as we’ve written above. The other is when we completely ignore (or forget to
even think about) the empty list case, and end up getting an error from Pyret,
which is also a kind of exception. If Pyret will raise an exception anyway,
does it make sense for us to go through the trouble of doing it ourselves?

Yes it does! For several reasons:


1. First, you get to control where the exception occurs and what it says.
2. You can document that the exception will occur.
3. You are less dependent on the behavior of Pyret or whatever underlying
  programming language, which can change in subtle ways.
4. You can create an exception that is unique to you, so it can’t be
  confused with other division-by-zero errors that may lurk in your program.

For these reasons, it’s better to check and raise an exception explicitly
than letting it “fall through” to the programming language. Instead, the real
problems with this solution are subtler: the lying contract, and the impact on
program execution.

### 23.3 The Option Type {#pd-option}

Let’s revisit `avg0`{.pyret}. The problem with it was that it returned a value
that was not distinguishable from an actual answer. So perhaps another
approach is to return a value that is guaranteed to be distinguishable!
For this, a growing number of languages (including Pyret) have something like
this type:

```pyret
data Option<T>:
  | none
  | some(value :: T)
end
```

This is a type we use when we aren’t sure we will have an answer: `none`{.pyret}
means we don’t have an answer, whereas `some`{.pyret} means we do and `value`{.pyret}
is that answer.

Here’s how our program now looks:

```pyret
avg2 :: LoN -> Option<Number>

fun avg2(l):
  cases (List) l:
    | empty => none
    | link(_, _) =>
      s = sum(l)
      c = l.length()
      some(s / c)
  end
end
```
Now our tests look a bit different:

```pyret
check:
  avg2([list: 1]) is some(1)
  avg2([list: 1, 2, 3]) is some(2)
  avg2([list: 1, 2, 3, 10]) is some(4)
end

check:
  avg2(empty) is none
end
```

The good news is, the contract is now truthful. Just by looking at it, we are
reminded that `avg0`{.pyret} may not always be able to compute an answer.

Unfortunately, this imposes some cost on every user: they have to use
`cases`{.pyret} to check return values and only use them if they are
legitimate. However, this is the same thing we expected in `avg0`{.pyret}—except
we lacked a discipline for making sure we didn’t abuse that value! So this is
`avg0`{.pyret} done in a principled way.

### 23.4 Total Domains, Dynamically {#pd-total-dyn}

All these problems arise because we said that `average`{.pyret} (like
`median`{.pyret}) is partial. However, it’s only partial if we give the domain as
`List<Number>`{.pyret}; it’s actually a total function on the `non-empty`{.pyret}
list of numbers. But how do we represent that?

In some languages, like Pyret, we can actually express this directly:

```pyret
type NeLoND = List<Number>%(is-link)
```
This says that we’re refining numeric lists to always have a `link`{.pyret},
i.e., to be non-empty. In Pyret, currently, this check is only done at
run-time; in some other programming languages, this can be done by the
type-checker itself.

This refinement lets us pretend that we’re dealing with regular lists and reuse
all existing list code, while knowing for sure we will never get a
divide-by-zero error:

```pyret
avg3 :: NeLoND -> Number

fun avg3(l):
  s = sum(l)
  c = l.length()
  s / c
end

check:
  avg3([list: 1]) is 1
  avg3([list: 1, 2, 3]) is 2
  avg3([list: 1, 2, 3, 10]) is 4
end
```
If we do try passing an empty list, we get an internal exception:

```pyret
check:
  avg3(empty) raises ""
end
```
This is a pretty interesting solution. Our function’s code is clean. We don’t
deal with nonsensical values. The interface is truthful! (However, it does require a
careful reading to observe that there’s an exception lurking underneath the
domain.) And it lets us reuse existing code.

There are two main weaknesses:


1. Dynamic refinements aren’t found in most
  languages, so we’d have to do more manual work to obtain the same
  solution.
2. We don’t get a static guarantee (i.e., before even running the program)
  that we’ll never get an exception.

### 23.5 Total Domains, Statically {#pd-total-static}

How do we make the function total with a static guarantee? That would require
that we ensure that we can never construct an empty list! Obviously, this is
not possible with the existing lists in Pyret. However, we can construct a new
list-like datatype that “bottoms out” not at empty lists but at lists of one
element:

```pyret
data NeLoN:
  | one(n :: Number)
  | more(n :: Number, r :: NeLoN)
end
```
Observe that there is simply no way to make an empty list: the smallest list
has one element in it. Furthermore, our type checker enforces this for us.

Of course, this is an entirely different datatype than a list of numbers. We
can’t, for instance, use the existing `sum`{.pyret} or `length`{.pyret} code on
it. However, one option is to convert a `NeLoN`{.pyret} into a `LoN`{.pyret}, which
is always safe, and reuse that code:

```pyret
fun nelon-to-lon(nl :: NeLoN):
  cases (NeLoN) nl:
    | one(n) => [list: n]
    | more(n, r) => link(n, nelon-to-lon(r))
  end
end

fun nl-sum(nl :: NeLoN) -> Number:
  sum(nelon-to-lon(nl))
end

fun nl-len(nl :: NeLoN) -> Number:
  nelon-to-lon(nl).length()
end
```
Now we can write the average in an interesting way:

```pyret
fun avg4(nl :: NeLoN) -> Number:
  s = nl-sum(nl)
  c = nl-len(nl)
  s / c
end
```

Once again, we don’t have to have any logic for dealing with errors. However,
it’s not because we’re sloppy or letting Pyret deal with it or getting it
checked at runtime or anything else: it’s because there is no way for an
empty list to arise. Thus we have both the simplest body and the
most truthful interface! But it comes at a cost: we need to do some work to
reuse existing functions.

This problem extends to writing tests, which is now more painful:

```pyret
check:
  nl1 = one(1)
  nl2 = more(1, more(2, one(3)))
  nl3 = more(1, more(2, more(3, one(10))))

  avg4(nl1) is 1
  avg4(nl2) is 2
  avg4(nl3) is 4
end
```
That is, we’ve lost our convenient way of writing lists. We can recover that by
 writing a helper that creates `NeLoN`{.pyret}s:

```pyret
fun lon-to-nelon(l :: LoN) -> NeLoN:
  cases (List) l:
    | empty => raise("can't make an empty NeLoN")
    | link(f, r) =>
      cases (List) r:
        | empty => one(f)
        | else => more(f, lon-to-nelon(r))
      end
  end
end

check:
  avg4(lon-to-nelon([list: 1])) is 1
  avg4(lon-to-nelon([list: 1, 2, 3])) is 2
  avg4(lon-to-nelon([list: 1, 2, 3, 10])) is 4
end
```
Notice that if we try to use an empty list, we get an exception:

```pyret
check:
  avg4(lon-to-nelon(empty)) raises ""
end
```
However, it’s very important to understand where the error is coming from: the
exception is not from `avg4`{.pyret}, it’s coming from `lon-to-nelon`{.pyret}, i.e., from the
“interface” function. The bad datum never makes it as far as `avg4`{.pyret}! We can
verify this:

```pyret
check:
  lon-to-nelon(empty) raises ""
end
```
Remember, there’s no way to send an empty list to `avg4`{.pyret}! Nevertheless,
this suggests a trade-off: we can either use `NeLoN`{.pyret} explicitly but with
more notational pain, or we can use `list`{.pyret} but run the risk of some
confusion about exceptions. This is a trade-off in general, but there are
better options in some languages ([A Note on Notation](partial-domains.html##pd-pyret-list-constr)).

So this is actually a very powerful technique: building a datatype that
reflects exactly what we want, thereby turning a partial function into a total
one. Programmers call this principle making illegal states
unrepresentable. It may require writing some procedures to convert to and from
other convenient representations for code reuse. Somewhere in those procedures
there must be checks that reflect the partiality.

### 23.6 Summary {#pd-summary}

In general, there is one non-solution:


- Return a sentinel value. Do not ever do this unless you’ve first fixed
  all the security bugs lurking in C programs from the past several decades.

and there are four solutions:


- Use `raise`{.pyret}. This is not very good for software engineering in
  general because exceptions are clunky, semantically complicated, and not
  compositional.
- Use a dynamic refinement. Dynamic refinements aren’t in most
  languages. Also, it’s less good than each of the other solutions, but it’s a
  decent compromise in many settings.
- Define a datatype to make illegal states unrepresentable. A bit of
  work. Pretty sophisticated, invaluable in some places, but not always worth the
  effort.
- Use `Option`{.pyret}. Often the ideal option, because:
  
  - The type tells us to expect funny business. (`raise`{.pyret} hides that.)
  - We can’t accidentally misuse the value. (Sentinels hide that.)
  - It’s compositional: we can create functions to help us handle it.
  - It’s much lower overhead than the static totality solution.
  - It’s more statically robust than the dynamic totality solution.
  - It generalizes: in practice, instead of just `none`{.pyret} and `some`{.pyret},
    a real program will have `some`{.pyret} for the “normal” case, and a bunch of
    variants describing the different kinds of errors that are possible, with extra
    information in each case. For concrete examples of this, see
    [Picking Elements from Sets](Collections_of_Structured_Data.html##coll-sd-pick) on sets [Combining Answers](queues-from-lists.html##qfl-comb-ans) on queues.

### 23.7 A Note on Notation {#pd-pyret-list-constr}

When we wrote above that we can’t get the convenience of writing, say,
`[list: 1, 2, 3]`{.pyret} when using `NeLoN`{.pyret}s, we were speaking in
general. In some languages, we can actually make similar convenient
constructors. In Pyret, for instance, there is a protocol for defining custom
constructors; in fact, seemingly built-in constructors like `list`{.pyret} and
`set`{.pyret} are built using this protocol. The code for doing this is a bit
ungainly (in part because it’s optimized to save some space and time by making
the constructor-writer’s life a little harder), but it only needs to be written
once. Here’s a `nelon`{.pyret} constructor for `NeLoN`{.pyret}s:

```pyret
fun ra-to-nelon(r :: RawArray<Number>) -> NeLoN:
  len = raw-array-length(r)
  fun make-from-index(n :: Number):
    v = raw-array-get(r, n)
    if n == (len - 1):
      one(v)
    else:
      more(v, make-from-index(n + 1))
    end
  end
  make-from-index(0)
end

nelon = {
  make0: {(): raise("can't make an empty NeLoN")},
  make1: {(a1): one(a1)},
  make2: {(a1, a2): more(a1, one(a2))},
  make3: {(a1, a2, a3): more(a1, more(a2, one(a3)))},
  make4: {(a1, a2, a3, a4): more(a1, more(a2, more(a3, one(a4))))},
  make5: {(a1, a2, a3, a4, a5): more(a1, more(a2, more(a3, more(a4, one(a5)))))},
  make: {(args :: RawArray<Number>): ra-to-nelon(args)} }
```
These tests show that this constructor works very much like the built-in `list`{.pyret}:

```pyret
check:
  [nelon: ] raises "empty"
  [nelon: 1] is one(1)
  [nelon: 1, 2] is more(1, one(2))
  [nelon: 1, 2, 3] is more(1, more(2, one(3)))
  [nelon: 1, 2, 3, 4] is more(1, more(2, more(3, one(4))))
  [nelon: 1, 2, 3, 4, 5] is more(1, more(2, more(3, more(4, one(5)))))
  [nelon: 1, 2, 3, 4, 5, 6] is
  more(1, more(2, more(3, more(4, more(5, one(6))))))
  [nelon: 1, 2, 3, 4, 5, 6, 7] is
  more(1, more(2, more(3, more(4, more(5, more(6, one(7)))))))
end
```
With this, we can rewrite the tests from [Total Domains, Statically](partial-domains.html##pd-total-static) very
conveniently:

```pyret
check:
  avg4([nelon: 1]) is 1
  avg4([nelon: 1, 2, 3]) is 2
  avg4([nelon: 1, 2, 3, 10]) is 4
end
```
thereby having our cake and eating it too!
