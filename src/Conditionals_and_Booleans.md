---
title: Conditionals and Booleans
section_number: 3.4
source_file: Conditionals_and_Booleans.html
prev: From_Repeated_Expressions_to_Functions.html
up: part_foundations.html
next: part_tabular-data.html
---

### 3.4 Conditionals and Booleans {#Conditionals-and-Booleans}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._add-shipping-setup%29">3.4.1<span class="hspace"> </span>Motivating Example: Shipping Costs</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._cond-boolean-intro%29">3.4.2<span class="hspace"> </span>Conditionals: Computations with Decisions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._booleans%29">3.4.3<span class="hspace"> </span>Booleans</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._bool-comparisons%29">3.4.3.1<span class="hspace"> </span>Other Boolean Operations</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._.Combining_.Booleans%29">3.4.3.2<span class="hspace"> </span>Combining Booleans</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._else-if%29">3.4.4<span class="hspace"> </span>Asking Multiple Questions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._conditional-nm%29">3.4.5<span class="hspace"> </span>Evaluating by Reducing Expressions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._.Composing_.Functions%29">3.4.6<span class="hspace"> </span>Composing Functions</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._.How_.Function_.Compositions_.Evaluate%29">3.4.6.1<span class="hspace"> </span>How Function Compositions Evaluate</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._func-comp-directory%29">3.4.6.2<span class="hspace"> </span>Function Composition and the Directory</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._.Nested_.Conditionals%29">3.4.7<span class="hspace"> </span>Nested Conditionals</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Conditionals_and_Booleans.html#%28part._.Recap__.Booleans_and_.Conditionals%29">3.4.8<span class="hspace"> </span>Recap: Booleans and Conditionals</a></p></td></tr></table>
```

#### 3.4.1 Motivating Example: Shipping Costs {#add-shipping-setup}

In [Functions Practice: Cost of pens](From_Repeated_Expressions_to_Functions.html##pen-cost-pyret), we wrote a program (`pen-cost`{.pyret}) to
compute the cost of ordering pens. Continuing the example, we now want
to account for shipping costs. We’ll determine shipping charges based
on the cost of the order.

Specifically, we will write a function `add-shipping`{.pyret} to compute
the total cost of an order including shipping. Assume an order valued
at $10 or less ships for $4, while an order valued above $10 ships for
$8. As usual, we will start by writing examples of the `add-shipping`{.pyret}
computation.

::: {.do-now}
Use the `assertEquals`{.jayret} notation from `where { }`{.jayret} blocks to write several
examples of add-shipping. How are you choosing which inputs to
use in your examples? Are you picking random inputs? Being strategic
in some way? If so, what’s your strategy?
:::

Here is a proposed collection of examples for `add-shipping`{.pyret}.

```jayret
assertEquals(add-shipping(10), 10 + 4);
assertEquals(add-shipping(3.95), 3.95 + 4);
assertEquals(add-shipping(20), 20 + 8);
assertEquals(add-shipping(10.01), 10.01 + 8);
```

::: {.do-now}
What do you notice about our examples? What strategies do you observe
across our choices?
:::

Our proposed examples feature several strategic decisions:

- Including `10`{.pyret}, which is at the boundary of charges based on
  the text
- Including `10.01`{.pyret}, which is just over the boundary
- Including both natural and real (decimal) numbers
- Including examples that should result in each shipping charge
  mentioned in the problem (`4`{.pyret} and `8`{.pyret})

So far, we have used a simple rule for creating a function body from
examples: locate the parts that are changing, replace them with names,
then make the names the parameters to the function.

::: {.do-now}
What is changing across our `add-shipping`{.pyret} examples? Do you
notice anything different about these changes compared to the examples
for our previous functions?
:::

Two things are new in this set of examples:


- The values of `4`{.pyret} and `8`{.pyret} differ across the
  examples, but they each occur in multiple examples.
- The values of `4`{.pyret} and `8`{.pyret} appear only in the computed
  answers—not as an input. Which one we use seems to depend on the input value.

These two observations suggest that something new is going on with
`add-shipping`{.pyret}. In particular, we have clusters of examples that
share a fixed value (the shipping charge), but different clusters (a) use
different values and (b) have a pattern to their inputs (whether the
input value is less than or equal to `10`{.pyret}). This calls for being able to
ask questions about inputs within our programs.

#### 3.4.2 Conditionals: Computations with Decisions {#cond-boolean-intro}

To ask a question about our inputs, we use a new kind of expression
called an if expression. Here’s the full definition of `add-shipping`{.pyret}:

```jayret
int add-shipping(int order-amt) {
    // add shipping costs to order total
    return if (order-amt <= 10) {
        return order-amt + 4;
    } else {
        return order-amt + 8;
    }
} where {
    assertEquals(add-shipping(10), 10 + 4);
    assertEquals(add-shipping(3.95), 3.95 + 4);
    assertEquals(add-shipping(20), 20 + 8);
    assertEquals(add-shipping(10.01), 10.01 + 8);
}
```

In an `if`{.pyret} expression, we ask a question that can produce an answer that
is true or false
(here `order-amt <= 10`{.pyret}, which we’ll explain below in
[Booleans](Conditionals_and_Booleans.html##booleans)), provide one expression for
when the answer to the question is true (`order-amt + 4`{.pyret}), and
another for when the result is false (`order-amt +
8`{.pyret}). The `else`{.jayret} in the program marks the answer in the false case; we call
this the else clause.

#### 3.4.3 Booleans {#booleans}

Every expression in Jayret evaluates in a value. So far, we have seen
three types of values: `Number`{.pyret}, `String`{.pyret}, and
`Image`{.pyret}. What type of value does a question like `order-amt
<= 10`{.jayret} produce? We can use the interactions prompt to experiment and
find out.

::: {.do-now}
Enter each of the following expressions at the interactions
prompt. What type of value did you get? Do the values fit the types
we have seen so far?

```jayret
3.95 <= 10;
20 <= 10;
```
:::

The values `true`{.pyret} and `false`{.pyret} belong to a new type in Jayret,
called `Boolean`{.pyret}.[Named for [George Boole](https://en.wikipedia.org/wiki/George_Boole).]{.margin-note} While
there are an infinitely many values of type `Number`{.pyret}, there are
only two of type `Boolean`{.pyret}: `true`{.pyret} and `false`{.pyret}.

::: {.exercise}
What would happen if we entered `order-amt <= 10`{.pyret} at the interactions prompt
to explore booleans? Why does that happen?
:::

##### 3.4.3.1 Other Boolean Operations {#bool-comparisons}

There are many other built-in operations that return `Boolean`{.pyret}
values. Comparing values for equality is a common one: [There is
much more we can and should say about equality, which we will do later
[[Re-Examining Equality](Sharing_and_Equality.html##identical-eq)].]{.margin-note}

::: {.pyret-repl}
```jayret
1 == 1;
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
1 == 2;
```
``` output
false
```
:::

::: {.pyret-repl}
```jayret
"cat" == "dog";
```
``` output
false
```
:::

::: {.pyret-repl}
```jayret
"cat" == "CAT";
```
``` output
false
```
:::

In general, `==`{.pyret} checks whether two values are equal. Note this
is different from the single `=`{.pyret} used to associate names with
values in the directory.

The last example is the most interesting: it illustrates that strings
are case-sensitive, meaning individual letters must match in
their case for strings to be considered equal.[This will
become relevant when we get to tables later.]{.margin-note}

Sometimes, we also want to compare strings to determine their
alphabetical order. Here are several examples:

::: {.pyret-repl}
```jayret
"a" < "b";
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
"a" >= "c";
```
``` output
false
```
:::

::: {.pyret-repl}
```jayret
"that" < "this";
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
"alpha" < "beta";
```
``` output
true
```
:::
which is the alphabetical order we’re used to;
but others need some explaining:

::: {.pyret-repl}
```jayret
"a" >= "C";
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
"a" >= "A";
```
``` output
true
```
:::
These use a convention laid down a long time ago in a system called
[ASCII](https://en.wikipedia.org/wiki/ASCII).[Things
get far more complicated with non-ASCII letters: e.g., Jayret thinks `"Ł"`{.pyret}
is `>`{.pyret} than `"Z"`{.pyret},
but in Polish, this should be `false`{.pyret}. Worse, the ordering
[depends on
location](https://en.wikipedia.org/wiki/Alphabetical_order) (e.g., Denmark/Norway vs. Finland/Sweden).]{.margin-note}

::: {.do-now}
Can you compare `true`{.pyret} and `false`{.pyret}? Try comparing them for
equality (`==`{.pyret}), then for inequality (such as `<`{.pyret}).
:::

In general, you can compare any two values for equality (well, almost,
we’ll come back to this later); for instance:

::: {.pyret-repl}
```jayret
"a" == 1;
```
``` output
false
```
:::
If you want to compare values of a specific kind, you can use more
specific operators:

::: {.pyret-repl}
```jayret
num-equal(1, 1);
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
num-equal(1, 2);
```
``` output
false
```
:::

::: {.pyret-repl}
```jayret
string-equal("a", "a");
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
string-equal("a", "b");
```
``` output
false
```
:::

Why use these operators instead of the more generic `==`{.pyret}?

::: {.do-now}
Try

```jayret
num-equal("a", 1);
string-equal("a", 1);
```
:::

Therefore, it’s wise to use the type-specific operators where you’re expecting
the two arguments to be of the same type. Then, Jayret will signal an error if
you go wrong, instead of blindly returning an answer (`false`{.pyret}) which lets
your program continue to compute a nonsensical value.

There are even more Boolean-producing operators, such as:

::: {.pyret-repl}
```jayret
wm = "will.i.am";
```
:::

::: {.pyret-repl}
```jayret
string-contains(wm, "will");
```
``` output
true
```
:::
[Note the capital `W`{.pyret}.]{.margin-note}

::: {.pyret-repl}
```jayret
string-contains(wm, "Will");
```
``` output
false
```
:::
In fact, just about every kind of data will have some Boolean-valued
operators to enable comparisons.

##### 3.4.3.2 Combining Booleans {#Combining-Booleans}

Often, we want to base decisions on more than one Boolean value. For
instance, you are allowed to vote if you’re a citizen of a country
and you are above a certain age. You’re allowed to board a bus
if you have a ticket or the bus is having a free-ride day. We
can even combine conditions: you’re allowed to drive if you are above
a certain age and have good eyesight and—either
pass a test or have a temporary license. Also, you’re allowed
to drive if you are not inebriated.

Corresponding to these forms of combinations, Jayret offers three main
operations: `&&`{.pyret}, `||`{.pyret}, and `!`{.pyret}. Here are some
examples of their use:

::: {.pyret-repl}
```jayret
(1 < 2) && (2 < 3);
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
(1 < 2) && (3 < 2);
```
``` output
false
```
:::

::: {.pyret-repl}
```jayret
(1 < 2) || (2 < 3);
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
(3 < 2) || (1 < 2);
```
``` output
true
```
:::

::: {.pyret-repl}
```jayret
not(1 < 2);
```
``` output
false
```
:::

::: {.exercise}
Explain why numbers and strings are not good ways to express the
answer to a true/false question.
:::

#### 3.4.4 Asking Multiple Questions {#else-if}

Shipping costs are rising, so we want to modify the
`add-shipping`{.pyret} program to include a third shipping level: orders
between $10 and $30 ship for $8, but orders over $30 ship for $12. This
calls for two modifications to our program:


- We have to be able to ask another question to distinguish
  situations in which the shipping charge is `8`{.pyret} from those
  in which the shipping charge is `12`{.pyret}.
- The question for when the shipping charge is `8`{.pyret} will need
  to check whether the input is between two values.

We’ll handle these in order.

The current body of `add-shipping`{.pyret} asks one question:
`order-amt <= 10`{.pyret}. We need to add another one for `order-amt
<= 30`{.pyret}, using a charge of `12`{.jayret} if that question fails. Where do
we put that additional question?

An expanded version of the if-expression, using `else if`{.pyret}, allows
you to ask multiple questions:

```jayret
int add-shipping(int order-amt) {
    // add shipping costs to order total
    return if (order-amt <= 10) {
        return order-amt + 4;
    } else if (order-amt <= 30) {
        return order-amt + 8;
    } else {
        return order-amt + 12;
    }
} where {
    assertEquals(add-shipping(10), 10 + 4);
    assertEquals(add-shipping(20), 20 + 8);
    assertEquals(add-shipping(31), 31 + 12);
}
```
At this point, you should also add `where { }`{.jayret} examples that use the
`12`{.pyret} charge.

How does Jayret determine which answer to return? It evaluates each
question expression in order, starting from the one that follows
`if`{.pyret}. It continues through the questions, returning the value of
the answer of the first question that returns true. Here’s a summary
of the if-expression syntax and how it evaluates.

```jayret
if (QUESTION1) {
    return <result in case first question true>;
} else if (QUESTION2) {
    return <result in case QUESTION1 false and QUESTION2 true>;
} else {
    return <result in case both QUESTIONs false>;
}
```
A program can have multiple `else if`{.jayret} cases, thus accommodating
an arbitrary number of questions within a program.

::: {.do-now}
The problem description for `add-shipping`{.pyret} said that orders
between `10`{.pyret} and `30`{.pyret} should incur an `8`{.pyret} charge. How
does the above code capture “between”?
:::

This is currently entirely implicit. It depends on us understanding the way an
`if`{.pyret} evaluates. The first question is `order-amt <= 10`{.pyret}, so if we
continue to the second question, it means `order-amt > 10`{.pyret}. In this
context, the second question asks whether `order-amt <= 30`{.pyret}. That’s how
we’re capturing “between”-ness.

::: {.do-now}
How might you modify the above code to build the “between 10 and 30”
requirement explicitly into the question for the `8`{.pyret} case?
:::

Remember the `&&`{.pyret} operator on booleans? We can use that to
capture “between” relationships, as follows:

```jayret
(order-amt > 10) && (order-amt <= 30);
```

::: {.do-now}
Why are there parentheses around the two comparisons? If you replace
`order-amt`{.pyret} with a concrete value (such as `20`{.pyret}) and leave
off the parenthesis, what happens when you evaluate this expression in
the interactions pane?
:::

Here is what `add-shipping`{.pyret} look like with the `&&`{.pyret} included:

```jayret
int add-shipping(int order-amt) {
    // add shipping costs to order total
    return if (order-amt <= 10) {
        return order-amt + 4;
    } else if ((order-amt > 10) && (order-amt <= 30)) {
        return order-amt + 8;
    } else {
        return order-amt + 12;
    }
} where {
    assertEquals(add-shipping(10), 10 + 4);
    assertEquals(add-shipping(20), 20 + 8);
    assertEquals(add-shipping(31), 31 + 12);
}
```

Both versions of `add-shipping`{.pyret} support the same examples. Are
both correct? Yes. And while the first part of the second question
(`order-amt > 10`{.pyret}) is redundant, it can be helpful to include such
conditions for three reasons:


1. They signal to future readers (including ourselves!) the condition
  covering a case.
2. They ensure that if we make a mistake in writing an earlier question, we
  won’t silently get surprising output.
3. They guard against future modifications, where someone might modify an
  earlier question without realizing the impact it’s having on a later one.

::: {.exercise}
An online-advertising firm needs to determine whether to show an ad
for a skateboarding park to website users. Write a function `show-ad`{.pyret}
that takes the age and haircolor of an individual user and returns
`true`{.pyret} if the user is between the ages of `9`{.pyret} and `18`{.pyret}
and has either pink or purple hair.

Try writing this two ways: once with `if`{.pyret} expressions and once
using just boolean operations.
:::

::: {.responsible-cs}
Assumptions about users get encoded in even the simplest
functions. The advertising exercise shows an example in which a decision
gets made on the basis of two pieces of information about a person: age
and haircolor. While some people might stereotypically associate
skateborders with being young and having colored hair, many
skateborders do not fit these criteria and many people who fit these
criteria don’t skateboard.

While real programs to match ads to users are more sophisticated than
this simple function, even the most sophisticated advertising programs
boil down to tracking features or information about individuals and
comparing it to information about the content of ads. A real ad system
would differ in tracking dozens (or more) of features and using more
advanced programming ideas than simple conditionals to determine the
suitability of an ad (we’ll discuss some of these later in the
book). This example also extends to situations far more serious than
ads: who gets hired, granted a bank loan, or [sent to or released from
jail](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) are other examples of real systems that depend on comparing data
about individuals with criteria maintained by a program.

From a social responsibility perspective, the questions here are
what data about individuals should be used to represent them for
processing by programs and what stereotypes might those data
encode. In some cases, individuals can be represented by data without
harm (a university housing office, for examples, stores student ID
numbers and which room a student is living in). But in other cases,
data about individuals get interpreted in order to predict something
about them. Decisions based on those predictions can be inaccurate and
hence harmful.
:::

#### 3.4.5 Evaluating by Reducing Expressions {#conditional-nm}

In [How Functions Evaluate](From_Repeated_Expressions_to_Functions.html##function-call-nm), we talked about how Jayret reduces expressions and
function calls to values. Let’s revisit this process, this time
expanding to consider if-expressions. Suppose we want
to compute the wages of a worker. The worker is paid $10 for every
hour up to the first 40 hours, and is paid $15 for every extra
hour. Let’s say `hours`{.pyret} contains the number of hours they work,
and suppose it’s `45`{.pyret}:

```jayret
hours = 45;
```
Suppose the formula for computing the wage is

```jayret
if (hours <= 40) {
    return hours * 10;
} else if (hours > 40) {
    return (40 * 10) + ((hours - 40) * 15);
}
```

Let’s now see how this results in an answer, using a step-by-step
process that should match what you’ve seen in algebra
classes (the steps are described in the margin notes to the right):
[The first step is to substitute the
`hours`{.pyret} with `45`{.pyret}.]{.margin-note}

```jayret
if (45 <= 40) {
    return 45 * 10;
} else if (45 > 40) {
    return (40 * 10) + ((45 - 40) * 15);
}
```

[Next, the conditional part of the `if`{.pyret} expression is evaluated,
which in this case is `false`{.pyret}.]{.margin-note}

```
=> if (false) {
       return 45 * 10;
   } else if (45 > 40) {
       return (40 * 10) + ((45 - 40) * 15);
   }
