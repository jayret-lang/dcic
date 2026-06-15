---
title: Functions as Data
section_number: 8.1
source_file: dcic_orig_func-as-data.html
prev: part_bonus-foundations.html
up: part_bonus-foundations.html
next: queues-from-lists.html
---

### Functions as Data {#func-as-data}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="func-as-data.html#%28part._fd-calculus%29">8.1.1<span class="hspace"> </span>A Little Calculus</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="func-as-data.html#%28part._lam-shorthand%29">8.1.2<span class="hspace"> </span>A Helpful Shorthand for Anonymous Functions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="func-as-data.html#%28part._streams-from-funs%29">8.1.3<span class="hspace"> </span>Streams From Functions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="func-as-data.html#%28part._d-dx-streams%29">8.1.4<span class="hspace"> </span>Combining Forces: Streams of Derivatives</a></p></td></tr></table>
```

It’s interesting to consider how expressive the little programming
we’ve learned so far can be. To illustrate this, we’ll work through a
few exercises of interesting concepts we can express using just
functions as values. We’ll write two quite different things, then show
how they converge nicely.

#### A Little Calculus {#fd-calculus}

If you’ve studied the differential calculus, you’ve come across
curious sytactic statements such as this:
\begin{equation*}{\frac{d}{dx}} x^2 = 2x\end{equation*}Let’s unpack what this means: the \(d/dx\), the \(x^2\), and the \(2x\).

First, let’s take on the two expressions; we’ll discuss one, and the
discussion will cover the other as well. The correct response to
“what does \(x^2\) mean?” is, of course, an error: it doesn’t mean
anything, because \(x\) is an unbound identifier.

So what is it intended to mean? The intent, clearly, is to
represent the function that squares its input, just as \(2x\) is meant
to be the function that doubles its input. We have nicer ways of
writing those:

```pyret
fun sq(x :: Number) -> Number: x * x end
fun dbl(x :: Number) -> Number: 2 * x end
```
and what we’re really trying to say is that the \(d/dx\) (whatever
that is) of `sq`{.pyret} is `dbl`{.pyret}.[We’re
assuming functions of arity one in the variable that is changing.]{.margin-note}

So now let’s unpack \(d/dx\), starting with its type. As the above
example illustrates, \(d/dx\) is really a function from
functions to functions. That is, we can write its type as follows:

```pyret
d-dx :: ((Number -> Number) -> (Number -> Number))
```
(This type might explain why your calculus course never explained this
operation this way—though it’s not clear that obscuring its true
meaning is any better for your understanding.)

Let us now implement `d-dx`{.pyret}. We’ll implement numerical
differentiation, though in principle we could also implement
symbolic differentiation—using rules you learned, e.g.,
given a polynomial, multiply by the exponent and reduce the exponent
by one—with a representation of expressions (a problem that will be covered in more detail in a future release).

In general, numeric differentiation of a function at a point yields
the value of the derivative at that point. We have a handy formula for
it: the derivative of \(f\) at \(x\) is
\begin{equation*}\frac{f(x + \epsilon) - f(x)}{\epsilon}\end{equation*}as \(\epsilon\) goes to zero in the limit. For now we’ll give the
infinitesimal a small but fixed value, and later
[[Combining Forces: Streams of Derivatives](func-as-data.html##d-dx-streams)] see how we can improve on this.

```pyret
epsilon = 0.00001
```

We can now translate the above formula into a function:

```pyret
d-dx-at :: (Number -> Number), Number -> Number

fun d-dx-at(f, x):
  (f(x + epsilon) - f(x)) / epsilon
end
```
And sure enough, we can check and make sure it works as expected:

```pyret
check:
  d-dx-at(sq, 10) is-roughly dbl(10)
