---
title: Shortest (or Lightest) Paths
section_number: 17.4
source_file: lightest-paths.html
prev: weighted-graphs.html
up: part_graphs.html
next: mst.html
---

```{=html}
<a name="(part._lightest-paths)"></a>
```

### 17.4 Shortest (or Lightest) Paths {#lightest-paths}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td></td></tr></table>
```

Imagine planning a trip: it’s natural that you might want to get to
your destination in the least time, or for the least money, or some
other criterion that involves minimizing the sum of edge
weights. This is known as computing the shortest path.

We should immediately clarify an unfortunate terminological
confusion. What we really want to compute is the lightest
path—the one of least weight. Unfortunately, computer science
terminology has settled on the terminology we use here; just be sure
to not take it literally.

::: {.exercise}
Construct a graph and select a pair of nodes in it such that the
shortest path from one to the other is not the lightest one, and vice
versa.
:::

We have already seen [[Depth- and Breadth-First Traversals](basic-graph-trav.html#dfs-bfs)] that breadth-first search
constructs shortest paths in unweighted graphs. These correspond to
lightest paths when there are no weights (or, equivalently, all
weights are identical and positive). Now we have to generalize this to
the case where the edges have weights.

We will proceed inductively, gradually defining a function seemingly
of this type

```jayret
/* contract: w :: Object */;
```
that reflects the weight of the lightest path from the source node to
that one. But let’s think about this annotation: since we’re building
this up node-by-node, initially most nodes have no weight to report;
and even at the end, a node that is unreachable from the source will
have no weight for a lightest (or indeed, any) path. Rather than make
up a number that pretends to reflect this situation, we will instead
use an option type:

```jayret
/* contract: w :: Object */;
```
When there is `some`{.jayret} value it will be the weight; otherwise the
weight will be `none`{.jayret}.

Now let’s think about this inductively. What do we know initially?
Well, certainly that the source node is at a distance of zero from
itself (that must be the lightest path, because we can’t get any
lighter). This gives us a (trivial) set of nodes for which we already
know the lightest weight. Our goal is to grow this set of
nodes—modestly, by one, on each iteration—until we either find the
destination, or we have no more nodes to add (in which case our
desination is not reachable from the source).

Inductively, at each step we have the set of all nodes for which we
know the lightest path (initially this is just the source node, but it
does mean this set is never empty, which will matter in what we say
next). Now consider all the edges adjacent to this set of nodes
that lead to nodes for which we don’t already know the lightest
path. Choose a node, \(q\), that minimizes the total weight of the
path to it. We claim that this will in fact be the lightest path to
that node.

If this claim is true, then we are done. That’s because we would now add
\(q\) to the set of nodes whose lightest weights we now know, and
repeat the process of finding lightest outgoing edges from there. This
process has thus added one more node. At some point we will find that
there are no edges that lead outside the known set, at which point we
can terminate.

It stands to reason that terminating at this point is safe: it
corresponds to having computed the reachable set. The only thing left
is to demonstrate that this greedy algorithm yields a
lightest path to each node.

We will prove this by contradiction. Suppose we have the path
\(s \rightarrow d\)
from source \(s\) to node \(d\), as found by the algorithm above, but
assume also that we have a different path that is actually lighter.
At every node, when we added a node along the \(s \rightarrow d\)
path, the algorithm would have added a lighter path if it existed. The
fact that it did not falsifies our claim that a lighter path
exists (there could be a different path of the same weight;
this would be permitted by the algorithm, but it also doesn’t
contradict our claim). Therefore the algorithm does indeed find the
lightest path.

What remains is to determine a data structure that enables this
algorithm. At every node, we want to know the least weight from the
set of nodes for which we know the least weight to all their
neighbors. We could achieve this by sorting, but this is overkill: we
don’t actually need a total ordering on all these weights, only the
lightest one. A heap [see Wikipedia](https://en.wikipedia.org/wiki/Heap_(data_structure)) gives us this.

::: {.exercise}
What if we allowed edges of weight zero? What would change in the
above algorithm?
:::

::: {.exercise}
What if we allowed edges of negative weight? What would change in the
above algorithm?[After you’ve thought about this for a while,
take a look at
[this article](https://www.quantamagazine.org/finally-a-fast-algorithm-for-shortest-paths-on-negative-graphs-20230118/).]{.margin-note}
:::

For your reference, this algorithm is known as
Dijkstra’s Algorithm.
