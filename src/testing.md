---
title: Examples, Testing, and Program Checking
section_number: 8.3
source_file: testing.html
prev: queues-from-lists.html
up: part_bonus-foundations.html
next: booklet_pyret-to-python.html
---

### 8.3 Examples, Testing, and Program Checking {#testing}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="testing.html#%28part._from-examples-to-tests%29">8.3.1<span class="hspace"> </span>From Examples to Tests</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="testing.html#%28part._s~3arefined%29">8.3.2<span class="hspace"> </span>More Refined Comparisons</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="testing.html#%28part._.When_.Tests_.Fail%29">8.3.3<span class="hspace"> </span>When Tests Fail</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="testing.html#%28part._test-oracle%29">8.3.4<span class="hspace"> </span>Oracles for Testing</a></p></td></tr></table>
```

Back in [Documenting Functions with Examples](From_Repeated_Expressions_to_Functions.html##writing-examples), we began to develop your habit of
writing concrete examples of functions. In [Task Plans](processing-tables.html##task-plans), we
showed you how to develop examples of intermediate values to help you
plan the code for you to write. As these examples show, there are many
ways to write down examples. We could write them on a board, on paper,
or even as comments in a computer document. These are all reasonable
and indeed, often, the best way to begin working on a
problem. However, if we can write our examples in a precise form
that a computer can understand, we achieve two things:


- When we’re done writing our purported solution, we can have the
  computer check whether we got it right.
- In the process of writing down our expectation, we often find it
  hard to express with the precision that a computer expects. Sometimes
  this is because we’re still formulating the details and haven’t yet
  pinned them down, but at other times it’s because we don’t yet
  understand the problem. In such situations, the force of precision
  actually does us good, because it helps us understand the weakness of
  our understanding.

#### 8.3.1 From Examples to Tests {#from-examples-to-tests}

Until now, we have written examples in `where:`{.pyret} blocks for two
purposes: to help us figure out what a function needs to do, and to
provide guidance to someone reading our code as to what behavior they can
expect when using our function. For the smaller programs that we have
written until now, `where`{.pyret}-based examples have been
sufficient. As our programs get more complicated, however, a small set
of related illustrative examples won’t suffice. We need to think about being
much more thorough in the sets of inputs that we consider.

Consider for example a function `count-uses`{.pyret} that counts how many
times a specific string appears in a list (this could be used to tally
votes, to compute the frequency of using a discount code, and so
on). What input scenarios might we need to check before using our
function to run an actual election or a business?

- The result for a string that is in the list once
- The result for a string that is in the list multiple times
- The result for a string that is at the end of a longer list (to make
  sure we are checking all of the elements)
- The result for a string that isn’t in the list
- The result for a string that is in the list but with different capitalization
- The result for a string that is a typo-away from a word in the list

Notice that here we are considering many more situations, including
fairly nuanced ones that affect how robust our code would be under
realistic situations. Once we start considering situations like these,
we are shifting from examples to illustrate our code to
tests to thoroughly test our code.

In Jayret, we use `where`{.pyret} blocks inside function definitions for
examples. We use a `check`{.pyret} block outside the function definition
for tests. For example:

```jayret
int count-uses(String of-string, List<Object> in-list) {
    return ...;
} where {
    
}
@Check void test() {
    assertEquals(count-uses("ppper", ["pepper"]), 0);
    assertEquals(count-uses("ONION", ["pepper", "onion"]), 1);
    assertEquals(count-uses("tomato", ["pepper", "onion", "onion", "pepper", "tomato", "tomato", "onion", "tomato"]), 3);
    ...;
}
```

As a guiding rule, we put illustrative cases that would help someone
else reading our code into the `where`{.pyret} block, while we put the
nitty-gritty checks that our code handles the wider range of usage
scenarios (including error cases) into the `check`{.pyret}. Sometimes,
the line between these two isn’t clear: for example, one could easily
argue that the second test (the function handles different
capitalization) belongs in `where`{.pyret} instead. The third test about
using a really long list would remain in `check`{.pyret}, however, as
longer inputs are generally not instructive to a reader of your code.

Putting tests in a block that lives outside the function has another
advantage at the level of professional programming: it allows your
tests to live in a separate file from your code. This has two key
benefits. First, it makes it easier for someone to read the essential parts
of your code (if they are building on your work). Second, it makes it
easier to control when tests are run. When your `check`{.pyret} blocks
are in the same file as your code, all the tests will be checked when
you run your code. When they are in a different file, an organization
can choose when to run the tests. During development, tests are run
frequently to make sure no errors have been introduced. Once code is
tested and ready to be deployed or used, tests are not run along with
the program (unless there has been a modification or someone has
discovered an error with the code). This is standard practice in software projects.

It is also worth noting that the collection of tests grows throughout
the development process, moreso than do the collection of examples. As
you are developing code, every time you find a bug in your code,
add a test for it in your

`check`{.pyret}

block so you don’t accidentally
introduce that same error again later. Whereas we develop
examples up front as we figure out what we want our program to do, we
augment our tests as we discover what our program actually does (and
perhaps should not do). In practice, developers write an
initial set of checks on the scenarios they thought of before and
while writing the code, then expand those tests as they try out more
scenarios and gain users who report scenarios where the code does not
work.

Nearly all programming languages come with some constructs or packages
in which you can write tests in separate files. Jayret is unique in
supporting the distinction between examples and tests (both for
learning and for readability of code by others). Many programming
tools that support professionals expect you to put all tests in
separate folders and files (offering no support for examples). In this
book, we emphasize the difference between these two uses of
input-output pairs in programming because we find them extremely
useful both professionally and pedagogically.

#### 8.3.2 More Refined Comparisons {#s-refined}

Sometimes, a direct comparison via `is`{.pyret} isn’t enough for
testing. We have already seen this in the case of `raises`{.pyret}
tests ([Computing Genetic Parents from an Ancestry Table](trees.html##compute-parents-table)). As another example, when doing
some computations, especially involving math with approximations, the
exact match of `is`{.pyret} isn’t feasible. For example, consider these tests for `distance-to-origin`{.pyret}:

```pyret
# TODO(pyret2jayret): parse failed (no shifts)
check:
  distance-to-origin(point(1, 1)) is ???
