---
title: From Repeated Expressions to Functions
section_number: 3.3
source_file: From_Repeated_Expressions_to_Functions.html
prev: Naming_Values.html
up: part_foundations.html
next: Conditionals_and_Booleans.html
---

```{=html}
<a name="(part._From-Repeated-Expressions-to-Functions)"></a>
```

### 3.3 From Repeated Expressions to Functions {#From-Repeated-Expressions-to-Functions}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._similar-flags%29">3.3.1<span class="hspace"> </span>Example: Similar Flags</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._defining-functions%29">3.3.2<span class="hspace"> </span>Defining Functions</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._function-call-nm%29">3.3.2.1<span class="hspace"> </span>How Functions Evaluate</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._fun-annotations%29">3.3.2.2<span class="hspace"> </span>Type Annotations</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._doc-strings%29">3.3.2.3<span class="hspace"> </span>Documentation</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._moon-weight-pyret%29">3.3.3<span class="hspace"> </span>Functions Practice: Moon Weight</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._writing-examples%29">3.3.4<span class="hspace"> </span>Documenting Functions with Examples</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._pen-cost-pyret%29">3.3.5<span class="hspace"> </span>Functions Practice: Cost of pens</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="From_Repeated_Expressions_to_Functions.html#%28part._.Recap__.Defining_.Functions%29">3.3.6<span class="hspace"> </span>Recap: Defining Functions</a></p></td></tr></table>
```

```{=html}
<a name="(part._similar-flags)"></a>
```

#### 3.3.1 Example: Similar Flags {#similar-flags}

Consider the following two expressions to draw the flags of Armenia
and Austria (respectively). These two countries have the same flag,
just with different colors. The `frame`{.pyret} operator draws a small
black frame around the image.

```jayret
// Lines starting with # are comments for human readers.
// Jayret ignores everything on a line after #.
// armenia
frame(above(rectangle(120, 30, "solid", "red"), above(rectangle(120, 30, "solid", "blue"), rectangle(120, 30, "solid", "orange"))));
// austria
frame(above(rectangle(120, 30, "solid", "red"), above(rectangle(120, 30, "solid", "white"), rectangle(120, 30, "solid", "red"))));
```

Rather than write this program twice, it would be nice to write the
common expression only once, then just change the colors to generate each
flag. Concretely, we’d like to have a custom operator such as
`three-stripe-flag`{.pyret} that we could use as follows:

```jayret
// armenia
three-stripe-flag("red", "blue", "orange");
// austria
three-stripe-flag("red", "white", "red");
```

In this program, we provide `three-stripe-flag`{.pyret} only with the
information that customizes the image creation to a specific flag. The
operation itself would take care of creating and aligning the
rectangles. We want to end up with the same images for the Armenian
and Austrian flags as we would have gotten with our original
program. Such an operator doesn’t exist in Jayret: it is specific only to
our application of creating flag images. To make this program work, then,
we need the ability to add our own operators (henceforth called
functions) to Jayret.

```{=html}
<a name="(part._defining-functions)"></a>
```

#### 3.3.2 Defining Functions {#defining-functions}

In programming, a function takes one or more (configuration)
parameters and uses them to produce a result.

::: {.strategy}
If we have multiple concrete expressions that are identical except for
a couple of specific data values, we create a function with the common
code as follows:

- Write down at least two expressions showing the desired computation (in this
  case, the expressions that produce the Armenian and Austrian flags).

- Identify which parts are fixed (i.e., the creation of rectangles
  with dimensions `120`{.pyret} and `30`{.pyret}, the use of `above`{.pyret} to stack the
  rectangles) and which
  are changing (i.e., the stripe colors).

- For each changing part, give it a name (say
  `top`{.pyret}, `middle`{.pyret}, and `bottom`{.pyret}), which will be the
  parameter that stands for that part.

- Rewrite the examples to be in terms of these parameters. For example:
  
  ```jayret
