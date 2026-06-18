---
title: Arrays and Lists in Memory
section_number: 12.3
source_file: unified-lists-memory.html
prev: unified-equality.html
up: part_state.html
next: unified-cyclic-data.html
---

```{=html}
<a name="(part._unified-lists-memory)"></a>
```

### 12.3 Arrays and Lists in Memory {#unified-lists-memory}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td></td></tr></table>
```

In [Understanding Equality](unified-equality.html), we drew memory diagrams to show how
values appear in the heap. At that time, we looked only at structured
data. Now we will look at aggregate data: lists in Python and arrays
in Jayret.

Both Python lists and Jayret arrays are stored in memory with a
starting value that indicates how many values there are, followed by
the actual elements in subsequent addresses. For instance, suppose we
write the following value:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">sl = ['bread', 'coffee', 'eggs']</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">sl = [array: 'bread', 'coffee', 'eggs']</code></pre></div></div></p></td></tr></table>
```
Here’s what memory might look like:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">sl</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">(length:3)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"bread"</code></span></p></li><li><p><span class="heapref source">1003</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"coffee"</code></span></p></li><li><p><span class="heapref source">1004</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"eggs"</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
[If these terms mean anything to you: Python’s default list
implementation is array-based, not a linked list.]{.margin-note}
So at 1001 there’s an indication of how many entries follow,
and the next memory locations have those values. There are no
directory entries for the individual elements, but they can be reached
by referring to `sl`{.jayret} followed by an offset: for instance,

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">sl[2]</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">sl.get-now(2)</code></pre></div></div></p></td></tr></table>
```
Internally, this turns into: “obtain the address of `sl`{.jayret}, then
add 1 and the offset `2`{.jayret} to it”. This produces the address
1001 + 1 + 2 = 1004. Looking up the value stored
at address 1004, in both languages, produces
`'eggs'`{.python}.[You may find it odd that the offsets begin
at 0. While it is indeed confusing—the “first” value is at offset
`0`{.jayret}, the “third” value at offset `2`{.jayret}, and so on—this is
a convention both Python and Jayret chose to be consistent with most
other programming languages.]{.margin-note}

Similarly, suppose we try to change the shopping list’s content to
replace the second value with `'tea'`{.jayret}. Recall that the second
value is at offset `1`{.jayret}:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">sl[1] = 'tea'</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">sl.set-now(1, 'tea')</code></pre></div></div></p></td></tr></table>
```
Again, we obtain the address of `sl`{.jayret}, which is 1001; add
1 and the offset (`1`{.jayret}) to it; this gives us the address
1003. Now, we modify the value at 1003 to be the new
value:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">sl</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">(length:3)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"bread"</code></span></p></li><li><p><span class="heapref source">1003</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"tea"</code></span></p></li><li><p><span class="heapref source">1004</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"eggs"</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
If we now ask the language for the list as a whole, we see the change:
in Python,

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `sl` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. There were com -->
```jayret
sl;
```
``` output
['bread', 'tea', 'eggs']
```
:::

and in Jayret,

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `sl` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. There were com -->
```jayret
sl;
```
``` output
[array: "bread", "tea", "eggs"]
```
:::

Observe that what we have learned about aliasing applies here,
too. Suppose Shaunae and Jonella share a shopping list, where
`sl`{.jayret} is Shaunae’s and Jonella writes:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jl = sl</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jl = sl</code></pre></div></div></p></td></tr></table>
```
Now `jl`{.jayret} and `sl`{.jayret} are aliases for the same data in the heap:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">sl</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jl</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">(length:3)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"bread"</code></span></p></li><li><p><span class="heapref source">1003</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"tea"</code></span></p></li><li><p><span class="heapref source">1004</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"eggs"</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
Thus, modifying the list `jl`{.jayret} has the same impact as modifying it
via `sl`{.jayret}:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jl[0] = 'butter'</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jl.set-now(0, 'butter')</code></pre></div></div></p></td></tr></table>
```
means the memory looks like

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">sl</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jl</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">(length:3)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"butter"</code></span></p></li><li><p><span class="heapref source">1003</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"tea"</code></span></p></li><li><p><span class="heapref source">1004</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"eggs"</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
Thus, if we ask for the value of `sl`{.jayret}, we will see in Python:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `sl` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. There were com -->
```jayret
sl;
```
``` output
['butter', 'tea', 'eggs']
```
:::

and in Jayret:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `sl` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. There were com -->
```jayret
sl;
```
``` output
[array: "butter", "tea", "eggs"]
```
:::

even though we did not make a modification through the name `sl`{.jayret}.
