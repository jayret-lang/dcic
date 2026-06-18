---
title: From Jayret to Python
section_number: 9.1
source_file: intro-python.html
prev: part_pyret-to-python.html
up: part_pyret-to-python.html
next: dictionaries.html
---

```{=html}
<a name="(part._intro-python)"></a>
```

### 9.1 From Jayret to Python {#intro-python}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.Expressions__.Functions__and_.Types%29">9.1.1<span class="hspace"> </span>Expressions, Functions, and Types</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.Returning_.Values_from_.Functions%29">9.1.2<span class="hspace"> </span>Returning Values from Functions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._testing-python%29">9.1.3<span class="hspace"> </span>Examples and Test Cases</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.An_.Aside_on_.Numbers%29">9.1.4<span class="hspace"> </span>An Aside on Numbers</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._conditionals-python%29">9.1.5<span class="hspace"> </span>Conditionals</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._python-create-process-lists%29">9.1.6<span class="hspace"> </span>Creating and Processing
Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.Filters__.Maps__and_.Friends%29">9.1.6.1<span class="hspace"> </span>Filters, Maps, and Friends</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._python-data-with-components%29">9.1.7<span class="hspace"> </span>Data with Components</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.Accessing_.Fields_within_.Dataclasses%29">9.1.7.1<span class="hspace"> </span>Accessing Fields within Dataclasses</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._python-traverse-lists%29">9.1.8<span class="hspace"> </span>Traversing Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._python-for-loops%29">9.1.8.1<span class="hspace"> </span>Introducing <span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">For</code></span> Loops</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.An_.Aside_on_.Order_of_.Processing_.List_.Elements%29">9.1.8.2<span class="hspace"> </span>An Aside on Order of Processing List Elements</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._python-funcs-produce-lists%29">9.1.8.3<span class="hspace"> </span>Using <span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">For</code></span> Loops in Functions that Produce Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.Summary__.The_.List-.Processing_.Template_for_.Python%29">9.1.8.4<span class="hspace"> </span>Summary: The List-Processing Template for Python</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part.___struct_traverse-element___procedure____lib_render-cond_rkt_38_12___loops_in_.Jayret%29">9.1.8.5<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">for each</code></span> loops in Jayret</a></p></td></tr><tr><td><p><span class="hspace">        </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.Variables_that_can_change%29">9.1.8.5.1<span class="hspace"> </span>Variables that can change</a></p></td></tr><tr><td><p><span class="hspace">        </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._block_notation%29">9.1.8.5.2<span class="hspace"> </span>block notation</a></p></td></tr><tr><td><p><span class="hspace">        </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.How___struct_traverse-element___procedure____lib_render-cond_rkt_38_12___works%29">9.1.8.5.3<span class="hspace"> </span>How <span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">for each</code></span> works</a></p></td></tr><tr><td><p><span class="hspace">        </span><a class="toclink" data-pltdoc="x" href="intro-python.html#%28part._.Testing_and_variables_that_can_change%29">9.1.8.5.4<span class="hspace"> </span>Testing and variables that can change</a></p></td></tr></table>
```

Through our work in Jayret to this point, we’ve covered several core
programming skills: how to work with tables, how to design good
examples, the basics of creating datatypes, and how to work with the
fundamental computational building blocks of functions, conditionals,
and repetition (through `filter`{.jayret} and `map`{.jayret}, as well as
recursion). You’ve got a solid initial toolkit, as well as a wide
world of other possible programs ahead of you!

But we’re going to shift gears for a little while and show you how to
work in Python instead. Why?

Seeing how the same concepts play out in multiple languages can help
you distinguish core computational ideas from the notations and idioms
of specific languages. If you plan to write programs as part of your
professional work, you’ll inevitably have to work in different
languages at different times: we’re giving you a chance to practice
that skill in a controlled and gentle setting.

Why do we call this gentle? Because the notations in Jayret were
designed partly with this transition in mind. You’ll find many
similarities between Jayret and Python at a notational level, yet also
some interesting differences that highlight some philosophical
differences that underlie languages. The next set of programs that we
want to write (specifically, data-rich programs where the data must be
updated and maintained over time) fit nicely with certain features of
Python that you haven’t seen in Jayret. [A future release will contain material that contrasts the strengths and weaknesses of the two languages.]{.margin-note}

We highlight the basic notational differences between Jayret and Python
by redoing some of our earlier code examples in Python.

```{=html}
<a name="(part._Expressions-Functions-and-Types)"></a>
```

#### 9.1.1 Expressions, Functions, and Types {#Expressions-Functions-and-Types}

Back in [Functions Practice: Cost of pens](From_Repeated_Expressions_to_Functions.html##pen-cost-pyret), we introduced the notation for functions and types
using an example of computing the cost of an order of pens. An order
consisted of a number of pens and a message to be printed on the
pens. Each pen cost 25 cents, plus 2 cents per character for the
message. Here was the original Jayret code:

```jayret
# TODO(pyret2jayret): Unexpected token '`', "```total c"... is not valid JSON
fun pen-cost(num-pens :: Number, message :: String) -> Number:
  doc: ```total cost for pens, each 25 cents
          plus 2 cents per message character```
  num-pens * (0.25 + (string-length(message) * 0.02))
