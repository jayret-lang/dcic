---
title: Understanding Equality
section_number: 12.2
source_file: unified-equality.html
prev: mutating-structures.html
up: part_state.html
next: unified-lists-memory.html
---

```{=html}
<a name="(part._unified-equality)"></a>
```

### 12.2 Understanding Equality {#unified-equality}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="unified-equality.html#%28part._equality-of-data%29">12.2.1<span class="hspace"> </span>Equality of Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="unified-equality.html#%28part._equality-operations%29">12.2.2<span class="hspace"> </span>Different Equality Operations</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="unified-equality.html#%28part._Equality-in-Python%29">12.2.2.1<span class="hspace"> </span>Equality in Python</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="unified-equality.html#%28part._Equality-in-Jayret%29">12.2.2.2<span class="hspace"> </span>Equality in Jayret</a></p></td></tr></table>
```

```{=html}
<a name="(part._equality-of-data)"></a>
```

#### 12.2.1 Equality of Data {#equality-of-data}

Now that we have the ability to mutate data, it’s worth asking what it
means for two pieces of data to be equal. We’ll motivate this through
a concrete example. Following the naming convention of
[Structure Mutation and the Directory](mutating-structures.html##structure-mut-dir), we will write every name only once, using the
upper-case name from Python, but everything we write will equally be
true for Jayret.

First, consider these three statements:

```python
a1 = Account(8603, 500)
a2 = Account(8603, 500)
a3 = Account(8603, 250)
```

::: {.do-now}
Which of the above `Account`{.python}s do you consider “equal”?
:::

The third `Account`{.python} has a different balance than the first two,
so it can’t be considered equal to either of the first two. The first
two have the same contents, so arguably they can be considered equal.

Now, let’s consider the directory and heap that would result from
running these three statements:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1120</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1121</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a3</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1122</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1120</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1121</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1122</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 250)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

From the perspective of the heap, each account ends up at its own
address. Those different addresses are a way in which the two values
are not the same: they have the same contents, but not the same
address. Is that relevant? To explore this, let’s associate another
name (`a4`{.python}) with the same address as `a2`{.python}, then change
the balance in `a2`{.python}.
For now we will show just the Python version:

```python
a1 = Account(8603, 500)
a2 = Account(8603, 500)
a3 = Account(8603, 250)
a4 = a2
# checkpoint 1
a2.balance = 800
# checkpoint 2
```

What does memory look like before and after checkpoint 1? Before the
checkpoint:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1130</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1131</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a3</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1132</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a4</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1131</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1130</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1131</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1132</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 250)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```
`a1`{.python} and `a2`{.python} refer to two different
`Account`{.python}s with the same contents. After checkpoint 1, those
contents are different because we modified the contents of the balance
field in `a2`{.python}:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1130</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1131</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a3</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1132</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a4</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1131</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1130</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1131</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 800)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1132</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8603, 250)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```
In contrast, `a2`{.python} and `a4`{.python} are aliases for the
same `Account`{.python}. Therefore, their values change in lockstep:
asking to display the value of either one would now show an account
with a balance of `800`{.python}.

::: {.do-now}
What do you think now? Are the first two accounts equal?
:::

```{=html}
<a name="(part._equality-operations)"></a>
```

#### 12.2.2 Different Equality Operations {#equality-operations}

This sequence of examples points out that we seem to be raising two
possible notions of equality:

1. Whether two values have the same contents. This is formally called
  structural equality; you can think of it as a “print
  equality”, namely, when displayed, do the two values look the same.

2. Whether two values live at the same address, i.e., there is
  actually only one value in memory. This is formally called
  reference equality. Usually, we would refer to the two values by
  different names (so there is the possibility that they are
  different), and reference equality checks whether the names are
  aliases. Observe that a given value always prints the same way, so
  any two names that have reference equality also have structural
  equality, but not vice versa.

Which notion of equality is “correct”? It turns out that they are
valuable in different contexts. For this reason, programming languages
generally provide multiple equality operations, letting the programmer
indicate which kind of equality they mean in their context.

Unfortunately, the names of equality operations, and their exact
meaning, vary across languages. Therefore, we will examine each of
Jayret and Python separately.

```{=html}
<a name="(part._Equality-in-Python)"></a>
```

##### 12.2.2.1 Equality in Python {#Equality-in-Python}

The `==`{.python} operator that you learned in Jayret and we carried into
Python checks for structural equality, independent of addresses:

::: {.pyret-repl}
```python
a1 == a2
```
``` output
True
```
:::

::: {.pyret-repl}
```python
a2 == a4
```
``` output
True
```
:::

However, note that this will no longer be true at checkpoint
2:

::: {.pyret-repl}
```python
a1 == a2
```
``` output
False
```
:::

::: {.pyret-repl}
```python
a2 == a4
```
``` output
True
```
:::

If we instead want to check for aliasing, we instead use an operation
called `is`{.python} (not to be confused with Jayret’s `is`{.jayret}, which
is used for writing tests):

::: {.pyret-repl}
```python
a1 is a2
```
``` output
False
```
:::

::: {.pyret-repl}
```python
a2 is a4
```
``` output
True
```
:::

This explains why `a2 == a4`{.python} was true both before and
after the mutation, but `a1 == a2`{.python} was no longer true
after it. The latter seems to violate a very basic meaning of
“equality”; the problem here is caused by the introduction of
mutation.

As we go forward, you’ll get more practice with when to use each kind
of equality. The `==`{.python} operator is more accepting, so it is
usually the right default. If you actually need to know whether two
expressions evaluate to the same address, you should instead use `is`{.python}.

```{=html}
<a name="(part._Equality-in-Pyret)"></a>
```

##### 12.2.2.2 Equality in Jayret {#Equality-in-Pyret}

Equality in Jayret is somewhat more detailed, because the language
wants you to think harder about what is happening in your programs.

Recall that we are using the datatype in [Example: Bank Accounts](mutating-structures.html##eg-bank-acc) and
have written the following definitions:

```jayret
a1 = account(8603, 500);
a2 = account(8603, 500);
a3 = account(8603, 250);
a4 = a2;
// checkpoint 1
a2 ! {balance 800 }
// checkpoint 2
```

In Python, we saw that `a1 == a2`{.python} before the
mutation. However, in Jayret, this produces `false`{.jayret}! Why?

The reason is because structural equality is actually complicated;
there are two different questions we could be asking:


1. Are these two values structurally equal right now?

2. Will these two values be structurally equal always?

Jayret makes a distinction between these two.

By default, Jayret tends towards safer programming
practices. Therefore, the standard (structural) equality predicate,
`==`{.jayret}, will only return `true`{.jayret} if the two values will
always be equal. Thus:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a2` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a4`  -->
```jayret
a2 == a4;
```
``` output
true
```
:::

Because the two values are actually aliases, no matter how one
changes, the “other” will always change in the same way. Therefore,
they will always “print the same”. We can confirm that they are
aliases by using Jayret’s reference equality operator, `<=>`{.jayret}:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: Evaluating an expression failed. It was expected to evaluate to a Pyret Value. It evaluated to the non-Pyret Value value: non-Pyret value; see the console for m -->
```jayret
a1 <=> a2;
```
``` output
false
```
:::

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: Evaluating an expression failed. It was expected to evaluate to a Pyret Value. It evaluated to the non-Pyret Value value: non-Pyret value; see the console for m -->
```jayret
a2 <=> a4;
```
``` output
true
```
:::

In contrast, that guarantee does not apply to `a1`{.jayret} and
`a2`{.jayret}; and indeed, at checkpoint 2, we see that they are no
longer equal. Hence

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a1` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a2`  -->
```jayret
a1 == a2;
```
``` output
false
```
:::

However, there is a time when `a1`{.jayret} and `a2`{.jayret} do print
the same, namely before checkpoint 1. Therefore, Jayret provides
another equality operator that checks whether values are equal
at the moment, `=~`{.jayret}. If we ask this before checkpoint 1,
we get:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: Evaluating an expression failed. It was expected to evaluate to a Pyret Value. It evaluated to the non-Pyret Value value: non-Pyret value; see the console for m -->
```jayret
a1 =~ a2;
```
``` output
true
```
:::

But if we ask the same question at checkpoint 2, we get:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: Evaluating an expression failed. It was expected to evaluate to a Pyret Value. It evaluated to the non-Pyret Value value: non-Pyret value; see the console for m -->
```jayret
a1 =~ a2;
```
``` output
false
```
:::

These operators and their funny symbols may be hard to remember, but
Jayret also gives them useful (if longer) names, and they can be
used as ordinary functions:

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span style="font-weight: bold">Symbol</span></p></td><td><p><span class="hspace">    </span></p></td><td><p><span style="font-weight: bold">Function</span></p></td><td><p><span class="hspace">    </span></p></td><td><p><span style="font-weight: bold">Type</span></p></td><td><p><span class="hspace">    </span></p></td><td><p><span style="font-weight: bold">Meaning</span></p></td></tr><tr><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">==</code></span></p></td><td><p><span class="hspace">    </span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">equal-always</code></span></p></td><td><p><span class="hspace">    </span></p></td><td><p>Structural</p></td><td><p><span class="hspace">    </span></p></td><td><p>If it returns <span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">true</code></span>, they will always be equal,
irrespective of any future mutations.</p></td></tr><tr><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">=~</code></span></p></td><td><p><span class="hspace">    </span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">equal-now</code></span></p></td><td><p><span class="hspace">    </span></p></td><td><p>Structural</p></td><td><p><span class="hspace">    </span></p></td><td><p>If it returns <span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">true</code></span> they are currently equal,
but that may change after future mutations.</p></td></tr><tr><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">&lt;=&gt;</code></span></p></td><td><p><span class="hspace">    </span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">identical</code></span></p></td><td><p><span class="hspace">    </span></p></td><td><p>Reference</p></td><td><p><span class="hspace">    </span></p></td><td><p>Returns <span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">true</code></span> if the two arguments are aliases,
<span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">false</code></span> otherwise.</p></td></tr></table>
```
Thus, before checkpoint 1:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a1` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a2`  -->
```jayret
equal-now(a1, a2);
```
``` output
true
```
:::

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a2` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a4`  -->
```jayret
equal-now(a2, a4);
```
``` output
true
```
:::

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a1` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a2`  -->
```jayret
equal-always(a1, a2);
```
``` output
false
```
:::

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a2` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a4`  -->
```jayret
equal-always(a2, a4);
```
``` output
true
```
:::

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a1` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a2`  -->
```jayret
identical(a1, a2);
```
``` output
false
```
:::

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a2` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a4`  -->
```jayret
identical(a2, a4);
```
``` output
true
```
:::

