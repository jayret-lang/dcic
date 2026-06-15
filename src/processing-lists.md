---
title: Processing Lists
section_number: 5.2
source_file: dcic_orig_processing-lists.html
prev: tables-to-lists.html
up: part_lists.html
next: recursive-data.html
---

### Processing Lists {#processing-lists}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._.Making_.Lists_and_.Taking_.Them_.Apart%29">5.2.1<span class="hspace"> </span>Making Lists and Taking Them Apart</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._my-len%29">5.2.2<span class="hspace"> </span>Some Example Exercises</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._.Structural_.Problems_with_.Scalar_.Answers%29">5.2.3<span class="hspace"> </span>Structural Problems with Scalar Answers</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._len-eg%29">5.2.3.1<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-len</code></span>: Examples</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._sum-eg%29">5.2.3.2<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-sum</code></span>: Examples</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._.From_.Examples_to_.Code%29">5.2.3.3<span class="hspace"> </span>From Examples to Code</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._.Structural_.Problems_that_.Transform_.Lists%29">5.2.4<span class="hspace"> </span>Structural Problems that Transform Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._doubles-eg-code%29">5.2.4.1<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-doubles</code></span>: Examples and Code</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._str-len-eg-code%29">5.2.4.2<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-str-len</code></span>: Examples and Code</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._.Structural_.Problems_that_.Select_from_.Lists%29">5.2.5<span class="hspace"> </span>Structural Problems that Select from Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._pos-nums-eg-code%29">5.2.5.1<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-pos-nums</code></span>: Examples and Code</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._alternating-eg-code%29">5.2.5.2<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-alternating</code></span>:
Examples and Code</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._struct-prob-sub-dom%29">5.2.6<span class="hspace"> </span>Structural Problems Over Relaxed Domains</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._my-max%29">5.2.6.1<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-max</code></span>: Examples</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part.___struct_traverse-element___procedure____lib_render-cond_rkt_38_12____.From_.Examples_to_.Code%29">5.2.6.2<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-max</code></span>: From Examples to Code</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._.More_.Structural_.Problems_with_.Scalar_.Answers%29">5.2.7<span class="hspace"> </span>More Structural Problems with Scalar Answers</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._avg-eg%29">5.2.7.1<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-avg</code></span>: Examples</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._accumulators%29">5.2.8<span class="hspace"> </span>Structural Problems with Accumulators</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._running-sum-1st-attempt%29">5.2.8.1<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-running-sum</code></span>: First Attempt</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._running-sum-eg-code%29">5.2.8.2<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-running-sum</code></span>: Examples and Code</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._alternating-accumulator%29">5.2.8.3<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">my-alternating</code></span>: Examples and Code</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._.Dealing_with_.Multiple_.Answers%29">5.2.9<span class="hspace"> </span>Dealing with Multiple Answers</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._uniq%29">5.2.9.1<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">uniq</code></span>: Problem Setup</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._uniq-eg%29">5.2.9.2<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">uniq</code></span>: Examples</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part.___struct_traverse-element___procedure____lib_render-cond_rkt_38_12____.Code%29">5.2.9.3<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">uniq</code></span>: Code</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part.___struct_traverse-element___procedure____lib_render-cond_rkt_38_12____.Reducing_.Computation%29">5.2.9.4<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">uniq</code></span>: Reducing Computation</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part.___struct_traverse-element___procedure____lib_render-cond_rkt_38_12____.Example_and_.Code_.Variations%29">5.2.9.5<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">uniq</code></span>: Example and Code Variations</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part.___struct_traverse-element___procedure____lib_render-cond_rkt_38_12____.Why_.Produce_a_.List_%29">5.2.9.6<span class="hspace"> </span><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">uniq</code></span>: Why Produce a List?</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="processing-lists.html#%28part._polymorphic-data%29">5.2.10<span class="hspace"> </span>Monomorphic Lists and Polymorphic Types</a></p></td></tr></table>
```

We have already seen [[From Tables to Lists](tables-to-lists.html)] several examples of
list-processing functions. They have been especially useful for
advanced processing of tables. However, lists arise frequently in
programs, and they do so naturally because so many things in our
lives—from shopping lists to to-do lists to checklists—are
naturally lists. Thinking about the functions that we might want
when processing lists, we can observe that there are some interesting
categories regarding the types of the data in the list:

- some list functions are generic and operate on any kind
  of list: e.g., the length of a list is the same irrespective of what
  kind of values it contains;
- some are specific at least to the type of data: e.g., the sum
  assumes that all the values are numbers (though they may be ages or
  prices or other information represented by numbers); and
- some are somewhere in-between: e.g., a maximum function applies
  to any list of comparable values, such as numbers or strings.

This seems like a great variety, and we might worry about how we can
handle this many different kinds of functions. Fortunately, and
perhaps surprisingly, there is one standard way in which we can think
about writing all these functions! Understanding
and internalizing this process is the goal of this chapter.

#### Making Lists and Taking Them Apart {#Making-Lists-and-Taking-Them-Apart}

So far we’ve seen one way to make a list: by writing
`[list: …]`{.pyret}. While useful, writing lists this way actually
hides their true nature. Every list actually has two parts: a
first element and the rest of the list. The rest of the
list is itself a list, so it too has two parts…and so on.

Consider the list `[list: 1, 2, 3]`{.pyret}. Its first element is `1`{.pyret}, and
the rest of it is `[list: 2, 3]`{.pyret}. For this second list, the first element
is `2`{.pyret} and the rest is `[list: 3]`{.pyret}.


::: {.do-now}
Take apart this third list.
:::


For the third list, the first element is `3`{.pyret} and the rest is
`[list: ]`{.pyret}, i.e., the empty list. In Pyret, we have another way
of writing the empty list: `empty`{.pyret}.

Lists are an instance of structured data: data with component
parts and a well-defined format for the shape of the parts. Lists are
formatted by the first element and the rest of the elements. Tables
are somewhat structured: they are formatted by rows and columns, but
the column names aren’t consistent across all tables. Structured data
is valuable in programming because a predictable format (the
structure) lets us write programs based on that structure. What do we
mean by that?

Programming languages can (and do!) provide built-in operators for
taking apart structured data. These operators are called
accessors. Accessors are defined on the structure of the
datatype alone, independent of the contents of the data. In the case
of lists, there are two accessors: `first`{.pyret} and
`rest`{.pyret}. We use an accessor by writing an expression, followed by
a dot (`.`{.pyret}), followed by the accessor’s name. As we saw with
tables, the dot means "dig into". Thus:

```pyret
l1 = [list: 1, 2, 3]
e1 = l1.first
l2 = l1.rest
e2 = l2.first
l3 = l2.rest
e3 = l3.first
l4 = l3.rest

check:
  e1 is 1
  e2 is 2
  e3 is 3
  l2 is [list: 2, 3]
  l3 is [list: 3]
  l4 is empty
end
```

::: {.do-now}
What are the accessors for tables?
:::

Accessors give a way to take data apart based on their structure
(there is another way that we will see shortly). Is there a way to
also build data based on its structure? So far, we have been
building lists using the `[list: ...]`{.pyret} form, but that doesn’t
emphasize the structural constraint that the `rest`{.pyret} is itself a
list. A structured operator for building lists would clearly show both
a `first`{.pyret} element and a `rest`{.pyret} that is itself a
list. Operators for building structured data are called
constructors.

The constructor for lists is called `link`{.pyret}. It takes two
arguments: a `first`{.pyret} element, and the list to build on (the
`rest`{.pyret} part). Here’s an example of using `link`{.pyret} to create a
three-element list.

```pyret
link(1, link(2, link(3, empty)))
```

The `link`{.pyret} form creates the same underlying list datum as our
previous `[list: ...]`{.pyret} operation, as confirmed by the following
check:

```pyret
check:
  [list: 1, 2, 3] is link(1, link(2, link(3, empty)))
