---
title: Basic Graph Traversals
section_number: 17.2
source_file: basic-graph-trav.html
prev: intro-graphs.html
up: part_graphs.html
next: weighted-graphs.html
---

### 17.2 Basic Graph Traversals {#basic-graph-trav}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="basic-graph-trav.html#%28part._.Reachability%29">17.2.1<span class="hspace"> </span>Reachability</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="basic-graph-trav.html#%28part._.Simple_.Recursion%29">17.2.1.1<span class="hspace"> </span>Simple Recursion</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="basic-graph-trav.html#%28part._.Cleaning_up_the_.Loop%29">17.2.1.2<span class="hspace"> </span>Cleaning up the Loop</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="basic-graph-trav.html#%28part._.Traversal_with_.Memory%29">17.2.1.3<span class="hspace"> </span>Traversal with Memory</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="basic-graph-trav.html#%28part._.A_.Better_.Interface%29">17.2.1.4<span class="hspace"> </span>A Better Interface</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="basic-graph-trav.html#%28part._dfs-bfs%29">17.2.2<span class="hspace"> </span>Depth- and Breadth-First Traversals</a></p></td></tr></table>
```

As with all the data we have seen so far, to process a datum we have
to traverse it—i.e., visit the constituent data. With graphs, that
can be quite interesting!

#### 17.2.1 Reachability {#Reachability}

Many uses of graphs need to address reachability: whether we
can, using edges in the graph, get from one node to another. For
instance, a social network might suggest as contacts all those who are
reachable from existing contacts. On the Internet, traffic engineers
care about whether packets can get from one machine to another. On the
Web, we care about whether all public pages on a site are reachable
from the home page. We will study how to compute reachability using
our travel graph as a running example.

##### 17.2.1.1 Simple Recursion {#Simple-Recursion}

At its simplest, reachability is easy. We want to know whether there
exists a path[A path is a sequence of zero or more
linked edges.]{.margin-note} between a pair of nodes, a source and a destination. (A
more sophisticated version of reachability might compute the actual
path, but we’ll ignore this for now.) There are two possibilities: the
source and destintion nodes are the same, or they’re not.


- If they are the same, then clearly reachability is trivially
  satisfied.
- If they are not, we have to iterate through the neighbors
  of the source node and ask whether the destination is reachable from
  each of those neighbors.

This translates into the following function:
<graph-reach-1-main> ::=
```pyret
# TODO(pyret2jayret): parse failed (no shifts)
fun reach-1(src :: Key, dst :: Key, g :: Graph) -> Boolean:
  if src == dst:
    true
  else:
    <graph-reach-1-loop>
    loop(neighbors(src, g))
  end
end
```
where the loop through the neighbors of `src`{.pyret} is:
<graph-reach-1-loop> ::=
```jayret
Object loop(ns) {
    return switch (ns) {
        case Empty: yield false;
        case Link(f, r): yield if (reach-1(f, dst, g)) {
            return true;
        } else {
            return loop(r);
        };
    }
}
```
We can test this as follows:
<graph-reach-tests> ::=
```jayret
@Check void test() {
    reach = reach-1;
    assertEquals(reach("was", "was", kn-cities), true);
    assertEquals(reach("was", "chi", kn-cities), true);
    assertEquals(reach("was", "bmg", kn-cities), false);
    assertEquals(reach("was", "hou", kn-cities), true);
    assertEquals(reach("was", "den", kn-cities), true);
    assertEquals(reach("was", "saf", kn-cities), true);
}
```
Unfortunately, we don’t find out about how these tests fare, because
some of them don’t complete at all. That’s because we have an infinite
loop, due to the cyclic nature of graphs!

::: {.exercise}
Which of the above examples leads to a cycle? Why?
:::

##### 17.2.1.2 Cleaning up the Loop {#Cleaning-up-the-Loop}

Before we continue, let’s try to improve the expression of the
loop. While the nested function above is a perfectly reasonable
definition, we can use Jayret’s `for`{.pyret} to improve its readability.

The essence of the above loop is to iterate over a list of boolean
values; if one of them is true, the entire loop evaluates to true; if
they are all false, then we haven’t found a path to the destination
node, so the loop evaluates to false. Thus:

```jayret
Object ormap(fun-body, l) {
    return switch (l) {
        case Empty: yield false;
        case Link(f, r): yield if (fun-body(f)) {
            return true;
        } else {
            return ormap(fun-body, r);
        };
    }
}
```
With this, we can replace the loop definition and use with:

```jayret
[for ormap(n : neighbors(src, g)) { yield reach-1(n, dst, g); }];
```

##### 17.2.1.3 Traversal with Memory {#Traversal-with-Memory}

Because we have cyclic data, we have to remember what nodes we’ve
already visited and avoid traversing them again. Then, every time we
begin traversing a new node, we add it to the set of nodes we’ve
already started to visit so that. If we return to that node, because
we can assume the graph has not changed in the meanwhile, we know that
additional traversals from that node won’t make any difference to the
outcome.[This property is known as
[☛ idempotence](glossary.html#%28elem._glossary-idempotence%29).]{.margin-note}

We therefore define a second attempt at reachability that take an
extra argument: the set of nodes we have begun visiting (where the set
is represented as a graph). The key difference from
[<graph-reach-1-main>](basic-graph-trav.html#%28elem._graph-reach-1-main%29) is, before we begin to traverse
edges, we should check whether we’ve begun processing the node or
not. This results in the following definition:
<graph-reach-2> ::=
```jayret
boolean reach-2(Key src, Key dst, Graph g, List<Object> visited) {
    return if (visited.member(src)) {
        return false;
    } else if (src == dst) {
        return true;
    } else {
        new-visited = link(src, visited);
        return [for ormap(n : neighbors(src, g)) { yield reach-2(n, dst, g, new-visited); }];
    }
}
```
In particular, note the extra new conditional: if the reachability
check has already visited this node before, there is no point
traversing further from here, so it returns
`false`{.pyret}. (There may still be other parts of the graph to explore,
which other recursive calls will do.)

::: {.exercise}
Does it matter if the first two conditions were swapped, i.e., the
beginning of `reach-2`{.pyret} began with

```pyret
# TODO(pyret2jayret): parse failed (no shifts)
if src == dst:
  true
