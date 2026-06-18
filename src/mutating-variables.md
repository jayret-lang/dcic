---
title: Mutating Variables
section_number: 13.1
source_file: mutating-variables.html
prev: part_python-state.html
up: part_python-state.html
next: mutable-lists.html
---

```{=html}
<a name="(part._mutating-variables)"></a>
```

### 13.1 Mutating Variables {#mutating-variables}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-variables.html#%28part._mutating-vars-memory%29">13.1.1<span class="hspace"> </span>Mutating Variables in Memory</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-variables.html#%28part._var-mut-aliasing%29">13.1.2<span class="hspace"> </span>Variable Mutation and Aliasing</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-variables.html#%28part._.Mutating_.Variables_versus_.Mutating_.Data_.Fields%29">13.1.3<span class="hspace"> </span>Mutating Variables versus Mutating Data Fields</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-variables.html#%28part._.Mutating_.Parameters_in_.Function_.Calls%29">13.1.4<span class="hspace"> </span>Mutating Parameters in Function Calls</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-variables.html#%28part._mut-top-level-vars-in-func%29">13.1.5<span class="hspace"> </span>Mutating Top-Level Variables within Functions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-variables.html#%28part._.The_.Many_.Roles_of_.Variables%29">13.1.6<span class="hspace"> </span>The Many Roles of Variables</a></p></td></tr></table>
```

```{=html}
<a name="(part._mutating-vars-memory)"></a>
```

#### 13.1.1 Mutating Variables in Memory {#mutating-vars-memory}

Now that we have introduced the idea of the heap, let’s revisit our
use of a variable to compute the sum of elements in a list. Here again
is the code we wrote for this earlier (in [Introducing `For`{.python} Loops](intro-python.html##python-for-loops)):

```python
run_total = 0
for num in [5, 1, 7, 3]:
   run_total = run_total + num
```

Let’s see how the directory and heap update as we run this code. In
[Basic Data and the Heap](mutating-structures.html##basic-data-heap), we pointed out that basic data (such as
numbers, strings, and booleans) don’t get put in the heap because they
have no internal structure. Those values are stored in the directory
itself. Therefore, the initial value for `run_total`{.python} is stored
within the directory.

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">run_total</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">0</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

The `for`{.python} loop also sets up a directory entry, this time for
the variable `num`{.python} that is used to refer to the list
elements. When the loop starts, `num`{.python} takes on the first value
in the list. Thus, the directory appears as:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">run_total</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">0</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">num</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">5</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

Inside the `for`{.python} loop, we compute a new value for
`run_total`{.python}. The use of `=`{.python} tells Python to modify the
value of `run_total`{.python}.

::: {.do-now}
Does this modification get made in the directory or the heap?
:::

Since basic data values are stored only in the directory, this update
modifies the contents of the directory. The heap isn’t involved:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">run_total</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">5</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">num</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">5</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

This process continues: Python advances `num`{.python} to the next list
element

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">run_total</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">5</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">num</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">1</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```
then modifies the value of `run_total`{.python}

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">run_total</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">6</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">num</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">1</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```
This process continues until all of the list elements have been
processed. When the for-loop ends, the directory contents are:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">run_total</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">16</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">num</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">3</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

There are two takeaways from this example:

- When we use `=`{.python} to update the value associated with a
  variable, the variable’s entry in the directory changes to reflect the
  new value.

- `For`{.python} loops
  introduce a name into the directory (the one the programmer chose to
  refer to the individual list elements). As the loop progresses, Python
  updates the value associated with that name to refer to each
  successive element.

::: {.exercise}
Draw the sequence of directory contents for the following program:

```python
score = 0
score = score + 4
score = 10
```
:::

::: {.exercise}
Draw the sequence of directory contents for the following program:

```python
count_long = 0
for word in ["here", "are", "some", "words"]:
  if len(word) > 4:
    count_long = count_long + 1