end
```

::: {.do-now}
Look at these two forms of writing lists: what differences do you notice?
:::

::: {.do-now}
Use the `link`{.pyret} form to write a four-element list of fruits containing
`"lychee"`{.pyret}, `"dates"`{.pyret}, `"mango"`{.pyret}, and `"durian"`{.pyret}.
:::

After doing this exercise, you might wonder why anyone would use the
`link`{.pyret} form: it’s more verbose, and makes the individual elements
harder to discern. This form is not very convenient to
humans. But it will prove very valuable to programs!

In particular, the `link`{.pyret} form highlights that we really have
two different structures of lists.
Some lists are empty. All other lists are non-empty
lists, meaning they have at least one `link`{.pyret}. There may be
more interesting structure to some lists (as we will see later), but all lists have this much
in common. Specifically, a list is either


- empty (written `empty`{.pyret} or `[list: ]`{.pyret}), or
- non-empty (written `link(…, …)`{.pyret} or `[list: ]`{.pyret} with
  at least one value inside the brackets), where the rest is also
  a list (and hence may in turn be empty or non-empty, …).

This means we actually have two structural features of lists, both of
which are important when writing programs over lists:


1. Lists can be empty or non-empty
2. Non-empty lists have a first element and a rest of the list

Let’s leverage these two structural features to write some programs to
process lists!

#### Some Example Exercises {#my-len}

To illustrate our thinking, let’s work through a few concrete examples
of list-processing functions. All of these will consume lists; some
will even produce them. Some will transform their inputs (like
`map`{.pyret}), some will select from their inputs (like `filter`{.pyret}),
and some will aggregate their inputs. Since some of these functions already exist in
Pyret, we’ll name them with the prefix `my-`{.pyret} to avoid
errors.[Be sure to use the `my-`{.pyret} name consistently,
including inside the body of the function.]{.margin-note} As we will see, there is a
standard strategy that we can use to approach writing all of these
functions: having you learn this strategy is the goal of this chapter.

#### Structural Problems with Scalar Answers {#Structural-Problems-with-Scalar-Answers}

Let’s write out examples for a few of the functions described
above. We’ll approach writing examples in a very specific, stylized
way. First of all, we should always construct at least two examples:
one with `empty`{.pyret} and the other with at least one `link`{.pyret}, so
that we’ve covered the two very broad kinds of lists. Then, we should
have more examples specific to the kind of list stated in the
problem. Finally, we should have even more examples to illustrate how
we think about solving the problem.

##### my-len : Examples {#len-eg}

We have’t precisely defined what it means to be “the length” of a
list. We confront this right away when trying to write an
example. What is the length of the list `empty`{.pyret}?

::: {.do-now}
What do you think?
:::

Two common examples are `0`{.pyret} and `1`{.pyret}. The latter, `1`{.pyret},
certainly looks reasonable. However, if you write the list as
`[list: ]`{.pyret}, now it doesn’t look so right: this is clearly (as the
name `empty`{.pyret} also suggests) an empty list, and an empty
list has zero elements in it. Therefore, it’s conventional to
declare that

```pyret
my-len(empty) is 0
```
How about a list like `[list: 7]`{.pyret}? Well, it’s clearly got one
element (`7`{.pyret}) in it, so

```pyret
my-len([list: 7]) is 1
```
Similarly, for a list like `[list: 7, 8, 9]`{.pyret}, we would say

```pyret
my-len([list: 7, 8, 9]) is 3
```

Now let’s look at that last example in a different light. Consider
the argument `[list: 7, 8, 9]`{.pyret}. Its first element is `7`{.pyret} and
the rest of it is `[list: 8, 9]`{.pyret}. Well, `7`{.pyret} is a number, not
a list; but `[list: 8, 9]`{.pyret} certainly is a list, so we can ask for
its length. What is `my-len([list: 8, 9])`{.pyret}? It has two
elements, so

```pyret
my-len([list: 8, 9]) is 2
```
The first element of that list is `8`{.pyret} while its rest is
`[list: 9]`{.pyret}. What is its length?
Note that we asked a very similar question before, for the length of
the list `[list: 7]`{.pyret}. But `[list: 7]`{.pyret} is not a
sub-list of `[list: 7, 8, 9]`{.pyret}, which we started with,
whereas `[list: 9]`{.pyret} is. And using the same reasoning as before,
we can say

```pyret
my-len([list: 9]) is 1
```
The rest of this last list is, of course, the empty list, whose length
we have already decided is `0`{.pyret}.

Putting together these examples, and writing out `empty`{.pyret} in its
other form, here’s what we get:

```pyret
my-len([list: 7, 8, 9]) is 3
my-len([list:    8, 9]) is 2
my-len([list:       9]) is 1
my-len([list:        ]) is 0
```
Another way we can write this (paying attention to the right side) is

```pyret
my-len([list: 7, 8, 9]) is 1 + 2
my-len([list:    8, 9]) is 1 + 1
my-len([list:       9]) is 1 + 0
my-len([list:        ]) is     0
```
Where did the `2`{.pyret}, `1`{.pyret}, and `0`{.pyret} on the right sides of
each `+`{.pyret} operation come from? Those are the lengths of the
`rest`{.pyret} component of the input list. In the previous example
block, we wrote those lengths as explicit examples. Let’s substitute
the numbers `2`{.pyret}, `1`{.pyret}, and `0`{.pyret} with the `my-len`{.pyret}
expressions that produce them:

```pyret
my-len([list: 7, 8, 9]) is 1 + my-len([list: 8, 9])
my-len([list:    8, 9]) is 1 + my-len([list:    9])
my-len([list:       9]) is 1 + my-len([list:     ])
my-len([list:        ]) is 0
```
From this, maybe you can start to see a pattern. For an empty list,
the length is `0`{.pyret}. For a non-empty list, it’s the sum of `1`{.pyret}
(the first element’s “contribution” to the list’s length) to the
length of the rest of the list. In other words, we can use the result
of computing `my-len`{.pyret} on the rest of the list to compute the
answer for the entire list.

::: {.do-now}
Each of our examples in this section has written a different check on
the expression `my-len([list: 7, 8, 9])`{.pyret}. Here are those examples
presented together, along with one last one that explicitly uses the
`rest`{.pyret} operation:

```pyret
my-len([list: 7, 8, 9]) is 3
my-len([list: 7, 8, 9]) is 1 + 2
my-len([list: 7, 8, 9]) is 1 + my-len([list: 8, 9])
my-len([list: 7, 8, 9]) is 1 + my-len([list: 7, 8, 9].rest)
```
Check that you agree with each of these assertions. Also check whether
you understand how the right-hand side of each `is`{.pyret} expression
derives from the right-hand-side just above it. The goal of this
exercise is to make sure that you believe that the last check (which
we will turn into code) is equivalent to the first (which we wrote
down when understanding the problem).
:::

##### my-sum : Examples {#sum-eg}

Let’s repeat this process of developing examples on a second function,
this time one that computes the sum of the elements in a list of numbers.
What is the
sum of the list `[list: 7, 8, 9]`{.pyret}? Just adding up the numbers by hand,
the result should be `24`{.pyret}. Let’s see how that works out through
the examples.

Setting aside the empty list for a moment, here are examples that show
the sum computations:

```pyret
my-sum([list: 7, 8, 9]) is 7 + 8 + 9
my-sum([list:    8, 9]) is     8 + 9
my-sum([list:       9]) is         9
```
which (by substitution) is the same as

```pyret
my-sum([list: 7, 8, 9]) is 7 + my-sum([list: 8, 9])
my-sum([list:    8, 9]) is 8 + my-sum([list:    9])
my-sum([list:       9]) is 9 + my-sum([list:     ])
```
From this, we can see that the sum of the empty list must be
`0`{.pyret}:[Zero is called the additive identity: a
fancy way of saying, adding zero to any number N gives you
N. Therefore, it makes sense that it would be the length of the
empty list, because the empty list has no items to contribute to a
sum. Can you figure out what the multiplicative identity is?]{.margin-note}

```pyret
my-sum(empty) is 0
```

Observe, again, how we can use the result of computing `my-sum`{.pyret}
of the rest of the list to compute its result for the whole list.

##### From Examples to Code {#From-Examples-to-Code}

Having developed these examples, we now want to use them to develop a
program that can compute the length or the sum of any list, not
just the specific ones we used in these examples. As we have done up
in earlier chapters, we will leverage patterns in the examples to
figure out how to define the general-purpose function.

Here is one last version of the examples for `my-len`{.pyret}, this time
making the `rest`{.pyret} explicit on the right-hand sides of `is`{.pyret}:

```pyret
my-len([list: 7, 8, 9]) is 1 + my-len([list: 7, 8, 9].rest)
my-len([list:    8, 9]) is 1 + my-len([list:    8, 9].rest)
my-len([list:       9]) is 1 + my-len([list:       9].rest)
my-len([list:        ]) is 0
```
As we did when developing functions over images, let’s try to identify
the common parts of these examples. We start by noticing that most of
the examples have a lot in common, except for the `[list: ]`{.pyret}
(`empty`{.pyret}) case. So let’s separate this into two sets of examples:

```pyret
my-len([list: 7, 8, 9]) is 1 + my-len([list: 7, 8, 9].rest)
my-len([list:    8, 9]) is 1 + my-len([list:    8, 9].rest)
my-len([list:       9]) is 1 + my-len([list:       9].rest)


