---
title: Making Sets Grow on Trees
section_number: 18.2
source_file: sets-from-trees.html
prev: sets-from-lists.html
up: part_sets.html
next: union-find.html
---

```{=html}
<a name="(part._sets-from-trees)"></a>
```

### 18.2 Making Sets Grow on Trees {#sets-from-trees}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-from-trees.html#%28part._.Using_.Binary_.Trees%29">18.2.1<span class="hspace"> </span>Using Binary Trees</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-from-trees.html#%28part._.Checking_the_.Complexity%29">18.2.2<span class="hspace"> </span>Checking the Complexity</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="sets-from-trees.html#%28part._sets-from-balanced-trees%29">18.2.3<span class="hspace"> </span>A Fine Balance: Tree Surgery</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="sets-from-trees.html#%28part._.Left-.Left_.Case%29">18.2.3.1<span class="hspace"> </span>Left-Left Case</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="sets-from-trees.html#%28part._.Left-.Right_.Case%29">18.2.3.2<span class="hspace"> </span>Left-Right Case</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="sets-from-trees.html#%28part._.Any_.Other_.Cases_%29">18.2.3.3<span class="hspace"> </span>Any Other Cases?</a></p></td></tr></table>
```

In [Representing Sets as Lists](sets-from-lists.html) we saw multiple list representations of
sets. They all came with at least some operations having linear time
complexity—linear in different ways, but always linear in at least
the number of distinct elements in the set. Can we do better?

Let’s start by noting that it seems better, if at all possible, to
avoid storing duplicates. Duplicates are only problematic during
insertion due to the need for a membership test. But if we can make
membership testing cheap, then we would be better off using it to
check for duplicates and storing only one instance of each value
(which also saves us space). Thus, let’s try to improve the time
complexity of membership testing (and, hopefully, of other operations
too).

It seems clear that with a (duplicate-free) list representation of a
set, we cannot really beat linear time for membership checking. This
is because at each step, we can eliminate only one element from
contention which in the worst case requires a linear amount of work to
examine the whole set. Instead, we need to eliminate many more
elements with each comparison—more than just a constant.

In our handy set of recurrences [[Solving Recurrences](predicting-growth.html##solving-recurrences)], one
stands out: \(T(k) = T(k/2) + c\). It says that if, with a
constant amount of work we can eliminate half the input,
we can perform membership checking in logarithmic time. This will be
our goal.

Before we proceed, it’s worth putting logarithmic growth in
perspective. Asymptotically, logarithmic is obviously not as nice as
constant. However, logarithmic growth is very pleasant because it
grows so slowly. For instance, if an input doubles from size \(k\) to
\(2k\), its logarithm—and hence resource usage—grows only by
\(\log 2k - \log k = \log 2\), which is a constant. Indeed, for just
about all problems, practically speaking the logarithm of the input
size is bounded by a constant (that isn’t even very large). Therefore,
in practice, for many programs, if we can shrink our resource
consumption to logarithmic growth, it’s probably time to move on and
focus on improving some other part of the system.

We have actually just made an extremely subtle assumption. In the list
representation of sets, when we check one element for membership and
eliminate it, we have eliminated only that one element. To
obtain this logarithmic complexity, we need comparing against one
element to remove an entire set of elements. Because we are
constructing sets of numbers, we don’t need to confront this issue
here. Instead, we go into it in much more detail in
[Converting Values to Ordered Values](orderability.html##hashing-values).

```{=html}
<a name="(part._Using-Binary-Trees)"></a>
```

#### 18.2.1 Using Binary Trees {#Using-Binary-Trees}

[Because logs come from trees.]{.margin-note}

Clearly, a list representation does not let us eliminate half the
elements with a constant amount of work; instead, we need a tree.
Thus we define a binary tree of (for simplicity) numbers:

```jayret
data BT {
    Leaf;
    Node(int v, BT l, BT r);
}
```

Given this definition, let’s define the membership checker:

```jayret
boolean is-in-bt(int e, BT s) {
    return switch (s) {
        case Leaf: yield false;
        case Node(v, l, r): yield if (e == v) {
            return true;
        } else {
            return is-in-bt(e, l) || is-in-bt(e, r);
        };
    }
}
```
Oh, wait. If the element we’re looking for isn’t the root, what do we
do? It could be in the left child or it could be in the right; we
won’t know for sure until we’ve examined both. Thus, we can’t throw
away half the elements; the only one we can dispose of is the value at
the root. Furthermore, this property holds at every level of the
tree. Thus, membership checking needs to examine the entire tree, and
we still have complexity linear in the size of the set.

How can we improve on this? The comparison needs to help us eliminate
not only the root but also one whole sub-tree. We can only do
this if the comparison “speaks for” an entire sub-tree. It can do
so if all elements in one sub-tree are less than or equal to the root
value, and all elements in the other sub-tree are greater than or
equal to it. Of course, we have to be consistent about which side
contains which subset; it is conventional to put the smaller elements
to the left and the bigger ones to the right. This refines our binary
tree definition to give us a binary search tree (BST).

::: {.do-now}
Here is a candiate predicate for recognizing when a binary tree is in
fact a binary search tree:

```jayret
boolean is-a-bst-buggy(BT b) {
    return switch (b) {
        case Leaf: yield true;
        case Node(v, l, r): yield (is-leaf(l) || (l.v <= v)) && (is-leaf(r) || (v <= r.v)) && is-a-bst-buggy(l) && is-a-bst-buggy(r);
    }
}
```
Is this definition correct?
:::

It’s not. To actually throw away half the tree, we need to be sure
that everything in the left sub-tree is less than the value in
the root and similarly, everything in the right sub-tree is greater
than the root.[We have used `<=`{.jayret} instead of `<`{.jayret} above
because even though we don’t want to permit duplicates when
representing sets, in other cases we might not want to be so
stringent; this way we can reuse the above implementation for other
purposes.]{.margin-note} But the definition above performs only a “shallow”
comparison. Thus we could have a root a with a right child,
b, such that b > a; and the b node
could have a left child c such that c < b;
but this does not guarantee that c > a. In fact, it is
easy to construct a counter-example that passes this check:

```jayret
@Check void test() {
    assertSatisfies(node(5, node(3, leaf, node(6, leaf, leaf)), leaf), is-a-bst-buggy);
}
// FALSE!
```

::: {.exercise}
Fix the BST checker.
:::

With a corrected definition, we can now define a refined version of
binary trees that are search trees:

```jayret
type BST = BT % (is-a-bst );
```
We can also remind ourselves that the purpose of this exercise was to
define sets, and define `TSet`{.jayret}s to be tree sets:

```jayret
type TSet = BST;
mt-set = leaf;
```

Now let’s implement our operations on the BST representation. First
we’ll write a template:

```jayret
Bool is-in(int e, BST s) {
    return switch (s) {
        case Leaf: yield ...;
        case Node(v, BST l, BST r): yield block {
            ...;
            ...;
            is-in(l);
            ...;
            ...;
            is-in(r);
            return ...;
        };
    }
}
```
Observe that the data definition of a BST gives us rich information
about the two children: they are each a BST, so we know their
elements obey the ordering property. We can use this to define the
actual operations:

```jayret
boolean is-in(int e, BST s) {
    return switch (s) {
        case Leaf: yield false;
        case Node(v, l, r): yield if (e == v) {
            return true;
        } else if (e < v) {
            return is-in(e, l);
        } else if (e > v) {
            return is-in(e, r);
        };
    }
}
BST insert(int e, BST s) {
    return switch (s) {
        case Leaf: yield node(e, leaf, leaf);
        case Node(v, l, r): yield if (e == v) {
            return s;
        } else if (e < v) {
            return node(v, insert(e, l), r);
        } else if (e > v) {
            return node(v, l, insert(e, r));
        };
    }
}
```
In both functions we are strictly assuming the invariant of
the BST, and in the latter case also ensuring it. Make sure you
identify where, why, and how.

You should now be able to define the remaining operations. Of these,
`size`{.jayret} clearly requires linear time (since it has to count all
the elements), but because `is-in`{.jayret} and `insert`{.jayret} both throw
away one of two children each time they recur, they take logarithmic
time.

::: {.exercise}
Suppose we frequently needed to compute the size of a set. We ought
to be able to reduce the time complexity of `size`{.jayret} by having each
tree [☛ cache](glossary.html#%28elem._glossary-cache%29) its size, so that `size`{.jayret} could
complete in constant time (note that the size of the tree clearly fits
the criterion of a cache, since it can always be reconstructed).
Update the data definition and all affected functions to keep track of
this information correctly.
:::

```{=html}
<a name="(part._Checking-the-Complexity)"></a>
```

#### 18.2.2 Checking the Complexity {#Checking-the-Complexity}

But wait a minute. Are we actually done? Our recurrence takes the
form \(T(k) = T(k/2) + c\), but what in our data definition guaranteed
that the size of the child traversed by `is-in`{.jayret} will be half the
size?

::: {.do-now}
Construct an example—consisting of a sequence of
`insert`{.jayret}s to the empty tree—such that the resulting tree is not
balanced. Show that searching for certain elements in this tree will
take linear, not logarithmic, time in its size.
:::

Imagine starting with the empty tree and inserting the values
`1`{.jayret}, `2`{.jayret}, `3`{.jayret}, and `4`{.jayret}, in order. The
resulting tree would be

```jayret
@Check void test() {
    assertEquals(insert(4, insert(3, insert(2, insert(1, mt-set)))), node(1, leaf, node(2, leaf, node(3, leaf, node(4, leaf, leaf)))));
}
```
Searching for `4`{.jayret} in this tree would have to examine all the set
elements in the tree. In other words, this binary search tree is
degenerate—it is effectively a list, and we are back to having
the same complexity we had earlier.

Therefore, using a binary tree, and even a BST, does not guarantee
the complexity we want: it does only if our inputs have arrived in
just the right order. However, we cannot assume any input ordering;
instead, we would like an implementation that works in all cases.
Thus, we must find a way to ensure that the tree is always
balanced, so each recursive call in `is-in`{.jayret}
really does throw away half the elements.

::: {.exercise}
Observe that we have not talked about computing the size of the set.
Even if we could assume that the binary tree is balanced, how do we
determine the size in logarithmic-or-better time?
:::

```{=html}
<a name="(part._sets-from-balanced-trees)"></a>
```

#### 18.2.3 A Fine Balance: Tree Surgery {#sets-from-balanced-trees}

Let’s define a balanced binary search tree (BBST). It must
obviously be a search tree, so let’s focus on the “balanced” part.
We have to be careful about precisely what this means: we can’t simply
expect both sides to be of equal size because this demands that the
tree (and hence the set) have an even number of elements and, even
more stringently, to have a size that is a power of two.

::: {.exercise}
Define a predicate for a BBST that consumes a `BT`{.jayret} and returns a
`Boolean`{.jayret} indicating whether or not it a balanced search tree.
:::

Therefore, we relax the notion of balance to one that is both
accommodating and sufficient. We use the term balance factor
for a node to refer to the height of its left child minus the height
of its right child (where the height is the depth, in edges, of the
deepest node). We allow every node of a BBST to have a balance
factor of \(-1\), \(0\), or \(1\) (but nothing else): that is, either
both have the same height, or the left or the right can be one taller.
Note that this is a recursive property, but it applies at all levels,
so the imbalance cannot accumulate making the whole tree arbitrarily
imbalanced.

::: {.exercise}
Given this definition of a BBST, show that the number of nodes is
exponential in the height. Thus, always recurring on one branch will
terminate after a logarithmic (in the number of nodes) number of
steps.
:::

Here is an obvious but useful observation: every BBST is also a
BST (this was true by the very definition of a BBST). Why
does this matter? It means that a function that operates on a BST can
just as well be applied to a BBST without any loss of correctness.

So far, so easy. All that leaves is a means of creating a
BBST, because it’s responsible for ensuring balance. It’s easy to
see that the constant `empty-set`{.jayret} is a BBST value. So that
leaves only `insert`{.jayret}.

Here is our situation with `insert`{.jayret}. Assuming we start with a
BBST, we can determine in logarithmic time whether the element is
already in the tree and, if so, ignore it.[To implement a
bag we count how many of each element are in it, which does not
affect the tree’s height.]{.margin-note}
When inserting an element, given balanced trees, the
`insert`{.jayret} for a BST takes only a logarithmic amount of time to
perform the insertion. Thus, if performing the insertion does not
affect the tree’s balance, we’re done. Therefore, we only need to
consider cases where performing the insertion throws off the balance.

Observe that because \(<\) and \(>\) are symmetric (likewise with
\(<=\) and \(>=\)), we can consider insertions into one half of the
tree and a symmetric argument handles insertions into the other half.
Thus, suppose we have a tree that is currently balanced into which we
are inserting the element \(e\). Let’s say \(e\) is going into the
left sub-tree and, by virtue of being inserted, will cause the entire
tree to become imbalanced.[Some trees, like family trees ([Data Design Problem – Ancestry Data](trees.html##ancestor-trees))
represent real-world data. It makes no sense to “balance” a family
tree: it must accurately model whatever reality it represents. These
set-representing trees, in contrast, are chosen by us, not dictated by
some external reality, so we are free to rearrange them.]{.margin-note}

There are two ways to proceed. One is to consider all the places
where we might insert \(e\) in a way that causes an imbalance and
determine what to do in each case.

::: {.exercise}
Enumerate all the cases where insertion might be problematic, and
dictate what to do in each case.
:::

The number of cases is actually quite overwhelming (if you didn’t
think so, you missed a few...). Therefore, we instead attack the
problem after it has occurred: allow the existing BST `insert`{.jayret}
to insert the element, assume that we have an imbalanced tree,
and show how to restore its balance.[The insight that a tree can
be made “self-balancing” is quite remarkable, and there are now many
solutions to this problem. This particular one, one of the oldest, is
due to G.M. Adelson-Velskii and E.M. Landis. In honor of their
initials it is called an AVL Tree, though the tree itself is quite
evident; their genius is in defining re-balancing.]{.margin-note}

Thus, in what follows, we begin with a tree that is balanced;
`insert`{.jayret} causes it to become imbalanced; we have assumed that the
insertion happened in the left sub-tree. In particular, suppose a
(sub-)tree has a balance factor of \(2\) (positive because we’re
assuming the left is imbalanced by insertion). The procedure for
restoring balance depends critically on the following property:

::: {.exercise}
Show that if a tree is currently balanced, i.e., the balance factor at every
node is \(-1\), \(0\), or \(1\), then `insert`{.jayret} can at worst make
the balance factor \(\pm 2\).
:::

The algorithm that follows is applied as `insert`{.jayret} returns from
its recursion, i.e., on the path from the inserted value back to the
root. Since this path is of logarithmic length in the set’s size (due
to the balancing property), and (as we shall see) performs only a
constant amount of work at each step, it ensures that insertion also
takes only logarithmic time, thus completing our challenge.

To visualize the algorithm, let’s use this tree schematic:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt"></span><span class="hspace">    </span><span class="stt">p</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">   </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">  </span><span class="stt">q</span><span class="hspace">   </span><span class="stt">C</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace"> </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt">A</span><span class="hspace">   </span><span class="stt">B</span></p></td></tr></table>
```
Here, \(p\) is the value of the element at the root (though we will
also abuse terminology and use the value at a root to refer to that
whole tree), \(q\) is the value at the root of the left sub-tree (so
\(q < p\)), and \(A\), \(B\), and \(C\) name the respective sub-trees.
We have assumed that \(e\) is being inserted into the left sub-tree,
which means \(e < p\).