frame(above(rectangle(120, 30, "solid", top), above(rectangle(120, 30, "solid", middle), rectangle(120, 30, "solid", bottom))));
  ```
- Name the function something suggestive: e.g., `three-stripe-flag`{.pyret}.

- Write the function declaration syntax around the expression:
  
  ```jayret
  Object <function-name>(<parameters>) {
      return <the expression goes here>;
  }
  ```
  where the expression is called the body of the
  function. (Programmers often use angle brackets to say “replace with
  something appropriate”; the brackets themselves aren’t part of the notation.)
:::

Here’s the end product:

```jayret
Object three-stripe-flag(top, middle, bottom) {
    return frame(above(rectangle(120, 30, "solid", top), above(rectangle(120, 30, "solid", middle), rectangle(120, 30, "solid", bottom))));
}
```
While this looks like a lot of work now, it won’t once you get used to
it. We will go through the same steps over and over, and eventually
they’ll become so intuitive that you won’t need to start from multiple
similar expressions.

::: {.do-now}
Why does the function body have only one expression, when before we had a separate one
for each flag?
:::


We have only one expression because the whole point was to get rid of
all the changing parts and replace them with parameters.

With this function in hand, we can write the following two expressions
to generate our original flag images:

```jayret
three-stripe-flag("red", "blue", "orange");
three-stripe-flag("red", "white", "red");
```

When we provide values for the parameters of a function to get a
result, we say that we are calling the function. We use the
term call for expressions of this form.

If we want to name the resulting images, we can do so as follows:

```jayret
armenia = three-stripe-flag("red", "blue", "orange");
austria = three-stripe-flag("red", "white", "red");
```

(Side note: Jayret only allows one value per name in the directory. If
your file already had definitions for the names `armenia`{.pyret} or
`austria`{.pyret}, Jayret will give you an error at this point. You can
use a different name (like `austria2`{.pyret}) or comment out the
original definition using `//`{.pyret}.)

```{=html}
<a name="(part._function-call-nm)"></a>
```

##### 3.3.2.1 How Functions Evaluate {#function-call-nm}

So far, we have learned three rules for how Jayret processes your program:

- If you write an expression, Jayret evaluates it to produce
  its value.

- If you write a statement that defines a name, Jayret evaluates
  the expression (right side of `=`{.pyret}), then makes an entry in the
  directory to associate the name with the value.

- If you write an expression that uses a name from the directory,
  Jayret substitutes the name with the corresponding value.

Now that we can define our own functions, we have to consider two more
cases: what does Jayret do when you define a function, and what does
Jayret do when you call a function (with values for the parameters)?

- When Jayret encounters a function definition in your file, it makes an
  entry in the directory to associate the name of the function with its
  code. The body of the function does not get evaluated at this time.

- When Jayret encounters a function call while evaluating an expression,
  it replaces the call with the body of the function, but with the
  parameter values substituted for the parameter names in the
  body. Jayret then continues to evaluate the body with the substituted
  values.

As an example of the function-call rule, if you evaluate

```jayret
three-stripe-flag("red", "blue", "orange");
```

Jayret starts from the function body

```jayret
frame(above(rectangle(120, 30, "solid", top), above(rectangle(120, 30, "solid", middle), rectangle(120, 30, "solid", bottom))));
```

substitutes the parameter values

```jayret
frame(above(rectangle(120, 30, "solid", "red"), above(rectangle(120, 30, "solid", "blue"), rectangle(120, 30, "solid", "orange"))));
```

then evaluates the expression, producing the flag image.

Note that the second expression (with the substituted values) is the
same expression we started from for the Armenian flag. Substitution
restores that expression, while still allowing the programmer to write
the shorthand in terms of `three-stripe-flag`{.pyret}.

```{=html}
<a name="(part._fun-annotations)"></a>
```

##### 3.3.2.2 Type Annotations {#fun-annotations}

What if we made a mistake, and tried to call the function as follows:

```jayret
three-stripe-flag(50, "blue", "red");
```

::: {.do-now}
What do you think Jayret will produce for this expression?
:::

The first parameter to `three-stripe-flag`{.pyret} is supposed to be the
color of the top stripe. The value `50`{.pyret} is not a string (much less a string naming a
color). Jayret will substitute `50`{.pyret} for `top`{.pyret} in the first call to
`rectangle`{.pyret}, yielding the following:

```jayret
frame(above(rectangle(120, 30, "solid", 50), above(rectangle(120, 30, "solid", "blue"), rectangle(120, 30, "solid", "red"))));
```

When Jayret tries to evaluate the `rectangle`{.pyret} expression to create
the top stripe, it generates an error that refers to that call to
`rectangle`{.pyret}.

If someone else were using your function, this error might not make
sense: they didn’t write an expression about rectangles. Wouldn’t it
be better to have Jayret report that there was a problem in the use of
`three-stripe-flag`{.pyret} itself?

As the author of `three-stripe-flag`{.pyret}, you can make that happen by
annotating the parameters with information about the expected type of
value for each parameter. Here’s the function definition again, this
time requiring the three parameters to be strings:

```jayret
Object three-stripe-flag(String top, String middle, String bottom) {
    return frame(above(rectangle(120, 30, "solid", top), above(rectangle(120, 30, "solid", middle), rectangle(120, 30, "solid", bottom))));
}
```

Notice that the notation here is similar to what we saw in contracts
within the documentation: the type name is written before each parameter
name, separated by a space (so far, one of
`Number`{.pyret}, `String`{.pyret}, or `Image`{.pyret}).[Putting each parameter
on its own line is not required, but it sometimes helps with readability.]{.margin-note}

Run your file with this new definition and try the erroneous call
again. You should get a different error message that is just in terms
of `three-stripe-flag`{.pyret}.

It is also common practice to add a type annotation that captures the
type of the function’s output. That annotation goes after the list of
parameters:

```jayret
Image three-stripe-flag(String top, String middle, String bottom) {
    return frame(above(rectangle(120, 30, "solid", top), above(rectangle(120, 30, "solid", middle), rectangle(120, 30, "solid", bottom))));
}
```

Note that all of these type annotations are optional. Jayret will run
your program whether or not you include them. You can put type
annotations on some parameters and not others; you can include the
output type but not any of the parameter types. Different programming
languages have different rules about types.

We will think of types as playing two roles: giving Jayret information
that it can use to focus error messages more accurately, and guiding
human readers of programs as to the proper use of user-defined functions.

```{=html}
<a name="(part._doc-strings)"></a>
```

##### 3.3.2.3 Documentation {#doc-strings}

Imagine that you opened your program file from this chapter a couple
of months from now. Would you remember what computation
`three-stripe-flag`{.pyret} does? The name is certainly suggestive, but
it misses details such as that the stripes are stacked vertically
(rather than horizontally) and that the stripes are equal
height. Function names aren’t designed to carry this much information.

Programmers also annotate a function with a docstring, a short,
human-language description of what the function does. Here’s what the
Jayret docstring might look like for `three-stripe-flag`{.pyret}:

```jayret
Image three-stripe-flag(String top, String middle, String bottom) {
    // produce image of flag with three equal-height horizontal stripes
    return frame(above(rectangle(120, 30, "solid", top), above(rectangle(120, 30, "solid", middle), rectangle(120, 30, "solid", bottom))));
}
```

While docstrings are also optional from Jayret’s perspective, you
should always provide one when you write a function. They are
extremely helpful to anyone who has to read your program, whether that is
a co-worker, grader…or yourself, a couple of weeks from now.

```{=html}
<a name="(part._moon-weight-pyret)"></a>
```

#### 3.3.3 Functions Practice: Moon Weight {#moon-weight-pyret}

Suppose we’re responsible for outfitting a team of astronauts for
lunar exploration. We have to determine how much each of them will
weigh on the Moon’s surface. On the Moon, objects weigh only one-sixth
their weight on earth. Here are the expressions for
several astronauts (whose weights are expressed in pounds):

```jayret
100 * 1/6;
150 * 1/6;
90 * 1/6;
```
As with our examples of the Armenian and Austrian flags, we are
writing the same expression multiple times. This is another situation
in which we should create a function that takes the changing data as a
parameter but captures the fixed computation only once.

In the case of the flags, we noticed we had written essentially the
same expression more than once. Here, we have a computation that we
expect to do multiple times (once for each astronaut). It’s
boring to write the same expression over and over again. Besides, if
we copy or re-type an expression multiple times, sooner or later we’re
bound to make a transcription error.[This is an instance of
the [DRY
principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), where DRY means "don’t repeat yourself".]{.margin-note}

Let’s remind ourselves of the steps for creating a function:

- Write down some examples of the desired calculation. We did that
  above.

- Identify which parts are fixed (above, `* 1/6`{.pyret}) and which
  are changing (above, `100`{.pyret}, `150`{.pyret}, `90`{.pyret}...).

- For each changing part, give it a name (say
  `earth-weight`{.pyret}), which will be the parameter that stands for it.

- Rewrite the examples to be in terms of this parameter:
  
  ```jayret
earth-weight * 1/6;
  ```
  This will be the body, i.e., the expression inside
  the function.
- Come up with a suggestive name for the function: e.g., `moon-weight`{.pyret}.

- Write the syntax for functions around the body expression:
  
  ```jayret
Object moon-weight(earth-weight) {
    return earth-weight * 1/6;
}
  ```