my-len([list:        ]) is 0
```
With this separation (which follows one of the structural features of
lists that we mentioned earlier), a clearer pattern emerges: for a
non-empty list (called `someList`{.pyret}), we compute its length via the
expression:

```pyret
1 + my-len(someList.rest)
```
In general, then, our `my-len`{.pyret} program needs to determine whether
its input list is empty or non-empty, using this expression with
`.rest`{.pyret} in the non-empty case. How do we indicate different code
based on the structure of the list?

Pyret has a construct called `cases`{.pyret} which is used to distinguish
different forms within a structured datatype. When working with lists,
the general shape of a `cases`{.pyret} expression is:

```pyret
cases (List) e:
  | empty      => …
  | link(f, r) => … f … r …
end
```
where most parts are fixed, but a few you’re free to change:


- `e`{.pyret} is an expression whose value needs to be a list; it
  could be a variable bound to a list, or some complex expression that
  evaluates to a list.
- `f`{.pyret} and `r`{.pyret} are names given to the first and rest of
  the list. You can choose any names you like, though in Pyret, it’s
  conventional to use `f`{.pyret} and `r`{.pyret}.[Occasionally
  using different names can help students recall that they can choose
  how to label the `first`{.pyret} and `rest`{.pyret} components. This can be
  particularly useful for `first`{.pyret}, which has a problem-specific
  meaning (such as `price`{.pyret} in a list of prices, and so on).]{.margin-note}

The right-hand side of every `=>`{.pyret} is an expression.

Here’s how `cases`{.pyret} works in this instance. Pyret first evaluates
`e`{.pyret}. It then checks that the resulting value truly is a list;
otherwise it halts with an error. If it is a list, Pyret examines what
kind of list it is. If it’s an empty list, it runs the
expression after the `=>`{.pyret} in the `empty`{.pyret} clause. Otherwise,
the list is not empty, which means it has a first and rest; Pyret
binds `f`{.pyret} and `r`{.pyret} to the two parts, respectively, and then
evaluates the expression after the `=>`{.pyret} in the `link`{.pyret} clause.

::: {.exercise}
Try using a non-list—e.g., a number—in the `e`{.pyret} position and
see what happens!
:::

Now let’s use `cases`{.pyret} to define `my-len`{.pyret}:

```pyret
fun my-len(l):
  cases (List) l:
    | empty      => 0
    | link(f, r) => 1 + my-len(r)
  end
end
```
This follows from our examples: when the list is empty `my-len`{.pyret}
produces `0`{.pyret}; when it is not empty, we add one to the length of
the rest of the list (here, `r`{.pyret}).

Note that while our most recent collection of `my-len`{.pyret} examples
explicitly said `.rest`{.pyret}, when using `cases`{.pyret} we instead use
just the name `r`{.pyret}, which Pyret has already defined (under the
hood) to be `l.rest`{.pyret}.

Similarly, let’s define `my-sum`{.pyret}:

```pyret
fun my-sum(l):
  cases (List) l:
    | empty      => 0
    | link(f, r) => f + my-sum(r)
  end
end
```
Notice how similar they are in code, and how readily the structure of
the data suggest a structure for the program. This is a pattern you
will get very used to soon!

::: {.strategy}
Leverage the structure of lists and the power of concrete examples to
develop list-processing functions.


- Pick a concrete list with (at least) three elements. Write a
  sequence of examples for each of the entire list and each suffix of
  the list (including the empty list).
- Rewrite each example to express its expected
  answer in terms of the `first`{.pyret} and `rest`{.pyret} data of its input
  list. You don’t have to use the `first`{.pyret} and `rest`{.pyret} operators
  in the new answers, but you should see the `first`{.pyret} and
  `rest`{.pyret} values represented explicitly in the answer.
- Look for a pattern across the answers in the examples. Use these
  to develop the code: write a `cases`{.pyret} expression, filling in the
  right side of each `=>`{.pyret} based on your examples.

This strategy applies to structured data in general, leveraging
components of each datum rather than specifically `first`{.pyret} and
`rest`{.pyret} as presented so far.
:::

#### Structural Problems that Transform Lists {#Structural-Problems-that-Transform-Lists}

Now that we have a systematic way to develop functions that take lists
as input, let’s apply that same strategy to functions that
produce a list as the answer.

##### my-doubles : Examples and Code {#doubles-eg-code}

As always, we’ll begin with some examples. Given a list of numbers, we
want a list that doubles each number (in the order of the
original list). Here’s a reasonable example with three numbers:

```pyret
my-doubles([list: 3, 5, 2]) is [list: 6, 10, 4]
```

As before, let’s write out the answers for each suffix of our example
list as well, including for the `empty`{.pyret} list:

```pyret
my-doubles([list:    5, 2]) is [list:    10, 4]
my-doubles([list:       2]) is [list:        4]
my-doubles([list:        ]) is [list:         ]
```

Now, we rewrite the answer expressions to include the concrete
`first`{.pyret} and `rest`{.pyret} data for each example. Let’s start with
just the `first`{.pyret} data, and just on the first example:

```pyret
my-doubles([list: 3, 5, 2]) is [list: 3 * 2, 10, 4]
my-doubles([list:    5, 2]) is [list:        10, 4]
my-doubles([list:       2]) is [list:            4]
my-doubles([list:        ]) is [list:             ]
```

Next, let’s include the `rest`{.pyret} data (`[list: 5, 2]`{.pyret}) in the
first example. The current answer in the first example is

```pyret
[list: 3 * 2, 10, 4]
```

and that `[list: 10, 4]`{.pyret} is the result of using the function on
`[list: 5, 2]`{.pyret}. We might therefore be tempted to replace the
right side of the first example with:

```pyret
[list: 3 * 2, my-doubles([list: 5, 2])]
```

::: {.do-now}
What value would this expression produce? You might want to try this
example that doesn’t use `my-doubles`{.pyret} directly:

```pyret
[list: 3 * 2, [list: 10, 4]]
```
:::

Oops! We want a single (flat) list, not a list-within-a-list. This
feels like it is on the right track in terms of reworking the answer
to use the `first`{.pyret} and `rest`{.pyret} values, but we’re clearly not
quite there yet.

::: {.do-now}
What value does the following expression produce?

```pyret
link(3 * 2, [list: 10, 4])
```
:::

Notice the difference between the two expressions in these last two
exercises: the latter used `link`{.pyret} to put the value involving
`first`{.pyret} into the conversion of the `rest`{.pyret}, while the former
tried to do this with `list:`{.pyret}.

::: {.do-now}
How many elements are in the lists that result from each of the
following expressions?

```pyret
[list: 25, 16, 32]
[list: 25, [list: 16, 32]]
link(25, [list: 16, 32])
```
:::

::: {.do-now}
Summarize the difference between how `link`{.pyret} and `list:`{.pyret}
combine an element and a list. Try additional examples at the
interactions prompt if needed to explore these ideas.
:::

The takeaway here is that we use `link`{.pyret} to insert an
element into an existing list, whereas we use `list:`{.pyret} to make a
new list that contains the old list as an element. Going back
to our examples, then, we include `rest`{.pyret} in the first example by
writing it as follows:

```pyret
my-doubles([list: 3, 5, 2]) is link(3 * 2, [list: 10, 4])
my-doubles([list:    5, 2]) is [list:        10, 4]
my-doubles([list:       2]) is [list:            4]
my-doubles([list:        ]) is [list:             ]
```

which we then convert to

```pyret
my-doubles([list: 3, 5, 2]) is link(3 * 2, my-doubles([list: 5, 2]))
my-doubles([list:    5, 2]) is [list:        10, 4]
my-doubles([list:       2]) is [list:            4]
my-doubles([list:        ]) is [list:             ]
```

Applying this idea across the examples, we get:

```pyret
my-doubles([list: 3, 5, 2]) is link(3 * 2, my-doubles([list: 5, 2]))
my-doubles([list:    5, 2]) is link(5 * 2, my-doubles([list: 2]))
my-doubles([list:       2]) is link(2 * 2, my-doubles([list: ]))
my-doubles([list:        ]) is [list:             ]
```

Now that we have examples that explicitly use the `first`{.pyret} and
`rest`{.pyret} elements, we can produce to write the `my-doubles`{.pyret}
function:

```pyret
fun my-doubles(l):
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      link(f * 2, my-doubles(r))
  end