Let’s say that \(C\) is of height \(k\). Before insertion, the tree
rooted at \(q\) must have had height \(k+1\) (or else one insertion
cannot create imbalance). In turn, this means \(A\) must have had
height \(k\) or \(k-1\), and likewise for \(B\).

Suppose that after insertion, the tree rooted at \(q\) has height
\(k+2\). Thus, either \(A\) or \(B\) has height \(k+1\) and the other
must have height less than that (either \(k\) or \(k-1\)).


::: {.exercise}
Why can they both not have height \(k+1\) after insertion?
:::


This gives us two cases to consider.

```{=html}
<a name="(part._Left-Left-Case)"></a>
```

##### 18.2.3.1 Left-Left Case {#Left-Left-Case}

Let’s say the imbalance is in \(A\), i.e., it has height \(k+1\).
Let’s expand that tree:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt"></span><span class="hspace">      </span><span class="stt">p</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">     </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">    </span><span class="stt">q</span><span class="hspace">   </span><span class="stt">C</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">   </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">  </span><span class="stt">r</span><span class="hspace">   </span><span class="stt">B</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace"> </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt">A1</span><span class="hspace">  </span><span class="stt">A2</span></p></td></tr></table>
```
We know the following about the data in the sub-trees. We’ll use the
notation \(T < a\) where \(T\) is a tree and \(a\) is a single value
to mean every value in \(T\) is less than \(a\).


- \(A_1 < r\).

- \(r < A_2 < q\).

- \(q < B < p\).

- \(p < C\).

Let’s also remind ourselves of the sizes:


- The height of \(A_1\) or of \(A_2\) is \(k\) (the cause of imbalance).

- The height of the other \(A_i\) is \(k-1\) (see the exercise above).

- The height of \(C\) is \(k\) (initial assumption; \(k\) is arbitrary).

- The height of \(B\) must be \(k-1\) or \(k\) (argued above).

Imagine this tree is a mobile, which has gotten a little skewed to the
left. You would naturally think to suspend the mobile a little
further to the left to bring it back into balance. That is
effectively what we will do:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt"></span><span class="hspace">     </span><span class="stt">q</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">    </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">  </span><span class="stt">r</span><span class="hspace">     </span><span class="stt">p</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace"> </span><span class="stt">/ \</span><span class="hspace">   </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt">A1</span><span class="hspace">  </span><span class="stt">A2 B</span><span class="hspace">  </span><span class="stt">C</span></p></td></tr></table>
```
Observe that this preserves each of the ordering properties above. In
addition, the \(A\) subtree has been brought one level closer to the
root than earlier relative to \(B\) and \(C\). This restores the
balance (as you can see if you work out the heights of each of
\(A_i\), \(B\), and \(C\)). Thus, we have also restored balance.

