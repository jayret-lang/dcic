---
title: Sharing and Equality
section_number: 16.1
source_file: Sharing_and_Equality.html
prev: part_dags.html
up: part_dags.html
next: size-of-dag.html
---

### 16.1 Sharing and Equality {#Sharing-and-Equality}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Sharing_and_Equality.html#%28part._identical-eq%29">16.1.1<span class="hspace"> </span>Re-Examining Equality</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Sharing_and_Equality.html#%28part._.The_.Cost_of_.Evaluating_.References%29">16.1.2<span class="hspace"> </span>The Cost of Evaluating References</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Sharing_and_Equality.html#%28part._equal-always%29">16.1.3<span class="hspace"> </span>Notations for Equality</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Sharing_and_Equality.html#%28part._.On_the_.Internet__.Nobody_.Knows_.You_re_a_.D.A.G%29">16.1.4<span class="hspace"> </span>On the Internet, Nobody Knows You’re a DAG</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Sharing_and_Equality.html#%28part._.It_s_.Always_.Been_a_.D.A.G%29">16.1.5<span class="hspace"> </span>It’s Always Been a DAG</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="Sharing_and_Equality.html#%28part._acyc-to-cyc%29">16.1.6<span class="hspace"> </span>From Acyclicity to Cycles</a></p></td></tr></table>
```

#### 16.1.1 Re-Examining Equality {#identical-eq}

Consider the following data definition and example values:

```jayret
data BT {
    Leaf;
    Node(v, BT l, BT r);
}
a-tree = node(5, node(4, leaf, leaf), node(4, leaf, leaf));
b-tree = block: four-node = node(4, leaf, leaf);
node(5, four-node, four-node);
```
In particular, it might seem that the way we’ve written `b-tree`{.pyret}
is morally equivalent to how we’ve written `a-tree`{.pyret}, but we’ve
created a helpful binding to avoid code duplication.

Because both `a-tree`{.pyret} and `b-tree`{.pyret} are bound to trees with
`5`{.pyret} at the root and a left and right child each containing
`4`{.pyret}, we can indeed reasonably consider these trees
equivalent. Sure enough:
<equal-tests> ::=
```jayret
@Check void test() {
    assertEquals(a-tree, b-tree);
    assertEquals(a-tree.l, a-tree.l);
    assertEquals(a-tree.l, a-tree.r);
    assertEquals(b-tree.l, b-tree.r);
}
```

However, there is another sense in which these trees are not
equivalent. concretely, `a-tree`{.pyret} constructs a distinct node for
each child, while `b-tree`{.pyret} uses the same node for both
children. Surely this difference should show up somehow, but we
have not yet seen a way to write a program that will tell these
apart.

By default, the `is`{.pyret} operator uses the same equality test as
Jayret’s `==`{.pyret}. There are, however, other equality tests in
Jayret. In particular, the way we can tell apart these data is by using
Jayret’s `identical`{.pyret} function, which implements
reference equality. This checks not only whether two
values are structurally equivalent but whether they are
the result of the very same act of value construction.
With this, we can now write additional tests:

```jayret
@Check void test() {
    assertEquals(identical(a-tree, b-tree), false);
    assertEquals(identical(a-tree.l, a-tree.l), true);
    assertEquals(identical(a-tree.l, a-tree.r), false);
    assertEquals(identical(b-tree.l, b-tree.r), true);
}
```

Let’s step back for a moment and consider the behavior that gives us this
result. We can visualize the different values by putting each distinct value
in a separate location alongside the running program. We can draw the
first step as creating a `node`{.pyret} with value `4`{.pyret}:

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">a-tree =
  node(5,
    <span class="heapref sink">1001</span>,
    node(4, leaf, leaf))

b-tree =
  block:
    four-node = node(4, leaf, leaf)
    node(5,
      four-node,
      four-node)
  end</code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

The next step creates another node with value `4`{.pyret}, distinct from the
first:

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">a-tree =
  node(5, <span class="heapref sink">1001</span>, <span class="heapref sink">1002</span>)

b-tree =
  block:
    four-node = node(4, leaf, leaf)
    node(5,
      four-node,
      four-node)
  end</code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1002</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

Then the `node`{.pyret} for `a-tree`{.pyret} is created:

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">a-tree = <span class="heapref sink">1003</span>

b-tree =
  block:
    four-node = node(4, leaf, leaf)
    node(5,
      four-node,
      four-node)
  end</code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1002</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1003</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1001</span>, <span class="heapref sink">1002</span>)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

When evaluating the `block`{.pyret} for `b-tree`{.pyret}, first a single node is
created for the `four-node`{.pyret} binding:

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">a-tree = <span class="heapref sink">1003</span>

b-tree =
  block:
    four-node = <span class="heapref sink">1004</span>
    node(5,
      four-node,
      four-node)
  end</code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1002</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1003</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1001</span>, <span class="heapref sink">1002</span>)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1004</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

These location values can be substituted just like any other, so they get
substituted for `four-node`{.pyret} to continue evaluation of the
block.[We skipped substituting `a-tree`{.pyret} for the moment, that
will come up later.]{.margin-note}

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">a-tree = <span class="heapref sink">1003</span>

b-tree =
  block:
    node(5, <span class="heapref sink">1004</span>, <span class="heapref sink">1004</span>)
  end</code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1002</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1003</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1001</span>, <span class="heapref sink">1002</span>)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1004</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

Finally, the node for `b-tree`{.pyret} is created:

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">a-tree = <span class="heapref sink">1003</span>

b-tree = <span class="heapref sink">1005</span></code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1002</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1003</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1001</span>, <span class="heapref sink">1002</span>)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1004</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1005</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1004</span>, <span class="heapref sink">1004</span>)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

This visualization can help us explain the test we wrote using `identical`{.pyret}.
Let’s consider the test with the appropriate location references substituted
for `a-tree`{.pyret} and `b-tree`{.pyret}:

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">check:
  identical(<span class="heapref sink">1003</span>, <span class="heapref sink">1005</span>)
    is false
  identical(<span class="heapref sink">1003</span>.l, <span class="heapref sink">1003</span>.l)
    is true
  identical(<span class="heapref sink">1003</span>.l, <span class="heapref sink">1003</span>.r)
    is false
  identical(<span class="heapref sink">1005</span>.l, <span class="heapref sink">1005</span>.r)
    is true
end</code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1002</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1003</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1001</span>, <span class="heapref sink">1002</span>)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1004</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1005</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1004</span>, <span class="heapref sink">1004</span>)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

```{=html}
<div class="HeapExpr"><div class="ExprPart"><pre class="HeapCode"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">check:
  identical(<span class="heapref sink">1003</span>, <span class="heapref sink">1005</span>)
    is false
  identical(<span class="heapref sink">1001</span>, <span class="heapref sink">1001</span>)
    is true
  identical(<span class="heapref sink">1001</span>, <span class="heapref sink">1004</span>)
    is false
  identical(<span class="heapref sink">1004</span>, <span class="heapref sink">1004</span>)
    is true
