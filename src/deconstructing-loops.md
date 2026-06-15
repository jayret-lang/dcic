---
title: Deconstructing Loops
section_number: 26
source_file: dcic_orig_deconstructing-loops.html
prev: factoring-numbers.html
up: booklet_advanced.html
next: booklet_interaction.html
---

## Deconstructing Loops {#deconstructing-loops}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="deconstructing-loops.html#%28part._.Setup__.Two_.Functions%29">26.1<span class="hspace"> </span>Setup: Two Functions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="deconstructing-loops.html#%28part._.Abstracting_a_.Loop%29">26.2<span class="hspace"> </span>Abstracting a Loop</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="deconstructing-loops.html#%28part._.Is_.It_.Really_a_.Loop_%29">26.3<span class="hspace"> </span>Is It Really a Loop?</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="deconstructing-loops.html#%28part._.Re-.Examining___struct_traverse-element___procedure____lib_render-cond_rkt_38_12__%29">26.4<span class="hspace"> </span>Re-Examining <span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">for</code></span></a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="deconstructing-loops.html#%28part._.Rewriting_.Pollard-.Rho%29">26.5<span class="hspace"> </span>Rewriting Pollard-Rho</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="deconstructing-loops.html#%28part._.Nested_.Loops%29">26.6<span class="hspace"> </span>Nested Loops</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="deconstructing-loops.html#%28part._.Loops__.Values__and_.Customization%29">26.7<span class="hspace"> </span>Loops, Values, and Customization</a></p></td></tr></table>
```

### Setup: Two Functions {#Setup-Two-Functions}

Let’s look at two functions we wrote earlier in [Factoring Numbers](factoring-numbers.html):

```pyret
fun gcd(a, b):
  if b == 0:
    a
  else:
    gcd(b, num-modulo(a, b))
  end
end

fun pr(n):
  fun g(x): num-modulo((x * x) + 1, n) end
  fun iter(x, y, d):
    new-x = g(x)
    new-y = g(g(y))
    new-d = gcd(num-abs(new-x - new-y), n)
    ask:
      | new-d == 1 then:
        iter(new-x, new-y, new-d)
      | new-d == n then:
        none
      | otherwise:
        some(new-d)
    end
  end
  iter(2, 2, 1)
end
```
We’ve written both recursively: `gcd`{.pyret} by calling itself and
`pr`{.pyret} with recursion on its inner function. But if you’ve
programmed before, you’ve probably written similar programs with
loops.

::: {.exercise}
Because we don’t have loops in Pyret, the best we can do is to use a
higher-order function; which ones would you use?
:::

But let’s see if we can do something “better”, i.e., get closer to a
traditional-looking program.

Before we start changing any code, let’s make sure we have some tests
for `gcd`{.pyret}:

```pyret
check:
  gcd(4, 5) is 1
  gcd(5, 7) is 1
  gcd(21, 21) is 21
  gcd(12, 24) is 12
  gcd(12, 9) is 3
end
```

### Abstracting a Loop {#Abstracting-a-Loop}

Now let’s think about how we can create a loop. At each iteration, a
loop has a status: whether it’s done or whether it should
continue. Since we have two parameters here, let’s record two
parameters for continuing:

```pyret
data LoopStatus:
  | done(final-value)
  | next-2(new-arg-1, new-arg-2)
end
```
Now we can write a function that does the actual iteration:

```pyret
fun loop-2(f, arg-1, arg-2):
  r = f(arg-1, arg-2)
  cases (LoopStatus) r:
    | done(v) => v
    | next-2(new-arg-1, new-arg-2) => loop-2(f, new-arg-1, new-arg-2)
  end
end
```
Note that this is completely generic: it has nothing to do with
`gcd`{.pyret}. (It is generic in the same way that higher-order functions
like `map`{.pyret} and `filter`{.pyret} are generic.) It just repeats if
`f`{.pyret} says to repeat, stops if `f`{.pyret} says to stop. This is the
essence of a loop.

::: {.exercise}
Observe also that we could, if we wanted, stage [[Staging](staging.html)]
`loop-2`{.pyret}, because `f`{.pyret} never changes. Rewrite it that way.
:::

With `loop-2`{.pyret}, we can rewrite `gcd`{.pyret}:

```pyret
fun gcd(p, q):
  loop-2(
    {(a, b):
      if b == 0:
        done(a)
      else:
        next-2(b, num-modulo(a, b))
      end},
    p,
    q)