end
```

##### my-str-len : Examples and Code {#str-len-eg-code}

In `my-doubles`{.pyret}, the input and output lists have the same type of
element. Functions can also produce lists whose contents have a
different type from the input list. Let’s work through an example.
Given a list of strings, we
want the lengths of each string (in the same order as in the input list). Thus, here’s a
reasonable example:

```pyret
my-str-len([list: "hi", "there", "mateys"]) is [list: 2, 5, 6]
```
As we have before, we should consider the answers for each
sub-problem of the above example:

```pyret
my-str-len([list:       "there", "mateys"]) is [list:    5, 6]
my-str-len([list:                "mateys"]) is [list:       6]
```

Or, in other words:

```pyret
my-str-len([list: "hi", "there", "mateys"]) is link(2, [list: 5, 6])
my-str-len([list:       "there", "mateys"]) is link(5, [list:    6])
my-str-len([list:                "mateys"]) is link(6, [list:     ])
```
which tells us that the response for the empty list should be
`empty`{.pyret}:

```pyret
my-str-len(empty) is empty
```

The next step is to rework the answers in the examples to make the
`first`{.pyret} and `rest`{.pyret} parts explicit. Hopefully by now you are
starting to detect a pattern: The result on the rest of the list
appears explicitly as another example. Therefore, we’ll start by
getting the `rest`{.pyret} value of each example input into the answer:

```pyret
my-str-len([list: "hi", "there", "mateys"]) is link(2, my-str-len([list: "there", "mateys"]))
my-str-len([list:       "there", "mateys"]) is link(5, my-str-len([list:          "mateys"]))
my-str-len([list:                "mateys"]) is link(6, my-str-len([list:                  ]))
my-str-len([list:                        ]) is [list: ]
```

All that remains now is to figure out how to work the `first`{.pyret}
values into the outputs. In the context of this problem, this means we
need to convert `"hi"`{.pyret} into `2`{.pyret}, `"there"`{.pyret} into
`5`{.pyret}, and so on. From the problem statement, we know that `2`{.pyret}
and `5`{.pyret} are meant to be the lengths (character counts) of the
corresponding strings. The operation that determines the length of a
string is called `string-length`{.pyret}. Thus, our examples appear as:

```pyret
my-str-len([list: "hi", "there", "mateys"]) is link(string-length("hi"), my-str-len([list: "there", "mateys"]))
my-str-len([list:       "there", "mateys"]) is link(string-length("there"), my-str-len([list:          "mateys"]))
my-str-len([list:                "mateys"]) is link(string-length("mateys"), my-str-len([list: ]))
my-str-len([list:                        ]) is [list: ]
```

From here, we write a function that captures the pattern developed
across our examples:

```pyret
fun my-str-len(l):
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      link(string-length(f), my-str-len(r))
  end
end
```

#### Structural Problems that Select from Lists {#Structural-Problems-that-Select-from-Lists}

In the previous section, we saw functions that transform list
elements (by doubling numbers or counting characters). The type of the
output list may or may not be the same as the type of the input
list. Other functions that produce lists instead select
elements: every element in the output list was in the input list, but
some input-list elements might not appear in the output list. This
section adapts our method of deriving functions from examples to
accommodate selection of elements.

##### my-pos-nums : Examples and Code {#pos-nums-eg-code}

As our first example, we will select the positive numbers from a list
that contains both positive and non-positive numbers.

::: {.do-now}
Construct the sequence of examples that we obtain from the input
`[list: 1, -2, 3, -4]`{.pyret}.
:::

Here we go:

```pyret
my-pos-nums([list: 1, -2, 3, -4]) is [list: 1, 3]
my-pos-nums([list:    -2, 3, -4]) is [list:    3]
my-pos-nums([list:        3, -4]) is [list:    3]
my-pos-nums([list:           -4]) is [list:     ]
my-pos-nums([list:             ]) is [list:     ]
```
We can write this in the following form:

```pyret
my-pos-nums([list: 1, -2, 3, -4]) is link(1, [list: 3])
my-pos-nums([list:    -2, 3, -4]) is         [list: 3]
my-pos-nums([list:        3, -4]) is link(3, [list: ])
my-pos-nums([list:           -4]) is         [list: ]
my-pos-nums([list:             ]) is         [list: ]
```
or, even more explicitly,

```pyret
my-pos-nums([list: 1, -2, 3, -4]) is link(1, my-pos-nums([list: -2, 3, -4]))
my-pos-nums([list:    -2, 3, -4]) is         my-pos-nums([list:     3, -4])
my-pos-nums([list:        3, -4]) is link(3, my-pos-nums([list:        -4]))
my-pos-nums([list:           -4]) is         my-pos-nums([list:          ])
my-pos-nums([list:             ]) is         [list: ]
```
Unlike in the example sequences for functions that transform lists,
here we see that the answers have different shapes: some involve a
`link`{.pyret}, while others simply process the `rest`{.pyret} of the
list. Whenever we need different shapes of outputs across a set of
examples, we will need an `if`{.pyret} expression in our code to
distinguish the conditions that yield each shape.

What determines which shape of output we get? Let’s rearrange the
examples (other than the empty-list input) by output shape:

```pyret
my-pos-nums([list: 1, -2, 3, -4]) is link(1, my-pos-nums([list: -2, 3, -4]))
my-pos-nums([list:        3, -4]) is link(3, my-pos-nums([list:        -4]))

my-pos-nums([list:    -2, 3, -4]) is         my-pos-nums([list:     3, -4])
my-pos-nums([list:           -4]) is         my-pos-nums([list:          ])
```
Re-organized, we can see that the examples that use `link`{.pyret} have a
positive number in the `first`{.pyret} position, while the ones that
don’t simply process the `rest`{.pyret} of the list. That indicates that
our `if`{.pyret} expression needs to ask whether the `first`{.pyret} element
in the list is positive. This yields the following program:

```pyret
fun my-pos-nums(l):
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      if f > 0:
        link(f, my-pos-nums(r))
      else:
        my-pos-nums(r)
      end
  end
end
```

::: {.do-now}
Is our set of examples comprehensive?
:::

Not really. There are many examples we haven’t considered, such
as lists that end with positive numbers and lists with `0`{.pyret}.

::: {.exercise}
Work through these examples and see how they affect the program!
:::

##### my-alternating : Examples and Code {#alternating-eg-code}

Now let’s consider a problem that selects elements not by value, but
by position. We want to write a function that selects
alternating elements from a list. Once again, we’re going to work from examples.


::: {.do-now}
Work out the results for `my-alternating`{.pyret} starting from the list
`[list: 1, 2, 3, 4, 5, 6]`{.pyret}.
:::

Here’s how they work out:
<alternating-egs-1> ::=
```pyret
check:
  my-alternating([list: 1, 2, 3, 4, 5, 6]) is [list: 1, 3, 5]
  my-alternating([list:    2, 3, 4, 5, 6]) is [list: 2, 4, 6]
  my-alternating([list:       3, 4, 5, 6]) is [list:    3, 5]
  my-alternating([list:          4, 5, 6]) is [list:    4, 6]
