---
title: Halloween Analysis
section_number: 15
source_file: amortized-analysis.html
prev: predicting-growth.html
up: booklet_algo-analysis.html
next: booklet_data-with-analysis.html
---

## Halloween Analysis {#amortized-analysis}

In [Predicting Growth](predicting-growth.html), we introduced the idea of big-Oh
complexity to measure the worst-case time of a computation. As we see
in [Choosing Between Representations](sets-from-lists.html##choosing-set-reps), however, this is sometimes too coarse
a bound when the complexity is heavily dependent on the exact sequence
of operations run. Now, we will consider a different style of
complexity analysis that better accommodates operation sequences.

### A First Example {#A-First-Example}

Consider, for instance, a set that starts out empty, followed by a
sequence of \(k\) insertions and then \(k\) membership tests, and
suppose we are using the representation without
duplicates. Insertion time is proportional to the size of the set (and
list); this is initially \(0\), then \(1\), and so on, until it reaches
size \(k\). Therefore, the total cost of the sequence of insertions is
\(k \cdot (k+1) / 2\). The membership tests cost \(k\) each in
the worst case, because we’ve inserted up to \(k\)
distinct elements into the set. The total time is then
\begin{equation*}k^2 / 2 + k / 2 + k^2\end{equation*}for a total of \(2k\) operations, yielding an average of
\begin{equation*}\frac{3}{4} k + \frac{1}{4}\end{equation*}steps per operation in the worst case.

### The New Form of Analysis {#The-New-Form-of-Analysis}

What have we computed? We are still computing a worst case
cost, because we have taken the cost of each operation in the sequence
in the worst case. We are then computing the average cost per
operation. Therefore, this is a average of worst
cases.[Importantly, this is different from what is known
as average-case analysis, which uses probability theory to
compute the estimated cost of the computation. We have not used any
probability here.]{.margin-note} Note that because this is an average per operation,
it does not say anything about how bad any one operation can be
(which, as we will see [[Amortization Versus Individual Operations](amortized-analysis.html##worst-case-ops-amort)], can be quite
a bit worse); it only says what their average is.

In the above case, this new analysis did not yield any big
surprises. We have found that on average we spend about \(k\) steps
per operation; a big-Oh analysis would have told us that we’re
performing \(2k\) operations with a cost of \(O([k \rightarrow k])\)
each in the number of distinct elements; per operation, then, we are
performing roughly linear work in the worst-case number of set
elements.

As we will soon see, however, this won’t always be the case: this new
analysis can cough up pleasant surprises.

Before we proceed, we should give this analysis its name. Formally,
it is called amortized analysis. Amortization is the process of
spreading a payment out over an extended but fixed term. In the same
way, we spread out the cost of a computation over a fixed sequence,
then determine how much each payment will be.[We have given
it a whimsical name because
[Halloween](http://en.wikipedia.org/wiki/Halloween)
is a(n American) holiday devoted to ghosts, ghouls, and other symbols
of death. Amortization comes from the Latin root mort-,
which means death, because an amortized analysis is one conducted “at
the death”, i.e., at the end of a fixed sequence of operations.]{.margin-note}

### An Example: Queues from Lists {#queue-data-structure}

We have seen lists [[From Tables to Lists](tables-to-lists.html)] and sets [[Several Variations on Sets](part_sets.html)].
Here we focus on queues, which too can be represented as lists:
[Queues from Lists](queues-from-lists.html). If you have not read that material, it’s worth
reading at least the early portions now. In this section, we will ignore the
various programming niceties discussed there, and focus on raw list
representations to make an algorithmic point.

#### List Representations {#List-Representations}

Consider two natural ways of defining queues using lists. One is that every
enqueue is implemented with `link`{.pyret}, while every
dequeue requires traversing the whole list until its
end. Conversely, we could make enqueuing traverse to the end, and
dequeuing correspond to `.rest`{.pyret}. Either way, one of these
operations will take constant time while the other will be linear in
the length of the list representing the queue. (This should be loosely
reminiscent of trade-offs we ran into when representing sets as lists:
[Representing Sets as Lists](sets-from-lists.html).)

In fact, however, the above paragraph contains a key insight that will
let us do better.

Observe that if we store the queue in a list with
most-recently-enqueued element first, enqueuing is cheap (constant
time). In contrast, if we store the queue in the reverse order, then
dequeuing is constant time. It would be wonderful if we could have
both, but once we pick an order we must give up one or the
other. Unless, that is, we pick...both.

One half of this is easy. We simply enqueue elements into a list with
the most recent addition first. Now for the (first) crucial insight:
when we need to dequeue, we reverse the list. Now, dequeuing
also takes constant time.

#### A First Analysis {#A-First-Analysis}

Of course, to fully analyze the complexity of this data structure, we
must also account for the reversal. In the worst case, we might argue
that any operation might reverse (because it might be the first
dequeue); therefore, the worst-case time of any operation is the time
it takes to reverse, which is linear in the length of the list (which
corresponds to the elements of the queue).

However, this answer should be unsatisfying. If we perform \(k\)
enqueues followed by \(k\) dequeues, then each of the enqueues takes
one step; each of the last \(k-1\) dequeues takes one step; and only
the first dequeue requires a reversal, which takes steps proportional
to the number of elements in the list, which at that point is
\(k\). Thus, the total cost of operations for this sequence is
\(k \cdot 1 + k + (k-1) \cdot 1 = 3k-1\) for a total of
\(2k\) operations, giving an amortized complexity of
effectively constant time per operation!

#### More Liberal Sequences of Operations {#More-Liberal-Sequences-of-Operations}

In the process of this, however, we’ve quietly glossed over something that you
may not have picked up on: in our candidate sequence all dequeues
followed all enqueues. What happens on the next enqueue? Because the
list is now reversed, it will have to take a linear amount of time! So
we have only partially solved the problem.

Now we can introduce the second insight: have two lists instead
of one. One of them will be the tail of the queue, where new elements
get enqueued; the other will be the head of the queue, where they get
dequeued:

```pyret
data Queue<T>:
  | queue(tail :: List<T>, head :: List<T>)
end

mt-q :: Queue = queue(empty, empty)
```
Provided the tail is stored so that the most recent element is the
first, then enqueuing takes constant time:

```pyret
fun enqueue<T>(q :: Queue<T>, e :: T) -> Queue<T>:
  queue(link(e, q.tail), q.head)
end
```

For dequeuing to take constant time, the head of the queue must be
stored in the reverse direction. However, how does any element ever
get from the tail to the head? Easy: when we try to dequeue and find
no elements in the head, we reverse the (entire) tail into the head
(resulting in an empty tail). We will first define a datatype to
represent the response from dequeuing:

```pyret
data Response<T>:
  | elt-and-q(e :: T, r :: Queue<T>)
end
```
Now for the implementation of `dequeue`{.pyret}:

```pyret
fun dequeue<T>(q :: Queue<T>) -> Response<T>:
  cases (List) q.head:
    | empty =>
      new-head = q.tail.reverse()
      elt-and-q(new-head.first,
        queue(empty, new-head.rest))
    | link(f, r) =>
      elt-and-q(f,
        queue(q.tail, r))
  end
end
```

#### A Second Analysis {#A-Second-Analysis}

We can now reason about sequences of operations as we did before, by
adding up costs and averaging. However, another way to think of it is
this. Let’s give each element in the queue three “credits”. Each
credit can be used for one constant-time operation.

One credit gets used up in enqueuing. So long as the element stays in
the tail list, it still has two credits to spare. When it needs to be
moved to the head list, it spends one more credit in the link step of
reversal. Finally, the dequeuing operation performs one operation
too.

Because the element does not run out of credits, we know it must have
had enough. These credits reflect the cost of operations on that
element. From this (very informal) analysis, we can conclude that in
the worst case, any permutation of enqueues and dequeues will still
cost only a constant amount of amortized time.

#### Amortization Versus Individual Operations {#worst-case-ops-amort}

Note, however, that the constant represents an average across the
sequence of operations. It does not put a bound on the cost of any one
operation. Indeed, as we have seen above, when dequeue finds the head
list empty it reverses the tail, which takes time linear in the size
of the tail—not constant at all! Therefore, we should be careful to
not assume that every step in the sequence will is
bounded. Nevertheless, an amortized analysis sometimes gives us a much
more nuanced understanding of the real behavior of a data structure
than a worst-case analysis does on its own.

### Reading More {#Reading-More}

At this point we have only briefly touched on the subject of amortized
analysis. A very nice
[tutorial by Rebecca Fiebrink](https://web.archive.org/web/20131020020356/http://www.cs.princeton.edu/~fiebrink/423/AmortizedAnalysisExplained_Fiebrink.pdf)
provides much more information. The authoritative book on algorithms,
Introduction to Algorithms by
Cormen, Leiserson, Rivest, and Stein,
covers amortized analysis in extensive detail.
