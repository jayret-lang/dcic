---
title: Naming Values
section_number: 3.2
source_file: Naming_Values.html
prev: getting-started.html
up: part_foundations.html
next: From_Repeated_Expressions_to_Functions.html
---

```{=html}
<a name="(part._Naming-Values)"></a>
```

### 3.2 Naming Values {#Naming-Values}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Naming_Values.html#%28part._naming-defns-pane%29">3.2.1<span class="hspace"> </span>The Definitions Pane</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Naming_Values.html#%28part._naming-name-vals%29">3.2.2<span class="hspace"> </span>Naming Values</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="Naming_Values.html#%28part._naming-strings%29">3.2.2.1<span class="hspace"> </span>Names Versus Strings</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="Naming_Values.html#%28part._naming-expr-statements%29">3.2.2.2<span class="hspace"> </span>Expressions versus
Statements</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Naming_Values.html#%28part._program-directory%29">3.2.3<span class="hspace"> </span>The Program Directory</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="Naming_Values.html#%28part._Understanding-the-Run-Button%29">3.2.3.1<span class="hspace"> </span>Understanding the Run Button</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Naming_Values.html#%28part._naming-for-images%29">3.2.4<span class="hspace"> </span>Using Names to Streamline Building Images</a></p></td></tr></table>
```

```{=html}
<a name="(part._naming-defns-pane)"></a>
```

#### 3.2.1 The Definitions Pane {#naming-defns-pane}

So far, we have only used the interactions pane on the right half of
the CPO screen. As we have seen, this pane acts like a calculator:
you type an expression at the prompt and CPO produces the result of
evaluating that expression.

The left pane is called the definitions pane. This is where
you can put code that you want
to save to a file. It has another use, too:
it can help you organize your code as your expressions get larger.

```{=html}
<a name="(part._naming-name-vals)"></a>
```

#### 3.2.2 Naming Values {#naming-name-vals}

The expressions that create images involve a bit of typing. It would
be nice to have shorthands so we can “name” images and refer to them
by their names. This is what the definitions pane is for: you can
put expressions and programs in the definitions pane, then use the
“Run” button in CPO to make the definitions available in the
interactions pane.

::: {.do-now}
Put the following in the definitions pane:

```jayret
red-circ = circle(30, "solid", "red");
```

Hit run, then enter `red-circ`{.jayret} in the interactions pane. You
should see the red circle.
:::

More generally, if you write code in the form:

```jayret
NAME = EXPRESSION;
```

Jayret will associate the value of `EXPRESSION`{.jayret} with `NAME`{.jayret}. Anytime you
write the (shorthand) `NAME`{.jayret}, Jayret will automatically (behind the
scenes) replace it with the value of `EXPRESSION`{.jayret}. For example,
if you write `x = 5 + 4`{.jayret} at the prompt, then write `x`{.jayret}, CPO will give
you the value `9`{.jayret} (not the original `5 + 4`{.jayret} expression).

What if you enter a name at the prompt that you haven’t associated
with a value?

::: {.do-now}
Try typing `puppy`{.jayret} at the interactions pane prompt (›››). Are there any terms in the
error message that are unfamiliar to you?
:::

CPO (and indeed many programming tools) use the phrase “unbound identifier”
when an expression contains a name that has not been associated with
(or bound to) a value.

```{=html}
<a name="(part._naming-strings)"></a>
```

##### 3.2.2.1 Names Versus Strings {#naming-strings}

At this point, we have seen words being used in two ways in
programming: (1) as data within strings and (2) as names for
values (also called identifiers). These are two very different
uses, so it is worth reviewing them.

- Syntactically (another way of saying “in terms of how we write it”), we
  distinguish strings and names by the presence of double quotation
  marks. Note the difference between `puppy`{.jayret} and `"puppy"`{.jayret}.

- Strings can contain spaces, but names cannot. For example,
  `"hot pink"`{.jayret} is a valid piece of data, but `hot;