end
```
Wait, what’s that? The two answers above are each correct, but
the second answer does not help us in any way construct the
first answer. That means the way we’ve solved these problems until
now is not enough for this new kind of problem. It’s still useful,
though: notice that there’s a connection between the first example and
the third, as well as between the second example and the fourth. This
observation is consistent with our goal of selecting alternating elements.

What would something like this look like in code? Before we try to
write the function, let’s rewrite the first example in terms of the
third:

```pyret
my-alternating([list: 1, 2, 3, 4, 5, 6]) is [list: 1, 3, 5]
my-alternating([list:       3, 4, 5, 6]) is [list:    3, 5]

my-alternating([list: 1, 2, 3, 4, 5, 6]) is link(1, my-alternating([list: 3, 4, 5, 6]))
```

Note that in the rewritten version, we are dropping two
elements from the list before using `my-alternating`{.pyret} again, not
just one. We will have to figure out how to handle that in our code.

Let’s start with our usual function pattern with a `cases`{.pyret}
expression:

```pyret
fun my-alternating(l):
  cases (List) l:
    | empty => [list:]
    | link(f, r) => link(f, … r …)
  end
end
```

Note that we cannot simply call `my-alternating`{.pyret} on `r`{.pyret},
because `r`{.pyret} excludes only one item from the list, not two as this
problem requires. We have to break down `r`{.pyret} as well, in order to
get to the `rest`{.pyret} of the `rest`{.pyret} of the original list. To do
this, we use another `cases`{.pyret} expression, nested within the first
`cases`{.pyret} expression:

```pyret
fun my-alternating(l):
  cases (List) l:
    | empty => [list:]
    | link(f, r) =>
      cases (List) r:  # note: deconstructing r, not l
        | empty => ??? # note the ???
        | link(fr, rr) =>
          # fr = first of rest, rr = rest of rest
          link(f, my-alternating(rr))
      end
  end
end
```
This code is consistent with the example that we just worked out. But
note that we still have a bit of unfinished work to do: we need to
decide what to do in the `empty`{.pyret} case of the inner `cases`{.pyret}
expression (marked by `???`{.pyret} in the code).

A common temptation at this point is to replace the `???`{.pyret} with
`[list:]`{.pyret}. After all, haven’t we always returned `[list:]`{.pyret} in
the `empty`{.pyret} cases?

::: {.do-now}
Replace `???`{.pyret} with `[list:]`{.pyret} and test the program on our
original examples:

```pyret
my-alternating([list: 1, 2, 3, 4, 5, 6]) is [list: 1, 3, 5]
my-alternating([list:    2, 3, 4, 5, 6]) is [list: 2, 4, 6]
my-alternating([list:       3, 4, 5, 6]) is [list:    3, 5]
my-alternating([list:          4, 5, 6]) is [list:    4, 6]
```
What do you observe?
:::

Oops! We’ve written a program that appears to work on lists with an
even number of elements, but not on lists with an odd number of
elements. How did that happen? The only part of this code that we
guessed at was how to fill in the `empty`{.pyret} case of the inner
`cases`{.pyret}, so the issue must be there. Rather than focus on the
code, however, focus on the examples. We need a simple example
that would land on that part of the code. We get to that spot when the
list `l`{.pyret} is not empty, but `r`{.pyret} (the rest of `l`{.pyret}) is
empty. In other words, we need an example with only one element.

::: {.do-now}
Finish the following example:

```pyret
my-alternating([list: 5]) is ???
```
:::


Given a list with one element, that element should be included in a
list of alternating elements. Thus, we should finish this example as

```pyret
my-alternating([list: 5]) is [list: 5]
```

::: {.do-now}
Use this example to update the result of `my-alternating`{.pyret} when
`r`{.pyret} is `empty`{.pyret} in our code.
:::

Leveraging this new example, the final version of
`my-alternating`{.pyret} is as follows:

```pyret
fun my-alternating(l):
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      cases (List) r: # note: deconstructing r, not l
        | empty =>    # the list has an odd number of elements
          [list: f]
        | link(fr, rr) =>
          # fr = first of rest, rr = rest of rest
          link(f, my-alternating(rr))
      end
  end
end
```

What’s the takeaway from this problem? There are two:


- Don’t skip the small examples: the result of a list-processing
  function on the `empty`{.pyret} case won’t always be `empty`{.pyret}.
- If a problem asks you to work with multiple elements from the
  front of a list, you can nest `cases`{.pyret} expressions to access later
  elements.

These takeaways will matter again in future examples: keep an eye out
for them!

#### Structural Problems Over Relaxed Domains {#struct-prob-sub-dom}

##### my-max : Examples {#my-max}

Now let’s find the maximum value of a list. Let’s assume for
simplicity that we’re dealing with just lists of numbers. What kinds
of lists should we construct? Clearly, we should have empty and
non-empty lists…but what else? Is a list like `[list: 1, 2, 3]`{.pyret} a
good example? Well, there’s nothing wrong with it, but we should also
consider lists where the maximum is at the beginning rather than at the
end; the maximum might be in the middle; the maximum might be
repeated; the maximum might be negative; and so on. While not
comprehensive, here is a small but interesting set of examples:

```pyret
my-max([list: 1, 2, 3]) is 3
my-max([list: 3, 2, 1]) is 3
my-max([list: 2, 3, 1]) is 3
my-max([list: 2, 3, 1, 3, 2]) is 3
my-max([list: 2, 1, 4, 3, 2]) is 4
my-max([list: -2, -1, -3]) is -1
```
What about `my-max(empty)`{.pyret}?


::: {.do-now}
Could we define `my-max(empty)`{.pyret} to be `0`{.pyret}? Returning
`0`{.pyret} for the empty list has worked well twice already!
:::


We’ll return to this in a while.

Before we proceed, it’s useful to know that there’s a function called
`num-max`{.pyret} already defined in Pyret, that compares two numbers:

```pyret
num-max(1, 2) is 2
num-max(-1, -2) is -1
```


::: {.exercise}
Suppose `num-max`{.pyret} were not already built in. Can you define it?
You will find what you learned about [Booleans](Conditionals_and_Booleans.html##booleans)
handy. Remember to write some tests!
:::

Now we can look at `my-max`{.pyret} at work:

```pyret
my-max([list: 1, 2, 3]) is 3
my-max([list:    2, 3]) is 3
my-max([list:       3]) is 3
```
Hmm. That didn’t really teach us anything, did it? Maybe, we can’t be
sure. And we still don’t know what to do with `empty`{.pyret}.

Let’s try the second example input:

```pyret
my-max([list: 3, 2, 1]) is 3
my-max([list:    2, 1]) is 2
my-max([list:       1]) is 1
```
This is actually telling us something useful as well, but maybe we
can’t see it yet. Let’s take on something more ambitious:

```pyret
my-max([list: 2, 1, 4, 3, 2]) is 4
my-max([list:    1, 4, 3, 2]) is 4
my-max([list:       4, 3, 2]) is 4
my-max([list:          3, 2]) is 3
my-max([list:             2]) is 2
```
Observe how the maximum of the rest of the list gives us a candidate
answer, but comparing it to the first element gives us a definitive
one:

```pyret
my-max([list: 2, 1, 4, 3, 2]) is num-max(2, 4)
my-max([list:    1, 4, 3, 2]) is num-max(1, 4)
my-max([list:       4, 3, 2]) is num-max(4, 3)
my-max([list:          3, 2]) is num-max(3, 2)
my-max([list:             2]) is …
```
The last one is a little awkward: we’d like to write

```pyret
my-max([list:             2]) is num-max(2, …)
```
but we don’t really know what the maximum (or minimum, or any other
element) of the empty list is, but we can only provide numbers
to `num-max`{.pyret}. Therefore, leaving out that dodgy case, we’re left
with

```pyret
my-max([list: 2, 1, 4, 3, 2]) is num-max(2, my-max([list: 1, 4, 3, 2]))
my-max([list:    1, 4, 3, 2]) is num-max(1, my-max([list:    4, 3, 2]))
my-max([list:       4, 3, 2]) is num-max(4, my-max([list:       3, 2]))
my-max([list:          3, 2]) is num-max(3, my-max([list:          2]))
```
Our examples have again helped: they’ve revealed how we can use the
answer for each rest of the list to compute the answer for the whole
list, which in turn is the rest of some other list, and so on. If you
go back and look at the other example lists we wrote above, you’ll see
the pattern holds there too.

However, it’s time we now confront the `empty`{.pyret} case. The real
problem is that we don’t have a maximum for the empty list: for any
number we might provide, there is always a number bigger than it
(assuming our computer is large enough) that could have been the
answer instead. In short, it’s nonsensical to ask for the maximum (or
minimum) of the empty list: the concept of “maximum” is only defined
on non-empty lists! That is, when asked for the maximum of an empty
list, we should signal an error:

```pyret
my-max(empty) raises ""
```
(which is how, in Pyret, we say that it will generate an error; we
don’t care about the details of the error, hence the empty string).

##### my-max : From Examples to Code {#struct-traverse-element-procedure-lib-render-cond-rkt-38-12-From-Examples-to-Code}

Once again, we can codify the examples above, i.e., turn them into a
uniform program that works for all instances. However, we now have a
twist. If we blindly followed the pattern we’ve used earlier, we would
end up with:

```pyret
fun my-max(l):
  cases (List) l:
    | empty      => raise("not defined for empty lists")
    | link(f, r) => num-max(f, my-max(r))
  end