end</code></pre></div></div></p></pre></div><div class="HeapPart"><p>Heap</p><ul><li><p><div class="SIntrapara"><span class="heapref source">1001</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1002</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1003</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1001</span>, <span class="heapref sink">1002</span>)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1004</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(4, leaf, leaf)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><span class="heapref source">1005</span>:<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">node(5, <span class="heapref sink">1004</span>, <span class="heapref sink">1004</span>)</code></pre></div></div></p></div></p></li></ul></div><div class="clear"></div></div>
```

There is actually another way to write these tests in Jayret: the
`is`{.pyret} operator can also be parameterized by a different equality
predicate than the default `==`{.pyret}. Thus, the above block can
equivalently be written as:[We can use `is-not`{.pyret}
to check for expected failure of equality.]{.margin-note}

```jayret
@Check void test() {
    assertNotEquals(a-tree, b-tree);
    assertEquals(a-tree.l, a-tree.l);
    assertNotEquals(a-tree.l, a-tree.r);
    assertEquals(b-tree.l, b-tree.r);
}
```
We will use this style of equality testing from now on.

Observe how these are the same values that were compared earlier
([<equal-tests>](Sharing_and_Equality.html#%28elem._equal-tests%29)), but the results are now different: some
values that were true earlier are now false. In particular,

```jayret
@Check void test() {
    assertEquals(a-tree, b-tree);
    assertNotEquals(a-tree, b-tree);
    assertEquals(a-tree.l, a-tree.r);
    assertNotEquals(a-tree.l, a-tree.r);
}
```
Later we will return both to
what `identical`{.pyret} really means
[[Understanding Equality](unified-equality.html)]
(Jayret has a full range of equality operations suitable for different situations).

::: {.exercise}
There are many more equality tests we can and should perform
even with the basic data above to make sure we really understand
equality and, relatedly, storage of data in memory. What other
tests should we conduct? Predict what results they should produce
before running them!
:::

#### 16.1.2 The Cost of Evaluating References {#The-Cost-of-Evaluating-References}

From a complexity viewpoint, it’s important for us to understand how
these references work. As we have hinted, `four-node`{.pyret} is computed
only once, and each use of it refers to the same value: if, instead,
it was evaluated each time we referred to `four-node`{.pyret}, there
would be no real difference between `a-tree`{.pyret} and `b-tree`{.pyret},
and the above tests would not distinguish between them.

This is especially relevant when understanding the cost of function
evaluation. We’ll construct two simple examples that illustrate
this. We’ll begin with a contrived data structure:

```jayret
L = range(0, 100);
```

Suppose we now define

```jayret
L1 = link(1, L);
L2 = link(-1, L);
```
Constructing a list clearly takes time at least proportional to the
length; therefore, we expect the time to compute `L`{.pyret} to be
considerably more than that for a single `link`{.pyret}
operation. Therefore, the question is how long it takes to compute
`L1`{.pyret} and `L2`{.pyret} after `L`{.pyret} has been computed: constant
time, or time proportional to the length of `L`{.pyret}?

The answer, for Jayret, and for most other contemporary languages
(including Java, C#, OCaml, Racket, etc.), is that these additional
computations take constant time. That is, the value bound to
`L`{.pyret} is computed once and bound to `L`{.pyret}; subsequent
expressions refer to this value (hence “reference”)
rather than reconstructing it, as reference equality shows:

```jayret
@Check void test() {
    assertEquals(L1.rest, L);
    assertEquals(L2.rest, L);
    assertEquals(L1.rest, L2.rest);
}
```

Similarly, we can define a function, pass `L`{.pyret} to it, and see
whether the resulting argument is `identical`{.pyret} to the original:

```jayret
Object check-for-no-copy(another-l) {
    return identical(another-l, L);
}
@Check void test() {
    assertEquals(check-for-no-copy(L), true);
}
```
or, equivalently,

```jayret
@Check void test() {
    assertSatisfies(L, check-for-no-copy);
}
```
Therefore, neither built-in operations (like `.rest`{.pyret}) nor
user-defined ones (like `check-for-no-copy`{.pyret}) make copies of their
arguments.[Strictly speaking, of course, we cannot
conclude that no copy was made. Jayret could have made a copy,
discarded it, and still passed a reference to the original. Given how
perverse this would be, we can assume—and take the language’s
creators’ word for it—that this doesn’t actually happen. By creating
extremely large lists, we can also use timing information to observe
that the time of constructing the list grows proportional to the
length of the list while the time of passing it as a parameter remains
constant.]{.margin-note} The important thing to observe here is that, instead of
simply relying on authority, we have used operations in the
language itself to understand how the language behaves.

#### 16.1.3 Notations for Equality {#equal-always}

Until now we have used `==`{.pyret} for equality. Now we have learned that it’s
only one of multiple equality operators, and that there is another one called
`identical`{.pyret}. However, these two have somewhat subtly different syntactic
properties. `identical`{.pyret} is a name for a function, which can
therefore be used to refer to it like any other function (e.g., when we need to
mention it in a `is-not`{.pyret} clause). In contrast, `==`{.pyret} is a binary
operator, which can only be used in the middle of expressions.

This should naturally make us wonder about the other two possibilities: a
binary expression version of `identical`{.pyret} and a function name equivalent of
`==`{.pyret}. They do, in fact, exist! The operation performed by `==`{.pyret} is
called `equal-always`{.pyret}. Therefore, we can write the first block of tests
equivalently, but more explicitly, as

```jayret
@Check void test() {
    assertEquals(a-tree, b-tree);
    assertEquals(a-tree.l, a-tree.l);
    assertEquals(a-tree.l, a-tree.r);
    assertEquals(b-tree.l, b-tree.r);
}
```
Conversely, the binary operator notation for `identical`{.pyret} is `<=>`{.pyret}.
Thus, we can equivalently write `check-for-no-copy`{.pyret} as

```jayret
Object check-for-no-copy(another-l) {
    return another-l <=> L;
}
```

#### 16.1.4 On the Internet, Nobody Knows You’re a DAG {#On-the-Internet-Nobody-Knows-You-re-a-D-A-G}

Despite the name we’ve given it, `b-tree`{.pyret} is not actually a
tree. In a tree, by definition, there are no shared nodes,
whereas in `b-tree`{.pyret} the node named by `four-node`{.pyret} is shared
by two parts of the tree. Despite this, traversing `b-tree`{.pyret} will
still terminate, because there are no cyclic references in it:
if you start from any node and visit its “children”, you cannot end
up back at that node. There is a special name for a value with such a
shape: directed acyclic graph (DAG).

Many important data structures are actually a DAG underneath. For
instance, consider Web sites. It is common to think of a site as a
tree of pages: the top-level refers to several sections, each of which
refers to sub-sections, and so on. However, sometimes an entry needs
to be cataloged under multiple sections. For instance, an academic
department might organize pages by people, teaching, and research. In
the first of these pages it lists the people who work there; in the
second, the list of courses; and in the third, the list of research
groups. In turn, the courses might have references to the people
teaching them, and the research groups are populated by these same
people. Since we want only one page per person (for both maintenance
and search indexing purposes), all these personnel links refer back to
the same page for people.

Let’s construct a simple form of this. First a datatype to represent a
site’s content:

```jayret
data Content {
    Page(String s);
    Section(String title, List<Object> sub);
}
```
Let’s now define a few people:

```jayret
people-pages = section("People", [page("Church"), page("Dijkstra"), page("Hopper")]);
```
and a way to extract a particular person’s page:

```jayret
Object get-person(n) {
    return get(people-pages.sub, n);
}
```
Now we can define theory and systems sections:

```jayret
theory-pages = section("Theory", [get-person(0), get-person(1)]);
systems-pages = section("Systems", [get-person(1), get-person(2)]);
```
which are integrated into a site as a whole:

```jayret
site = section("Computing Sciences", [theory-pages, systems-pages]);
```
Now we can confirm that each of these luminaries needs to keep only
one Web page current; for instance:

```jayret
@Check void test() {
    theory = get(site.sub, 0);
    systems = get(site.sub, 1);
    theory-dijkstra = get(theory.sub, 1);
    systems-dijkstra = get(systems.sub, 0);
    assertEquals(theory-dijkstra, systems-dijkstra);
    assertEquals(theory-dijkstra, systems-dijkstra);
}
```

#### 16.1.5 It’s Always Been a DAG {#It-s-Always-Been-a-D-A-G}

What we may not realize is that we’ve actually been creating a DAG for longer
than we think. To see this, consider `a-tree`{.pyret}, which very clearly seems to
be a tree. But look more closely not at the `node`{.pyret}s but rather at the
`leaf`{.pyret}(s). How many actual `leaf`{.pyret}s do we create?

One hint is that we don’t seem to call a function when creating a `leaf`{.pyret}:
the data definition does not list any fields, and when constructing a
`BT`{.pyret} value, we simply write `leaf`{.pyret}, not (say)
`leaf()`{.pyret}. Still, it would be nice to know what is happening behind the
scenes. To check, we can simply ask Jayret:

```jayret
@Check void test() {
    assertEquals(leaf, leaf);
}
```
[It’s important that we not write `leaf <=> leaf`{.pyret} here, because
that is just an expression whose result is ignored. We have to write `is`{.pyret}
to register this as a test whose result is checked and reported.]{.margin-note}
and this check passes. That is, when we write a variant without any
fields, Jayret automatically creates a singleton: it makes just one
instance and uses that instance everywhere. This leads to a more efficient
memory representation, because there is no reason to have lots of distinct
`leaf`{.pyret}s each taking up their own memory. However, a subtle consequence of
that is that we have been creating a DAG all along.

If we really wanted each `leaf`{.pyret} to be distinct, it’s easy: we can write

```jayret
data BTDistinct {
    Leaf();
    Node(v, BTDistinct l, BTDistinct r);
}
```
Then we would need to use the `leaf`{.pyret} function everywhere:

```jayret
c-tree = node(5, node(4, leaf(), leaf()), node(4, leaf(), leaf()));
```
And sure enough:

```jayret
@Check void test() {
    assertNotEquals(leaf(), leaf());
}
```

#### 16.1.6 From Acyclicity to Cycles {#acyc-to-cyc}

Here’s another example that arises on the Web. Suppose we are
constructing a table of output in a Web page. We would like the rows
of the table to alternate between white and grey. If the table had
only two rows, we could map the row-generating function over a list of
these two colors. Since we do not know how many rows it will have,
however, we would like the list to be as long as necessary. In effect,
we would like to write:

```jayret
web-colors = link("white", link("grey", web-colors));
```
to obtain an indefinitely long list, so that we could eventually write

```jayret
map2(color-table-row, table-row-content, web-colors);
```
which applies a `color-table-row`{.pyret} function to two arguments: the
current row from `table-row-content`{.pyret}, and the current color from
`web-colors`{.pyret}, proceeding in lockstep over the two lists.

Unfortunately, there are many things wrong with this attempted
definition.

::: {.do-now}
Do you see what they are?
:::

Here are some problems in turn:


- This will not even parse. The identifier `web-colors`{.pyret} is
  not bound on the right of the `=`{.pyret}.
- Earlier, we saw a solution to such a problem: use `rec`{.pyret}
  [[Streams From Functions](func-as-data.html##streams-from-funs)]. What happens if we write
  
  ```jayret