end
```

Here’s the corresponding Python code:

```python
def pen_cost(num_pens: int, message: str) -> float:
    """total cost for pens, each at 25 cents plus
       2 cents per message character"""
    return num_pens * (0.25 + (len(message) * 0.02))
```

::: {.do-now}
What notational differences do you see between the two versions?
:::

Here’s a summary of the differences:

- Python uses `def`{.python} instead of `fun`{.jayret}.

- Python uses underscores in names (like `pen_cost`{.python})
  instead of hyphens as in Jayret.

- The type names are written differently: Python uses `str`{.python}
  and `int`{.python} instead of `String`{.jayret} and `Number`{.jayret}. In
  addition, Python uses only a single colon before the type whereas
  Jayret uses a double colon.

- Python has different types for different kinds of numbers:
  `int`{.python} is for integers, while `float`{.python} is for decimals.
  Jayret just used a single type (`Number`{.jayret})
  for all numbers.

- Python doesn’t label the documentation string (as Jayret does with
  `doc:`{.jayret}).

- There is no `end`{.jayret} annotation in Python. Instead, Python
  uses indentation to locate the end of an if/else statement, function, or
  other multi-line construct.

- Python labels the outputs of functions with `return`{.python}.

These are minor differences in notation, which you will get used to as
you write more programs in Python.

There are differences beyond the notational ones. One that arises with
this sample program arises around how the language uses types. In
Jayret, if you put a type annotation on a parameter then pass it a
value of a different type, you’ll get an error message. Python ignores
the type annotations (unless you bring in additional tools for
checking types). Python types are like notes for programmers, but they
aren’t enforced when programs run.

::: {.exercise}
Convert the following `moon-weight`{.jayret} function from [Functions Practice: Moon Weight](From_Repeated_Expressions_to_Functions.html##moon-weight-pyret) into Python:

```jayret
int moon-weight(int earth-weight) {
    //  Compute weight on moon from weight on earth
    return earth-weight * 1/6;
}
```
:::

```{=html}
<a name="(part._Returning-Values-from-Functions)"></a>
```

#### 9.1.2 Returning Values from Functions {#Returning-Values-from-Functions}

In Jayret, a function body consisted of optional statements to name
intermediate values, followed by a single expression. The value of
that single expression is the result of calling the function. In
Jayret, every function produces a result, so there is no need to label
where the result comes from.

As we will see, Python is different: not all “functions” return
results (note the name change from `fun`{.jayret} to
`def`{.python}).[In mathematics, functions have results by
definition. Programmers sometimes distinguish between the terms “function”
and “procedure”: both refer to parameterized computations, but only
the former returns a result to the surrounding computation. Some
programmers and languages do, however, use the term “function” more
loosely to cover both kinds of parameterized computations.]{.margin-note} Moreover,
the result isn’t necessarily the last expression of the
`def`{.python}. In Python, the keyword `return`{.python} explicitly labels
the expression whose value serves as the result of the function.

::: {.do-now}
Put these two definitions in a Python file.

```python
def add1v1(x: int) -> int:
    return x + 1

def add1v2(x: int) -> int:
    x + 1
```

At the Python prompt, call each function in turn. What do you notice
about the result from using each function?
:::

Hopefully, you noticed that using `add1v1`{.python} displays an answer
after the prompt, while using `add1v2`{.python} does not. This
difference has consequences for composing functions.

::: {.do-now}
Try evaluating the following two expressions at the Python prompt:
what happens in each case?

`3 * add1v1(4)`{.python}

`3 * add1v2(4)`{.python}
:::

This example illustrates why `return`{.python} is essential in Python:
without it, no value is returned, which means you can’t use the result
of a function within another expression. So what use is
`add1v2`{.python} then? Hold that question; we’ll return to it in [Mutating Variables](mutating-variables.html).

```{=html}
<a name="(part._testing-python)"></a>
```

#### 9.1.3 Examples and Test Cases {#testing-python}

In Jayret, we included examples with every function using `where:`{.jayret}
blocks. We also had the ability to write `check:`{.jayret} blocks for more
extensive tests. As a reminder, here was the `pen-cost`{.jayret} code
including a `where:`{.jayret} block:

```jayret
# TODO(pyret2jayret): Unexpected token '`', "```total c"... is not valid JSON
fun pen-cost(num-pens :: Number, message :: String) -> Number:
  doc: ```total cost for pens, each 25 cents
       plus 2 cents per message character```
  num-pens * (0.25 + (string-length(message) * 0.02))