pink`{.jayret} is not
  a single name. When you want to combine multiple words into a name
  (like we did above with `red-circ`{.jayret}), use a hyphen to separate
  the words while still having a single name (as a sequence of
  characters). Different programming languages allow different
  separators; for Jayret, we’ll use hyphens.
- Entering a word as a name versus as a string at the interactions
  prompt changes the computation that you are asking Jayret to
  perform. If you enter `puppy`{.jayret} (the name, without double quotes),
  you are asking Jayret to lookup the value that you previously stored
  under that name. If you enter `"puppy"`{.jayret} (the string, with double
  quotes) you are simply writing down a piece of data (akin to typing a
  number like `3`{.jayret}): Jayret returns the value you
  entered as the result of the computation.

- If you enter a name that you have not previously associated with
  a value, Jayret will give you an “unbound identifier” error
  message. In contrast, since strings are just data, you won’t get an
  error for writing a previously-unused string (there are some special
  cases of strings, such as when you want to put a quotation mark inside
  them, but we’ll set that aside for now).

Novice programmers frequently confuse names and strings at first. For
now, remember that the names you associate with values using `=`{.jayret}
cannot contain quotation marks, while word- or text-based data must
be wrapped in double quotes.

```{=html}
<a name="(part._naming-expr-statements)"></a>
```

##### 3.2.2.2 Expressions versus Statements {#naming-expr-statements}

Definitions and expressions are two useful aspects of programs, each
with their own role. Definitions tell Jayret to associate names with
values. Expressions tell Jayret to perform a computation and return
the result.

::: {.exercise}
Enter each of the following at the interactions prompt:

- `5 + 8`{.jayret}

- `x = 14 + 16`{.jayret}

- `triangle(20, "solid", "purple")`{.jayret}

- `blue-circ = circle(x, "solid", "blue")`{.jayret}

The first and third are expressions, while the second and fourth are
definitions. What do you observe about the results of entering
expressions versus the results of entering definitions?
:::

Hopefully, you notice that Jayret doesn’t seem to return anything from
the definitions, but it does display a value from the
expressions. In programming, we distinguish expressions, which yield values,
from statements, which don’t yield values but instead give some
other kind of instruction to the language. So far,
definitions are the only kinds of statements we’ve seen.

::: {.exercise}
Assuming you still have the `blue-circ`{.jayret} definition from above in
your interactions pane, enter `blue-circ`{.jayret} at the prompt (you
can re-enter that definition if it is no longer there).

Based on what Jayret does in response, is `blue-circ`{.jayret} an
expression or a definition?
:::

Since `blue-circ`{.jayret} yielded a result, we infer that a name by
itself is also an expression. This exercise highlights the difference
between making a definition and using a defined name. One produces a
value while the other does not. But surely something must
happen, somewhere, when you run a definition. Otherwise, how
could you use that name later?

```{=html}
<a name="(part._program-directory)"></a>
```

#### 3.2.3 The Program Directory {#program-directory}

Programming tools do work behind the scenes as they run
programs. Given the program `2 + 3`{.jayret}, for example, a calculation
takes place to produce `5`{.jayret}, which in turn displays in the
interactions pane.

When you write a definition, Jayret makes an entry in an internal
directory in which it associates names with values. You can’t
see the directory, but Jayret uses it to manage the values that you’ve
associated with names. If you write:

```jayret
width = 30;
```
Jayret makes a new directory entry for `width`{.jayret} and records that
`width`{.jayret} has value `30`{.jayret}. If you then write

```jayret
height = width * 3;
```
Jayret evaluates the expression on the right side
(`width * 3`{.jayret}), then stores the resulting value (here, `90`{.jayret})
alongside `height`{.jayret} in the directory.

How does Jayret evaluate (`width * 3`{.jayret})? Since `width`{.jayret} is a
word (not a string), Jayret looks up its value in the directory. Jayret
substitutes that value for the name in the expression, resulting in
`30 * 3`{.jayret}, which then evaluates to `90`{.jayret}. After running
these two expressions, the directory looks like:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">width</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">30</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">height</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">90</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```
Note that the entry for `height`{.jayret} in the directory has the
result of `width * 3`{.jayret}, not the expression. This will
become important as we use named values to prevent us from doing the
same computation more than once.

The program directory is an essential part of how programs
evaluate. If you are trying to track how your program is working, it
sometimes helps to track the directory contents on a sheet of paper
(since you can’t view Jayret’s directory).

::: {.exercise}
Imagine that you have the following code in the definitions pane
when you press the Run button:

```jayret
name = "Matthias";
"name";
```
What appears in the interactions pane? How does each of these lines
interact with the program directory?
:::

::: {.do-now}
What happens if you enter a subsequent definition for the same name,
such as `width = 50`{.jayret}? How does Jayret respond? What if you then ask to see the value associated with this same name at the prompt? What does this tell
you about the directory?
:::