end
```
Now it might seem to you we haven’t done anything useful at all. In
fact, this looks like a significant step backward. At least before we
just had simple, clean recursion, the way Euclid intended it. Now we
have a higher-order function and we’re passing it the erstwhile
`gcd`{.pyret} code as a function and there’s this `LoopStatus`{.pyret}
datatype and…everything’s gotten much more complicated.

But, not really. The reason we put it in this form is because we’re
about to exploit a feature of Pyret. The `for`{.pyret} construct in Pyret
actually rewrites as follows:

```pyret
for F(a from a_i, b from b_i, …): BODY end
```
gets rewritten to

```pyret
F({(a, b, …): BODY}, a_i, b_i, …)
```
For example, if we write

```pyret
for map(i from range(0, 10)): i + 1 end
```
this becomes

```pyret
map({(i): i + 1}, range(0, 10))
```

Now you may see why we rewrote `gcd`{.pyret}.
Going in reverse, we can rewrite

```pyret
F({(a, b, …): BODY}, a_i, b_i, …)
```
as

```pyret
for F(a from a_i, b from b_i, …): BODY end
```
so the function becomes just

```pyret
fun gcd(p, q):
  for loop-2(a from p, b from q):
    if b == 0:
      done(a)
    else:
      next-2(b, num-modulo(a, b))
    end
  end
end
```
and now closely resembles a traditional “loop” program.

### Is It Really a Loop? {#Is-It-Really-a-Loop}

This whole section should be considered an aside for people with more
advanced computing knowledge.

If you know something about language implementation, you may know that
loops have the property that the iteration does not consume extra
space (beyond what the program already needs), and the repetition
takes place very quickly (a “jump instruction”). In principle, our
`loop-2`{.pyret} function does not have this property: every iteration is
a function call, which is more expensive and builds additional stack
context. However, one or both of these does not actually occur in
practice.

In terms of space, the recursive call to `loop-2`{.pyret} is the
last thing that a call to `loop-2`{.pyret} does. Furthermore,
nothing in `loop-2`{.pyret} consumes and manipulates the return from that
recursive call. This is therefore called a tail call.
Pyret—like some other languages—causes tail calls to not
take any extra stack space. In principle, Pyret can also turn some
tail calls into jumps. Therefore, this version has close to the same
performance as a traditional loop.

### Re-Examining for {#Re-Examining-struct-traverse-element-procedure-lib-render-cond-rkt-38-12}

The definition of `for`{.pyret} given above should make you suspicious:
Where’s the loop?!? In fact, Pyret’s `for`{.pyret} does not do any
looping at all: it’s simply a fancy way of writing `lam`{.pyret}. Any
“looping” behavior is in the function written after `for`{.pyret}. To
see that, let’s use for with a non-looping function.

Recall that

```pyret
for F(a from a_i, b from b_i, …): BODY end
```
gets rewritten to

```pyret
F({(a, b, …): BODY}, a_i, b_i, …)
```
Thus, suppose we have this function (from [Functions as Data](func-as-data.html)):

```pyret
delta-x = 0.0001
fun d-dx-at(f, x):
  (f(x + delta-x) - f(x)) / delta-x
end
```
We can call it like this to get approximately 20:

```pyret
d-dx-at({(n): n * n}, 10)
```
That means we can also call it like this:

```pyret
for d-dx-at(n from 10): n * n end
```
Indeed:

```pyret
check:
  for d-dx-at(n from 10): n * n end
  is
  d-dx-at({(n): n * n}, 10)
end
```
Since `d-dx-at`{.pyret} has no iterative behavior, no iteration
occurs. The looping behavior is given entirely by the function
specified after `for`{.pyret}, such as `map`{.pyret}, `filter`{.pyret}, or
`loop-2`{.pyret} above.

### Rewriting Pollard-Rho {#Rewriting-Pollard-Rho}

Now let’s tackle Pollard-rho. Notice that it’s a three-parameter
function, so we can’t use the `loop-2`{.pyret} we had before: that’s only
a suitable loop when we have two arguments that change on each
iteration (often the iteration variable and an accumulator). It would
be easy to design a 3-argument version of loop, say `loop-3`{.pyret}, but
we could also have a more general solution, using a tuple:

```pyret
data LoopStatus:
  | done(v)
  | next–2(new-x, new-y)
  | next-n(new-t)
end

fun loop-n(f, t):
  r = f(t)
  cases (LoopStatus) r:
    | done(v) => v
    | next-n(new-t) => loop-n(f, new-t)
  end
end
```
where `t`{.pyret} is a tuple.

So now we can rewrite `pr`{.pyret}. Let’s first rename the old `pr`{.pyret}
function as `pr-old`{.pyret} so we can keep it around for testing. Now we
can define a “loop”-based `pr`{.pyret}:

```pyret
fun pr(n):
  fun g(x): num-modulo((x * x) + 1, n) end
  for loop-n({x; y; d} from {2; 2; 1}):
    new-x = g(x)
    new-y = g(g(y))
    new-d = gcd(num-abs(new-x - new-y), n)
    ask:
      | new-d == 1 then:
        next-n({new-x; new-y; new-d})
      | new-d == n then:
        done(none)
      | otherwise:
        done(some(new-d))
    end
  end
