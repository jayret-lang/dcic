---
title: Getting Started
section_number: 3.1
source_file: getting-started.html
prev: part_foundations.html
up: part_foundations.html
next: Naming_Values.html
---

```{=html}
<a name="(part._getting-started)"></a>
```

### 3.1 Getting Started {#getting-started}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._flags-notice-wonder%29">3.1.1<span class="hspace"> </span>Motivating Example: Flags</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-numbers%29">3.1.2<span class="hspace"> </span>Numbers</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions%29">3.1.3<span class="hspace"> </span>Expressions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-terminology%29">3.1.4<span class="hspace"> </span>Terminology</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-strings%29">3.1.5<span class="hspace"> </span>Strings</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-images%29">3.1.6<span class="hspace"> </span>Images</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-combine-images%29">3.1.6.1<span class="hspace"> </span>Combining Images</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-first-flag%29">3.1.6.2<span class="hspace"> </span>Making a Flag</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._types-and-errors%29">3.1.7<span class="hspace"> </span>Stepping Back: Types, Errors, and Documentation</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-types%29">3.1.7.1<span class="hspace"> </span>Types and Contracts</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-errors%29">3.1.7.2<span class="hspace"> </span>Format and Notation Errors</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="getting-started.html#%28part._expressions-documentation%29">3.1.7.3<span class="hspace"> </span>Finding Other
Functions: Documentation</a></p></td></tr></table>
```

```{=html}
<a name="(part._flags-notice-wonder)"></a>
```

#### 3.1.1 Motivating Example: Flags {#flags-notice-wonder}

Imagine that you are starting a graphic design company, and want to be
able to create images of flags of different sizes and configurations
for your customers. The following diagram shows a sample of the images
that your software will have to help you create:

![](flags.png){width="393" height="207"}

Before we try to write code to create these different images, you
should step back, look at this collection of images, and try to
identify features of the images that might help us decide what to
do. To help with this, we’re going to answer a pair of specific
questions to help us make sense of the images:

- What do you notice about the flags?

- What do you wonder about the flags or a program that might
  produce them?

::: {.do-now}
Actually write down your answers. Noticing features of data and
information is an essential skill in computing.
:::

Some things you might have noticed:

- Some flags have similar structure, just with different colors

- Some flags come in different sizes

- Some flags have poles

- Most of these look pretty simple, but some real flags have
  complicated figures on them

…and so on.

Some things you might have wondered:

- Do I need to be able to draw these images by hand?

- Will we be able to generate different sized flags from the same
  code?

- What if we have a non-rectangular flag?

…and so on.

The features that we noticed suggest some things we’ll need to be able
to do to write programs to generate flags:

- We might want to compute the heights of the stripes from the
  overall flag dimensions (we’ll write programs using numbers)

- We need a way to describe colors to our program (we’ll learn strings)

- We need a way to create images based on simple shapes of
  different colors (we’ll create and combine expressions)

Let’s get started!

```{=html}
<a name="(part._expressions-numbers)"></a>
```

#### 3.1.2 Numbers {#expressions-numbers}

Start simple: compute the sum of 3 and 5.

To do this computation with a computer, we need to write down the
computation and ask the computer to run or evaluate the
computation so that we get a number back. A software or
web-application in which you write and run programs is called a
programming environment. In the first part of this course, we
will use a language called Jayret.

Go to [the on-line editor](https://jayret-lang.github.io/code/editor) (which we’ll henceforth refer to as “CPO”).
For now, we will work only in the right-hand side (the
interactions pane).

The ››› is called the “prompt”—that’s where we tell CPO to run a
program. Let’s tell it to add `3`{.pyret} and `5`{.pyret}. Here’s what we write:

::: {.pyret-repl}
```jayret
3 + 5;
```
:::

Press the Return key, and the result of the computation will appear on
the line below the prompt, as shown below:

::: {.pyret-repl}
```jayret
3 + 5;
```
``` output
8
```
:::

Not surprisingly, we can do other arithmetic computations

::: {.pyret-repl}
```jayret
2 * 6;
```
``` output
12
```
:::

(Note: `*`{.pyret} is how we write the multiplication sign.)

What if we try `3 + 4 * 5`{.pyret}?

::: {.do-now}
Try it! See what Jayret says.
:::

Jayret gave you an error message. What it says is that
Jayret isn’t sure whether we mean

```jayret
(3 + 4) * 5;
```

or

```jayret
3 + (4 * 5);
```

so it asks us to include parentheses to make that explicit.
Every programming language has a set of rules about how you have to
write down programs. Jayret’s rules require parentheses to avoid
ambiguity.

::: {.pyret-repl}
```jayret
(3 + 4) * 5;
```
``` output
35
```
:::

::: {.pyret-repl}
```jayret
3 + (4 * 5);
```
``` output
23
```
:::

Another Jayret rule requires spaces around the arithmetic operators.
See what happens if you forget
the spaces:

::: {.pyret-repl}
```jayret
3;
+4;
```
:::

Jayret will show a different error message that highlights the part of
the code that isn’t formatted properly, along with an explanation of
the issue that Jayret has detected. To fix the error, you can press the
up-arrow key within the right pane and edit the previous computation
to add the spaces.

::: {.do-now}
Try doing it right now, and confirm that you succeeded!
:::

What if we want to get beyond basic arithmetic operators? Let’s say
we want the minimum of two numbers. We’d write this as

::: {.pyret-repl}
```jayret
num-min(2, 8);
```
:::
[Why `num-`{.pyret}? It’s because “minimum” is a concept that makes sense
on data other than numbers; Jayret calls the min operator `num-min`{.pyret} to
avoid ambiguity.]{.margin-note}

```{=html}
<a name="(part._expressions)"></a>
```

#### 3.1.3 Expressions {#expressions}

Note that when we run `num-min`{.pyret}, we get a number in return (as we did
for `+`{.pyret}, `*`{.pyret}, …). This means we should be able to use the result of
`num-min`{.pyret} in other computations where a number is expected:

::: {.pyret-repl}
```jayret
5 * num-min(2, 8);
```
``` output
10
```
:::

::: {.pyret-repl}
```jayret
(1 + 5) * num-min(2, 8);
```
``` output
12
```
:::

Hopefully you are starting to see a pattern. We can build up more
complicated computations from smaller ones, using operations to combine
the results from the smaller computations. We will use the term
expression to refer a computation written in a format
that Jayret can understand and evaluate to an answer.

::: {.exercise}
In CPO, try to write the expressions for each of the
following computations:

- subtract 3 from 7, then multiply the result by 4

- subtract 3 from the multiplication of 7 and 4

- the sum of 3 and 5, divided by 2

- the max of 10 subtracted from 5 and -20

- 2 divided by the sum of 3 and 5
:::

::: {.do-now}
What if you get a fraction as a response?

If you’re not sure how to get a fraction, there are two ways: you can either
write an expression that produces a fractional answer, or you can type
one in directly (e.g., `1/3`{.pyret}).

Either way, you can click on the result
in the interactions pane to change how the number is presented. Try it!
:::

```{=html}
<a name="(part._expressions-terminology)"></a>
```

#### 3.1.4 Terminology {#expressions-terminology}

Look at an interaction like

::: {.pyret-repl}
```jayret
(3 + 4) * (5 + 1);
```
``` output
42
```
:::

There are actually several kinds of information in this interaction,
and we should give them names:

- Expression: a computation written in the formal notation
  of a programming language
  
  Examples here include `4`{.pyret}, `5 + 1`{.pyret}, and `(3 + 4) * (5 + 1)`{.pyret}

- Value: an expression that can’t be computed further (it is
  its own result)
  
  So far, the only values we’ve seen are numbers.

- Program: a sequence of expressions that you want to run

```{=html}
<a name="(part._expressions-strings)"></a>
```

#### 3.1.5 Strings {#expressions-strings}

What if we wanted to write a program that used information other than
numbers, such as someone’s name? For names and other text-like data,
we use what are called strings. Here are some examples:

```jayret
"Kathi";
"Go Bears!";
"CSCI0111";
"Carberry, Josiah";
```

What do we notice? Strings can contain spaces, punctuation, and
numbers. We use them to capture textual data. For our flags
example, we’ll use strings to name colors: `"red"`{.pyret}, `"blue"`{.pyret}, etc.

Note that strings are case-sensitive, meaning that
capitalization matters (we’ll see where it matters shortly).

```{=html}
<a name="(part._expressions-images)"></a>
```

#### 3.1.6 Images {#expressions-images}

We have seen two kinds of data: numbers and strings. For flags, we’ll
also need images. Images are different from both numbers and strings
(you can’t describe an entire image with a single number—well, not
unless you get much farther into computer science but let’s not get
ahead of ourselves).

Jayret has built-in support for images. When you start up Jayret, you’ll
see a grayed-out line that says “use context essentials2021” (or
something similar). This line configures Jayret with some basic
functionality beyond basic numbers and strings.

::: {.do-now}
Press the “Run”
button (to activate the features in essentials), then write each of
these Jayret expressions at the interactions prompt to see
what they produce:


- `circle(30, "solid", "red")`{.pyret}

- `circle(30, "outline", "blue")`{.pyret}

- `rectangle(20, 10, "solid", "purple")`{.pyret}
:::

Each of these expressions names the shape to draw, then configures the
shape in the parentheses that follow. The configuration information
consists of the shape dimensions (the radius for circles, the width
and height for rectangles, both measured in screen pixels), a string
indicating whether to make a solid shape or just an outline, then a
string with the color to use in drawing the shape.

Which shapes and colors does Jayret know about? Hold this
question for just a moment. We’ll show you how to look up information
like this in the documentation shortly.

```{=html}
<a name="(part._expressions-combine-images)"></a>
```

##### 3.1.6.1 Combining Images {#expressions-combine-images}

Earlier, we saw that we could use operations like `+`{.pyret} and
`*`{.pyret} to combine numbers through expressions. Any time you get a
new kind of datum in programming, you should ask what operations the
language gives you for working with that data. In the case of images
in Jayret, the collection includes the ability to:

- rotate them

- scale them

- flip them

- put two of them side by side

- place one on top of the other

- and more ...

Let’s see how to use some of these.

::: {.exercise}
Type the following expressions into Jayret:

```jayret
rotate(45, rectangle(20, 30, "solid", "red"));
```

What does the `45`{.pyret} represent? Try some different numbers in place of the
`45`{.pyret} to confirm or refine your hypothesis.

```jayret
overlay(circle(25, "solid", "yellow"),
  rectangle(50, 50, "solid", "blue"));