end
```

::: {.do-now}
What’s wrong with this?
:::

Consider the list `[list: 2]`{.pyret}. This turns into

```pyret
num-max(2, my-max([list: ]))
```
which of course raises an error. Therefore, this function never works
for any list that has one or more elements!

That’s because we need to make sure we aren’t trying to compute the
maximum of the empty list.
Going back to our examples, we see that what we need to do, before
calling `my-max`{.pyret}, is check whether the rest of the list is
empty. If it is, we do not want to call `my-max`{.pyret} at all. That is:

```pyret
fun my-max(l):
  cases (List) l:
    | empty      => raise("not defined for empty lists")
    | link(f, r) =>
      cases (List) r:
        | empty => …
        | …
      end
  end
end
```
We’ll return to what to do when the rest is not empty in a moment.

If the rest of the list `l`{.pyret} is empty, our examples above tell us
that the maximum is the first element in the list. Therefore, we can
fill this in:

```pyret
fun my-max(l):
  cases (List) l:
    | empty      => raise("not defined for empty lists")
    | link(f, r) =>
      cases (List) r:
        | empty => f
        | …
      end
  end
end
```
Note in particular the absence of a call to `my-max`{.pyret}. If the list
is not empty, however, our examples above tell us that `my-max`{.pyret}
will give us the maximum of the rest of the list, and we just need to
compare this answer with the first element (`f`{.pyret}):

```pyret
fun my-max(l):
  cases (List) l:
    | empty      => raise("not defined for empty lists")
    | link(f, r) =>
      cases (List) r:
        | empty => f
        | else  => num-max(f, my-max(r))
      end
  end
end
```
And sure enough, this definition does the job!

#### More Structural Problems with Scalar Answers {#More-Structural-Problems-with-Scalar-Answers}

##### my-avg : Examples {#avg-eg}

Let’s now try to compute the average of a list of numbers. Let’s start
with the example list `[list: 1, 2, 3, 4]`{.pyret} and work out more
examples from it. The average of numbers in this list is clearly
`(1 + 2 + 3 + 4)/4`{.pyret}, or `10/4`{.pyret}.

Based on the list’s structure, we see that the rest of the list is
`[list: 2, 3, 4]`{.pyret}, and the rest of that is `[list: 3, 4]`{.pyret},
and so on. The resulting averages are:

```pyret
my-avg([list: 1, 2, 3, 4]) is 10/4
my-avg([list:    2, 3, 4]) is 9/3
my-avg([list:       3, 4]) is 7/2
my-avg([list:          4]) is 4/1
```
The problem is, it’s simply not clear how we get from the answer for
the sub-list to the answer for the whole list. That is, given the
following two bits of information:


- The average of the remainder of the list is `9/3`{.pyret}, i.e.,
  `3`{.pyret}.
- The first number in the list is `1`{.pyret}.

How do we determine that the average of the whole list must be
`10/4`{.pyret}? If it’s not clear to you, don’t worry: with just those
two pieces of information, it’s impossible!

Here’s a simpler example that explains why. Let’s suppose the first
value in a list is `1`{.pyret}, and the average of the rest of the list
is `2`{.pyret}. Here are two very different lists that fit this
description:

```pyret
[list: 1, 2]    # the rest has one element with sum 2
[list: 1, 4, 0] # the rest has two elements with sum 4
```
The average of the entire first list is `3/2`{.pyret}, while the average
of the entire second list is `5/3`{.pyret}, and the two are not the same.

That is, to compute the average of a whole list, it’s not even useful to
know the average of the rest of the list. Rather, we need to
know the sum and the length of the rest of the
list. With these two, we can add the first to the sum, and `1`{.pyret} to
the length, and compute the new average.

In principle, we could try to make a `average`{.pyret} function that
returns all this information. Instead, it will be a lot simpler to
simply decompose the task into two smaller tasks. After all, we
have already seen how to compute the length and how to compute the
sum. The average, therefore, can just use these existing functions:

```pyret
fun my-avg(l):
  my-sum(l) / my-len(l)
end
```

::: {.do-now}
What should be the average of the empty list? Does the above code
produce what you would expect?
:::

Just as we argued earlier about the maximum
[[Structural Problems Over Relaxed Domains](processing-lists.html##struct-prob-sub-dom)], the average of the empty list isn’t
a well-defined concept. Therefore, it would be appropriate to signal
an error. The implementation above does this, but poorly: it reports
an error on division. A better programming practice would be to
catch this situation and report the error right away, rather than
hoping some other function will report the error.

::: {.exercise}
Alter `my-avg`{.pyret} above to signal an error when given the empty
list.
:::

Therefore, we see that the process we’ve used—of inferring code from
examples—won’t always suffice, and we’ll need more
sophisticated techniques to solve some problems. However, notice that
working from examples helps us quickly identify situations
where this approach does and doesn’t work. Furthermore, if you look
more closely you’ll notice that the examples above do hint at
how to solve the problem: in our very first examples, we wrote answers
like `10/4`{.pyret}, `9/3`{.pyret}, and `7/2`{.pyret}, which correspond to the
sum of the numbers divided by the length. Thus, writing the answers in
this form (as opposed, for instance, to writing the second of those as
`3`{.pyret}) already reveals a structure for a solution.

#### Structural Problems with Accumulators {#accumulators}

##### my-running-sum : First Attempt {#running-sum-1st-attempt}

One more time, we’ll begin with an example.

::: {.do-now}
Work out the results for `my-running-sum`{.pyret} starting from the list
`[list: 1, 2, 3, 4, 5]`{.pyret}.
:::

Here’s what our first few examples look like:
<running-sum-egs-1> ::=
```pyret
check:
  my-running-sum([list: 1, 2, 3, 4, 5]) is [list: 1, 3, 6, 10, 15]
  my-running-sum([list:    2, 3, 4, 5]) is [list: 2, 5, 9, 14]
  my-running-sum([list:       3, 4, 5]) is [list: 3, 7, 12]