end
```
[Confession: We chose the value of `epsilon`{.pyret} so that the
default tolerance `is-roughly`{.pyret} works for this example.]{.margin-note}

However, there is something unsatisfying about this. The function we’ve written
clearly does not have the type we described earlier! What we wanted was an
operation that takes just a function, and represents the platonic notion of
differentiation; but we’ve been forced, by the nature of numeric
differentiation, to describe the derivative at a point. We might
instead like to write something like this:

```pyret
fun d-dx(f):
  (f(x + epsilon) - f(x)) / epsilon
end
```

::: {.do-now}
What’s the problem with the above definition?
:::

If you didn’t notice, Pyret will soon tell you: `x`{.pyret} isn’t
bound. Indeed, what is `x`{.pyret}? It’s the point at which we’re trying
to compute the numeric derivative. That is, `d-dx`{.pyret} needs to
return not a number but a function (as the type indicates) that
will consume this `x`{.pyret}:[“Lambdas are relegated to
relative obscurity until Java makes them popular by not having
them.”—James Iry,
[A
Brief, Incomplete, and Mostly Wrong History of Programming Languages](https://james-iry.blogspot.com/2009/05/brief-incomplete-and-mostly-wrong.html)]{.margin-note}

```pyret
fun d-dx(f):
  lam(x):
    (f(x + epsilon) - f(x)) / epsilon
  end
end
```
If we want to be a little more explicit we can annotate the inner function:

```pyret
fun d-dx(f):
  lam(x :: Number) -> Number:
    (f(x + epsilon) - f(x)) / epsilon
  end
end
```
This is a special case of a concept useful in many programming contexts, which
we explore in more detail elsewhere: [Staging](staging.html).

Sure enough, this definition now works. We can, for instance, test it
as follows (note the use of `num-floor`{.pyret} to avoid numeric precision
issues from making our tests appear to fail):

```pyret
d-dx-sq = d-dx(sq)

check:
  ins = [list: 0, 1, 10, 100]
  for map(n from ins):
    num-floor(d-dx-sq(n))
  end
  is
  for map(n from ins):
    num-floor(dbl(n))
  end
end
```
Now we can return to the original example that launched this
investigation: what the sloppy and mysterious notation of math is
really trying to say is,

```pyret
d-dx(lam(x): x * x end) = lam(x): 2 * x end
```
or, in the notation of [A Notation for Functions](predicting-growth.html##math-anon-functions),
\begin{equation*}{\frac{d}{dx}} [x \rightarrow x^2] = [x \rightarrow 2x]\end{equation*}Pity math textbooks for not wanting to tell us the truth!

#### A Helpful Shorthand for Anonymous Functions {#lam-shorthand}

Pyret offers a shorter syntax for writing anonymous functions. Though,
stylistically, we generally avoid it so that our programs don’t become
a jumble of special characters, sometimes it’s particularly
convenient, as we will see below. This syntax is

```pyret
{(a): b}
```
where `a`{.pyret} is zero or more arguments and `b`{.pyret} is the body. For
instance, we can write `lam(x): x * x end`{.pyret} as

```pyret
{(x): x * x}
```
where we can see the benefit of brevity. In particular, note that
there is no need for `end`{.pyret}, because the braces take the place of
showing where the expression begins and ends. Similarly, we could have
written `d-dx`{.pyret} as

```pyret
fun d-dx-short(f):
  {(x): (f(x + epsilon) - f(x)) / epsilon}
end
```
but many readers would say this makes the function harder to read,
because the prominent `lam`{.pyret} makes clear that `d-dx`{.pyret} returns
an (anonymous) function, whereas this syntax obscures it. Therefore,
we will usually only use this shorthand syntax for “one-liners”.

#### Streams From Functions {#streams-from-funs}

People typically think of a function as serving one purpose: to
parameterize an expression. While that is both true and the most
common use of a function, it does not justify having a function of no
arguments, because that clearly parameterizes over nothing at all. Yet
functions of no argument also have a use, because functions actually
serve two purposes: to parameterize, and to suspend evaluation
of the body until the function is applied. In fact, these two uses
are orthogonal, in that one can employ one feature without the
other. Below, we will focus on delay without abstraction (the other
shows up in other computer science settings).

Let’s consider the humble list. A list can be only finitely
long. However, there are many lists (or sequences) in nature
that have no natural upper bound: from mathematical objects (the
sequence of natural numbers) to natural ones (the sequence of hits to
a Web site). Rather than try to squeeze these unbounded lists into
bounded ones, let’s look at how we might represent and program over
these unbounded lists.

First, let’s write a program to compute the sequence of natural
numbers:

```pyret
fun nats-from(n):
  link(n, nats-from(n + 1))
