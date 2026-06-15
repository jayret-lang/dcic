---
title: Arrays
section_number: 9.3
source_file: dcic_orig_arrays.html
prev: dictionaries.html
up: part_pyret-to-python.html
next: part_python-tables.html
---

### Arrays {#arrays}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="arrays.html#%28part._.Two_.Memory_.Layouts_for_.Ordered_.Items%29">9.3.1<span class="hspace"> </span>Two Memory Layouts for Ordered Items</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="arrays.html#%28part._.Iterating_.Partly_through_an_.Ordered_.Datum%29">9.3.2<span class="hspace"> </span>Iterating Partly through an Ordered Datum</a></p></td></tr></table>
```

We ended the last chapter with a question about how fast one can access a
specific element of a list. Specifically, if you have a list called
finishers of Runners (our example from last time) and you
write:

```python
finishers[9]
```

How long does it take to locate the Runner in 10th place (remember,
indices start at 0)?

It depends on how the list is laid out in memory.

#### Two Memory Layouts for Ordered Items {#Two-Memory-Layouts-for-Ordered-Items}

When we say "list", we usually mean simply: a collection of items with
order. How might a collection of ordered items be arranged in memory?
Here are two examples, using a list of course names:

```python
courses = ["CS111", "ENGN90", "VISA100"]
```

In the first version, the elements are laid out in consecutive memory
locations (this is rougly how we’ve shown lists up to now):

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">Prog Directory</span><span class="hspace">           </span><span class="stt">Memory</span></p></td></tr><tr><td><p><span class="stt">--------------------------------------------------------------------</span></p></td></tr><tr><td><p><span class="stt">courses --&gt; loc 1001</span><span class="hspace">      </span><span class="stt">loc 1001 --&gt; [loc 1002, loc1003, loc 1004]</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">                          </span><span class="stt">loc 1002 --&gt; "CS111"</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">                          </span><span class="stt">loc 1003 --&gt; "ENGN90"</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">                          </span><span class="stt">loc 1004 --&gt; "VISA100"</span></p></td></tr></table>
```

In the second version, each element is captured as a datatype
containing the element and the next list location. When we were in
Pyret, this datatype was called `link`{.python}.

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">Prog Directory</span><span class="hspace">           </span><span class="stt">Memory</span></p></td></tr><tr><td><p><span class="stt">--------------------------------------------------------------------</span></p></td></tr><tr><td><p><span class="stt">courses --&gt; loc 1001</span><span class="hspace">      </span><span class="stt">loc 1001 --&gt; link("CS111", loc 1002)</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">                          </span><span class="stt">loc 1002 --&gt; link("ENGN90", loc 1003)</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">                          </span><span class="stt">loc 1003 --&gt; link("VISA100", loc 1004)</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">                          </span><span class="stt">loc 1004 --&gt; empty</span></p></td></tr></table>
```

What are the tradeoffs between the two versions? In the first, we can
access items by index in constant time, as we could for hashtables,
but changing the contents (adding or deleting) requires moving things
around in memory. In the second, the size of the collection can grow
or shrink arbitrarily, but it takes time proportional to the index to
look up a specific value. Each organization has its place in some
programs.

In data structures terms, the first organization is called an
array. The second is called a linked list. Pyret
implements linked lists, with arrays being a separate data type (with
a different notation from lists). Python implements lists as
arrays. When you approach a new programming language, you need to look
up whether its lists are linked lists or arrays if you care about the
run-time performance of the underlying operations.

Going back to our Runners discussion from the last chapter, we can simply
use Python lists (arrays) rather than a hashtable, and be able to
access the names of Runners who finished in particular positions. But
let’s instead ask a different question.

How would we report the top finishers in each age category? In
particular, we want to write a function such as the following:

```python
def top_5_range(runners: list, lo: int, high: int) -> list:
    """get list of top 5 finishers with ages in
       the range given by lo to high, inclusive
    """
```

Think about how you would write this code.

Here’s our solution:

```python
def top_5_range(runners: list, lo: int, high: int) -> list:
    """get list of top 5 finishers with ages in
       the range given by lo to high, inclusive
    """

    # count of runners seen who are in age range
    in_range: int = 0
    # the list of finishers
    result: list = []

    for r in runners:
        if lo <= r.age and r.age <= high:
            in_range += 1
            result.append(r)
        if in_range == 5:
            return result
    print("Fewer than five in category")
    return result
```

Here, rather than return only when we get to the end of the list, we
want to return once we have five runners in the list. So we set up an
additional variable (`in_range`{.python}) to help us track progress of the
computation. Once we have gotten to 5 runners, we return the list. If
we never get to 5 runners, we print a warning to the user then return
the results that we do have.

Couldn’t we have just looked at the length of the list, rather than
maintain the `in_range`{.python} variable? Yes, we could have, though
this version sets up a contrast to our next example.

#### Iterating Partly through an Ordered Datum {#Iterating-Partly-through-an-Ordered-Datum}

What if instead we just wanted to print out the top 5 finishers,
rather than gather a list? While in general it is usually better to
separate computing and displaying data, in practice we do sometimes
merge them, or do other operations (like write some data to file)
which won’t return anything. How do we modify the code to print the
names rather than build up a list of the runners?

The challenge here is how to stop the computation. When we are
building up a list, we stop a computation using return. But if our
code isn’t returning, or otherwise needs to stop a loop before it
reaches the end of the data, what do we do?

We use a command called `break`{.python}, which says to terminate the loop
and continue the rest of the computation. Here, the break is in place
of the inner return statement:

```python
def print_top_5_range(runners: list, lo: int, high: int):
    """print top 5 finishers with ages in
       the range given by lo to high, inclusive
    """

    # count of runners seen who are in age range
    in_range: int = 0

    for r in runners:
        if lo <= r.age and r.age <= high:
            in_range += 1
            print(r.name)
        if in_range == 5:
            break
    print("End of results")
```

If Python reaches the `break`{.python} statement, it terminates the for
loop and goes to the next statement, which is the print at the end of
the function.