When you try to give a new value to a name that is already in the
directory, Jayret will respond that the new definition “conflicts with an earlier declaration of the same name”. This is Jayret’s way of
warning you that the name is already in the directory. If you ask for
the value associated with the name again, you’ll see that it still has
the original value. Jayret doesn’t let you change the value associated
with an existing name with the `name = value`{.jayret} notation. While
there is a notation that will let you reassign values, we won’t work
with this concept until [Mutating Variables](mutating-variables.html).

```{=html}
<a name="(part._Understanding-the-Run-Button)"></a>
```

##### 3.2.3.1 Understanding the Run Button {#Understanding-the-Run-Button}

Now that we’ve learned about the program directory, let’s discuss what happens when you
press the Run button. Let’s assume the following contents are in the
definitions pane:

```jayret
width = 30;
height = width * 3;
blue-rect = rectangle(width, height, "solid", "blue");
```
When you press Run, Jayret first clears out the program directory. It
then processes your file line by line, starting at the top. If you
have an `include`{.jayret} statement, Jayret adds the definitions from the
included library to the directory. After processing all of the lines
for this program, the directory will look like:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">circle</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span>&lt;the circle operation&gt;</div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">rectangle</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span>&lt;the rectangle operation&gt;</div></p></li><li><p>...</p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">width</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">30</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">height</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">90</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">blue-rect</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span>&lt;the actual rectangle image&gt;</div></p></li></ul></div><p></p><div class="clear"></div></div>
```

If you now type at the interactions prompt, any use of an identifier
(a sequence of characters not enclosed in quotation marks) results in Jayret
consulting the directory.

If you now type

```jayret
beside(blue-rect, rectangle(20, 20, "solid", "purple"));
```
Jayret will look up the image associated with `blue-rect`{.jayret}.

::: {.do-now}
Is the purple rectangle in the directory? What about the image with
the two rectangles?
:::

Neither of these shapes is in the directory. Why? We didn’t ask Jayret
to store them there with a name. What would be different if we instead
wrote the following (at the interactions prompt)?

```jayret
two-rects = beside(blue-rect, rectangle(20, 20, "solid", "purple"));
```
Now, the two-shape image would be in the directory, associated with
the name `two-rects`{.jayret}. The purple rectangle by itself, however,
still would not be stored in the directory. We could, however,
reference the two-shape image by name, as shown below:

![](run-demo.png){width="982" height="239"}

::: {.do-now}
Imagine that we now hit the Run button again, then typed
`two-rects`{.jayret} at the interactions prompt. How would Jayret respond
and why?
:::

```{=html}
<a name="(part._naming-for-images)"></a>
```

#### 3.2.4 Using Names to Streamline Building Images {#naming-for-images}

The ability to name values can make it easier to build up complex
expressions. Let’s put a rotated purple triangle inside a green square:

```jayret
overlay(rotate(45, triangle(30, "solid", "purple")), rectangle(60, 60, "solid", "green"));
```

However, this can get quite difficult to read and understand. Instead,
we can name the individual shapes before building the overall
image:

```jayret
purple-tri = triangle(30, "solid", "purple");
green-sqr = rectangle(60, 60, "solid", "green");
overlay(rotate(45, purple-tri), green-sqr);
```

In this version, the `overlay`{.jayret} expression is quicker to read
because we gave descriptive names to the initial shapes.

Go one step further: let’s add another purple-triangle on top of the
existing image:

```jayret
purple-tri = triangle(30, "solid", "purple");
green-sqr = rectangle(60, 60, "solid", "green");
above(purple-tri, overlay(rotate(45, purple-tri), green-sqr));
```

Here, we see a new benefit to leveraging names: we can use
`purple-tri`{.jayret} twice in the same expression without having to write
out the longer `triangle`{.jayret} expression more than once.

::: {.exercise}
Assume that your definitions pane contained only this most recent
code example (including the `purple-tri`{.jayret} and `green-sqr`{.jayret} definitions). How many separate images
would appear in the interactions pane if you pressed Run? Do you see
the purple triangle and green square on their own, or only combined?
Why or why not?
:::

::: {.exercise}
Re-write your expression of the Armenian flag (from
[Making a Flag](getting-started.html##expressions-first-flag)), this
time giving intermediate names to each of the stripes.
:::

In practice, programmers don’t name every individual image or
expression result when creating more complex expressions. They name
ones that will get used more than once, or ones that have particular
significance for understanding their program. We’ll have more to
say about naming as our programs get more complicated.