```
:::

```{=html}
<a name="(part._var-mut-aliasing)"></a>
```

#### 13.1.2 Variable Mutation and Aliasing {#var-mut-aliasing}

In [Mutating Structures](mutating-structures.html), we saw how a statement of the form
`elena.acct.balance = 500`{.python} resulted in a change to
`jorge.acct.balance`{.python}. Does this same effect occur if we update the
value of a variable directly, rather than a field? Consider the
following example:

```python
y = 5
x = y
```

::: {.do-now}
What do the directory and heap look like after running this code?
:::

Since `x`{.python} and `y`{.python} are assigned basic values, there are
no values in the heap:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">y</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">5</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">x</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">5</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

::: {.do-now}
If we now evaluate `y = 3`{.python}, does the value of `x`{.python}
change?
:::

It does not. The value associated with `y`{.python} in the directory
changes, but there is no connection between `x`{.python} and `y`{.python}
in the directory. The statement `x = y`{.python} says “get the value of
`y`{.python} and associate it with `x`{.python} in the
directory”. Immediately after this statement, `y`{.python} and
`x`{.python} refer to the same value, but this relationship is neither
tracked nor maintained. If we associate either variable with a new
value, as we do with `y = 3`{.python}, the directory entry for that
variable—and only the directory entry for that variable—are
changed to reflect the new value. Thus, the directory after we
evaluate `y = 3`{.python} appears as follows:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">y</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">3</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">x</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">5</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

This example highlights that aliasing occurs only when two variables
refer to the same piece of data with components, not when variables
refer to basic data. This is because data with components are stored
in the heap, with heap address stored in the directory. Note, though,
that uses of `varname = ...`{.python} still affect the directory, even
when the values are data with components.

::: {.do-now}
After running the following code, what is the value of `ac2.balance`{.python}?

```python
ac1 = Account(8623, 600)
ac2 = ac1
ac1 = Account(8721, 350)
```
Draw the directory and heap contents for this program and check your
prediction.
:::

All three of these lines results in changes in the directory; the
first two result in changes in the heap, but only because we made new
pieces of data. `ac1`{.python} and `ac2`{.python} are alises immediately
after running the second line, but the third line breaks that
relationship.

::: {.do-now}
After running the following code, what is the value of `ac3.balance`{.python}?

```python
savings = 475
ac3 = Account(8722, savings)
savings = 500
```
Draw the directory and heap contents for this program and check your
prediction.
:::

Since the value of `savings`{.python} is stored in `ac3.balance`{.python},
and not the name `savings`{.python} itself, updating the value of
`savings`{.python} on the third line does not affect `ac3.balance`{.python}.

```{=html}
<a name="(part._Mutating-Variables-versus-Mutating-Data-Fields)"></a>
```

#### 13.1.3 Mutating Variables versus Mutating Data Fields {#Mutating-Variables-versus-Mutating-Data-Fields}

We’ve now seen two different forms of updates in programs: updates to
fields of structured data in [Mutating Structures](mutating-structures.html), and updates to
the values associated with names when computing over lists with
`for`{.python} loops. At a quick glance, these two forms of update look
similar:

```python
acct1.balance = acct1.balance - 50
run_total = run_total + fst
```
Both use the `=`{.python} operator and compute a new value on the right
side. The left sides, however, are subtly different: one is a field
within structured data, while the other is a name in the directory. This
difference turns out to be significant: the first form changes a value
stored in the heap but leaves the directory unchanged, while the
second updates the directory but leaves the heap unchanged.

At this point, you might not appreciate why this difference is
significant. But for now, let’s summarize how each of these forms
impacts each of the directory and the heap.

::: {.strategy}
Summarizing, the rules for how the directory and memory update are as follows:

- We add to the heap when a data constructor is used

- We update the heap when a field of existing data is reassigned

- We add to the directory when a name is used for the first time (this
  includes parameters and internal variables when a function is called)

- We update the directory when a name that is already in the
  directory is subsequently assigned a new value)
:::

::: {.do-now}
After running the following code, what is the value of `ac3.balance`{.python}?

```python
ac2 = Account(8728, 200)
ac3 = ac2
print(ac3.balance)
ac2.balance = 500
print(ac3.balance)
ac2 = Account(8734, 350)
ac2.balance = 700
print(ac3.balance)
```
Draw the directory and heap contents for this program and check your
prediction.
:::

This example combines updates to variables and updates to fields. On
the third line, `ac2`{.python} and `ac3`{.python} refer to the same
address in the heap (which contains the `Account`{.python} with id
`8728`{.python}. Immediately after updating `ac2.balance`{.python} on the
fourth line, the balance in both `ac2`{.python} and `ac3`{.python} is 500. Line
six, however, creates a new `Account`{.python} in the heap and updates
the directory to have `ac2`{.python} refer to that new
`Account`{.python}. From that point on, `ac2`{.python} and `ac3`{.python}
refer to different accounts, so the update to the balance in
`ac2`{.python} on the seventh line does not affect `ac3`{.python}.

This example illustrates the subtleties and impacts of different uses of
`=`{.python}. Programs behave differently depending on whether the left
side of the `=`{.python} is a variable name or a field reference, and on
whether the right side is basic data or data with components. We will
continue to work with these various combinations to build your
understanding of when and how to use each one.

```{=html}
<a name="(part._Mutating-Parameters-in-Function-Calls)"></a>
```

#### 13.1.4 Mutating Parameters in Function Calls {#Mutating-Parameters-in-Function-Calls}

In [Function Composition and the Directory](Conditionals_and_Booleans.html##func-comp-directory), we showed how
function calls create their own local directory segments to store any
names that get introduced while running the function. Now that we have
the ability to update the values associated with variables, we should
revisit this topic to understand what happens when these updates occur
within functions.

Consider the following two functions:

```python
def add10(num: int):
  num = num + 10

