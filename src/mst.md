---
title: Moravian Spanning Trees
section_number: 17.5
source_file: mst.html
prev: lightest-paths.html
up: part_graphs.html
next: part_sets.html
---

### 17.5 Moravian Spanning Trees {#mst}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mst.html#%28part._.The_.Problem%29">17.5.1<span class="hspace"> </span>The Problem</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mst.html#%28part._.A_.Greedy_.Solution%29">17.5.2<span class="hspace"> </span>A Greedy Solution</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mst.html#%28part._.Another_.Greedy_.Solution%29">17.5.3<span class="hspace"> </span>Another Greedy Solution</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mst.html#%28part._.A_.Third_.Solution%29">17.5.4<span class="hspace"> </span>A Third Solution</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mst.html#%28part._union-find-functional%29">17.5.5<span class="hspace"> </span>Checking Component Connectedness</a></p></td></tr></table>
```

At the turn of the milennium, the US National Academy of Engineering
surveyed its members to determine the “Greatest Engineering
Achievements of the 20th Century”. The list contained the usual
suspects: electronics, computers, the Internet, and so on. But a
perhaps surprising idea topped the list: (rural)
electrification.[Read more about it
[on their site](http://www.greatachievements.org/).]{.margin-note}

#### 17.5.1 The Problem {#The-Problem}

To understand the history of national electrical grids, it helps to go
back to [Moravia](http://en.wikipedia.org/wiki/Moravia)
in the 1920s. Like many parts of the world, it was beginning to
realize the benefits of electricity and intended to spread it around
the region. A Moravian academia named Otakar Borůvka heard about the
problem, and in a remarkable effort, described the problem abstractly,
so that it could be understood without reference to Moravia or
electrical networks. He modeled it as a problem about graphs.

Borůvka observed that at least initially, any solution to the problem
of creating a network must have the following characteristics:


- The electrical network must reach all the towns intended to be
  covered by it. In graph terms, the solution must be spanning,
  meaning it must visit every node in the graph.
- Redundancy is a valuable property in any network: that way, if
  one set of links goes down, there might be another way to get a
  payload to its destination. When starting out, however, redundancy
  may be too expensive, especially if it comes at the cost of not
  giving someone a payload at all. Thus, the initial solution was best
  set up without loops or even redundant paths. In graph terms, the
  solution had to be a tree.
- Finally, the goal was to solve this problem for the least cost
  possible. In graph terms, the graph would be weighted, and the
  solution had to be a minimum.

Thus Borůvka defined the Moravian Spanning Tree (MST) problem.

#### 17.5.2 A Greedy Solution {#A-Greedy-Solution}

Borůvka had published his problem, and another Czech mathematician,
[Vojtěch Jarník](http://en.wikipedia.org/wiki/Vojt%C4%9Bch_Jarn%C3%ADk),
came across it. Jarník came up with a solution that should sound
familiar:


- Begin with a solution consisting of a single node, chosen
  arbitrarily. For the graph consisting of this one node, this
  solution is clearly a minimum, spanning, and a tree.
- Of all the edges incident on nodes in the solution that
  connect to a node not already in the solution, pick the edge with
  the least weight.[Note that we consider only the
  incident edges, not their weight added to the weight of the node to
  which they are incident.]{.margin-note}
- Add this edge to the solution. The claim is that for the new
  solution will be a tree (by construction), spanning (also by
  construction), and a minimum. The minimality follows by an argument
  similar to that used for Dijkstra’s Algorithm.

Jarník had the misfortune of publishing this work in Czech in 1930,
and it went largely ignored. It was rediscovered by others, most
notably by R.C. Prim in 1957, and is now generally known as
Prim’s Algorithm, though calling it Jarník’s Algorithm
would attribute credit in the right place.

Implementing this algorithm is pretty easy. At each point, we need to
know the lightest edge incident on the current solution tree. Finding
the lightest edge takes time linear in the number of these edges, but
the very lightest one may create a cycle. We therefore need to
efficiently check for whether adding an edge would create a cycle, a
problem we will return to multiple times [[Checking Component Connectedness](mst.html##union-find-functional)].
Assuming we can do
that effectively, we then want to add the lightest edge and
iterate. Even given an efficient solution for checking cyclicity, this
would seem to require an operation linear in the number of edges for
each node. With better representations we can improve on this
complexity, but let’s look at other ideas first.

#### 17.5.3 Another Greedy Solution {#Another-Greedy-Solution}

Recall that Jarník presented his algorithm in 1930, when computers
didn’t exist, and Prim his in 1957, when they were very much in their
infancy. Programming computers to track heaps was a non-trivial
problem, and many algorithms were implemented by hand, where keeping
track of a complex data structure without making errors was harder
still. There was need for a solution that was required less manual
bookkeeping (literally speaking).

In 1956,
[Joseph Kruskal](http://en.wikipedia.org/wiki/Joseph_Kruskal)
presented such a solution. His idea was elegantly simple. The Jarník
algorithm suffers from the problem that each time the tree grows, we
have to revise the content of the heap, which is already a messy
structure to track. Kruskal noted the following.

To obtain a minimum solution, surely we want to include one of the
edges of least weight in the graph. Because if not, we can take an
otherwise minimal solution, add this edge, and remove one other edge;
the graph would still be just as connected, but the overall weight
would be no more and, if the removed edge were heavier, would be
less.[Note the careful wording: there may be many edges
of the same least weight, so adding one of them may remove another,
and therefore not produce a lighter tree; but the key point is that it
certainly will not produce a heavier one.]{.margin-note} By the same argument we can
add the next lightest edge, and the next lightest, and so on. The only
time we cannot add the next lightest edge is when it would create a
cycle (that problem again!).

Therefore, Kruskal’s algorithm is utterly straightforward. We first
sort all the edges, ordered by ascending weight. We then take each
edge in ascending weight order and add it to the solution provided it
will not create a cycle. When we have thus processed all the edges, we
will have a solution that is a tree (by construction), spanning
(because every connected vertex must be the endpoint of some edge),
and of minimum weight (by the argument above). The complexity is that
of sorting (which is \([e \rightarrow e \log e]\) where \(e\) is the
size of the edge set. We then iterate over each element in \(e\),
which takes time linear in the size of that set—modulo the time to
check for cycles. This algorithm is also easy to implement on paper,
because we sort all the edges once, then keep checking them off in
order, crossing out the ones that create cycles—with no dynamic
updating of the list needed.

#### 17.5.4 A Third Solution {#A-Third-Solution}

Both the Jarník and Kruskal solutions have one flaw: they require a
centralized data structure (the priority heap, or the sorted list) to
incrementally build the solution. As parallel computers became
available, and graph problems grew large, computer scientists looked
for solutions that could be implemented more efficiently in
parallel—which typically meant avoiding any centralized points of
synchronization, such as these centralized data structures.

In 1965, M. Sollin constructed an algorithm that met these needs
beautifully. In this algorithm, instead of constructing a single
solution, we grow multiple solution components (potentially in
parallel if we so wish). Each node starts out as a solution component
(as it was at the first step of Jarník’s Algorithm). Each node
considers the edges incident to it, and picks the lightest one that
connects to a different component (that problem again!). If
such an edge can be found, the edge becomes part of the solution, and
the two components combine to become a single component. The entire
process repeats.

Because every node begins as part of the solution, this algorithm
naturally spans. Because it checks for cycles and avoids them, it
naturally forms a tree.[Note that avoiding cycles yields
a DAG and is not automatically guaranteed to yield a tree. We have
been a bit lax about this difference throughout this section.]{.margin-note}
Finally, minimality follows through similar reasoning as we used in
the case of Jarník’s Algorithm, which we have essentially run in
parallel, once from each node, until the parallel solution components
join up to produce a global solution.

Of course, maintaining the data for this algorithm by hand is a
nightmare. Therefore, it would be no surprise that this algorithm was
coined in the digital age. The real surprise, therefore, is that it
was not: it was originally created by
[Otakar Borůvka](http://en.wikipedia.org/wiki/Otakar_Bor%C5%AFvka)
himself.

Borůvka, you see, had figured it all out. He’d not only understood the
problem, he had:


- pinpointed the real problem lying underneath the
  electrification problem so it could be viewed in a
  context-independent way,
- created a descriptive language of graph theory to define it
  precisely, and
- even solved the problem in addition to defining it.

He’d just come up with a solution so complex to implement by hand that
Jarník had in essence de-parallelized it so it could be done
sequentially. And thus this algorithm lay unnoticed until it was
reinvented
([several times, actually](http://en.wikipedia.org/wiki/Bor%C5%AFvka's_algorithm))
by Sollin in time for parallel computing folks to notice a need for
it. But now we can just call this Borůvka’s Algorithm, which is
only fitting.

As you might have guessed by now, this problem is indeed called the
MST in other textbooks, but “M” stands not for Moravia but for
“Minimum”. But given Borůvka’s forgotten place in history, we prefer
the more whimsical name.

#### 17.5.5 Checking Component Connectedness {#union-find-functional}

As we’ve seen, we need to be able to efficiently tell whether two
nodes are in the same component. One way to do this is to conduct a
depth-first traversal (or breadth-first traversal) starting from the
first node and checking whether we ever visit the second one. (Using
one of these traversal strategies ensures that we terminate in the
presence of loops.) Unfortunately, this takes a linear amount of time
(in the size of the graph) for every pair of nodes—and
depending on the graph and choice of node, we might do this for every
node in the graph on every edge addition! So we’d clearly like to do
this better.

It is helpful to reduce this problem from graph connectivity to a more
general one: of disjoint-set structure (colloquially known as
union-find for reasons that will soon be clear). If we think of
each connected component as a set, then we’re asking whether two nodes
are in the same set. But casting it as a set membership problem makes
it applicable in several other applications as well.

The setup is as follows. For arbitrary values, we want the ability to
think of them as elements in a set.
We are interested in two operations. One is obviously `union`{.pyret},
which merges two sets into one. The other would seem to be something
like `is-in-same-set`{.pyret} that takes two elements and determines
whether they’re in the same set. Over time, however, it has proven
useful to instead define the operator `find`{.pyret} that, given an
element, “names” the set (more on this in a moment) that the element
belongs to. To check whether two elements are in the same set, we then
have to get the “set name” for each element, and check whether these
names are the same. This certainly sounds more roundabout, but this
means we have a primitive that may be useful in other contexts, and
from which we can easily implement `is-in-same-set`{.pyret}.

Now the question is, how do we name sets? The real question we should
ask is, what operations do we care to perform on these names? All we
care about is, given two names, they represent the same set precisely
when the names are the same. Therefore, we could construct a new
string, or number, or something else, but we have another option:
simply pick some element of the set to represent it, i.e., to serve as
its name. Thus we will associate each set element with an
indicator of the “set name” for that element; if there isn’t one,
then its name is itself (the `none`{.pyret} case of `parent`{.pyret}):

```jayret
data Element {
    Elt(T val, Option<Object> parent);
}
```
We will assume we have some equality predicate for checking when two
elements are the same, which we do by comparing their value parts,
ignoring their parent values:

```jayret
Object is-same-element(e1, e2) {
    return e1.val <=> e2.val;
}
```

::: {.do-now}
Why do we check only the value parts?
:::

We will assume that for a given set, we always return the
same representative element. (Otherwise, equality will fail
even though we have the same set.) Thus:[We’ve used the
name `fynd`{.pyret} because `find`{.pyret} is already defined to mean
something else in Jayret. If you don’t like the misspelling, you’re
welcome to use a longer name like `find-root`{.pyret}.]{.margin-note}

```jayret
boolean is-in-same-set(Element e1, Element e2, Sets s) {
    s1 = fynd(e1, s);
    s2 = fynd(e2, s);
    return identical(s1, s2);
}
```
where `Sets`{.pyret} is the list of all elements:

```jayret
type Sets = List < Element >;
```

How do we find the representative element for a set? We first find it
using `is-same-element`{.pyret}; when we do, we check the
element’s `parent`{.pyret} field. If it is `none`{.pyret}, that means this
very element names its set; this can happen either because the element
is a singleton set (we’ll initialize all elements with `none`{.pyret}),
or it’s the name for some larger set. Either way, we’re
done. Otherwise, we have to recursively find the parent:

```jayret
Element fynd(Element e, Sets s) {
    return switch (s) {
        case Empty: yield raise("fynd: shouldn't have gotten here");
        case Link(f, r): yield if (is-same-element(f, e)) {
            return switch (f.parent) {
                case None: yield f;
                case Some(p): yield fynd(p, s);
            }
        } else {
            return fynd(e, r);
        };
    }
}
```

::: {.exercise}
Why is there a recursive call in the nested `cases`{.pyret}?
:::

What’s left is to implement `union`{.pyret}. For this, we find the
representative elements of the two sets we’re trying to union; if they
are the same, then the two sets are already in a union; otherwise, we
have to update the data structure:

```jayret
Sets union(Element e1, Element e2, Sets s) {
    s1 = fynd(e1, s);
    s2 = fynd(e2, s);
    return if (identical(s1, s2)) {
        return s;
    } else {
        return update-set-with(s, s1, s2);
    }
}
```
To update, we arbitrarily choose one of the set names to be the name
of the new compound set. We then have to update the parent of the
other set’s name element to be this one:

```jayret
Sets update-set-with(Sets s, Element child, Element parent) {
    return switch (s) {
        case Empty: yield raise("update: shouldn't have gotten here");
        case Link(f, r): yield if (is-same-element(f, child)) {
            return link(elt(f.val, some(parent)), r);
        } else {
            return link(f, update-set-with(r, child, parent));
        };
    }
}
```
Here are some tests to illustrate this working:

```jayret
@Check void test() {
    s0 = map(elt(_, none), [0, 1, 2, 3, 4, 5, 6, 7]);
    s1 = union(get(s0, 0), get(s0, 2), s0);
    s2 = union(get(s1, 0), get(s1, 3), s1);
    s3 = union(get(s2, 3), get(s2, 5), s2);
    print(s3);
    assertEquals(is-same-element(fynd(get(s0, 0), s3), fynd(get(s0, 5), s3)), true);
    assertEquals(is-same-element(fynd(get(s0, 2), s3), fynd(get(s0, 5), s3)), true);
    assertEquals(is-same-element(fynd(get(s0, 3), s3), fynd(get(s0, 5), s3)), true);
    assertEquals(is-same-element(fynd(get(s0, 5), s3), fynd(get(s0, 5), s3)), true);
    assertEquals(is-same-element(fynd(get(s0, 7), s3), fynd(get(s0, 7), s3)), true);
}
```

Unfortunately, this implementation suffers from two major problems:


- First, because we are performing functional updates, the value
  of the `parent`{.pyret} reference keeps “changing”, but these changes
  are not visible to older copies of the “same” value. An element
  from different stages of unioning has different parent references,
  even though it is arguably the same element throughout. This is a
  place where functional programming hurts.
- Relatedly, the performance of this implementation is quite
  bad. `fynd`{.pyret} recursively traverses parents to find the set’s
  name, but the elements traversed are not updated to record this new
  name. We certainly could update them by reconstructing the set
  afresh each time, but that complicates the implementation and, as we
  will soon see, we can do much better.

Even worse, it may not even be correct!

::: {.exercise}
Is it? Consider constructing `union`{.pyret}s that are not quite so skewed as
above, and see whether you get the results you expect.
:::

The bottom line is that pure functional programming is not a
great fit with this problem. We need a better implementation
strategy: [Union-Find](union-find.html).
