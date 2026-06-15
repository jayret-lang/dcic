---
title: Pyret for Racketeers and Schemers
section_number: 28
source_file: p4rs.html
prev: booklet_appendices.html
up: booklet_appendices.html
next: pyret-vs-python.html
---

## Pyret for Racketeers and Schemers {#p4rs}

If you’ve programmed before in a language like Scheme or the student
levels of Racket (or the WeScheme programming environment), or for
that matter even in certain parts of OCaml, Haskell, Scala, Erlang,
Clojure, or other languages, you will find many parts of Pyret very
familiar. This chapter is specifically written to help you make the
transition from (student) Racket/Scheme/WeScheme (abbreviated “RSW”)
to Pyret by showing you how to convert the syntax. Most of what we say
applies to all these languages, though in some cases we will refer
specifically to Racket (and WeScheme) features not found in Scheme.

In every example below, the two programs will produce the same results.

### Numbers, Strings, and Booleans {#Numbers-Strings-and-Booleans}

Numbers are very similar between the two. Like Scheme, Pyret
implements arbitrary-precision numbers and rationals. Some of the more
exotic numeric systems of Scheme (such as complex numbers) aren’t in
Pyret; Pyret also treats imprecise numbers slightly differently.

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktVal">1</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">1</code></span></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktVal">1/2</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">1/2</code></span></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktVal">#i3.14</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">~3.14</code></span></p></td></tr></table>
```

Strings are also very similar, though Pyret allows you to use
single-quotes as well.

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktVal">"Hello,</span><span class="hspace"> </span><span class="RktVal">world!"</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">"Hello, world!"</code></span></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktVal">"\"Hello\",</span><span class="hspace"> </span><span class="RktVal">he</span><span class="hspace"> </span><span class="RktVal">said"</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">"\"Hello\", he said"</code></span></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktVal">"\"Hello\",</span><span class="hspace"> </span><span class="RktVal">he</span><span class="hspace"> </span><span class="RktVal">said"</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">'"Hello", he said'</code></span></p></td></tr></table>
```

Booleans have the same names:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktSym">true</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">true</code></span></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktSym">false</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">false</code></span></p></td></tr></table>
```

### Infix Expressions {#Infix-Expressions}

Pyret uses an infix syntax, reminiscent of many other textual
programming languages:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">+</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">2</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">1 + 2</code></span></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">*</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym"><span class="nobreak">-</span></span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">4</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">2</span><span class="RktPn">)</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">5</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">(4 - 2) * 5</code></span></p></td></tr></table>
```

Note that Pyret does not have rules about orders of precedence between
operators, so when you mix operators, you have to parenthesize the
expression to make your intent clear. When you chain the same
operator you don’t need to parenthesize; chaining associates to the
left in both languages:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">/</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">2</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">3</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">4</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">1 / 2 / 3 / 4</code></span></p></td></tr></table>
```
These both evaluate to 1/24.

### Function Definition and Application {#Function-Definition-and-Application}

Function definition and application in Pyret have an infix syntax,
more reminiscent of many other textual programming
languages. Application uses a syntax familiar from conventional
algebra books:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">dist</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">3</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">4</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">dist(3, 4)</code></span></p></td></tr></table>
```

Application correspondingly uses a similar syntax in function headers,
and infix in the body:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">define</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">dist</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">y</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">sqrt</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">+</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">*</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">x</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">           </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">*</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">y</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">y</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Pyret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="pyret"><code class="sourceCode" data-lang="pyret">fun dist(x, y):
  num-sqrt((x * x) +
           (y * y))
end</code></pre></div></div></p></td></tr></table>
```

### Tests {#Tests}

There are essentially three different ways of writing the equivalent
of Racket’s check-expect tests. They can be translated into
check blocks:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">check-expect</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Pyret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="pyret"><code class="sourceCode" data-lang="pyret">check:
  1 is 1
end</code></pre></div></div></p></td></tr></table>
```
Note that multiple tests can be put into a single block:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">check-expect</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">check-expect</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">2</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">2</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Pyret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="pyret"><code class="sourceCode" data-lang="pyret">check:
  1 is 1
  2 is 2
end</code></pre></div></div></p></td></tr></table>
```

The second way is this: as an alias for `check`{.pyret} we can also write
`examples`{.pyret}. The two are functionally identical, but they capture
the human difference between examples (which explore the
problem, and are written before attempting a solution) and
tests (which try to find bugs in the solution, and are written
to probe its design).

The third way is to write a `where`{.pyret} block to accompany a function
definition. For instance:

```pyret
fun double(n):
  n + n
where:
  double(0) is 0
  double(10) is 20
  double(-1) is -2