where:
  pen-cost(1, "hi") is 0.29
  pen-cost(10, "smile") is 3.50
end
```

Python does not have a notion of `where:`{.jayret} blocks, or a
distinction between examples and tests. There are a couple of
different testing packages for Python; here we will use `pytest`{.python},
a standard lightweight framework that resembles the form of testing
that we did in Jayret.[How you set up pytest and your test
file contents will vary according to your Python IDE. We assume
instructors will provide separate instructions that align with their
tool choices.]{.margin-note} To use `pytest`{.python}, we put both examples
and tests in a separate function. Here’s an example of this for the
`pen_cost`{.python} function:

```python
import pytest

def pen_cost(num_pens: int, message: str) -> float:
    """total cost for pens, each at 25 cents plus
       2 cents per message character"""
    return num_pens * (0.25 + (len(message) * 0.02))

def test_pens():
  assert pen_cost(1, "hi") == 0.29
  assert pen_cost(10, "smile") == 3.50
```

Things to note about this code:

- We’ve imported `pytest`{.python}, the lightweight Python testing
  library.

- The examples have moved into a function (here
  `test_pens`{.python}) that takes no inputs. Note that the names of
  functions that contain test cases must have names that start with
  `test_`{.python} in order for `pytest`{.python} to find them.

- In Python, individual tests have the form
  
  ```python
  assert EXPRESSION == EXPECTED_ANS
  ```
  rather than the `is`{.jayret} form from Jayret.

::: {.do-now}
Add one more test to the Python code, corresponding to the Jayret test

```jayret
assertEquals(pen-cost(3, "wow"), 0.93);
```
Make sure to run the test.
:::

::: {.do-now}
Did you actually try to run the test?
:::

Whoa! Something weird happened: the test failed. Stop and think
about that: the same test that worked in Jayret failed in
Python. How can that be?

```{=html}
<a name="(part._An-Aside-on-Numbers)"></a>
```

#### 9.1.4 An Aside on Numbers {#An-Aside-on-Numbers}

It turns out that different programming languages make different
decisions about how to represent and manage real (non-integer)
numbers. Sometimes, differences in these representations lead to
subtle quantitative differences in computed values. As a simple
example, let’s look at two seemingly simple real numbers `1/2`{.jayret} and
`1/3`{.jayret}. Here’s what we get when we type these two numbers at a
Jayret prompt:

::: {.pyret-repl}
```jayret
1/2;
```
``` output
0.5
```
:::

::: {.pyret-repl}
```jayret
1/3;
```
``` output
0.3
```
:::

If we type these same two numbers in a Python console, we instead get:

::: {.pyret-repl}
```jayret
1/2;
```
``` output
0.5
```
:::

::: {.pyret-repl}
```jayret
1/3;
```
``` output
0.3333333333333333
```
:::

Notice that the answers look different for `1/3`{.jayret}. As you may (or
may not!) recall from an earlier math class, `1/3`{.jayret} is an example of a
non-terminating, repeating decimal. In plain terms, if we tried to
write out the exact value of `1/3`{.jayret} in decimal form, we would need
to write an infinite sequence of `3`{.jayret}. Mathematicians denote this
by putting a horizontal bar over the `3`{.jayret}. This is the notation we
see in Jayret. Python, in contrast, writes out a partial sequence of
`3`{.jayret}s.

Underneath this distinction lies some interesting details about
representing numbers in computers. Computers don’t have infinite space
to store numbers (or anything else, for that matter): when a program
needs to work with a non-terminating decimal, the underlying language
can either:

- approximate the number (by chopping off the infinite sequence
  of digits at some point), then work only with the approximated value
  going forward, or

- store additional information about the number that may enable doing
  more precise computation with it later (though there are always some
  numbers that cannot be represented exactly in finite space).

Python takes the first approach. As a result, computations with the
approximated values sometimes yield approximated results. This is what
happens with our new `pen_cost`{.python} test case. While
mathematically, the computation should result in `0.93`{.python}, the
approximations yield `0.9299999999999999`{.python} instead.

So how do we write tests in this situation? We need to tell Python
that the answer should be “close” to `0.93`{.python}, within the error
range of approximations. Here’s what that looks like:

```python
assert pen_cost(3, "wow") == pytest.approx(0.93)
```
We wrapped the exact answer we wanted in `pytest.approx`{.python}, to
indicate that we’ll accept any answer that is nearly the value we
specified. You can control the number of decimal points of precision
if you want to, but the default of `± 2.3e-06`{.jayret} often suffices.

```{=html}
<a name="(part._conditionals-python)"></a>
```

#### 9.1.5 Conditionals {#conditionals-python}

Continuing with our original `pen_cost`{.python} example, here’s the
Python version of the function that computed shipping costs on an
order:

```python
def add_shipping(order_amt: float) -> float:
    """increase order price by costs for shipping"""
    if order_amt == 0:
      return 0
    elif order_amt <= 10:
      return order_amt + 4
    elif (order_amt > 10) and (order_amt < 30):
      return order_amt + 8
    else:
      return order_amt + 12