end
```
Again, there doesn’t appear to be any clear connection between the
result on the rest of the list and the result on the entire list.

(That isn’t strictly true: we can still line up the answers as
follows:

```pyret
my-running-sum([list: 1, 2, 3, 4, 5]) is [list: 1, 3, 6, 10, 15]
my-running-sum([list:    2, 3, 4, 5]) is [list:    2, 5,  9, 14]
my-running-sum([list:       3, 4, 5]) is [list:       3,  7, 12]
```
and observe that we’re computing the answer for the rest of the list,
then adding the first element to each element in the answer, and
`link`{.pyret}ing the first element to the front. In principle, we can
compute this solution directly, but for
now that may be more work than finding a simpler way to answer it.)

##### my-running-sum : Examples and Code {#running-sum-eg-code}

Recall how we began in [`my-running-sum`{.pyret}: First Attempt](processing-lists.html##running-sum-1st-attempt). Our
examples [[<running-sum-egs-1>](processing-lists.html#%28elem._running-sum-egs-1%29)] showed the following
problem. When we process the rest of the list, we have forgotten
everything about what preceded it. That is, when processing the list
starting at `2`{.pyret} we forget that we’ve seen a `1`{.pyret} earlier;
when starting from `3`{.pyret}, we forget that we’ve seen both `1`{.pyret}
and `2`{.pyret} earlier; and so on. In other words, we keep
forgetting the past. We need some way of avoiding that.

The easiest thing we can do is simply change our function to carry
along this “memory”, or what we’ll call an accumulator. That
is, imagine we were defining a new function, called `my-rs`{.pyret}. It
will consume a list of numbers and produce a list of numbers, but in
addition it will also take the sum of numbers preceding the
current list.


::: {.do-now}
What should the initial sum be?
:::


Initially there is no “preceding list”, so we will use the additive
identity: `0`{.pyret}. The type of `my-rs`{.pyret} is

```pyret
my-rs :: Number, List<Number> -> List<Number>
```

Let’s now re-work our examples from [<running-sum-egs-1>](processing-lists.html#%28elem._running-sum-egs-1%29) as
examples of `my-rs`{.pyret} instead. The examples use the `+`{.pyret}
operator to append two lists into one (the elements of the first list
followed by the elements of the second):

```pyret
my-rs( 0, [list: 1, 2, 3, 4, 5]) is [list:  0 + 1] + my-rs( 0 + 1, [list: 2, 3, 4, 5])
my-rs( 1, [list:    2, 3, 4, 5]) is [list:  1 + 2] + my-rs( 1 + 2, [list:    3, 4, 5])
my-rs( 3, [list:       3, 4, 5]) is [list:  3 + 3] + my-rs( 3 + 3, [list:       4, 5])
my-rs( 6, [list:          4, 5]) is [list:  6 + 4] + my-rs( 6 + 4, [list:          5])
my-rs(10, [list:             5]) is [list: 10 + 5] + my-rs(10 + 5, [list:           ])
my-rs(15, [list:              ]) is empty
```
That is, `my-rs`{.pyret} translates into the following code:

```pyret
fun my-rs(acc, l):
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      new-sum = acc + f
      link(new-sum, my-rs(new-sum, r))
  end
end
```
All that’s then left is to call it from `my-running-sum`{.pyret}:

```pyret
fun my-running-sum(l):
  my-rs(0, l)
end
```

Observe that we do not change `my-running-sum`{.pyret} itself to take
extra arguments. The correctness of our code depends on the initial
value of `acc`{.pyret} being 0. If we added a parameter for `acc`{.pyret},
any code that calls `my-running-sum`{.pyret} could supply an unexpected
value, which would distort the result. In addition, since the value is
fixed, adding the parameter would amount to shifting additional (and
needless) work onto others who use our code.

##### my-alternating : Examples and Code {#alternating-accumulator}

Recall our examples in [`my-alternating`{.pyret}:
Examples and Code](processing-lists.html##alternating-eg-code). There, we
noticed that the code built on every-other example. We might have
chosen our examples differently, so that from one example to the next
we skipped two elements rather than one.
Here we will see another way to think about the same problem.

Return to the examples we’ve already seen
[[<alternating-egs-1>](processing-lists.html#%28elem._alternating-egs-1%29)]. We wrote `my-alternating`{.pyret}
to traverse the list essentially two elements at a time. Another option is to traverse it just one
element at a time, but keeping track of whether we’re at an odd
or even element—i.e., add “memory” to our program. Since we just
need to track that one piece of information, we can use a
`Boolean`{.pyret} to do it. Let’s define a new function for this purpose:

```pyret
my-alt :: List<Any>, Boolean -> List<Any>
```
The extra argument accumulates whether we’re at an element to keep or
one to discard.

We can reuse the existing template for list functions. When we have an
element, we have to consult the accumulator whether to keep it or
not. If its value is `true`{.pyret} we `link`{.pyret} it to the answer;
otherwise we ignore it. As we process the rest of the list, however,
we have to remember to update the accumulator: if we kept an element
we don’t wish to keep the next one, and vice versa.

```pyret
fun my-alt(l, keep):
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      if keep:
        link(f, my-alt(r, false))
      else:
        my-alt(r, true)
      end
  end
end
```
Finally, we have to determine the initial value of the accumulator. In
this case, since we want to keep alternating elements starting
with the first one, its initial value should be `true`{.pyret}:

```pyret
fun my-alternating(l):
  my-alt(l, true)
end
```

::: {.exercise}
Define `my-max`{.pyret} using an accumulator. What does the accumulator
represent? Do you encounter any difficulty?
:::

#### Dealing with Multiple Answers {#Dealing-with-Multiple-Answers}

Our discussion above has assumed there is only one answer for a given
input. This is often true, but it also depends on how the problem is
worded and how we choose to generate examples. We will study this in
some detail now.

##### uniq : Problem Setup {#uniq}

Consider the task of writing `uniq`{.pyret}:[uniq is the
name of a Unix utility with similar behavior; hence the spelling of
the name.]{.margin-note} given a list of values, it produces a collection of the
same elements while avoiding any duplicates (hence `uniq`{.pyret}, short
for “unique”).

Consider the following input: `[list: 1, 2, 1, 3, 1, 2, 4, 1]`{.pyret}.

::: {.do-now}
What is the sequence of examples this input generates? It’s
really important you stop and try to do this by hand. As we
will see there are multiple solutions, and it’s useful for you to
consider what you generate. Even if you can’t generate a sequence,
trying to do so will better prepare you for what you read next.
:::

How did you obtain your example? If you just “thought about it for a
moment and wrote something down”, you may or may not have gotten
something you can turn into a program. Programs can only proceed
systematically; they can’t “think”. So, hopefully you took a
well-defined path to computing the answer.

##### uniq : Examples {#uniq-eg}

It turns out there are several possible answers, because we
have (intentionally) left the problem unspecified. Suppose there are
two instances of a value in the list; which one do we keep, the first
or the second? On the one hand, since the two instances must be
equivalent it doesn’t matter, but it does for writing concrete
examples and deriving a solution.

For instance, you might have generated this sequence:

```pyret
examples:
  uniq([list: 1, 2, 1, 3, 1, 2, 4, 1]) is [list: 3, 2, 4, 1]
  uniq([list:    2, 1, 3, 1, 2, 4, 1]) is [list: 3, 2, 4, 1]
  uniq([list:       1, 3, 1, 2, 4, 1]) is [list: 3, 2, 4, 1]
  uniq([list:          3, 1, 2, 4, 1]) is [list: 3, 2, 4, 1]
  uniq([list:             1, 2, 4, 1]) is [list:    2, 4, 1]
  uniq([list:                2, 4, 1]) is [list:    2, 4, 1]
  uniq([list:                   4, 1]) is [list:       4, 1]
  uniq([list:                      1]) is [list:          1]
  uniq([list:                       ]) is [list:           ]
end
```
However, you might have also generated sequences that began with

```pyret
uniq([list: 1, 2, 1, 3, 1, 2, 4, 1]) is [list: 1, 2, 3, 4]
```
or

```pyret
uniq([list: 1, 2, 1, 3, 1, 2, 4, 1]) is [list: 4, 3, 2, 1]
```
and so on. Let’s work with the examples we’ve worked out above.

##### uniq : Code {#struct-traverse-element-procedure-lib-render-cond-rkt-38-12-Code}

What is the systematic approach that gets us to this answer?
When given a non-empty list, we split it into its first element and
the rest of the list. Suppose we have the answer to `uniq`{.pyret}
applied to the rest of the list. Now we can ask: is the first element
in the rest of the list? If it is, then we can ignore it, since it is
certain to be in the `uniq`{.pyret} of the rest of the list. If, however,
it is not in the rest of the list, it’s critical that we `link`{.pyret}
it to the answer.

This translates into the following program. For the empty list, we
return the empty list. If the list is non-empty, we check whether the
first is in the rest of the list. If it is not, we include it;
otherwise we can ignore it for now.

This results in the following program:

```pyret
fun uniq-rec(l :: List<Any>) -> List<Any>:
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      if r.member(f):
        uniq-rec(r)
      else:
        link(f, uniq-rec(r))
      end
  end