end
```
These can even be written for internal functions (i.e., functions
contained inside other functions), which isn’t true for
check-expect.

In Pyret, unlike in Racket, a testing block can contain a
documentation string. This is used by Pyret when reporting test
successes and failures. For instance, try to run and see what you get:

```pyret
check "squaring always produces non-negatives":
  (0 * 0) is 0
  (-2 * -2) is 4
  (3 * 3) is 9
end
```
This is useful for documenting the purpose of a testing block.

Just as in Racket, there are many testing operators in Pyret (in
addition to `is`{.pyret}). See
[the
documentation](https://www.pyret.org/docs/latest/testing.html).

### Variable Names {#Variable-Names}

Both languages have a fairly permissive system for naming
variables. While you can use CamelCase and under_scores in both, it is
conventional to instead use what is known as
[kebab-case](http://c2.com/cgi/wiki?KebabCase).[This name is inaccurate. The word “kebab”
just means “meat”. The skewer is the “shish”. Therefore, it ought
to at least be called “shish kebab case”.]{.margin-note} Thus:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktSym">this-is-a-name</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">this-is-a-name</code></span></p></td></tr></table>
```
Even though Pyret has infix subtraction, the language can
unambiguously tell apart `this-name`{.pyret} (a variable) from
`this - name`{.pyret} (a subtraction expression) because the `-`{.pyret} in
the latter must be surrounded by spaces.

Despite this spacing convention, Pyret does not permit some of the
more exotic names permitted by Scheme. For instance, one can write

```{=html}
<blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">define</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">e^i*pi</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">-1</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote>
```
in Scheme but that is not a valid variable name in Pyret.

### Data Definitions {#Data-Definitions}

Pyret diverges from Racket (and even more so from Scheme) in its
handling of data definitions. First, we will see how to define a
structure:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">define-struct</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">pt</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">y</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Pyret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="pyret"><code class="sourceCode" data-lang="pyret">data Point:
  | pt(x, y)
end</code></pre></div></div></p></td></tr></table>
```

This might seem like a fair bit of overkill, but we’ll see in a moment
why it’s useful. Meanwhile, it’s worth observing that when you have
only a single kind of datum in a data definition, it feels unwieldy to
take up so many lines. Writing it on one line is valid, but now it
feels ugly to have the `|`{.pyret} in the middle:

```pyret
data Point: | pt(x, y) end
```
Therefore, Pyret permits you to drop the initial `|`{.pyret}, resulting
in the more readable

```pyret
data Point: pt(x, y) end
```

Now suppose we have two kinds of points. In the student languages of
Racket, we would describe this with a comment:

```{=html}
<blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktCmt">;;</span><span class="hspace"> </span><span class="RktCmt">A</span><span class="hspace"> </span><span class="RktCmt">Point</span><span class="hspace"> </span><span class="RktCmt">is</span><span class="hspace"> </span><span class="RktCmt">either</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="RktCmt">;;</span><span class="hspace"> </span><span class="RktCmt">-</span><span class="hspace"> </span><span class="RktCmt">(pt</span><span class="hspace"> </span><span class="RktCmt">number</span><span class="hspace"> </span><span class="RktCmt">number),</span><span class="hspace"> </span><span class="RktCmt">or</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="RktCmt">;;</span><span class="hspace"> </span><span class="RktCmt">-</span><span class="hspace"> </span><span class="RktCmt">(pt3d</span><span class="hspace"> </span><span class="RktCmt">number</span><span class="hspace"> </span><span class="RktCmt">number</span><span class="hspace"> </span><span class="RktCmt">number)</span><span class="RktMeta"></span></td></tr></table></blockquote>
```
In Pyret, we can express this directly:

```pyret
data Point:
  | pt(x, y)
  | pt3d(x, y, z)