rec web-colors = link("white", link("grey", web-colors));
  ```
  instead?
  
  
  
  ::: {.exercise}
  Why does `rec`{.pyret} work in the definition of `ones`{.pyret} but not above?
  :::
- Assuming we have fixed the above problem, one of two things will
  happen. It depends on what the initial value of `web-colors`{.pyret}
  is. Because it is a dummy value, we do not get an arbitrarily long
  list of colors but rather a list of two colors followed by the dummy
  value. Indeed, this program will not even type-check.
  
  Suppose, however, that `web-colors`{.pyret} were written instead as a
  function definition to delay its creation:
  
  ```jayret
Object web-colors() {
    return link("white", link("grey", web-colors()));
}
  ```
  On its own this just defines a function. If, however, we use
  it—`web-colors()`{.pyret}—it goes into an infinite loop constructing
  `link`{.pyret}s.
- Even if all that were to work, `map2`{.pyret} would either (a) not
  terminate because its second argument is indefinitely long, or (b)
  report an error because the two arguments aren’t the same length.

All these problems are symptoms of a bigger issue. What we are trying
to do here is not merely create a shared datum (like a DAG) but
something much richer: a cyclic datum, i.e., one that refers
back to itself:

![image](pict_4.png){width="108" height="108"}

When you get to cycles, even defining the datum becomes difficult
because its definition depends on itself so it (seemingly) needs to
already be defined in the process of being defined. We will return to
cyclic data later in [Cyclic Data](unified-cyclic-data.html), and to this
specific example in [Recursion and Cycles from Mutation](rec-from-mut.html).