```

Can you describe in prose what `overlay`{.pyret} does?

```jayret
above(circle(25, "solid", "red"), rectangle(30, 50, "solid", "blue"));
```

What kind of value do you get from using the `rotate`{.pyret} or
`above`{.pyret} operations? (hint: your answer should be one of
number, string, or image)
:::

These examples let us think a bit deeper about expressions. We have
simple values like numbers and strings. We have operations or
functions that combine values, like `+`{.pyret} or
`rotate`{.pyret} (“functions” is the term more commonly used in
computing, whereas your math classes likely used “operations”). Every
function produces a value, which can be used as input to another
function. We build up expressions by using values and the outputs of
functions as inputs to other functions.

For example, we used `above`{.pyret} to create an image out of two
smaller images. We could take that image and rotate it using the
following expression.

```jayret
rotate(45, above(circle(25, "solid", "red"), rectangle(30, 50, "solid", "blue")));
```

This idea of using the output of one function as input to another is
known as composition. Most interesting programs arise from
composing results from one computation with another. Getting
comfortable with composing expressions is an essential first step in
learning to program.

::: {.exercise}
Try to create the following images:


- a blue triangle (you pick the size). As with `circle`{.pyret},
  there is a `triangle`{.pyret} function that takes a side length, fill
  style, and color and produces an image of an equilateral triangle.

- a blue triangle inside a yellow rectangle

- a triangle oriented at an angle

- a bullseye with 3 nested circles aligned in their centers (e.g.,
  the [Target](https://www.target.com/) logo)

- whatever you want—play around and have fun!

The bullseye might be a bit challenging. The

`overlay`{.pyret}

function only takes two images, so you’ll need to think about how to
use composition to layer three circles.
:::

```{=html}
<a name="(part._expressions-first-flag)"></a>
```

##### 3.1.6.2 Making a Flag {#expressions-first-flag}

We’re ready to make our first flag! Let’s start with the flag of
Armenia, which has three horizontal stripes: red on top, blue in the
middle, and orange on the bottom.

::: {.exercise}
Use the functions we have learned so far to create an image of the
Armenian flag. You pick the dimensions (we recommend a width between
100 and 300).

Make a list of the questions and ideas that occur to you along the way.
:::

```{=html}
<a name="(part._types-and-errors)"></a>
```

#### 3.1.7 Stepping Back: Types, Errors, and Documentation {#types-and-errors}

Now that you have an idea of how to create a flag image, let’s go back
and look a bit more carefully at two concepts that you’ve already
encountered: types and error messages.

```{=html}
<a name="(part._expressions-types)"></a>
```

##### 3.1.7.1 Types and Contracts {#expressions-types}

Now that we are composing functions to build more complicated
expressions out of smaller ones, we will have to keep track of which
combinations make sense. Consider the following sample of Jayret code:

```jayret
8 * circle(25, "solid", "red");
```

What value would you expect this to produce? Multiplication is meant to work
on numbers, but this code asks Jayret to multiply a number and an image. Does
this even make sense?

This code does not make sense, and indeed Jayret will produce an error
message if we try to run it.

::: {.do-now}
Try to run that code, then look at the error message. Write down the
information that the error message is giving you about what went wrong
(we’ll come back to your list shortly).
:::

The bottom of the error message says:

_The `*`{.pyret} operator expects to be given two Numbers_

Notice the word “Numbers”. Jayret is telling you what kind of
information works with the `*`{.pyret} operation. In programming, values
are organized into types (e.g., number, string, image). These
types are used in turn to describe what kind of inputs and results (a.k.a.,
outputs) a function works with. For example, * expects to be given two
numbers, from which it will return a number. The last expression we
tried violated that expectation, so Jayret produced an error message.

Talking about “violating expectations” sounds almost legal, doesn’t
it? It does, and the term contract refers to the required types
of inputs and promised types of outputs when using a specific
function. Here are several examples of Jayret contracts (written in the
notation you will see in the documentation):

```pyret
# TODO(pyret2jayret): parse failed (no shifts)
* :: (x1 :: Number, x2 :: Number) -> Number