end
```
In short, Racket optimizes for the single-variant case, whereas Pyret
optimizes for the multi-variant case. As a result, it is difficult to
clearly express the multi-variant case in Racket, while it is unwieldy
to express the single-variant case in Pyret.

For structures, both Racket and Pyret expose constructors, selectors,
and predicates. Constructors are just functions:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">pt</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">2</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">pt(1, 2)</code></span></p></td></tr></table>
```
Predicates are also functions with a particular naming scheme:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">pt?</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">x</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="RktSym">is-pt</span><span class="RktPn">(</span><span class="RktSym">x</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td></tr></table>
```
and they behave the same way (returning true if the argument
was constructed by that constructor, and false otherwise). In
contrast, selection is different in the two languages (and we will see
more about selection below, with `cases`{.pyret}):

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">pt-x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">v</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">v.x</code></span></p></td></tr></table>
```
Note that in the Racket case, pt-x checks that the parameter
was constructed by pt before extracting the value of the
x field. Thus, pt-x and pt3d-x are two different
functions and neither one can be used in place of the other. In
contast, in Pyret, `.x`{.pyret} extracts an `x`{.pyret} field of any value
that has such a field, without attention to how it was
constructed. Thus, we can use `.x`{.pyret} on a value whether it was
constructed by `pt`{.pyret} or `pt3d`{.pyret} (or indeed anything else with
that field). In contrast, `cases`{.pyret} does pay attention to this
distinction.

### Conditionals {#Conditionals}

There are several kinds of conditionals in Pyret, one more than in the
Racket student languages.

General conditionals can be written using `if`{.pyret}, corresponding to
Racket’s `if`{.pyret} but with more syntax.

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">if</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">full-moon</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">    </span><span class="RktMeta"></span><span class="RktVal">"howl"</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">    </span><span class="RktMeta"></span><span class="RktVal">"meow"</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Pyret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="pyret"><code class="sourceCode" data-lang="pyret">if full-moon:
  "howl"
else:
  "meow"
end</code></pre></div></div></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">if</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">full-moon</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">    </span><span class="RktMeta"></span><span class="RktVal">"howl"</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">    </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">if</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">new-moon</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">        </span><span class="RktMeta"></span><span class="RktVal">"bark"</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">        </span><span class="RktMeta"></span><span class="RktVal">"meow"</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Pyret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="pyret"><code class="sourceCode" data-lang="pyret">if full-moon:
  "howl"
else if new-moon:
  "bark"
else:
  "meow"
end</code></pre></div></div></p></td></tr></table>
```

Note that `if`{.pyret} includes `else if`{.pyret}, which makes it possible
to list a collection of questions at the same level of indentation,
which if in Racket does not have. The corresponding code in
Racket would be written

```{=html}
<blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">cond</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">[</span><span class="RktSym">full-moon</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">"howl"</span><span class="RktPn">]</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">[</span><span class="RktSym">new-moon</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">"bark"</span><span class="RktPn">]</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">[</span><span class="RktSym">else</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">"meow"</span><span class="RktPn">]</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote>
```
to restore the indentation. There is a similar construct in Pyret
called `ask`{.pyret}, designed to parallel `cond`{.pyret}:

```pyret
ask:
  | full-moon then: "howl"
  | new-moon then:  "bark"
  | otherwise:      "meow"
end
```

In Racket, we also use `cond`{.pyret} to dispatch on a datatype:

```{=html}
<blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">cond</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">[</span><span class="RktPn">(</span><span class="RktSym">pt?</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">v</span><span class="RktPn">)</span><span class="RktMeta"></span><span class="hspace">   </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">+</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">pt-x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">v</span><span class="RktPn">)</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">pt-y</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">v</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktPn">]</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">[</span><span class="RktPn">(</span><span class="RktSym">pt3d?</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">v</span><span class="RktPn">)</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">+</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">pt-x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">v</span><span class="RktPn">)</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">pt-z</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">v</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktPn">]</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote>
```
We could write this in close parallel in Pyret:

```pyret
ask:
  | is-pt(v)   then: v.x + v.y
  | is-pt3d(v) then: v.x + v.z
end
```
or even as:

```pyret
if is-pt(v):
  v.x + v.y
else if is-pt3d(v):
  v.x + v.z
end
```
(As in Racket student languages, the Pyret versions will signal an
error if no branch of the conditional matched.)

However, Pyret provides a special syntax just for data
definitions:

```pyret
cases (Point) v:
  | pt(x, y)      => x + y
  | pt3d(x, y, z) => x + z
end
```
This checks that `v`{.pyret} is a `Point`{.pyret}, provides a clean
syntactic way of identifying the different branches, and makes
it possible to give a concise local name to each field position
instead of having to use selectors like `.x`{.pyret}. In general, in
Pyret we prefer to use `cases`{.pyret} to process data
definitions. However, there are times when, for instance, there many
variants of data but a function processes only very few of them. In
such situations, it makes more sense to explicitly use predicates and
selectors.

### Lists {#Lists}

In Racket, depending on the language level, lists are created using
either cons or list, with empty for the empty
list. The corresponding notions in Pyret are called `link`{.pyret},
`list`{.pyret}, and `empty`{.pyret}, respectively. `link`{.pyret} is a
two-argument function, just as in Racket:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">cons</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">empty</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">link(1, empty)</code></span></p></td></tr></table>
```

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">list</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">1</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">2</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">3</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">[list: 1, 2, 3]</code></span></p></td></tr></table>
```

Note that the syntax `[1, 2, 3]`{.pyret}, which represents lists in many
languages, is not legal in Pyret: lists are not privileged with
their own syntax. Rather, we must use an explicit constructor:
just as `[list: 1, 2, 3]`{.pyret} constructs a list, `[set: 1, 2,
3]`{.pyret} constructs a set instead of a list.[In fact, we can
[create our own constructors](https://www.pyret.org/docs/latest/Expressions.html##s-construct-expr)
and use them with this syntax.]{.margin-note}

::: {.exercise}
Try typing `[1, 2, 3]`{.pyret} and see the error message.
:::

This shows us how to construct lists. To take them apart, we use
`cases`{.pyret}. There are two variants, `empty`{.pyret} and `link`{.pyret}
(which we used to construct the lists):

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktPn">(</span><span class="RktSym">cond</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">[</span><span class="RktPn">(</span><span class="RktSym">empty?</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">l</span><span class="RktPn">)</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktVal">0</span><span class="RktPn">]</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">  </span><span class="RktMeta"></span><span class="RktPn">[</span><span class="RktPn">(</span><span class="RktSym">cons?</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">l</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">   </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">+</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">first</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">l</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="hspace">      </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">g</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">rest</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">l</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktPn">]</span><span class="RktPn">)</span><span class="RktMeta"></span></td></tr></table></blockquote></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Pyret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="pyret"><code class="sourceCode" data-lang="pyret">cases (List) l:
  | empty      =&gt; 0
  | link(f, r) =&gt; f + g(r)
end</code></pre></div></div></p></td></tr></table>
```
It is conventional to call the fields `f`{.pyret} and `r`{.pyret} (for
“first” and “rest”). Of course, this convention does not work if
there are other things by the same name; in particular, when writing a
nested destructuring of a list, we conventionally write `fr`{.pyret} and
`rr`{.pyret} (for “first of the rest” and “rest of the rest”).

### First-Class Functions {#First-Class-Functions}

The equivalent of Racket’s lambda is Pyret’s `lam`{.pyret}:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">RSW</span></p></td><td><p><span style="font-weight: bold">Pyret</span></p></td></tr><tr><td><p><span class="RktPn">(</span><span class="RktSym">lambda</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">y</span><span class="RktPn">)</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktPn">(</span><span class="RktSym">+</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">x</span><span class="RktMeta"></span><span class="hspace"> </span><span class="RktMeta"></span><span class="RktSym">y</span><span class="RktPn">)</span><span class="RktPn">)</span><span class="RktMeta"></span></p></td><td><p><span class="sourceCode" title="Pyret"><code class="sourceCode" data-lang="pyret">lam(x, y): x + y end</code></span></p></td></tr></table>
```

### Annotations {#Annotations}

In student Racket languages, annotations are usually written as comments:

```{=html}
<blockquote class="SCodeFlow"><table cellpadding="0" cellspacing="0" class="RktBlk"><tr><td><span class="RktCmt">;</span><span class="hspace"> </span><span class="RktCmt">square:</span><span class="hspace"> </span><span class="RktCmt">Number</span><span class="hspace"> </span><span class="RktCmt">-&gt;</span><span class="hspace"> </span><span class="RktCmt">Number</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="RktCmt">;</span><span class="hspace"> </span><span class="RktCmt">sort-nums:</span><span class="hspace"> </span><span class="RktCmt">List&lt;Number&gt;</span><span class="hspace"> </span><span class="RktCmt">-&gt;</span><span class="hspace"> </span><span class="RktCmt">List&lt;Number&gt;</span><span class="RktMeta"></span></td></tr><tr><td><span class="RktMeta"></span><span class="RktCmt">;</span><span class="hspace"> </span><span class="RktCmt">sort:</span><span class="hspace"> </span><span class="RktCmt">List&lt;T&gt;</span><span class="hspace"> </span><span class="RktCmt">*</span><span class="hspace"> </span><span class="RktCmt">(T</span><span class="hspace"> </span><span class="RktCmt">*</span><span class="hspace"> </span><span class="RktCmt">T</span><span class="hspace"> </span><span class="RktCmt">-&gt;</span><span class="hspace"> </span><span class="RktCmt">Boolean)</span><span class="hspace"> </span><span class="RktCmt">-&gt;</span><span class="hspace"> </span><span class="RktCmt">List&lt;T&gt;</span><span class="RktMeta"></span></td></tr></table></blockquote>
```
In Pyret, we write the annotations directly on the parameters and
return values. Pyret will check them to a limited extent dynamically,
and can check them statically with its type checker. The corresponding
annotations to those above would be written as

```pyret
fun square(n :: Number) -> Number: ...

fun sort-nums(l :: List<Number>) -> List<Number>: ...

fun sort<T>(l :: List<T>, cmp :: (T, T -> Boolean)) -> List<T>: ...
```

### What Else? {#What-Else}

If there are other parts of Scheme or Racket syntax that you would
like to see translated, please
[let us know](http://cs.brown.edu/~sk/Contact/).