else if visited.member(src):
  false
```
? Explain concretely with examples.
:::

::: {.exercise}
We repeatedly talk about remembering the nodes that we have
begun to visit, not the ones we’ve finished
visiting. Does this distinction matter? How?
:::

##### 17.2.1.4 A Better Interface {#A-Better-Interface}

As the process of testing `reach-2`{.pyret} shows, we may have a better
implementation, but we’ve changed the function’s interface; now it has
a needless extra argument, which is not only a nuisance but might also
result in errors if we accidentally misuse it. Therefore, we should
clean up our definition by moving the core code to an internal
function:

```jayret
boolean reach-3(Key s, Key d, Graph g) {
    boolean reacher(Key src, Key dst, List<Object> visited) {
        return if (visited.member(src)) {
            return false;
        } else if (src == dst) {
            return true;
        } else {
            new-visited = link(src, visited);
            return [for ormap(n : neighbors(src, g)) { yield reacher(n, dst, new-visited); }];
        }
    }
    return reacher(s, d, empty);
}
```
We have now restored the original interface while correctly
implementing reachability.

::: {.exercise}
Does this really gives us a correct implementation? In particular,
does this address the problem that the `size`{.pyret} function above
addressed? Create a test case that demonstrates the problem, and then
fix it.
:::

#### 17.2.2 Depth- and Breadth-First Traversals {#dfs-bfs}

[It is
conventional for computer science texts to call these depth- and
breadth-first search. However, searching is just a specific
purpose; traversal is a general task that can be used for many
purposes.]{.margin-note}

The reachability algorithm we have seen above has a special
property. At every node it visits, there is usually a set of adjacent
nodes at which it can continue the traversal. It has at least two
choices: it can either visit each immediate neighbor first, then visit
all of the neighbors’ neighbors; or it can choose a neighbor, recur,
and visit the next immediate neighbor only after that visit is
done. The former is known as breadth-first traversal, while the
latter is depth-first traversal.

The algorithm we have designed uses a depth-first strategy: inside
[<graph-reach-1-loop>](basic-graph-trav.html#%28elem._graph-reach-1-loop%29), we recur on the first element of the
list of neighbors before we visit the second neighbor, and so on. The
alternative would be to have a data structure into which we insert all
the neighbors, then pull out an element at a time such that we first
visit all the neighbors before their neighbors, and so on. This
naturally corresponds to a queue
[[An Example: Queues from Lists](amortized-analysis.html##queue-data-structure)].

::: {.exercise}
Using a queue, implement breadth-first traversal.
:::

If we correctly check to ensure we don’t re-visit nodes, then both
breadth- and depth-first traversal will properly visit the entire
reachable graph without repetition (and hence not get into an infinite
loop). Each one traverses from a node only once, from which it
considers every single edge. Thus, if a graph has \(N\) nodes and
\(E\) edges, then a lower-bound on the complexity of traversal is
\(O([N, E \rightarrow N + E])\). We must also consider the cost of checking whether we
have already visited a node before (which is a set membership problem,
which we address elsewhere: [Several Variations on Sets](part_sets.html)). Finally, we have to
consider the cost of maintaining the data structure that keeps track
of our traversal. In the case of depth-first traversal,
recursion—which uses the machine’s stack—does it
automatically at constant overhead. In the case of breadth-first
traversal, the program must manage the queue, which can add more than
constant overhead.[In practice, too, the stack will
usually perform much better than a queue, because it is supported by
machine hardware.]{.margin-note}

This would suggest that depth-first traversal is always better than
breadth-first traversal. However, breadth-first traversal has one very
important and valuable property. Starting from a node \(N\), when it
visits a node \(P\), count the number of edges taken to get to
\(P\). Breadth-first traversal guarantees that there cannot have been
a shorter path to \(P\): that is, it finds a shortest path to
\(P\).

::: {.exercise}
Why “a” rather than “the” shortest path?
:::

::: {.exercise}
Prove that breadth-first traversal finds a shortest path.
:::
