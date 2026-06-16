---
title: Graphs With Weighted Edges
section_number: 17.3
source_file: weighted-graphs.html
prev: basic-graph-trav.html
up: part_graphs.html
next: lightest-paths.html
---

### 17.3 Graphs With Weighted Edges {#weighted-graphs}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td></td></tr></table>
```

Consider a transportation graph: we are usually interested not only in
whether we can get from one place to another, but also in what it
“costs” (where we may have many different cost measures: money,
distance, time, units of carbon dioxide, etc.). On the Internet, we
might care about the [☛ latency](glossary.html#%28elem._glossary-latency%29) or
[☛ bandwidth](glossary.html#%28elem._glossary-bandwidth%29) over a link. Even in a social network, we
might like to describe the degree of closeness of a friend. In short,
in many graphs we are interested not only in the direction of an edge
but also in some abstract numeric measure, which we call its
weight.

In the rest of this study, we will assume that our graph edges have
weights. This does not invalidate what we’ve studied so far: if a node
is reachable in an unweighted graph, it remains reachable in a
weighted one. But the operations we are going to study below
only make sense in a weighted graph.[We can, however,
always treat an unweighted graph as a weighted one by giving every
edge the same, constant, positive weight (say one).]{.margin-note}

::: {.exercise}
When treating an unweighted graph as a weighted one, why do we care
that every edge be given a positive weight?
:::

::: {.exercise}
Revise the graph data definitions to account for edge weights.
:::

::: {.exercise}
Weights are not the only kind of data we might record about edges. For
instance, if the nodes in a graph represent people, the edges might be
labeled with their relationship (“mother”, “friend”, etc.). What
other kinds of data can you imagine recording for edges?
:::