def deposit10(ac: Account)
  ac.balance = ac.balance + 10
```

Let’s use these two functions in a program:

```python
x = 15
a = Account(8435, 500)
add10(x)
deposit10(a)
```

::: {.do-now}
What are the values of `x`{.python} and `a`{.python} when the program has
finished?
:::

Let’s draw out the directory and heap for this program.

[We need a way to distinguish local directories from the
global one – easiest for now might be to add a form for
local-env-with-heap that uses the label “Local Directory (fun name)”.]{.margin-note}

After the first two lines but before the function calls, we have the
following:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">x</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">15</code></span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1014</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1014</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8435, 500)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

Calling `add10`{.python} creates a local directory containing the name
of the parameter:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">num</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">15</code></span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1014</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8435, 500)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

Wait – why is the heap listed alongside the local directory? Only the
directory gets localized during function calls. The same heap is used
at all times.

The body of `add10`{.python} now updates the value of `num`{.python} in
the directory to 25. This does not affect the value of `x`{.python} in
the top-level directory, for the same reasons we explained in [Variable Mutation and Aliasing](mutating-variables.html##var-mut-aliasing)
regarding the lack of aliasing between variables that refer to basic
data. Thus, once the function finishes and the local directory is
deleted, the value associated with `x`{.python} is unchanged.

Now, let’s evaluate the call `deposit10(a)`{.python}. As with
`add10`{.python}, we create a local directory and create an entry for
the parameter. What gets associated with that parameter in the
directory, however?

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">ac</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1014</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1014</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8435, 500)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

::: {.do-now}
Why didn’t we create a new `Account`{.python} datum when we made the
function call?
:::

Remember our rule for when we create new data in the heap: we only
create heap data when we explicitly use a constructor. The function
call does not involve creating a new `Account`{.python}. Whatever is
associated with the name `a`{.python} gets associated with the parameter
name `ac`{.python}. In other words, we have created an alias between
`a`{.python} and `ac`{.python}.

In the body of `deposit10`{.python}, we update the balance of
`ac`{.python}, which is also the balance of `a`{.python} due to the
aliasing. Since there is no local heap, when the function call is
over, the new balance persists in `a`{.python}.

All we’ve done here is put together pieces that we’ve already seen,
just in a new context. We’re passing parameters and updating either
the (local) directory or the heap according to how we have used
`=`{.python}. But this example highlights a detail that initially
confuses many people when they start writing functions that update
variables.

::: {.strategy}
If you want a function to update a value and have that update persist
after the function completes, you must put that value inside a piece
of data. You cannot have it be basic data associated with a variable
name.
:::

```{=html}
<a name="(part._mut-top-level-vars-in-func)"></a>
```

#### 13.1.5 Mutating Top-Level Variables within Functions {#mut-top-level-vars-in-func}

Let’s return to our banking example to illustrate a situation where
the ability to update variables is extremely useful. Consider our
current process for creating new accounts in the bank by looking at
the following example:

```python
ac5 = Account(8702, 435)
ac6 = Account(8703, 280)
ac7 = Account(8704, 375)
```

Notice that each time we create an `Account`{.python} we have to take
care to increase the id number? What if we made a typo or
accidentally forgot to do this?

```python
ac5 = Account(8702, 435)
ac6 = Account(8703, 280)
ac7 = Account(8703, 375)
```

Now we’d have multiple accounts with the same ID number, when we
really need these numbers to be unique across all accounts. To avoid
such problems, we should instead have a function for creating accounts
that takes the initial balance as input and uses a guaranteed-unique
ID number.

How might we write such a function? The challenge is to be able to
generate unique ID numbers each time. What if we used a variable to
store the next available ID number, updating it each time we created a
new account? That function might look at follows:

```python
nextID = 8000 # stores the next available ID number

def create_acct(init_bal: float) -> Account:
  new_acct = Account(nextID, init_bal)
  nextID = nextID + 1
  return(new_acct)