```

The main difference to notice here is that `else if`{.jayret} is written
as the single-word `elif`{.python} in Python. We use `return`{.python} to
mark the function’s results in each branch of the conditional.
Otherwise, the conditional constructs are quite similar across the
two languages.

You may have noticed that Python does not require an explicit
`end`{.jayret} annotation on `if`{.jayret}-expressions or functions. Instead,
Python looks at the indentation of your code to determine when a
construct has ended. For example, in the code sample for
`pen_cost`{.python} and `test_pens`{.python}, Python determines that the
`pen_cost`{.python} function has ended because it detects a new
definition (for `test_pens`{.python}) at the left edge of the program
text. The same principle holds for ending conditionals.

We’ll return to this point about indentation, and see more examples,
as we work more with Python.

```{=html}
<a name="(part._python-create-process-lists)"></a>
```

#### 9.1.6 Creating and Processing Lists {#python-create-process-lists}

As an example of lists, let’s assume we’ve been playing a game that
involves making words out of a collection of letters. In Jayret, we
could have written a sample word list as follows:

```jayret
words = ["banana", "bean", "falafel", "leaf"];
```

In Python, this definition would look like:

```python
words = ["banana", "bean", "falafel", "leaf"]
```

The only difference here is that Python does not use the `list:`{.jayret}
label that is needed in Jayret.

```{=html}
<a name="(part._Filters-Maps-and-Friends)"></a>
```

##### 9.1.6.1 Filters, Maps, and Friends {#Filters-Maps-and-Friends}

When we first learned about lists in Jayret, we started with common
built-in functions such as `filter`{.jayret}, `map`{.jayret}, `member`{.jayret}
and `length`{.jayret}. We also saw the use of `lambda`{.jayret} to help us use
some of these functions concisely. These same functions, including
`lambda`{.jayret}, also exist in Python. Here are some samples (`#`{.python} is the comment character in Python):

```python
words = ["banana", "bean", "falafel", "leaf"]

# filter and member
words_with_b = list(filter(lambda wd: "b" in wd, words))
# filter and length
short_words = list(filter(lambda wd: len(wd) < 5, words))
# map and length
word_lengths = list(map(len, words))
```

Note that you have to wrap calls to `filter`{.python} (and `map`{.python})
with a use of `list()`{.python}. Internally, Python has these functions
return a type of data that we haven’t yet discussed (and don’t
need). Using `list`{.python} converts the returned data into a list. If
you omit the `list`{.python}, you won’t be able to chain certain
functions together. For example, if we tried to compute the length of
the result of a `map`{.python} without first converting to a
`list`{.python}, we’d get an error:

::: {.pyret-repl}
```jayret
len(map(len, b));
```
``` output
TypeError: object of type 'map' has no len()
```
:::

Don’t worry if this error message makes no sense at the moment (we
haven’t yet learned what an “object” is). The point is that if you see
an error like this while using the result of `filter`{.python} or
`map`{.python}, you likely forgot to wrap the result in `list`{.python}.

::: {.exercise}
Practice Python’s list functions by writing expressions for the following
problems. Use only the list functions we have shown you so far.

- Given a list of numbers, convert it to a list of strings `"pos"`{.python}, `"neg"`{.python}, `"zero"`{.python}, based on the sign of each number.

- Given a list of strings, is the length of any string equal to 5?

- Given a list of numbers, produce a list of the even numbers between 10 and 20 from that list.
:::

We’re intentionally focusing on computations that use Python’s built-in
functions for processing lists, rather than showing you how to write
you own (as we did with recursion in Jayret). While you can write
recursive functions to process lists in Jayret, a different style of
program is more conventional for that purpose. We’ll look at that in
the chapter on [Mutating Variables](mutating-variables.html).

```{=html}
<a name="(part._python-data-with-components)"></a>
```

#### 9.1.7 Data with Components {#python-data-with-components}