end
```

::: {.do-now}
Does this program have a problem?
:::

While this represents our intent, it doesn’t work: running it—e.g.,
`nats-from(0)`{.pyret}—creates an infinite loop evaluating
`nats-from`{.pyret} for every subsequent natural number. In other words,
we want to write something very like the above, but that doesn’t recur
until we want it to, i.e., on demand. In other words, we want
the rest of the list to be lazy.

This is where our insight into functions comes in. A function, as we
have just noted, delays evaluation of its body until it is
applied. Therefore, a function would, in principle, defer the
invocation of `nats-from(n + 1)`{.pyret} until it’s needed.

Except, this creates a type problem: the second argument to
`link`{.pyret} needs to be a list, and cannot be a function. Indeed,
because it must be a list, and every value that has been constructed
must be finite, every list is finite and eventually terminates in
`empty`{.pyret}. Therefore, we need a new data structure to represent the
links in these lazy lists (also known as streams):
<stream-type-def> ::=
```pyret
data Stream<T>:
  | lz-link(h :: T, t :: ( -> Stream<T>))
end
```
where the annotation `( -> Stream<T>)`{.pyret} means a function from no
arguments (hence the lack of anything before `->`{.pyret}),
also known as a thunk. Note that the way we have
defined streams they must be infinite, since we have provided
no way to terminate them.

Let’s construct the simplest example we can, a stream of constant
values:

```pyret
ones = lz-link(1, lam(): ones end)
```
Pyret will actually complain about this definition. Note that
the list equivalent of this also will not work:

```pyret
ones = link(1, ones)
```
because `ones`{.pyret} is not defined at the point of
definition, so when Pyret evaluates `link(1, ones)`{.pyret}, it complains
that `ones`{.pyret} is not defined. However, it is being overly
conservative with our former definition: the use of `ones`{.pyret} is
“under a `lam`{.pyret}”, and hence won’t be needed until after the
definition of `ones`{.pyret} is done, at which point `ones`{.pyret}
will be defined. We can indicate this to Pyret by using the
keyword `rec`{.pyret}:

```pyret
rec ones = lz-link(1, lam(): ones end)
```
Note that in Pyret, every `fun`{.pyret}
implicitly has a `rec`{.pyret} beneath it, which is why we can
create recursive functions with aplomb.

::: {.exercise}
Earlier we said that we can’t write

```pyret
ones = link(1, ones)
```
What if we tried to write

```pyret
rec ones = link(1, ones)
```
instead? Does this work and, if so, what value is `ones`{.pyret} bound
to? If it doesn’t work, does it fail to work for the same reason as
the definition without the `rec`{.pyret}?
:::

Henceforth, we will use the shorthand [[A Helpful Shorthand for Anonymous Functions](func-as-data.html##lam-shorthand)]
instead. Therefore, we can rewrite the above definition as:

```pyret
rec ones = lz-link(1, {(): ones})
```
Notice that `{(): …}`{.pyret} defines an anonymous function of no
arguments. You can’t leave out the `()`{.pyret}! If you do, Pyret will
get confused about what your program means.

Because functions are automatically recursive, when we write a
function to create a stream, we don’t need to use `rec`{.pyret}. Consider
this example:

```pyret
fun nats-from(n :: Number):
  lz-link(n, {(): nats-from(n + 1)})