```

Let’s run this program, creating new accounts as follows:

```python
ac5 = create_acct(435)
ac6 = create_acct(280)
ac7 = create_acct(375)
```

::: {.do-now}
Copy this code into Python and run it. Check that each of
`ac5`{.python}, `ac6`{.python}, and `ac7`{.python} have unique ID numbers.
:::

What happened? All three of these have the same ID of
`8000`{.python}. It looks like our update to `nextID`{.python} just didn’t
work. Actually, it did work, but to understand how, we have to look at
what happened in the directory.

::: {.do-now}
Draw the memory diagram for this example.
:::

After we set up `nextID`{.python} and define the function, our memory
diagram appears as:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">nextID</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">8000</code></span></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

Now, let’s evaluate `ac5 = create_acct(435)`{.python}. We call
`create_acct`{.python}, which yields the following local directory after
creating the `Account`{.python} but before updating `nextID`{.python}.

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">init_bal</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">435</code></span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">new_acct</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1015</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1015</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8000, 435)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

::: {.do-now}
What do you think happens when we run `nextID = nextID + 1`{.python}?
:::

Let’s run this carefully. Python first evaluates the right side of the
`=`{.python} (`nextID + 1`{.python}). `nextID`{.python} is not in the local
directory, so Python retrieves its value (`8000`{.python}) from the
top-level directory. Thus, this computation becomes `nextID = 8001`{.python}.

The question here is how Python treats `nextID = 8001`{.python}: we
currently have both the local directory for the function call and the
top-level directory. Which one should get the new value of
`nextID`{.python}? Since the local directory is active, Python sets the
value of `nextID`{.python} there.

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">init_bal</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">435</code></span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">new_acct</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1015</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">nextID</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">8001</code></span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1015</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(8000, 435)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

Let’s repeat that: Python computed `nextID + 1`{.python} using the
`nextID`{.python} value from the top-level directory since there was no
value for `nextID`{.python} in the local directory. But the setting of
the value of `nextID`{.python} could and did occur in the local
directory. Thus, when `create_acct`{.python} finishes, the value of
`nextID`{.python} in the top-level directory is unchanged. As a result,
all of the accounts get the same value.

The computuation we are trying to do—updating the top-level
variable—is just fine. The problem is that Python (reasonably)
defaults to the local directory. To make this work, we need to tell
Python that we want to make updates to `next_id`{.python} in the
top-level directory. Here’s the version of `create_acct`{.python} that
does that:

```python
def create_acct(init_bal: float) -> Account:
  global nextID
  new_acct = Account(nextID, init_bal)
  nextID = nextID + 1
  return(new_acct)
```

The `global`{.python} keyword tells Python to make updates to the given
variable in the top-level directory, not the local directory. Once we
make this modification, each account we create will get a unique ID
number.

::: {.responsible-cs}
While this general pattern of generating unique IDs works, in practice
we shouldn’t use consecutive numbers. Consecutive numbers are
guessable: if there is an account `8000`{.python} there must be an
account `8001`{.python}, and so on. Guessable account numbers could make
it easier for someone who keeps trying to guess valid IDs to use to
log into websites or otherwise access information.

Instead, we would use a computation that is less predictable than
“add 1” when storing the `nextID`{.python} value. For now, the
pattern we have shown you is fine. If you were building a real system,
however, you’d want to make that computation a bit more sophisticated.
:::

```{=html}
<a name="(part._The-Many-Roles-of-Variables)"></a>
```

#### 13.1.6 The Many Roles of Variables {#The-Many-Roles-of-Variables}

At this point, we have used the single coding construct of a variable
in the directory for multiple purposes. It’s worth stepping back and
calling those out explicitly. In general, variables serve one of the
following purposes:

1. Tracking progress of a computation (e.g., the running value of a
  result in a `for`{.python}-loop)

2. Maintaining information across multiple calls to a single
  function (e.g., the `next-id`{.python} variable)

3. Naming a local or intermediate value in a computation

Each of these uses involves a different programming pattern. The first
creates a variable locally within a function. The second two create
top-level variables and require using `global`{.python} in functions
that modify the contents. The third is different from the second,
however, in that the third is only meant to be used by a single
function. Ideally, there would be a way to not expose the variable to
all functions in the third case. Indeed, many programming languages
(including Jayret) make it easy to do that. This is harder to achieve
with introductory-level concepts in Python, however. The fourth is
more about local names rather than variables, in that our code never
updates the value after the variable is created.

We call out these three roles precisely because they invoke different
code patterns, despite using the same fine-grained concept (assigning
a new value to a variable). When you look at a new programming
problem, you can ask yourself whether the problem involves one of
these purposes, and use that to guide your choice of pattern to use.