end
```
which we’ve called `uniq-rec`{.pyret} instead of `uniq`{.pyret} to
differentiate it from other versions of `uniq`{.pyret}.

::: {.exercise}
Note that we’re using `.member`{.pyret} to check whether an element is a
member of the list. Write a function `member`{.pyret} that consumes an
element and a list, and tells us whether the element is a member of
the list.
:::

::: {.exercise}
Uniqueness checking has many practical applications. For example, one
might have a list of names of people who have registered to vote in an
election. To keep the voting fair, with only one vote allowed per
person, we should remove duplicate names from the list.

1. Propose a set of examples for a function `rem-duplicate-voters`{.pyret}
  that takes a list of voter names and returns a list in which duplicate
  registrations have been removed. In developing your examples, consider
  real-world scenarios that you can imagine arising when identifying
  duplicate names. Can you identify cases in which two names
  might appear to be the same person, but not be? Cases in which two
  names might appear different but be referring to the same person?
2. What might you need to change about our current `uniq-rec`{.pyret}
  function to handle a situation like removing duplicate voters?
:::

::: {.responsible-cs}
The data de-duplication context in the above exercise reminds us that
different contexts may call for different notions of when two data values
are the same. Sometimes, we want exact matching to determine that two
strings are equal. Sometimes, we need methods that normalize data,
either in simple ways like capitalization or subtler ways based on
middle initials. Sometimes, we need more information (like street
addresses in addition to names) in order to determine whether two
items in a list should be considered “the same”.

It is easy to write programs that encode assumptions about our data
that might not apply in practice. This is again a situation that can
be helped by thinking about the concrete examples on which your code
needs to work in context.
:::

##### uniq : Reducing Computation {#struct-traverse-element-procedure-lib-render-cond-rkt-38-12-Reducing-Computation}

Notice that this function has a repeated expression. Instead of
writing it twice, we could call it just once and use the result in
both places:

```pyret
fun uniq-rec2(l :: List<Any>) -> List<Any>:
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      ur = uniq-rec2(r)
      if r.member(f):
        ur
      else:
        link(f, ur)
      end
  end
end
```
You might think, because we replaced two function calls with one, that
we’ve reduced the amount of computation the program does. It does not!
The two function calls are both in the two branches of the same
conditional; therefore, for any given list element, only one or the
other call to `uniq`{.pyret} happens. In fact, in both cases, there was
one call to `uniq`{.pyret} before, and there is one now. So we have
reduced the number of calls in the source program, but not the number
that take place when the program runs. In that sense, the name of this
section was intentionally misleading!

However, there is one useful reduction we can perform, which is
enabled by the structure of `uniq-rec2`{.pyret}. We currently check
whether `f`{.pyret} is a member of `r`{.pyret}, which is the list of
all the remaining elements. In our example, this means that in
the very second turn, we check whether `2`{.pyret} is a member of the list
`[list: 1, 3, 1, 2, 4, 1]`{.pyret}. This is a list of six elements,
including three copies of `1`{.pyret}. We compare `2`{.pyret} against
two copies of `1`{.pyret}. However, we gain nothing from the
second comparison. Put differently, we can think of `uniq(r)`{.pyret} as
a “summary” of the rest of the list that is exactly as good as
`r`{.pyret} itself for checking membership, with the advantage that it
might be significantly shorter. This, of course, is exactly what
`ur`{.pyret} represents. Therefore, we can encode this intuition as
follows:

```pyret
fun uniq-rec3(l :: List<Any>) -> List<Any>:
  cases (List) l:
    | empty => empty
    | link(f, r) =>
      ur = uniq-rec3(r)
      if ur.member(f):
        ur
      else:
        link(f, ur)
      end
  end
end
```
Note that all that changed is that we check for membership in
`ur`{.pyret} rather than in `r`{.pyret}.

::: {.exercise}
Later [[Predicting Growth](predicting-growth.html)] we will study how to formally
study how long a program takes to run. By the measure introduced in
that section, does the change we just made make any difference? Be
careful with your answer: it depends on how we count “the length” of
the list.
:::

Observe that if the list never contained duplicates in the first
place, then it wouldn’t matter which list we check membership in—but
if we knew the list didn’t contain duplicates, we wouldn’t be
using `uniq`{.pyret} in the first place! We will return to the issue of
lists and duplicate elements in [Representing Sets as Lists](sets-from-lists.html).

##### uniq : Example and Code Variations {#struct-traverse-element-procedure-lib-render-cond-rkt-38-12-Example-and-Code-Variations}

As we mentioned earlier, there are other example sequences you might
have written down. Here’s a very different process:


- Start with the entire given list and with the empty answer (so
  far).
- For each list element, check whether it’s already in the answer
  so far. If it is, ignore it, otherwise extend the answer with it.
- When there are no more elements in the list, the answer so far
  is the answer for the whole list.

Notice that this solution assumes that we will be accumulating the
answer as we traverse the list. Therefore, we can’t even write the
example with one parameter as we did before. We would argue that a
natural solution asks whether we can solve the problem just
from the structure of the data using the computation we are already
defining, as we did above. If we cannot, then we have to resort to an
accumulator. But because we can, the accumulator is unnecessary here
and greatly complicates even writing down examples (give it a try!).

##### uniq : Why Produce a List? {#struct-traverse-element-procedure-lib-render-cond-rkt-38-12-Why-Produce-a-List}

If you go back to the original statement of the `uniq`{.pyret} problem
[[`uniq`{.pyret}: Problem Setup](processing-lists.html##uniq)], you’ll notice it said nothing about what order the
output should have; in fact, it didn’t even say the output needs to be
a list (and hence have an order). In that case, we should think about
whether a list even makes sense for this problem. In fact, if we don’t
care about order and don’t want duplicates (by definition of
`uniq`{.pyret}), then there is a much simpler solution, which is to
produce a set. Pyret already has sets built in, and converting
the list to a set automatically takes care of duplicates. This is of
course cheating from the perspective of learning how to write
`uniq`{.pyret}, but it is worth remembering that sometimes the right data
structure to produce isn’t necessarily the same as the one we were
given. Also, later [[Representing Sets as Lists](sets-from-lists.html)], we will see how to build sets
for ourselves (at which point, `uniq`{.pyret} will look familiar, since
it is at the heart of set-ness).

#### Monomorphic Lists and Polymorphic Types {#polymorphic-data}

Earlier we wrote contracts like:

```pyret
my-len :: List<Any> -> Number
my-max :: List<Any> -> Any
```
These are unsatisfying for several reasons. Consider
`my-max`{.pyret}. The contract suggests that any kind of element can be
in the input list, but in fact that isn’t true: the input
`[list: 1, "two", 3]`{.pyret} is not valid, because we can’t compare
`1`{.pyret} with `"two"`{.pyret} or `"two"`{.pyret} with `3`{.pyret}.

::: {.exercise}
What happens if we run `1 > "two"`{.pyret} or `"two" > 3`{.pyret}?
:::

Rather, what we mean is a list where all the elements are of the
same kind,[Technically, elements that are also comparable.]{.margin-note}
and the contract has not captured that. Furthermore, we don’t mean
that `my-max`{.pyret} might return any old type: if we supply it with a
list of numbers, we will not get a string as the maximum element!
Rather, it will only return the kind of element that is in the
provided list.

In short, we mean that all elements of the list are of the same type,
but they can be of any type. We call the former monomorphic:
“mono” meaning one, and “morphic” meaning shape, i.e., all values
have one type. But the function `my-max`{.pyret} itself can operate over
many of these kinds of lists, so we call it polymorphic
(“poly” meaning many).

Therefore, we need a better way of writing these
contracts. Essentially, we want to say that there is a
type variable (as opposed to regular program variable) that represents the
type of element in the list. Given that type, `my-max`{.pyret} will
return an element of that type. We write this syntactically as
follows:

```pyret
fun my-max<T>(l :: List<T>) -> T: … end
```
The notation `<T>`{.pyret} says that `T`{.pyret} is a type variable
parameter that will be used in the rest of the function (both the
header and the body).

Using this notation, we can also revisit `my-len`{.pyret}. Its header now
becomes:

```pyret
fun my-len<T>(l :: List<T>) -> Number: … end
```
Note that `my-len`{.pyret} did not actually “care” that whether all the
values were of the same type or not: it never looks at the individual
elements, much less at pairs of them. However, as a convention
we demand that lists always be monomorphic. This is important because
it enables us to process the elements of the list uniformly: if we
know how to process elements of type `T`{.pyret}, then we will know how
to process a `List<T>`{.pyret}. If the list elements can be of truly any
old type, we can’t know how to process its elements.
