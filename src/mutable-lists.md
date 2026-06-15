---
title: Mutable Lists
section_number: 13.2
source_file: dcic_orig_mutable-lists.html
prev: mutating-variables.html
up: part_python-state.html
next: booklet_algo-analysis.html
---

### Mutable Lists {#mutable-lists}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td></td></tr></table>
```

Let’s expand our study of updates yet again, this time looking at
updating lists. We’ll start with lists.

Imagine that Shaunae wants to use a program to maintain her shopping
list. She creates an initial list with two items:

```python
shaunae_list = ["bread", "coffee"]
```

::: {.do-now}
Shaunae wants to add eggs to her list. Write a line of code to
accomplish this.
:::

There are two ways you could have done this:

```python
# approach 1
shaunae_list = shaunae_list + ["eggs"]

#approach 2
shaunae_list.append("eggs")
```

What is the difference between these two approaches? The difference
lies in the impact on the heap.


- The first version creates a new list containing `"eggs"`{.python},
  then puts the elements of the two lists together in a new list.
- The second version inserts `"eggs"`{.python} into the existing
  list in the heap.

Let’s look at the directories for each version. Here’s the final directory
for the first version:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">shaunae_list</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1010</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1005</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">List(len:2)</code></span></p></li><li><p><span class="heapref source">1006</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"bread"</code></span></p></li><li><p><span class="heapref source">1007</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"coffee"</code></span></p></li><li><p><span class="heapref source">1008</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">List(len:1)</code></span></p></li><li><p><span class="heapref source">1009</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"eggs"</code></span></p></li><li><p><span class="heapref source">1010</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">List(len:3)</code></span></p></li><li><p><span class="heapref source">1011</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"bread"</code></span></p></li><li><p><span class="heapref source">1012</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"coffee"</code></span></p></li><li><p><span class="heapref source">1013</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"eggs"</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
The original version of `shaunae_list`{.python} is in address
1005, the list with `"eggs"`{.python} is in 1008, and
the combined list is in 1010.

In contrast, the final directory for the second version would look like:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">shaunae_list</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1010</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1005</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">List(len:3)</code></span></p></li><li><p><span class="heapref source">1006</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"bread"</code></span></p></li><li><p><span class="heapref source">1007</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"coffee"</code></span></p></li><li><p><span class="heapref source">1008</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"eggs"</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
Notice here that the length and contents of the original list are
changed to include the newly-appended `"eggs"`{.python}.

::: {.do-now}
Which approach do you think is better? Why?
:::

At first glance, the second approach might seem better because it
doesn’t create additional unnecessary lists. Both approaches result in
the same contents in `shaunae_List`{.python}, so there seems little
benefit to using the additional space.

Unless, of course, we want to still have access to the old version of
`shaunae_list`{.python} later on. The old list is still in the heap
(though our current program has no name through which to access that
old list). What if we instead had written the program this way?

```python
shaunae_list = ["bread", "coffee"]
prev_list = shaunae_list
shaunae_list = ["paint", "brushes"] + shaunae_list
```

Now, if Shaunae realizes she goofed and put her art supply shopping on
the grocery list on that last update, she could “undo” the update by
resetting her list variable to the previous list:

```python
shaunae_list = prev_list
```

Undoing a modification (just like the undo feature in document-editing
tools) is just one example of where it can help to hang on to older
versions of data for a little while. The point here is not to give a
sophisticated treatment of undoing computations, but more to motivate
that there are situations in which creating a new list is preferable
to updating the old one.

When might we want to update, rather than preserve, the existing list?

Remember our discussion of aliasing? We wanted two people, Elena and
Jorge to share access to a common bank account. Might we ever want a
shared shopping list? Sure, Shaunae and her roommate Jonella do share
a shopping list, so that they can both add items while letting either
one go to the store.

::: {.do-now}
Set up a shared shopping list that is accessible through two names,
`shaunae_list`{.python} and `jonella_list`{.python}. Then, add an item to
the list via one of these names and check that the item appears under
the other name.
:::

You might have written something like the following:

```python
shaunae_list = ["bread", "coffee"]
jonella_list = shaunae_list
jonella_list.append("eggs")
```
If you load this code at the prompt and look at both lists at the end,
you’ll see they have the same values.

In contrast, had we written the code as follows, only one of them
would see the new item:

```python
>>> jonella_list = ["apples"] + jonella_list
>>> jonella_list
["apples", "bread", "coffee", "eggs"]
>>> shaunae_list
["bread", "coffee", "eggs"]
```

::: {.do-now}
Draw the memory diagram for the above program.
:::

#### Exercise: Creating Lists of Accounts {#Exercise-Creating-Lists-of-Accounts}

In [Mutating Top-Level Variables within Functions](mutating-variables.html##mut-top-level-vars-in-func), we wrote a function to create new accounts for the
bank. That function returned each new account as it was created. That
meant that every newly-created account had to be associated with a
name in the directory (otherwise we would not be able to access it
from the heap).

Maintaining either a list or a dictionary of all the created accounts
makes much more sense. We’d need only a single name for the collection
of accounts, but could still access individual accounts as needed. For
example, we might want an `all_accts`{.python} list that looks something
like the following:

```python
all_accts = [Account(8623, 100),
             Account(8624, 300),
             Account(8625, 225),
             ...
             ]
```

::: {.do-now}
Write a program that creates an empty `all_accts`{.python} list, then
adds a new `Account`{.python} to it each time `create_acct`{.python} is called. You
will need to modify `create_acct`{.python} in order to do this. Here is
the existing code as a starting point.

```python
next_id = 1

def create_acct(init_bal: float) -> Account:
  global next_id
  new_acct = Account(next_id, init_bal, [])
  next_id = next_id + 1
  return new_acct
```
:::

::: {.do-now}
Did you include a line like `global all_accts`{.python} in your code?
Why or why not?
:::

If you used `append`{.python} to update the `all_accts`{.python} list,
then you would not need to include `global all_accts`{.python}. Recall
that `global`{.python} is needed to tell Python to update a variable in
the top-level directory rather than the local directory. If you use
`all_accts.append`{.python}, however, you are modifying the heap instead
of the directory. There is no need for `global`{.python} if your code is
only modifying heap contents.