- Remember to include the types of the parameter and output, as
  well as the documentation string. This yields the final function:
  
  ```jayret
int moon-weight(int earth-weight) {
    // Compute weight on moon from weight on earth
    return earth-weight * 1/6;
}
  ```

```{=html}
<a name="(part._writing-examples)"></a>
```

#### 3.3.4 Documenting Functions with Examples {#writing-examples}

In each of the functions above, we’ve started with some examples of
what we wanted to compute, generalized from there to a generic
formula, turned this into a function, and then used the function in
place of the original expressions.

Now that we’re done, what use are the initial examples? It seems
tempting to toss them away. However, there’s an important rule about
software that you should learn: Software Evolves. Over time,
any program that has any use will change and grow, and as a result may
end up producing different values than it did initially. Sometimes
these are intended, but sometimes these are a result of mistakes
(including such silly but inevitable mistakes like accidentally adding
or deleting text while typing). Therefore, it’s always useful to keep
those examples around for future reference, so you can immediately be
alerted if the function deviates from the examples it was supposed to
generalize.

Jayret makes this easy to do. Every function can be accompanied by a
`where { }`{.jayret} block that records the examples. For instance, our
`moon-weight`{.pyret} function can be modified to read:

```jayret
int moon-weight(int earth-weight) {
    // Compute weight on moon from weight on earth
    return earth-weight * 1/6;
} where {
    assertEquals(moon-weight(100), 100 * 1/6);
    assertEquals(moon-weight(150), 150 * 1/6);
    assertEquals(moon-weight(90), 90 * 1/6);
}
```
When written this way, Jayret will actually check the answers every
time you run the program, and notify you if you have changed the
function to be inconsistent with these examples.

::: {.do-now}
Check this! Change the formula—for instance, replace the body of the
function with

```jayret
earth-weight * 1/3;
```
—and see what happens. Pay attention to the output from CPO: you
should get used to recognizing this kind of output.
:::

::: {.do-now}
Now, fix the function body, and instead change one of the answers—e.g., write

```jayret
assertEquals(moon-weight(90), 90 * 1/3);
```
—and see what happens. Contrast the output in this case with the output above.
:::

Of course, it’s pretty unlikely you will make a mistake with a
function this simple (except through a typo). After all, the examples
are so similar to the function’s own body. Later, however, we will see
that the examples can be much simpler than the body, and there is a real chance
for things to get inconsistent. At that point, the examples become invaluable
in making sure we haven’t made a mistake in our program. In fact, this is so
valuable in professional software development that good programmers
always write down large collections of examples—called
tests—to make sure their programs are behaving as they expect.

For our purposes, we are writing examples as part of the process of
making sure we understand the problem. It’s always a good idea
to make sure you understand the question before you start writing
code to solve a problem. Examples are a nice intermediate point: you
can sketch out the relevant computation on concrete
values first, then worry about turning it into a function. If you
can’t write the examples, chances are you won’t be able to write the
function either. Examples break down the programming process into
smaller, manageable steps.

```{=html}
<a name="(part._pen-cost-pyret)"></a>
```

#### 3.3.5 Functions Practice: Cost of pens {#pen-cost-pyret}

Let’s create one more function, this time for a more complicated example.
Imagine that you are trying to compute the total cost of an order of
pens with slogans (or messages) printed on them. Each pen costs 25
cents plus an additional 2 cents per character in the message (we’ll
count spaces between words as characters).

Following our steps to create a function once again,
let’s start by writing two concrete expressions that do this
computation.

```jayret
// ordering 3 pens that say "wow"
3 * (0.25 + (string-length("wow") * 0.02));
// ordering 10 pens that say "smile"
10 * (0.25 + (string-length("smile") * 0.02));
```

