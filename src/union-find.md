---
title: Union-Find
section_number: 18.3
source_file: dcic_orig_union-find.html
prev: sets-from-trees.html
up: part_sets.html
next: hash-set-kv.html
---

### Union-Find {#union-find}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="union-find.html#%28part._.Implementing_with_.State%29">18.3.1<span class="hspace"> </span>Implementing with State</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="union-find.html#%28part._.Optimizations%29">18.3.2<span class="hspace"> </span>Optimizations</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="union-find.html#%28part._.Analysis%29">18.3.3<span class="hspace"> </span>Analysis</a></p></td></tr></table>
```

We have previously [[Checking Component Connectedness](mst.html##union-find-functional)] seen how to
check connectedness of components, but found that solution
unsatisfactory. Recall that it comes down to two set operations: we
want to construct the unions of sets, and then determine whether two
elements are in the same set.

We will now see how to do this using state. We will
try to keep things as similar to the previous version as possible, to
enhance comparison.

#### Implementing with State {#Implementing-with-State}

First, we have to update the definition of an element, making the
`parent`{.pyret} field be mutable:

```pyret
data Element:
  | elt(val, ref parent :: Option<Element>)
end
```
To determine whether two elements are in the same set, we will still
rely on `fynd`{.pyret}. However, as we will soon see, `fynd`{.pyret} no
longer needs to be given the entire set of elements. Because the only
reason `is-in-same-set`{.pyret} consumed that set was to pass it on to
`fynd`{.pyret}, we can remove it from here. Nothing else changes:

```pyret
fun is-in-same-set(e1 :: Element, e2 :: Element) -> Boolean:
  s1 = fynd(e1)
  s2 = fynd(e2)
  identical(s1, s2)
end
```
Updating is now the crucial difference: we use mutation to change the
value of the parent:

```pyret
fun update-set-with(child :: Element, parent :: Element):
  child!{parent: some(parent)}
end
```
In `parent: some(parent)`{.pyret}, the first `parent`{.pyret} is the name of
the field, while the second one is the parameter name. In addition, we
must use `some`{.pyret} to satisfy the option type. Naturally, it is not
`none`{.pyret} because the entire point of this mutation is to change the
parent to be the other element, irrespective of what was there before.

Given this definition, `union`{.pyret} also stays largely unchanged,
other than the change to the return type. Previously, it needed to
return the updated set of elements; now, because the update is
performed by mutation, there is no longer any need to return anything:

```pyret
fun union(e1 :: Element, e2 :: Element):
  s1 = fynd(e1)
  s2 = fynd(e2)
  if identical(s1, s2):
    s1
  else:
    update-set-with(s1, s2)
  end
end
```
Finally, `fynd`{.pyret}. Its implementation is now remarkably
simple. There is no longer any need to search through the
set. Previously, we had to search because after union operations have
occurred, the parent reference might have no longer been valid. Now,
any such changes are automatically reflected by mutation. Hence:

```pyret
fun fynd(e :: Element) -> Element:
  cases (Option) e!parent:
    | none => e
    | some(p) => fynd(p)
  end
end
```

#### Optimizations {#Optimizations}

Look again at `fynd`{.pyret}. In the `some`{.pyret} case, the element bound
to `e`{.pyret} is not the set name; that is obtained by recursively
traversing `parent`{.pyret} references. As this value returns, however,
we don’t do anything to reflect this new knowledge! Instead, the next
time we try to find the parent of this element, we’re going to perform
this same recursive traversal all over again.

Using mutation helps address this problem. The idea is as simple as
can be: compute the value of the parent, and update it.

```pyret
fun fynd(e :: Element) -> Element:
  cases (Option) e!parent block:
    | none => e
    | some(p) =>
      new-parent = fynd(p)
      e!{parent: some(new-parent)}
      new-parent
  end
end
```
Note that this update will apply to every element in the recursive
chain to find the set name. Therefore, applying `fynd`{.pyret} to
any of those elements the next time around will benefit from
this update. This idea is called path compression.

There is one more interesting idea we can apply. This is to maintain a
rank of each element, which is roughly the depth of the tree of
elements for which that element is their set name. When we union two
elements, we then make the one with larger rank the parent of the one
with the smaller rank. This has the effect of avoiding growing very
tall paths to set name elements, instead tending towards “bushy”
trees. This too reduces the number of parents that must be traversed
to find the representative.

#### Analysis {#Analysis}

This optimized union-find data structure has a remarkble analysis. In
the worst case, of course, we must traverse the entire chain of
parents to find the name element, which takes time proportional to the
number of elements in the set. However, once we apply the above
optimizations, we never need to traverse that same chain again! In
particular, if we conduct an amortized analysis over a sequence
of set equality tests after a collection of union operations, we find
that the cost for subsequent checks is very small—indeed, about as
small a function can get without being constant. The
[actual analysis](http://en.wikipedia.org/wiki/Disjoint-set_data_structure)
is quite sophisticated; it is also one of the most
remarkable algorithm analyses in all of computer science.[Here’s a
[brief talk](https://www.youtube.com/watch?v=Hhk8ANKWGJA)
by Robert Tarjan describing the history of his analysis.]{.margin-note}