end
```

What can we check here? Typing this into the REPL, we can find that the answer
prints as `1.4142135623730951`{.pyret}. That’s an approximation of the real
answer, which Jayret cannot represent exactly. But it’s hard to know that this
precise answer, to this decimal place, and no more, is the one we should expect
up front, and thinking through the answers is supposed to be the first thing we
do!

Since we know we’re getting an approximation, we can really only check that the
answer is roughly correct, not exactly correct. If we can check that
the answer to `distance-to-origin(point(1, 1))`{.pyret} is around, say,
`1.41`{.pyret}, and can do the same for some similar cases, that’s probably good
enough for many applications, and for our purposes here. If we were
calculating orbital dynamics, we might demand higher precision, but note that
we’d still need to pick a cutoff! Testing for inexact results is a necessary
task.

Let’s first define what we mean by “around” with one of the most precise ways
we can, a function:

```jayret
boolean around(int actual, int expected) {
    // Return whether actual is within 0.01 of expected
    return num-abs(actual - expected) < 0.01;
} where {
    
}
```

The `is`{.pyret} form now helps us out. There is special syntax for supplying a
user-defined function to use to compare the two values, instead of just
checking if they are equal:

```jayret
@Check void test() {
    assertEquals(5, 5.01);
    assertEquals(num-sqrt(2), 1.41);
    assertEquals(distance-to-origin(point(1, 1)), 1.41);
}
```

Adding `%(something)`{.pyret} after `is`{.pyret} changes the behavior of
`is`{.pyret}. Normally, it would compare the left and right values for equality.
If something is provided with `%`{.pyret}, however, it instead passes the left
and right values to the provided function (in this example `around`{.pyret}). If
the provided function produces `true`{.pyret}, the test passes, if it produces
`false`{.pyret}, the test fails. This gives us the control we need to test
functions with predictable approximate results.

::: {.exercise}
Extend the definition of `distance-to-origin`{.pyret} to include
`polar`{.pyret} points.
:::

::: {.exercise}
[This might save you a Google search:
[polar
conversions](http://en.wikipedia.org/wiki/Polar_coordinate_system#Converting_between_polar_and_Cartesian_coordinates).]{.margin-note}
Use the design recipe to write `x-component`{.pyret} and
`y-component`{.pyret}, which return the `x`{.pyret} and `y`{.pyret} Cartesian parts
of the point (which you would need, for example, if you were plotting them on a graph).
Read about `num-sin`{.pyret} and other functions you’ll need at
[the Jayret number
documentation](http://jayret-lang.github.io/docs/latest/numbers.html).
:::

::: {.exercise}
Write a data definition called `Pay`{.pyret} for pay types that includes
both hourly employees, whose pay type includes an hourly rate, and salaried
employees, whose pay type includes a total salary for the year. Use the design
recipe to write a function called `expected-weekly-wages`{.pyret} that takes a
`Pay`{.pyret}, and returns the expected weekly salary: the expected weekly salary
for an hourly employee assumes they work 40 hours, and the expected weekly
salary for a salaried employee is 1/52 of their salary.
:::

#### 8.3.3 When Tests Fail {#When-Tests-Fail}

Suppose we’ve written the function `sqrt`{.pyret}, which computes the
square root of a given number. We’ve written some tests for this
function. We run the program, and find that a test fails. There are
two obvious reasons why this can happen.

::: {.do-now}
What are the two obvious reasons?
:::

The two reasons are, of course, the two “sides” of the test: the
problem could be with the values we’ve written or with the function
we’ve written. For instance, if we’ve written

```jayret
assertEquals(sqrt(4), 1.75);
```
then the fault clearly lies with the values (because \(1.75^2\) is
clearly not \(4\)). On the other hand, if it fails the test

```jayret
assertEquals(sqrt(4), 2);
```
then the odds are that we’ve made an error in the definition of
`sqrt`{.pyret} instead, and that’s what we need to fix.

Note that there is no way for the computer to tell what went
wrong. When it reports a test failure, all it’s saying is that there
is an inconsistency between the program and the tests. The
computer is not passing judgment on which one is “correct”, because
it can’t do that. That is a matter for human
judgment.[For this reason, we’ve been doing research on
[peer review of tests](http://cs.brown.edu/~sk/Publications/Papers/Published/pkf-ifpr-tests-tf-prog/), so students can help one another review their
tests before they begin writing programs.]{.margin-note}

Actually...not so fast. There’s one more possibility we didn’t
consider: the third, not-so-obvious reason why a test might
fail. Return to this test:

```jayret
assertEquals(sqrt(4), 2);
```
Clearly the inputs and outputs are correct, but it could be that the
definition of `sqrt`{.pyret} is also correct, and yet the test
fails.

::: {.do-now}
Do you see why?
:::

Depending on how we’ve programmed `sqrt`{.pyret}, it might return the
root `-2`{.pyret} instead of `2`{.pyret}. Now `-2`{.pyret} is a perfectly good
answer, too. That is, neither the function nor the particular set of
test values we specified is inherently wrong; it’s just that the
function happens to be a relation, i.e., it maps one input to
multiple outputs (that is, \(\sqrt{4} = \pm 2\)). The question now is
how to write the test properly.

#### 8.3.4 Oracles for Testing {#test-oracle}

In other words, sometimes what we want to express is not a concrete
input-output pair, but rather check that the output has the right
relationship to the input. Concretely, what might this be in
the case of `sqrt`{.pyret}? We hinted at this earlier when we said that
`1.75`{.pyret} clearly can’t be right, because squaring it does not yield
`4`{.pyret}. That gives us the general insight: that a number is a valid
root (note the use of “a” instead of “the”) if squaring it yields
the original number. That is, we might write a function like this:

```jayret
Object is-sqrt(n) {
    n-root = sqrt(n);
    return n == (n-root * n-root);
}
```
and then our test looks like

```jayret
@Check void test() {
    assertEquals(is-sqrt(4), true);
}
```
Unfortunately, this has an awkward failure case. If `sqrt`{.pyret} does
not produce a number that is in fact a root, we aren’t told what the
actual value is; instead, `is-sqrt`{.pyret} returns false, and the test
failure just says that `false`{.pyret} (what `is-sqrt`{.pyret} returns) is
not `true`{.pyret} (what the test expects)—which is both absolutely
true and utterly useless.

Fortunately, Jayret has a better way of expressing the same
check. Instead of `is`{.pyret}, we can write `satisfies`{.pyret}, and then
the value on the left must satisfy the predicate on the
right. Concretely, this looks like:

```jayret
Object check-sqrt(n) {
    return (n-root) -> n == (n-root * n-root);
}
```
which lets us write:

```jayret
@Check void test() {
    assertSatisfies(sqrt(4), check-sqrt(4));
}
```
Now, if there’s a failure, we learn of the actual value produced by
`sqrt(4)`{.pyret} that failed to satisfy the predicate.