These examples introduce a new built-in function called
`string-length`{.pyret}. It takes a string as input and produces the
number of characters (including spaces and punctuation) in the string.
These examples also show an example of working with
numbers other than integers.[Jayret requires a number before the
decimal point, so if the “whole number” part is zero, you need to write
`0`{.pyret} before the decimal. Also observe that Jayret uses a decimal
point; it doesn’t support conventions such as
[“0,02”](https://en.wikipedia.org/wiki/Decimal_separator).]{.margin-note}

The second step to writing a function was to identify which
information differs across our two examples. In this case, we have
two: the number of pens and the message to put on the pens.
This means our function will have two parameters rather than just one.

```jayret
int pen-cost(int num-pens, String message) {
    return num-pens * (0.25 + (string-length(message) * 0.02));
}
```
Of course, as things get too long, it may be helpful to use multiple lines:

```jayret
int pen-cost(int num-pens, String message) {
    return num-pens * (0.25 + (string-length(message) * 0.02));
}
```
If you want to write a multi-line docstring, use `/* ... */`{.jayret}
block-comment syntax:

```jayret
int pen-cost(int num-pens, String message) {
    /* total cost for pens, each 25 cents
       plus 2 cents per message character */
    return num-pens * (0.25 + (string-length(message) * 0.02));
}
```
We should also document the examples that we used when creating the
function:

```jayret
int pen-cost(int num-pens, String message) {
    /* total cost for pens, each 25 cents
       plus 2 cents per message character */
    return num-pens * (0.25 + (string-length(message) * 0.02));
} where {
    assertEquals(pen-cost(3, "wow"), 3 * (0.25 + (string-length("wow") * 0.02)));
    assertEquals(pen-cost(10, "smile"), 10 * (0.25 + (string-length("smile") * 0.02)));
}
```

When writing `where { }`{.jayret} examples, we also want to include special
yet valid cases that the function might have to handle, such as an empty
message.

```jayret
assertEquals(pen-cost(5, ""), 5 * 0.25);
```
Note that our empty-message example has a simpler expression as the
second argument to `assertEquals`{.jayret}. The expression for what the function returns
doesn’t have to match the body expression; it simply has to evaluate
to the same value as you expect the example to produce. Sometimes,
we’ll find it easier to just write the expected value directly. For
the case of someone ordering no pens, for example, we’d include:

```jayret
assertEquals(pen-cost(0, "bears"), 0);
```
The point of the examples is to document how a function behaves on a
variety of inputs. What goes in the second argument to `assertEquals`{.jayret} should
summarize the computation or the answer in some meaningful way. Most
important? Do not write the function, run it to determine the answer,
then use that answer as the second argument to

`assertEquals`{.jayret}

! Why not?
Because the examples are meant to give some redundancy to the design
process, so that you catch errors you might have made. If your
function body is incorrect, and you use the function to generate the
example, you won’t get the benefit of using the example to check for
errors.

We’ll keep returning to this idea of writing good examples. Don’t
worry if you still have questions for now. Also, for the time being,
we won’t worry about nonsensical situations like negative numbers of
pens. We’ll get to those after we’ve learned additional coding
techniques that will help us handle such situations properly.

::: {.do-now}
We could have combined our two special cases into one example, such as

```jayret
assertEquals(pen-cost(0, ""), 0);
```
Does doing this seem like a good idea? Why or why not?
:::

```{=html}
<a name="(part._Recap-Defining-Functions)"></a>
```

#### 3.3.6 Recap: Defining Functions {#Recap-Defining-Functions}

This chapter has introduced the idea of a function. Functions play a
key role in programming: they let us configure computations with
different concrete values at different times. The first time we
compute the cost of pens, we might be asking about `10`{.pyret} pens that say
`"Welcome"`{.pyret}. The next time, we might be asking about `100`{.pyret} pens that say
`"Go Bears!"`{.pyret}. The core computation is the same in both cases, so we
want to write it out once, configuring it with different concrete
values each time we use it.

We’ve covered several specific ideas about functions:

- We showed the function declaration syntax for writing functions. You learned
  that a function has a name (that we can use to refer to it),
  one or more parameters (names for the values we want to configure), as
  well as a body, which is the computation that we want to
  perform once we have concrete values for the parameters.

- We showed that we should include examples with our functions,
  to illustrate what the function computes on various specific
  values. Examples go in a `where { }`{.jayret} block after the function body.

- We showed that we can use a function by providing concrete
  values to configure its parameters. To do this, we write the name of
  the function we want to use, followed by a pair of parenthesis around
  comma-separated values for the parameters. For example, writing the following
  expression (at the interactions prompt) will compute the cost of a
  specific order of pens:
  
  ```jayret
pen-cost(10, "Welcome");
  ```
- We discussed that if we define a function in the definitions
  pane then press Run, Jayret will make an entry in the directory with
  the name of the function. If we later use the function, Jayret will
  look up the code that goes with that name, substitute the concrete
  values we provided for the parameters, and return the result of
  evaluating the resulting expression. Jayret will NOT produce anything
  in the interactions pane for a function definition (other than a
  report about whether the examples hold).

There’s much more to learn about functions, including different
reasons for creating them. We’ll get to those in due course.