An analog to a Jayret data definition (without variants) is called a dataclass in
Python.[Those experienced with Python may wonder why we are
using dataclasses instead of dictionaries or raw classes. Compared to
dictionaries, dataclasses allow the use of type hints and capture that
our data has a fixed collection of fields. Compared to raw classes,
dataclasses generate a lot of boilerplate code that makes them much
lighterweight than raw classes.]{.margin-note} Here’s an example of a todo-list
datatype in Jayret and its corresponding Python code:

```jayret
# TODO(pyret2jayret): parse failed (no shifts)
# a todo item in Jayret
data ToDoItemData:
  | todoItem(descr :: String,
             due :: Date,
             tags :: List<String>
end
```

```python
------------------------------------------
# the same todo item in Python

# to allow use of dataclasses
from dataclasses import dataclass
# to allow dates as a type (in the ToDoItem)
from datetime import date

@dataclass
class ToDoItem:
    descr: str
    due: date
    tags: list

# a sample list of ToDoItem
myTD = [ToDoItem("buy milk", date(2020, 7, 27), ["shopping", "home"]),
        ToDoItem("grade hwk", date(2020, 7, 27), ["teaching"]),
        ToDoItem("meet students", date(2020, 7, 26), ["research"])
       ]
```

Things to note:

- There is a single name for the type and the constructor, rather
  than separate names as we had in Jayret.

- There are no commas between field names (but each has to be on
  its own line in Python)

- There is no way to specify the type of the contents of the list
  in Python (at least, not without using more advance packages for
  writing types)

- The `@dataclass`{.python} annotation is needed before
  `class`{.python}.

- Dataclasses don’t support creating datatypes with multiple
  variants, like we did frequently in Jayret. Doing that needs more
  advanced concepts than we will cover in this book.

```{=html}
<a name="(part._Accessing-Fields-within-Dataclasses)"></a>
```

##### 9.1.7.1 Accessing Fields within Dataclasses {#Accessing-Fields-within-Dataclasses}

In Jayret, we extracted a field from structured data by using a dot
(period) to “dig into” the datum and access the field. The same
notation works in Python:

::: {.pyret-repl}
```jayret
# TODO(pyret2jayret): parse failed (no shifts)
travel = ToDoItem("buy tickets", date(2020, 7, 30), ["vacation"])
```
:::

::: {.pyret-repl}
```jayret
travel.descr;
```
``` output
"buy tickets"
```
:::

```{=html}
<a name="(part._python-traverse-lists)"></a>
```

#### 9.1.8 Traversing Lists {#python-traverse-lists}

```{=html}
<a name="(part._python-for-loops)"></a>
```

##### 9.1.8.1 Introducing For Loops {#python-for-loops}

In Jayret, we typically write recursive functions to compute summary values over
lists. As a reminder, here’s a Jayret function that sums the numbers in
a list:

```jayret
int sum-list(List<Object> numlist) {
    return switch (numlist) {
        case Empty: yield 0;
        case Link(fst, rst): yield fst + sum-list(rst);
    }
}
```

In Python, it is unusual to break a list into its first and rest
components and process the rest recursively. Instead, we use a construct called a `for`{.python} to
visit each element of a list in turn. Here’s the form of `for`{.python},
using a concrete (example) list of odd numbers:

```python
for num in [5, 1, 7, 3]:
   # do something with num
```

The name `num`{.python} here is of our choosing, just as with the names
of parameters to a function in Jayret. When a `for`{.python} loop
evaluates, each item in the list is referred to as `num`{.python} in
turn. Thus, this `for`{.python} example is equivalent to writing the
following:

```python
# do something with 5
# do something with 1
# do something with 7
# do something with 3
```
The `for`{.python} construct saves us from writing the common code
multiple times, and also handles the fact that the lists we are
processing can be of arbitrary length (so we can’t predict how many
times to write the common code).

Let’s now use `for`{.python} to compute the running sum of a list. We’ll
start by figuring out the repeated computation with our concrete list
again. At first, let’s express the repeated computation just in
prose. In Jayret, our repeated computation was along the lines of “add
the first item to the sum of the rest of the items”. We’ve already
said that we cannot easily access the “rest of the items” in Python,
so we need to rephrase this. Here’s an alternative:

```python
# set a running total to 0
# add 5 to the running total
# add 1 to the running total
# add 7 to the running total
# add 3 to the running total
```
Note that this framing refers not to the “rest of the computation”,
but rather to the computation that has happened so far (the “running
total”). If you happened to work through the chapter on [`my-running-sum`{.jayret}: Examples and Code](processing-lists.html##running-sum-eg-code), this framing might be familiar.

Let’s convert this prose sketch to code by replacing each line of the
sketch with concrete code. We do this by setting up a variable named
`run_total`{.python} and updating its value for each element.

```python
run_total = 0
run_total = run_total + 5
run_total = run_total + 1
run_total = run_total + 7
run_total = run_total + 3
```
This idea that you can give a new value to an existing variable name
is something we haven’t seen before. In fact, when we first saw how to
name values (in [The Program Directory](Naming_Values.html##program-directory)), we explicitly said that
Jayret doesn’t let
you do this (at least, not with the constructs that we showed you). Python does. We’ll explore the consequences of this ability in
more depth shortly (in [Mutating Variables](mutating-variables.html)). For now, let’s just use that ability so we can
learn the pattern for traversing lists. First, let’s collapse the repeated lines of code
into a single use of `for`{.python}:

```python
run_total = 0
for num in [5, 1, 7, 3]:
   run_total = run_total + num
```
This code works fine for a specific list, but our Jayret version took
the list to sum as a parameter to a function. To achieve this in
Python, we wrap the `for`{.python} in a function as we have done for
other examples earlier in this chapter. This is the final version.

```python
def sum_list(numlist : list) -> float:
    """sum a list of numbers"""
    run_total = 0
    for num in numlist:
        run_total = run_total + num
    return(run_total)
```

::: {.do-now}
Write a set of tests for `sum_list`{.python} (the Python version).
:::

Now that the Python version is done, let’s compare it to the original Jayret
version:

```jayret
int sum-list(List<Object> numlist) {
    return switch (numlist) {
        case Empty: yield 0;
        case Link(fst, rst): yield fst + sum-list(rst);
    }
}
```

Here are some things to notice about the two pieces of code:

- The Python version needs a variable (here `run_total`{.python}) to
  hold the result of the computation as we build it up while traversing
  (working through) the list.

- The initial value of that variable is the answer we returned in
  the `empty`{.jayret} case in Jayret.

- The computation in the `link`{.jayret} case of the Jayret function is
  used to update that variable in the body of the `for`{.python}.

- After the `for`{.python} has finished processing all items in the
  list, the Python version returns the value in the variable as the
  result of the function.

```{=html}
<a name="(part._An-Aside-on-Order-of-Processing-List-Elements)"></a>
```

##### 9.1.8.2 An Aside on Order of Processing List Elements {#An-Aside-on-Order-of-Processing-List-Elements}

There’s another subtlety here if we consider how the two programs run:
the Python version sums the elements from left to right, whereas
the Jayret version sums them right to left. Concretely, the sequence of
values of `run_total`{.python} are computed as:

```python
run_total = 0
run_total = 0 + 5
run_total = 5 + 1
run_total = 6 + 7
run_total = 13 + 3
```
In contrast, the Jayret version unrolls as:

```jayret
sum_list([5, 1, 7, 3]);
5 + sum_list([1, 7, 3]);
5 + 1 + sum_list([7, 3]);
5 + 1 + 7 + sum_list([3]);
5 + 1 + 7 + 3 + sum_list([]);
5 + 1 + 7 + 3 + 0;
5 + 1 + 7 + 3;
5 + 1 + 10;
5 + 11;
16;
```
As a reminder, the Jayret version did this because the `+`{.jayret} in the
`link`{.jayret} case can only reduce to an answer once the sum of the rest
of the list has been computed. Even though we as humans see the chain
of `+`{.jayret} operations in each line of the Jayret unrolling, Jayret sees
only the expression `fst + sum-list(rst)`{.jayret}, which requires the
function call to finish before the `+`{.jayret} executes.

In the case of summing a list, we don’t notice the difference between
the two versions because the sum is the same whether we compute it
left-to-right or right-to-left. In other functions we write, this
difference may start to matter.

```{=html}
<a name="(part._python-funcs-produce-lists)"></a>
```

##### 9.1.8.3 Using For Loops in Functions that Produce Lists {#python-funcs-produce-lists}

Let’s practice using `for`{.python} loops on another function that
traverses lists, this time one that produces a list. Specifically,
let’s write a program that takes a list of strings and produces a list
of words within that list that contain the letter `"z"`{.python}.

As in our `sum_list`{.python} function, we will need a variable to store
the resulting list as we build it up. The following code calls this
`zlist`{.python}. The code also shows how to use `in`{.python} to check
whether a character is in a string (it also works for checking whether
an item is in a list) and how to add an element to the end of a list
(`append`{.python}).

```python
def all_z_words(wordlist : list) -> list:
    """produce list of words from the input that contain z"""
    zlist = [] # start with an empty list
    for wd in wordlist:
        if "z" in wd:
            zlist = [wd] + zlist
    return(zlist)
```
This code follows the structure of `sum_list`{.python}, in that we
update the value of `zlist`{.python} using an expression similar to what
we would have used in Jayret. [For those with prior Python
experience who would have used `zlist.append`{.python} here, hold that
thought. We will get there in [Mutable Lists](mutable-lists.html).]{.margin-note}

::: {.exercise}
Write tests for `all_z_words`{.python}.
:::

::: {.exercise}
Write a second version of `all_z_words`{.python} using
`filter`{.python}. Be sure to write tests for it!
:::

::: {.exercise}
Contrast these two versions and the corresponding tests. Did you
notice anything interesting?
:::

```{=html}
<a name="(part._Summary-The-List-Processing-Template-for-Python)"></a>
```

##### 9.1.8.4 Summary: The List-Processing Template for Python {#Summary-The-List-Processing-Template-for-Python}

Just as we had a template for writing list-processing functions in
Jayret, there is a corresponding template in Python based on
`for`{.python} loops. As a reminder, that pattern is as follow:

```python
def func(lst: list):
  result = ...  # what to return if the input list is empty
  for item in lst:
    # combine item with the result so far
    result = ... item ... result
  return result
```

Keep this template in mind as you learn to write functions over lists
in Python.

```{=html}
<a name="(part._struct-traverse-element-procedure-lib-render-cond-rkt-38-12-loops-in-Pyret)"></a>
```

##### 9.1.8.5 for each loops in Jayret {#struct-traverse-element-procedure-lib-render-cond-rkt-38-12-loops-in-Pyret}

[This section can be read
without reading the rest of this chapter, so if you have been directed to it
before being introduced to Python, do not worry! While the content below mirrors
similar constructs that exist in Python, it is introduced on its own.]{.margin-note}

The previous sections introduced `for`{.python} loops in Python, and showed a
template for processing lists with them. Jayret can
do similar, using the following pattern:

```jayret
Object func(List lst) {
    var result = ...;
    // what to return if the input list is empty
    for (item : lst) {
        // combine item with the result so far
        result = ...;
        item;
        ...;
        result;
    }
    return result;
}
```

There are a few new language features used in this example, introduced in the
following several sections.

```{=html}
<a name="(part._Variables-that-can-change)"></a>
```

##### 9.1.8.5.1 Variables that can change {#Variables-that-can-change}

First, note that we introduce the variable `result`{.jayret} with `var result`{.jayret}
– this means that it can vary, which is important for the use with
`for each`{.jayret}.

By default, all variables in the program directory can never be changed. i.e.,
if I define a variable `x`{.jayret}, I can not redefine it later:

```jayret
x = 10;
// ...
x = 20;
// produces shadowing error
```

If we do want to change (or mutate) a variable in the directory later, we can, but we must
declare the variable can change – as in, when we define it, rather than writing
`x = 10`{.jayret}, we must write `var x = 10`{.jayret}. Then, when we want to
update it, we can do so with the `=`{.jayret} operator, as is done in the template above.

```jayret
var x = 10;
// ... x points to 10 in directory
x = 20;
// ... x now points to 20 in directory
```

Note that trying to use `=`{.jayret} on a variable that was not declared using
`var`{.jayret} will produce an error, and variables can still only ever be declared
once (whether with `var x = ...`{.jayret} or `x = ...`{.jayret}).

```{=html}
<a name="(part._block-notation)"></a>
```

##### 9.1.8.5.2 block notation {#block-notation}

Another new language feature shown in these examples is that since Jayret
functions by default expect only a single (non-definition) expression, we have
to add the `block`{.jayret} annotation at the top, indicating that the body of the
function is multiple expressions, with the final one being what the function
evaluates to.

As another example, if we tried to write:

```jayret
Object my-function() {
    1;
    return 2;
}
```

Jayret would (rightly) error – since the function returns the last expression in
its body, the `1`{.jayret} will be ignored – and is most likely a mistake! Perhaps
the goal was to write:

```jayret
Object my-function() {
    return 1 + 2;
}
```

However, since a `for each`{.jayret} expression exists only to modify a variable,
functions that contain them will always have multiple expressions, and so
we need to communicate to Jayret that this is not a mistake. Adding `block`{.jayret}
before the `:`{.jayret} that begins the function (or, in general, wrapping any
expressions in `block:`{.jayret} and `end`{.jayret}) communicates to Jayret that we
understand that there are multiple expressions, and just want to evaluate to the
last one. So, if we truly wanted to write a function as our first example, we
could do that with:

```jayret
Object my-function() {
    1;
    return 2;
}
```

```{=html}
<a name="(part._How-struct-traverse-element-procedure-lib-render-cond-rkt-38-12-works)"></a>
```

##### 9.1.8.5.3 How for each works {#How-struct-traverse-element-procedure-lib-render-cond-rkt-38-12-works}

A `for each`{.jayret} expression runs its body once for each element in the input
list, adding an entry to the program directory for each element as it goes. It
does not produce any value directly, so much instead rely on modifying variables
(described above) to produce a computation.

Consider summing a list of numbers. We could write a function that does this,
following our pattern, as:

```jayret
Object sum-list(List lst) {
    var run_total = 0;
    for (item : lst) {
        run_total = item + run_total;
    }
    return run_total;
} where {
    
}
```

On the concrete test input `[5, 1, 7, 3]`{.jayret}, the loop runs four times,
once with `item`{.jayret} set to `5`{.jayret}, then with `item`{.jayret} set to `1`{.jayret},
then with `item`{.jayret} set to `7`{.jayret}, and finally with `item`{.jayret} set to
`3`{.jayret}.

The `for each`{.jayret} construct saves us from writing the common code
multiple times, and also handles the fact that the lists we are
processing can be of arbitrary length (so we can’t predict how many
times to write the common code). Thus, what happens is:

```python
run_total = 0
run_total = run_total + 5
run_total = run_total + 1
run_total = run_total + 7
run_total = run_total + 3
```

```{=html}
<a name="(part._Testing-and-variables-that-can-change)"></a>
```

##### 9.1.8.5.4 Testing and variables that can change {#Testing-and-variables-that-can-change}

We intentionally showed a very particular pattern of using variables that can
change. While there are other uses (explored in part in
[Mutating Variables](mutating-variables.html)), a main reason to stay with this particular
template is the difficulty in testing and correspondingly, understanding, code
that uses them in other ways.

In particular, note that the pattern means that we never define a variables that
can change outside a function, which means it can never be used by
different functions, or multiple function calls. Each time the function runs, a
new variable is created, it is modified in the `for each`{.jayret} loop, and then
the value is returned, and the entry in the program directory is removed.

Consider what happens if we don’t follow our pattern. Let’s say we had the
following problem:

::: {.exercise}
Given a list of numbers, return the prefix of the list (i.e., all
elements, starting from the beginning) that sums to less than 100.
:::

Having learned about mutable variables, but not following the pattern, you might
come up with code like this:

```jayret
var count = 0;
List prefix-under-100(List l) {
    var output = [];
    return for (elt : l) {
        count = count + elt;
        when ((count < 100)) {
            output = output + [elt];
        }
    }
}
```

Now, this might seem reasonable – we’ve used a new construct, `when`{.jayret},
which is an `if`{.jayret} expression that has no `else`{.jayret} – this only makes
sense to do inside of a `for each`{.jayret} block, where we don’t need a value as a
result. It is equivalent to:

```jayret
if ((count < 100)) {
    output = output + [elt];
} else {
    return nothing;
}
```

Where `nothing`{.jayret} is a value that is used in Jayret to indicate that there is
no particular value of importance.

But what happens when we use this function?

```jayret
@Check void test() {
    assertEquals(prefix-under-100([1, 2, 3]), [1, 2, 3]);
    assertEquals(prefix-under-100([20, 30, 40]), [20, 30, 40]);
    assertEquals(prefix-under-100([80, 20, 10]), [80]);
}
```

The first two tests pass, but the last one doesn’t. Why? If we run the first one
again, things are even more confusing, i.e., if instead of the above, we ran
this `check`{.jayret} block:

```jayret
@Check void test() {
    assertEquals(prefix-under-100([1, 2, 3]), [1, 2, 3]);
    assertEquals(prefix-under-100([20, 30, 40]), [20, 30, 40]);
    assertEquals(prefix-under-100([80, 20, 10]), [80]);
    assertEquals(prefix-under-100([1, 2, 3]), [1, 2, 3]);
}
```

Now the test that passed at first no longer passes!

What we are seeing is that since the variable is outside the function, it is
shared across different calls to the function. It is added to the program
directory once, and each time we call `prefix-under-100`{.jayret}, the program
directory entry is changed, but it is never reset.

Intentionally, all other uses of mutation have been on directory entries that
were created only for the body of the function, which meant that when the
function exited, they were removed. But now, we are always modifying the single
`count`{.jayret} variable. This means that every time we call
`prefix-under-100`{.jayret}, it behaves differently, because it not only do we have
to understand the code in the body of the function, we have to know the current
value of the count variable, which is not something we can figure out by just
looking at the code!

Functions that behave like this are said to have "side effects", and they are
much harder to test and much harder to understand, and as a result, much more
likely to have bugs! While the above example is wrong in a relatively
straightforward way, side effects can cause extremely subtle bugs that only
happen when functions are called in particular orders – orders that may only
arised in very specific situations, making them hard to understand or reproduce.

While there are some places where doing this is necessary, almost all code can
be written without side effects, and will be much more reliable. We will explore
some cases where we might want to do this in [Mutating Variables](mutating-variables.html).