After checkpoint 2, we no longer need to check any of the
`equal-always`{.jayret} or `identical`{.jayret} relationships again, because
by definition they cannot change. But we should check `equal-now`{.jayret}
again. Sure enough:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a1` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a2`  -->
```jayret
equal-now(a1, a2);
```
``` output
false
```
:::

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `a2` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `a4`  -->
```jayret
equal-now(a2, a4);
```
``` output
true
```
:::

Therefore, in Jayret, the `==`{.jayret} operator is the same as
`equal-always`{.jayret}. When data contain mutable fields, this will
always produce `false`{.jayret}, because even if the values are
structurally equal now, it’s possible that a future
mutation will change that. This is to remind you to be careful in the
presence of mutation. In situations where we really care only about
equality at that instant, we can use `=~`{.jayret}, i.e., `equal-now`{.jayret}.

The examples above might suggest that only aliased values are
`equal-always`{.jayret}. This is not true! If our data are immutable
(which is the default in the language), then if two values are
structurally equal now, they must remain structurally equal
forever. For such data, `equal-always`{.jayret} will return `true`{.jayret}
even when they are not aliases. This is a reminder that we get
stronger guarantees about immutable data.

It is worth noting that upto this point we have used
`equal-always`{.jayret}—in the form of both `==`{.jayret} and Jayret’s
`is`{.jayret} in testing—without really bothering to understand very
much about how it works, and yet have always gotten predictable
answers. This suggests that there is something natural about working
with immutable data. In contrast, with mutable data, something has to
give. Jayret made a conscious design choice to reflect this in the
distinction between `equal-always`{.jayret} and `equal-now`{.jayret}. Python
made a different choice, which results in “equality” having a
perhaps surprising meaning. (Python has no notion of
`equal-always`{.jayret}, only `equal-now`{.jayret} or `=~`{.jayret}, which is
written as `==`{.python}, and `identical`{.jayret} or `<=>`{.jayret}, which is
written as `is`{.python}.)