```

[Since the condition is `false`{.pyret}, the next branch is tried.]{.margin-note}

```
=> if (45 > 40) {
       return (40 * 10) + ((45 - 40) * 15);
   }
```

[Jayret evaluates the question in the conditional, which in this case produces `true`{.pyret}.]{.margin-note}

```
=> if (true) {
       return (40 * 10) + ((45 - 40) * 15);
   }
```

[Since the condition is `true`{.pyret}, the expression reduces to the body
of that branch. After that, it’s just arithmetic.]{.margin-note}

```
=> (40 * 10) + ((45 - 40) * 15)
```

```
=> 400 + (5 * 15)
=> 475
```

This style of reduction is the best way to think about the evaluation
of Jayret expressions. The whole expression takes steps that simplify
it, proceeding by simple rules. You can use this style yourself if you
want to try and work through the evaluation of a Jayret program by hand
(or in your head).

#### 3.4.6 Composing Functions {#Composing-Functions}

We started this chapter wanting to account for shipping costs on an
order of pens. So far, we have written two functions:


- `pen-cost`{.pyret} for computing the cost of the pens
- `add-shipping`{.pyret} for adding shipping costs to a total amount

What if we now wanted to compute the price of an order of pens
including shipping? We would have to use both of these functions
together, sending the output of `pen-cost`{.pyret} to the input of
`add-shipping`{.pyret}.

::: {.do-now}
Write an expression that computes the total cost, with shipping, of an
order of `10`{.pyret} pens that say `"bravo"`{.pyret}.
:::

There are two ways to structure this computation. We could pass the
result of `pen-cost`{.pyret} directly to `add-shipping`{.pyret}:

```jayret
add-shipping(pen-cost(10, "bravo"));
```

Alternatively, you might have named the result of `pen-cost`{.pyret} as
an intermediate step:

```jayret
pens = pen-cost(10, "bravo");
add-shipping(pens);
```

Both methods would produce the same answer.

##### 3.4.6.1 How Function Compositions Evaluate {#How-Function-Compositions-Evaluate}

Let’s review how these programs evaluate in the context of
substitution and the directory. We’ll start with the second
version, in which we explicitly name the result of calling
`pen-cost`{.pyret}.

Evaluating the second version: At a high level, Jayret goes
through the following steps:

- Substitute `10`{.pyret} for `num-pens`{.pyret} and `"bravo"`{.pyret} for
  `message`{.pyret} in the body of `pen-cost`{.pyret}, then evaluate the
  substituted body
- Store `pens`{.pyret} in the directory, with a value of `3.5`{.pyret}
- As a first step in evaluating `add-shipping(pens)`{.pyret}, look up
  the value of `pens`{.pyret} in the directory
- Substitute `3.5`{.pyret} for `order-amt`{.pyret} in the body of
  `add-shipping`{.pyret} then evaluate the resulting expression, which
  results in `7.5`{.pyret}

Evaluating the first version: As a reminder, the first version
consisted of a single expression:

```jayret
add-shipping(pen-cost(10, "bravo"));
```

- Since arguments are evaluated before functions get called,
  start by evaluating `pen-cost(10, "bravo")`{.pyret} (again using
  substitution), which reduces to `3.5`{.pyret}
- Substitute `3.5`{.pyret} for `order-amt`{.pyret} in the body of
  `add-shipping`{.pyret} then evaluate the resulting expression, which
  results in `7.5`{.pyret}

::: {.do-now}
Contrast these two summaries. Where do they differ? What aspects of the
code led to those differences?
:::

The difference lies in the use of the directory: the version that
explicitly named `pens`{.pyret} uses the directory. The other version
doesn’t use the directory at all. Yet both approaches lead to the same
result, since the same value (the result of calling `pen-cost`{.pyret})
gets substituted into the body of `add-shipping`{.pyret}.

This analysis might suggest that the version that uses the directory
is somehow wasteful: it seems to take more steps just to end up at the
same result. Yet one might argue that the version that uses the
directory is easier to read (different readers will have different
opinions on this, and that’s fine). So which should we use?

Use whichever makes more sense to you on a given problem. There will
be times when we prefer each of these styles. Furthermore, it will
turn out (once we’ve learned more about nuances of how programs
evaluate) that the two versions aren’t as different as they appear
right now.

##### 3.4.6.2 Function Composition and the Directory {#func-comp-directory}

Let’s try one more variation on this problem. Perhaps seeing us name
the intermediate result of `pen-cost`{.pyret} made you wish that we had
used intermediate names to make the body of `pen-cost`{.pyret} more
readable. For example, we could have written it as:

```jayret
int pen-cost(int num-pens, String message) {
    /* total cost for pens, each 25 cents
       plus 2 cents per message character */
    message-cost = string-length(message) * 0.02;
    return num-pens * (0.25 + message-cost);
} where {
    assertEquals(pen-cost(3, "wow"), 3 * (0.25 + (string-length("wow") * 0.02)));
    assertEquals(pen-cost(10, "smile"), 10 * (0.25 + (string-length("smile") * 0.02)));
}
```

::: {.do-now}
Write out the high level steps for how Jayret will evaluate
the following program using this new version of `pen-cost`{.pyret}:

```jayret
pens = pen-cost(10, "bravo");
add-shipping(pens);
```
:::

Hopefully, you made two entries into the directory, one for
`message-cost`{.pyret} inside the body of `pen-cost`{.pyret} and one for
`pens`{.pyret} as we did earlier.

::: {.do-now}
Consider the following program. What result do you think
Jayret should produce?

```jayret
pens = pen-cost(10, "bravo");
cheap-message = (message-cost > 0.5);
add-shipping(pens);
```

Using the directory you envisioned for the previous activity, what
answer do you think you will get?
:::

Something odd is happening here. The new program tries to use
`message-cost`{.pyret} to define `cheap-message`{.pyret}. But the name
`message-cost`{.pyret} doesn’t appear anywhere in the program, unless we
peek inside the function bodies. But letting code peek inside function
bodies doesn’t make sense: you might not be able to see inside the
functions (if they are defined in libraries, for example), so this
program should report an error that `message-cost`{.pyret} is undefined.

Okay, so that’s what should happen. But our discussion of the
directory suggests that both `pens`{.pyret} and `message-cost`{.pyret} will
be in the directory, meaning Jayret would be able to use
`message-cost`{.pyret}. What’s going on?

This example prompts us to explain one more nuance about the
directory. Precisely to avoid problems like the one illustrated here
(which should produce an error), directory entries made within a
function are local (private) to the function body. When you call a function,
Jayret sets up a local directory that other functions can’t
see. A function body can add or refer to names in either its local,
private directory (as with `message-cost`{.pyret}) or the overall
(global) directory (as with `pens`{.pyret}). But in no case can one
function call peek inside the local directory for another function
call. Once a function call completes, its local directory disappears
(because nothing else would be able to use it anyway).

#### 3.4.7 Nested Conditionals {#Nested-Conditionals}

We showed that the results in `if`{.pyret}-expressions are themselves
expressions (such as `order-amt + 4`{.pyret} in the following function):

```jayret
int add-shipping(int order-amt) {
    // add shipping costs to order total
    return if (order-amt <= 10) {
        return order-amt + 4;
    } else {
        return order-amt + 8;
    }
}
```

The result expressions can be more complicated. In fact, they could be
entire if-expressions!. To see an example of this, let’s develop
another function. This time, we want a function that will compute the
cost of movie tickets. Let’s start with a simple version in which
tickets are `$10`{.pyret} apiece.

```jayret
int buy-tickets1(int count) {
    // Compute the price of tickets at $10 each
    return count * 10;
} where {
    assertEquals(buy-tickets1(0), 0);
    assertEquals(buy-tickets1(5), 5 * 10);
}
```

Now, let’s augment the function with an extra parameter to indicate
whether the purchaser is a senior citizen who is entitled to a discount. In such cases, we will reduce the overall price by
`15%`{.pyret}.

```jayret
int buy-tickets2(int count, boolean is-senior) {
    /* Compute the price of tickets at $10 each with
       senior discount of 15% */
    return if (is-senior == true) {
        return count * 10 * 0.85;
    } else {
        return count * 10;
    }
} where {
    assertEquals(buy-tickets2(0, false), 0);
    assertEquals(buy-tickets2(0, true), 0);
    assertEquals(buy-tickets2(2, false), 2 * 10);
    assertEquals(buy-tickets2(2, true), 2 * 10 * 0.85);
    assertEquals(buy-tickets2(6, false), 6 * 10);
    assertEquals(buy-tickets2(6, true), 6 * 10 * 0.85);
}
```
There are a couple of things to notice here:


- The function now has an additional parameter of type
  `Boolean`{.pyret} to indicate whether the purchaser is a senior citizen.
- We have added an `if`{.pyret} expression to check whether to
  apply the discount.
- We have more examples, because we have to vary both the number
  of tickets and whether a discount applies.

Now, let’s extend the program once more, this time also offering the
discount if the purchaser is not a senior but has bought more than 5 tickets. Where should
we modify the code to do this? One option is to first check whether
the senior discount applies. If not, we check whether the number of
tickets qualifies for a discount:

```jayret
int buy-tickets3(int count, boolean is-senior) {
    /* Compute the price of tickets at $10 each with
       discount of 15% for more than 5 tickets
       or being a senior */
    return if (is-senior == true) {
        return count * 10 * 0.85;
    } else {
        return if (count > 5) {
            return count * 10 * 0.85;
        } else {
            return count * 10;
        }
    }
} where {
    assertEquals(buy-tickets3(0, false), 0);
    assertEquals(buy-tickets3(0, true), 0);
    assertEquals(buy-tickets3(2, false), 2 * 10);
    assertEquals(buy-tickets3(2, true), 2 * 10 * 0.85);
    assertEquals(buy-tickets3(6, false), 6 * 10 * 0.85);
    assertEquals(buy-tickets3(6, true), 6 * 10 * 0.85);
}
```
Notice here that we have put a second `if`{.pyret} expression within the
`else`{.pyret} case. This is valid code. (We could have also made an
`else if`{.pyret} here, but we didn’t so that we could show that nested
conditionals are also valid).

::: {.exercise}
Show the steps through which this function would evaluate in
a situation where no discount applies, such as `buy-tickets3(2,
false)`{.jayret}.
:::

::: {.do-now}
Look at the current code: do you see a repeated computation
that we might end up having to modify later?
:::

Part of good code style is making sure that our programs would be easy
to maintain later. If the theater changes its discount policy, for
example, the current code would require us to change the discount
(`0.85`{.pyret}) in two places. It would be much better to have that
computation written only one time. We can achieve that by asking which
conditions lead to the discount applying, and writing them as the
check within just one `if`{.pyret} expression.

::: {.do-now}
Under what conditions should the discount apply?
:::


Here, we see that the discount applies if either the purchaser is a
senior or more than 5 tickets have been bought. We can therefore
simplify the code by using `||`{.pyret} as follows (we’ve left out the
examples because they haven’t changed from the previous version):

```jayret
int buy-tickets4(int count, boolean is-senior) {
    /* Compute the price of tickets at $10 each with
       discount of 15% for more than 5 tickets
       or being a senior */
    return if ((is-senior == true) || (count > 5)) {
        return count * 10 * 0.85;
    } else {
        return count * 10;
    }
}
```
This code is much tighter, and all of the cases where the discount
applies are described together in one place. There are still two small
changes we want to make to really clean this up though.

::: {.do-now}
Take a look at the expression `is-senior == true`{.pyret}. What will this
evaluate to when the value of `is-senior`{.pyret} is `true`{.pyret}? What
will it evaluate to when the value of `is-senior`{.pyret} is `false`{.pyret}?
:::


Notice that the `== true`{.pyret} part is redundant. Since
`is-senior`{.pyret} is already a boolean, we can check its value without
using the `==`{.pyret} operator. Here’s the revised code:

```jayret
int buy-tickets5(int count, boolean is-senior) {
    /* Compute the price of tickets at $10 each with
       discount of 15% for more than 5 tickets
       or being a senior */
    return if (is-senior || (count > 5)) {
        return count * 10 * 0.85;
    } else {
        return count * 10;
    }
}
```
Notice the revised question in the `if`{.jayret} expression. As a general
rule, your code should never include `== true`{.pyret}. You can always
take that out and just use the expression you were comparing to
`true`{.pyret}.

::: {.do-now}
What do you write to eliminate `== false`{.pyret}? For example, what
might you write instead of `is-senior == false`{.pyret}?
:::

Finally, notice that we still have one repeated computation: the base
cost of the tickets (`count * 10`{.pyret}): if the ticket price changes,
it would be better to have only one place to update that price. We can
clean that up by first computing the base price, then applying the
discount when appropriate:

```jayret
int buy-tickets6(int count, boolean is-senior) {
    /* Compute the price of tickets at $10 each with
       discount of 15% for more than 5 tickets
       or being a senior */
    base = count * 10;
    return if (is-senior || (count > 5)) {
        return base * 0.85;
    } else {
        return base;
    }
}
```

#### 3.4.8 Recap: Booleans and Conditionals {#Recap-Booleans-and-Conditionals}

With this chapter, our computations can produce different results in
different situations. We ask questions using if-expressions, in
which each question or check uses an operator that produces a
boolean.

- There are two Boolean values: `true`{.pyret} and `false`{.pyret}.
- A simple kind of check (that produces a boolean) compares values for equality (`==`{.pyret})
  or inequality(`<>`{.pyret}). Other operations that you know from math,
  like `<`{.pyret} and `>=`{.pyret}, also produce booleans.
- We can build larger expressions that produce booleans from smaller ones using
  the operators `&&`{.pyret}, `||`{.pyret}, `!`{.pyret}.
- We can use `if`{.pyret} expressions to ask true/false questions
  within a computation, producing different results in each case.
- We can nest conditionals inside one another if needed.
- You never need to use `==`{.pyret} to compare a value to
  `true`{.pyret} or `false`{.pyret}: you can just write the value or
  expression on its own (perhaps with `!`{.pyret} to get the same computation).