circle :: (radius :: Number,
           mode :: String,
           color :: String) -> Image

rotate :: (degrees :: Number,
           img :: Image) -> Image

overlay :: (upper-img :: Image,
            lower-img :: Image) -> Image
```

::: {.do-now}
Look at the notation pattern across these contracts. Can you label the
various parts and what information they appear to be giving you?
:::

Let’s look closely at the `overlay`{.pyret} contract to make sure you
understand how to read it. It gives us several pieces of information:

- There is a function called `overlay`{.pyret}

- It takes two inputs (the parts within the parentheses), both of which have the type `Image`{.pyret}

- The first input is the image that will appear on top

- The second input is the image that will appear on the bottom

- The output from calling the function (which follows `->`{.pyret}) will have type `Image`{.pyret}

In general, we read the double-colon (`:`{.pyret}) as “has the type”. We
read the arrow (`->`{.pyret}) as “returns”.

Whenever you compose smaller expressions into more complex
expressions, the types produced by the smaller expressions have to
match the types required by the function you are using to compose
them. In the case of our erroneous `*`{.pyret} expression, the contract
for `*`{.pyret} expects two numbers as inputs, but we gave an image for
the second input. This resulted in an error message when we tried to
run the expression.

A contract also summarizes how many inputs a function
expects. Look at the contract for the `circle`{.pyret} function. It
expects three inputs: a number (for the radius), a string (for the
style), and a string (for the color). What if we forgot the style
string, and only provided the radius and color, as in:

```jayret
circle(100, "purple");
```

The error here is not about the type of the inputs, but rather about
the number of inputs provided.

::: {.exercise}
Run some expressions in Jayret that use an incorrect type for some input
to a function. Run others where you provide the wrong number of
inputs to a function.

What text is common to the incorrect-type
errors? What text is common to the wrong numbers of inputs?

Take note
of these so you can recognize them if they arise while you are programming.
:::

```{=html}
<a name="(part._expressions-errors)"></a>
```

##### 3.1.7.2 Format and Notation Errors {#expressions-errors}

We’ve just seen two different kinds of mistakes that we might make
while programming: providing the wrong type of inputs and
providing the wrong number of inputs to a function. You’ve
likely also run into one additional kind of error, such as when you
make a mistake with the punctuation of programming. For example, you
might have typed an example such as these:

- `3+7`{.pyret}

- `circle(50 "solid" "red")`{.pyret}

- `circle(50, "solid,  "red")`{.pyret}

- `circle(50, "solid," "red")`{.pyret}

- `circle 50, "solid," "red")`{.pyret}

::: {.do-now}
Make sure you can spot the error in each of these! Evaluate these in
Jayret if necessary.
:::

You already know various punctuation rules for writing prose. Code
also has punctuation rules, and programming tools are strict about
following them. While you can leave out a comma and still turn in an
essay, a programming environment won’t be able to evaluate your
expressions if they have punctuation errors.

::: {.do-now}
Make a list of the punctuation rules for Jayret code that you believe
you’ve encountered so far.
:::

Here’s our list:

- Spaces are required around arithmetic operators.

- Parentheses are required to indicate order of operations.

- When we use a function, we put a pair of parentheses
  around the inputs, and we separate the inputs with commas.

- If we use a double-quotation mark to start a string, we need
  another double-quotation mark to close that string.

In programming, we use the term syntax to refer to the rules of
writing proper expressions (we explicitly didn’t say “rules of
punctuation” because the rules go beyond what you think of as
punctuation, but that’s a fair place to start). Making mistakes in
your syntax is common at first. In time, you’ll internalize the
rules. For now, don’t get discouraged if you get errors about syntax
from Jayret. It’s all part of the learning process.

```{=html}
<a name="(part._expressions-documentation)"></a>
```

##### 3.1.7.3 Finding Other Functions: Documentation {#expressions-documentation}

At this point, you may be wondering what else you can do with
images. We mentioned scaling images. What other shapes might we make?
Is there a list somewhere of everything we can do with images?

Every programming language comes with documentation, which is
where you find out the various operations and functions that are
available, and your options for configuring their
parameters. Documentation can be overwhelming for novice programmers,
because it contains a lot of detail that you don’t even know that you
need just yet. Let’s take a look at how you can use the documentation
as a beginner.

Open the [Jayret Image Documentation](https://jayret-lang.github.io/docs/latest/image.html). Focus on the
sidebar on the left. At the top, you’ll see a list of all the
different topics covered in the documentation. Scroll down until you
see “rectangle” in the sidebar: surrounding that, you’ll see
the various function names you can use to create different
shapes. Scroll down a bit further, and you’ll see a list of functions for
composing and manipulating images.

If you click on a shape or function name, you’ll bring up details on
using that function in the area on the right. You’ll see the contract
in a shaded box, a description of what the function does (under the
box), and then a concrete example or two of what you type to use the
function. You could copy and paste any of the examples into Jayret to
see how they work (changing the inputs, for example).

For now, everything you need documentation wise is in the section on
images. We’ll go further into Jayret and the documentation as we go.