end
```
with which we can define the natural numbers:

```pyret
nats = nats-from(0)
```
Note that the definition of `nats`{.pyret} is not recursive itself—the
recursion is inside `nats-from`{.pyret}—so we don’t need to use
`rec`{.pyret} to define `nats`{.pyret}.

::: {.do-now}
Earlier, we said that every list is finite and hence eventually
terminates. How does this remark apply to streams, such as the
definition of `ones`{.pyret} or `nats`{.pyret} above?
:::

The description of `ones`{.pyret} is still a finite one; it simply
represents the potential for an infinite number of values. Note
that:


1. A similar reasoning doesn’t apply to lists because the rest of
  the list has already been constructed; in contrast, placing a function
  there creates the potential for a potentially unbounded amount of
  computation to still be forthcoming.
2. That said, even with streams, in any given computation, we will
  create only a finite prefix of the stream. However, we don’t have to
  prematurely decide how many; each client and use is welcome to extract
  less or more, as needed.

Now we’ve created multiple streams, but we still don’t have an easy
way to “see” one. First we’ll define the traditional list-like
selectors. Getting the first element works exactly as with lists:

```pyret
fun lz-first<T>(s :: Stream<T>) -> T: s.h end
```
In contrast, when trying to access the rest of the stream, all we get
out of the data structure is a thunk. To access the actual rest, we
need to force the thunk, which of course means applying it to no
arguments:

```pyret
fun lz-rest<T>(s :: Stream<T>) -> Stream<T>: s.t() end
```

This is useful for examining individual values of the
stream. It is also useful to extract a finite prefix of
it (of a given size) as a (regular) list, which would be especially
handy for testing. Let’s write that function:

```pyret
fun take<T>(n :: Number, s :: Stream<T>) -> List<T>:
  if n == 0:
    empty
  else:
    link(lz-first(s), take(n - 1, lz-rest(s)))
  end
end
```
If you pay close attention, you’ll find that this body is not defined
by cases over the structure of the (stream) input—instead,
it’s defined by the cases of the definition of a natural number (zero
or a successor). We’ll return to this below ([<lz-map2-def>](func-as-data.html#%28elem._lz-map2-def%29)).

Now that we have this, we can use it for testing. Note that usually we
use our data to test our functions; here, we’re using this function to
test our data:

```pyret
check:
  take(10, ones) is map(lam(_): 1 end, range(0, 10))
  take(10, nats) is range(0, 10)
  take(10, nats-from(1)) is map((_ + 1), range(0, 10))
end
```
[The notation `(_ + 1)`{.pyret} defines a Pyret function of
one argument that adds `1`{.pyret} to the given argument.]{.margin-note}

Let’s define one more function: the equivalent of `map`{.pyret} over
streams. For reasons that will soon become obvious, we’ll define a
version that takes two lists and applies the first argument to them
pointwise:
<lz-map2-def> ::=
```pyret
fun lz-map2<A, B, C>(
    f :: (A, B -> C),
    s1 :: Stream<A>,
    s2 :: Stream<B>) -> Stream<C>:
  lz-link(
    f(lz-first(s1), lz-first(s2)),
    {(): lz-map2(f, lz-rest(s1), lz-rest(s2))})
end
```
Now we can see our earlier remark about the structure of the function
driven home especially clearly. Whereas a traditional `map`{.pyret} over
lists would have two cases, here we have only one case because the
data definition ([<stream-type-def>](func-as-data.html#%28elem._stream-type-def%29)) has only one case!
What is the consequence of this? In a traditional `map`{.pyret}, one case
looks like the above, but the other case corresponds to the `empty`{.pyret}
input, for which it produces the same output. Here, because the stream
never terminates, mapping over it doesn’t either, and the structure of
the function reflects this.[This raises a much subtler
problem: if the function’s body doesn’t have base- and
inductive-cases, how can we perform an inductive proof over it? The
short answer is we can’t: we must instead use
[☛ coinduction](glossary.html#%28elem._glossary-coinduction%29).]{.margin-note}

Why did we define `lz-map2`{.pyret} instead of `lz-map`{.pyret}? Because it
enables us to write the following:

```pyret
rec fibs =
  lz-link(0,
    {(): lz-link(1,
          {(): lz-map2({(a :: Number, b :: Number): a + b},
                fibs,
            lz-rest(fibs))})})