```{=html}
<a name="(part._Left-Right-Case)"></a>
```

##### 18.2.3.2 Left-Right Case {#Left-Right-Case}

The imbalance might instead be in \(B\). Expanding:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt"></span><span class="hspace">    </span><span class="stt">p</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">   </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">  </span><span class="stt">q</span><span class="hspace">   </span><span class="stt">C</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace"> </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt">A</span><span class="hspace">   </span><span class="stt">r</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">   </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">  </span><span class="stt">B1</span><span class="hspace">  </span><span class="stt">B2</span></p></td></tr></table>
```
Again, let’s record what we know about data order:


- \(A < q\).

- \(q < B_1 < r\).

- \(r < B_2 < p\).

- \(p < C\).

and sizes:


- Suppose the height of \(C\) is \(k\).

- The height of \(A\) must be \(k-1\) or \(k\).

- The height of \(B_1\) or \(B_2\) must be \(k\), but not both
  (see the exercise above). The other must be \(k-1\).

We therefore have to somehow bring \(B_1\) and \(B_2\) one level
closer to the root of the tree. By using the above data ordering
knowledge, we can construct this tree:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt"></span><span class="hspace">      </span><span class="stt">p</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">     </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">    </span><span class="stt">r</span><span class="hspace">   </span><span class="stt">C</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">   </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">  </span><span class="stt">q</span><span class="hspace">   </span><span class="stt">B2</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace"> </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt">A</span><span class="hspace">   </span><span class="stt">B1</span></p></td></tr></table>
```
Of course, if \(B_1\) is the problematic sub-tree, this still does not
address the problem. However, we are now back to the previous
(left-left) case; rotating gets us to:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt"></span><span class="hspace">      </span><span class="stt">r</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">   </span><span class="stt">/</span><span class="hspace">    </span><span class="stt">\</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">  </span><span class="stt">q</span><span class="hspace">      </span><span class="stt">p</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace"> </span><span class="stt">/ \</span><span class="hspace">    </span><span class="stt">/ \</span></p></td></tr><tr><td><p><span class="stt">A</span><span class="hspace">   </span><span class="stt">B1 B2</span><span class="hspace">  </span><span class="stt">C</span></p></td></tr></table>
```
Now observe that we have precisely maintained the data ordering
constraints. Furthermore, from the root, \(A\)’s lowest node is at
height \(k+1\) or \(k+2\); so is \(B_1\)’s; so is \(B_2\)’s; and
\(C\)’s is at \(k+2\).

```{=html}
<a name="(part._Any-Other-Cases)"></a>
```

##### 18.2.3.3 Any Other Cases? {#Any-Other-Cases}

Were we a little too glib before? In the left-right case we said that
only one of \(B_1\) or \(B_2\) could be of height \(k\) (after
insertion); the other had to be of height \(k-1\). Actually, all we
can say for sure is that the other has to be at most height
\(k-2\).

::: {.exercise}
- Can the height of the other tree actually be \(k-2\) instead of
  \(k-1\)?

- If so, does the solution above hold? Is there not still an
  imbalance of two in the resulting tree?

- Is there actually a bug in the above algorithm?
:::