end
```
Indeed, we can test that the two behave in exactly the same way:

```pyret
check:
  ns = range(2, 100)
  l1 = map(pr-old, ns)
  l2 = map(pr, ns)
  l1 is l2
end
```

### Nested Loops {#Nested-Loops}

We can also write a nested loop this way. Suppose we have a list like

```pyret
lol = [list: [list: 1, 2], [list: 3], [list:], [list: 4, 5, 6]]
```
and we want to sum the whole thing by summing each sub-list. Here it is:

```pyret
for loop-2(ll from lol, sum from 0):
  cases (List) ll:
    | empty => done(sum)
    | link(l, rl) =>
      l-sum =
        for loop-2(es from l, sub-sum from 0):
          cases (List) es:
            | empty => done(sub-sum)
            | link(e, r) => next-2(r, e + sub-sum)
          end
        end
      next-2(rl, sum + l-sum)
  end
end
```
We can simplify this by writing it as two functions:

```pyret
fun sum-a-lon(lon :: List<Number>):
  for loop-2(es from lon, sum from 0):
    cases (List) es:
      | empty => done(sum)
      | link(e, r) =>
        next-2(r, e + sum)
    end
  end
end

fun sum-a-lolon(lolon :: List<List<Number>>):
  for loop-2(l from lolon, sum from 0):
    cases (List) l:
      | empty => done(sum)
      | link(lon, r) =>
        next-2(r, sum-a-lon(lon) + sum)
    end
  end
end

check:
  sum-a-lolon(lol) is 21
end
```

Notice that the two functions are remarkably similar. This suggests an abstraction:

```pyret
fun sum-a-list(f, L):
  for loop-2(e from L, sum from 0):
    cases (List) e:
      | empty => done(sum)
      | link(elt, r) =>
        next-2(r, f(elt) + sum)
    end
  end
end
```
Using this, we can rewrite the two previous functions as:

```pyret
fun sum-a-lon(lon :: List<Number>):
  sum-a-list({(e): e}, lon)
end

fun sum-a-lolon(lolon :: List<List<Number>>):
  sum-a-list(sum-a-lon, lolon)
end

check:
  sum-a-lolon(lol) is 21
end
```
With the annotations, it becomes clear what each function does. In
`sum-a-lon`{.pyret}, each element is a number, so it “contributes
itself” to the overall sum. In `sum-a-lolon`{.pyret}, each element is a
list of numbers, so it “contributes its `sum-a-lon`{.pyret}” to the
overall sum.

Finally, to bring this full circle, we can rewrite the above the
functions as follows:

```pyret
fun sum-a-lon(lon :: List<Number>):
  for sum-a-list(e :: Number from lon): e end
end

fun sum-a-lolon(lolon :: List<List<Number>>):
  for sum-a-list(l :: List<Number> from lolon): sum-a-lon(l) end
end
```

Arguably this makes even clearer what each element contributes. In
`sum-a-lon`{.pyret} each element is a number, so it contributes just that
number. In `sum-a-lolon`{.pyret}, each element is a list of numbers, so
it must contribute `sum-a-lon`{.pyret} of that list.

### Loops, Values, and Customization {#Loops-Values-and-Customization}

Observe two important ways in which the loops above differ from
traditional loops:


1. Every loop produces a value. This is consistent with the rest of
  the language, where—as much as possible—computations try to
  produce answers. We don’t have to produce a value; for
  instance, the following program, reminiscent of looping programs in
  many other languages, will work just fine in Pyret:
  
  ```pyret
  for each(i from range(0, 10)): print(i) end
  ```
  However, this is the unusual case. In general, we want expressions to
  produce values so that we can compose them together.
2. Many languages have strong opinions on exactly how many looping
  constructs there should be: two? three? four? In Pyret, there are no
  built-in looping constructs at all; there’s just a syntax (`for`{.pyret})
  that serves as a proxy for creating a specific `lam`{.pyret}. With it, we
  can reuse existing iterative functions (like `map`{.pyret} and
  `filter`{.pyret}), but also define new ones. Some can be very generic,
  like `loop-2`{.pyret} or `loop-n`{.pyret}, but others can be very specific,
  like `sum-a-list`{.pyret}. The language designers don’t prevent you from
  writing a loop that is useful to your situation, and sometimes the
  loop can be very expressive, as we see from rewriting `sum-a-lon`{.pyret}
  and `sum-a-lolon`{.pyret} atop `for`{.pyret} and `sum-a-list`{.pyret}.