```
from which, of course, we can extract as many Fibonacci numbers as we
want!

```pyret
check:
  take(10, fibs) is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
end
```

::: {.exercise}
Define the equivalent of `map`{.pyret} and `filter`{.pyret}
for streams.
:::

Streams and, more generally, infinite data structures that unfold on
demand are extremely valuable in programming. Consider, for instance,
the possible moves in a game. In some games, this can be infinite;
even if it is finite, for interesting games the combinatorics mean
that the tree is too large to feasibly store in memory. Therefore, the
programmer of the computer’s intelligence must unfold the game tree
on demand. Programming it by using the encoding we have
described above means the program describes the entire tree,
lazily, and the tree unfolds automatically on demand, relieving the
programmer of the burden of implementing such a strategy.

In some languages, such as Haskell, lazy evaluation is built in
by default. In such a language, there is no need to use
thunks. However, lazy evaluation places other burdens on the language,
which you can learn about in a programming-languages class.

#### Combining Forces: Streams of Derivatives {#d-dx-streams}

When we defined `d-dx`{.pyret}, we set `epsilon`{.pyret} to an arbitrary, high
value. We could instead think of `epsilon`{.pyret} as itself a stream that
produces successively finer values; then, for instance, when the
difference in the value of the derivative becomes small enough, we can
decide we have a sufficient approximation to the derivative.

The first step is, therefore, to make `epsilon`{.pyret} some kind of
parameter rather than a global constant. That leaves open what kind of
parameter it should be (number or stream?) as well as when it should
be supplied.

It makes most sense to consume this parameter after we have decided
what function we want to differentiate and at what value we want its
derivative; after all, the stream of `epsilon`{.pyret} values may depend
on both. Thus, we get:

```pyret
fun d-dx(f :: (Number -> Number)) ->
    (Number -> (Number -> Number)):
  lam(x :: Number) -> (Number -> Number):
    lam(epsilon :: Number) -> Number:
      (f(x + epsilon) - f(x)) / epsilon
    end
  end
end
```
with which we can return to our `square`{.pyret} example:

```pyret
d-dx-square = d-dx(square)
```
Note that at this point we have simply redefined `d-dx`{.pyret} without
any reference to streams: we have merely made a constant into a
parameter.

Now let’s define the stream of negative powers of ten:

```pyret
tenths = block:
  fun by-ten(d):
    new-denom = d / 10
    lz-link(new-denom, lam(): by-ten(new-denom) end)
  end
  by-ten(1)
end
```
so that

```pyret
check:
  take(3, tenths) is [list: 1/10, 1/100, 1/1000]
end
```
For concreteness, let’s pick an abscissa at which to compute the
numeric derivative of `square`{.pyret}—say `10`{.pyret}:

```pyret
d-dx-square-at-10 = d-dx-square(10)
```
Recall, from the types, that this is now a function of type
`(Number -> Number)`{.pyret}: given a value for `epsilon`{.pyret}, it computes
the derivative using that value. We know, analytically, that the
value of this derivative should be `20`{.pyret}. We can now (lazily) map
`tenths`{.pyret} to provide increasingly better approximations for
`epsilon`{.pyret} and see what happens:

```pyret
lz-map(d-dx-square-at-10, tenths)
```
Sure enough, the values we obtain are `20.1`{.pyret}, `20.01`{.pyret},
`20.001`{.pyret}, and so on: progressively better numerical
approximations to `20`{.pyret}.

::: {.exercise}
Extend the above program to take a tolerance, and draw as many values
from the `epsilon`{.pyret} stream as necessary until the difference
between successive approximations of the derivative fall within this
tolerance.
:::
