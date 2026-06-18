---
title: Queues from Lists
section_number: 8.2
source_file: queues-from-lists.html
prev: func-as-data.html
up: part_bonus-foundations.html
next: testing.html
---

```{=html}
<a name="(part._queues-from-lists)"></a>
```

### 8.2 Queues from Lists {#queues-from-lists}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._Using-a-Wrapper-Datatype%29">8.2.1<span class="hspace"> </span>Using a Wrapper Datatype</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._qfl-comb-ans%29">8.2.2<span class="hspace"> </span>Combining Answers</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._Using-a-Picker%29">8.2.3<span class="hspace"> </span>Using a Picker</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._qfl-tuples%29">8.2.4<span class="hspace"> </span>Using Tuples</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._A-Picker-Method%29">8.2.5<span class="hspace"> </span>A Picker Method</a></p></td></tr></table>
```

Suppose you have a list. When you take its first element, you get the
element that was most recently `link`{.jayret}ed to create it. The next element is the
second most recent one that was `link`{.jayret}ed, and so on. That is, the last one in is
the first one out. This is called a LIFO, short for “last-in-first-out”, data
structure. A list is LIFO; we sometimes also refer to this as a stack.

But there are many settings where you want the first-in to be the
first-out. When you stand at a supermarket line, try to purchase concert
tickets, submit a job request, or any number of other tasks, you want to be
rewarded, not punished, for being there first. That is, you want a FIFO instead. This
is called a queue.

The game we’re playing here is that we want one datatype but our language has
given us another (in this case, lists), and we have to figure out how to encode
one in the other. We’ll see elsewhere how to encode sets with lists
[[Representing Sets as Lists](sets-from-lists.html)]. Here let’s see how we can encode queues with lists.

With sets, we allowed the set type to be an alias for lists; that is, the two
were the same. Another option we have when encoding is to create a completely
new type that does nothing more than wrap a value of the encoding type. We’ll
use that principle here to illustrate how that might work.

```{=html}
<a name="(part._Using-a-Wrapper-Datatype)"></a>
```

#### 8.2.1 Using a Wrapper Datatype {#Using-a-Wrapper-Datatype}

Concretely, here’s how we’ll represent queues. For all the code that follows,
it’s helpful to use the Jayret type-checker to make sure we’re composing code
correctly:

```jayret
data Queue {
    Queue(List<Object> l);
}
```
With this encoding, we can start define a few helper functions: e.g., a way to
construct an empty queue and to check for emptiness:

```jayret
Queue<Object> mk-mtq() {
    return queue(empty);
}
boolean is-mtq(Queue<Object> q) {
    return is-empty(q.l);
}
```
Adding an element to a queue is usually called “enqueueing”. It has this type:

```jayret
/* contract: enqueue :: Object */;
```
Here’s the corresponding implementation:

```jayret
Object enqueue(q, e) {
    return queue(link(e, q.l));
}
```

::: {.do-now}
Did we have a choice?
:::

Yes, we did! We could have made the new element the first element or the
last element.[Be careful here: we mean the first or last
element of the list that represents the queue, not of the queue
itself. There, FIFO gives us no choice.]{.margin-note} We just happened to choose one
representation. The other would be equally valid; we would just need to
implement all the other operations consistently. Let’s stick to this one for
now.

Now we come to a problem. What does it mean to “dequeue”? We need to get back
the one element, but we also need to get back the rest. Let’s first write this
as two functions, very analogous to first and rest on lists:

```jayret
/* contract: qpeek :: Object */;
/* contract: qrest :: Object */;
```
Let’s write out a few examples to make sure we know how these should work:

```jayret
q_ = mk-mtq();
q3 = enqueue(q_, 3);
m43 = enqueue(q3, 4);
m543 = enqueue(m43, 5);
@Check void test() {
    assertEquals(qpeek(q3), 3);
    assertEquals(qpeek(m43), 3);
    assertEquals(qpeek(m543), 3);
}
@Check void test() {
    assertEquals(qrest(q3), mk-mtq());
    assertEquals(qrest(m43), enqueue(mk-mtq(), 4));
    assertEquals(qrest(m543), enqueue(enqueue(mk-mtq(), 4), 5));
}
```
Now let’s implement these:

```jayret
Object qpeek(q) {
    return if (is-mtq(q)) {
        return raise("can't peek an empty queue");
    } else {
        return q.l.get(q.l.length() - 1);
    }
}
Object qrest(q) {
    List<Object> safe-rest(List<Object> l) {
        return switch (l) {
            case Empty: yield raise("can't dequeue an empty queue");
            case Link(f, r): yield r;
        }
    }
    return queue(safe-rest(q.l.reverse()).reverse());
}
```

```{=html}
<a name="(part._qfl-comb-ans)"></a>
```

#### 8.2.2 Combining Answers {#qfl-comb-ans}

However, it would be nice if we could obtain both the oldest element and the
rest of the queue at once, if we want them both. That means the single function
would need to return two values; since a function can return only one value at
a time, it would need to use a data structure to hold both of
them. Furthermore, note that both `qpeek`{.jayret} and `qrest`{.jayret} above have the
possibility of not having any more elements! We might as well reflect that too
in the type. Thus we end up with a type that looks like

```jayret
data Dequeued {
    None-left;
    Elt-and-q(T e, Queue<Object> q);
}
```

::: {.exercise}
Write out the function to use this return type.
:::

Observe that this also follows our principle of making exceptional behavior
manifest in the return type: [The Option Type](partial-domains.html#pd-option), and especially in
[Summary](partial-domains.html#pd-summary).

::: {.exercise}
Write out the function using this return type.
:::

```{=html}
<a name="(part._Using-a-Picker)"></a>
```

#### 8.2.3 Using a Picker {#Using-a-Picker}

Does `Dequeued`{.jayret} look familiar? Of course it should! It’s basically the
same as the pickers used for sets in Jayret: [Picking Elements from Sets](Collections_of_Structured_Data.html#coll-sd-pick). If we make
queues provide the same operations, we can reuse the `Pick`{.jayret} library
already built into the language, and reuse any code that is written expecting
the picker interface.

To do so, first we need to import the picker library:

```jayret
import pick

```
Then we can write:

```jayret
/* contract: dequeue :: Object */;
```
Here are some examples showing how it would work:

```jayret
@Check void test() {
    assertEquals(dequeue(q_), pick-none);
    assertEquals(dequeue(q3), pick-some(3, mk-mtq()));
    assertEquals(dequeue(m43), pick-some(3, enqueue(mk-mtq(), 4)));
    assertEquals(dequeue(m543), pick-some(3, enqueue(enqueue(mk-mtq(), 4), 5)));
}
```
And here’s the corresponding code:

```jayret
Object dequeue(q) {
    rev = q.l.reverse();
    return switch (rev) {
        case Empty: yield pick-none;
        case Link(f, r): yield pick-some(f, queue(r.reverse()));
    }
}
```
In terms of big-O complexity, this is a dreadfully inefficient implementation,
causing two reversals on every `qrest`{.jayret} or `dequeue`{.jayret}. To see how to do
better, and to conduct a more sophisticated analysis, see
[An Example: Queues from Lists](amortized-analysis.html#queue-data-structure).

One thing to note is that by providing only a picker interface, we’re slightly
changing the meaning of queues. The picker interface in Jayret is designed for
sets, which don’t have a notion of order. But queues are, of course, very much
an ordered datatype; order is why they exist. So by providing only a
picker interface, we don’t offer the very guarantee that queues are designed
for. Therefore, we should provide a picker in addition to an ordered
interface, rather than in place of one.

At this point we’re done with the essential content, but here are two more
parts that you may find interesting.

```{=html}
<a name="(part._qfl-tuples)"></a>
```

#### 8.2.4 Using Tuples {#qfl-tuples}

Earlier, we created the `Dequeued`{.jayret} datatype to represent the return value
from the dequeue. Indeed, it is often useful to create datatypes of this sort
to document functions and make sure the types can be meaningfully interpreted
even when their values flow around the code some distance from where they were
created.

Sometimes, however, we want to create a compound datum in a special
circumstance: it represents the return value of a function, and that return
value will not live for very long, i.e., it will be taken apart as soon as it
has returned and only the constituent parts will be used thereafter. In such
situations, it can feel like a burden to create a new datatype for such a
fleeting purpose. For such cases, Jayret has a built-in generic datatype called
the tuple.

Here are some examples of tuples, which illustrate their syntax; note that each
position (separated by `;`{.jayret}) takes an expression, not only a
constant value:

```jayret
/* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {1 ;2}
/* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {3 ;4 ;5}
/* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {1 + 2 ;3}
/* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {6}
{}
```
We can also pull values out of tuples as follows:

```jayret
/* TODO(pyret2jayret): tuple-binding deferred in Jayret v0.1 */ /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {1 ;2}
```
Evaluate `a`{.jayret} and `b`{.jayret} and see what they are bound to.

```jayret
/* TODO(pyret2jayret): tuple-binding deferred in Jayret v0.1 */ /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {1 + 2 ;6 - 2 ;5}
```
Similarly, see what `c`{.jayret}, `d`{.jayret}, and `e`{.jayret} are bound to.

::: {.exercise}
What happens if we use too few or too many variables? Try out the following in
Jayret and see what happens:

```jayret
/* TODO(pyret2jayret): tuple-binding deferred in Jayret v0.1 */ /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {1}
/* TODO(pyret2jayret): tuple-binding deferred in Jayret v0.1 */ /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {1 ;2}
/* TODO(pyret2jayret): tuple-binding deferred in Jayret v0.1 */ 1;
```
:::

::: {.do-now}
What happens if instead we write this?

```jayret
p = /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {1 ;2}
```
:::

This binds `p`{.jayret} to the entire tuple.

::: {.exercise}
How might we pull apart the constituents of `p`{.jayret}?
:::

Now that we have tuples, we can write dequeue as:

```jayret
/* tuple-ann (deferred) */ Object dequeue-tuple(Queue<Object> q) {
    rev = q.l.reverse();
    return switch (rev) {
        case Empty: yield raise("can't dequeue an empty queue");
        case Link(f, r): yield /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {f ;queue(r.reverse())};
    }
}
@Check void test() {
    assertEquals(dequeue-tuple(q3), /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {3 ;mk-mtq()});
    assertEquals(dequeue-tuple(m43), /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {3 ;enqueue(mk-mtq(), 4)});
    assertEquals(dequeue-tuple(m543), /* TODO(pyret2jayret): tuples deferred in Jayret v0.1 */ {3 ;enqueue(enqueue(mk-mtq(), 4), 5)});
}
```
And here’s how we can use it more generally:

```jayret
List<Object> q2l(Queue<Object> q) {
    return if (is-mtq(q)) {
        return empty;
    } else {
        /* TODO(pyret2jayret): tuple-binding deferred in Jayret v0.1 */ dequeue-tuple(q);
        return link(e, q2l(rq));
    }
}
@Check void test() {
    assertEquals(q2l(mk-mtq()), empty);
    assertEquals(q2l(q3), [3]);
    assertEquals(q2l(m43), [3, 4]);
    assertEquals(q2l(m543), [3, 4, 5]);
}
```
You should feel free to use tuples in your programs provided you follow the
rules above for when tuples are applicable. In general, tuples can cause a
reduction in readability, and increase the likelihood of errors (because tuples
from one source aren’t distinguishable from those from another source). Use
them with caution!

```{=html}
<a name="(part._A-Picker-Method)"></a>
```

#### 8.2.5 A Picker Method {#A-Picker-Method}

Second, and this is truly optional: you may have noticed earlier that `Set`{.jayret}s had a
built-in `pick`{.jayret} method. We have a function, but not method,
that picks. Now we’ll see how we can write this as a method:

```jayret
data Queue {
    Queue(List<Object> l); /* TODO: with: methods */
}
```
This is a drop-in replacement for our previous definition of `Queue`{.jayret},
because we’ve added a method but left the general datatype structure intact, so
all our existing code will still work. In addition, we can rewrite `q2l`{.jayret} in terms
of the picker interface:

```jayret
List<Object> q2lm(Queue<Object> c) {
    return switch (c.pick()) {
        case Pick-none: yield empty;
        case Pick-some(e, r): yield link(e, q2lm(r));
    }
}
@Check void test() {
    q2lm(m543);
}
```
We can also write generic programs over data that support the Pick interface. For instance, here’s a function that will convert anything satisfying that interface into a list:

```jayret
List<Object> pick2l(c) {
    return switch (c.pick()) {
        case Pick-none: yield empty;
        case Pick-some(e, r): yield link(e, pick2l(r));
    }
}
```
For instance, it works on both sets and our new `Queue`{.jayret}s:

```jayret
import sets as S
// put this at the top of the file
@Check void test() {
    assertEquals(pick2l([S.set: 3, 4, 5]).sort(), [3, 4, 5]);
    assertEquals(pick2l(m543), [3, 4, 5]);
}
```

::: {.exercise}
Do you see why we invoked `sort`{.jayret} in the test above?
:::

The only weakness here is that for this last part (making the function
generic), we have to transition out of the type-checker, because `pick2l`{.jayret}
cannot be typed by the current Jayret type checker. It requires a feature that
the type checker does not (yet) have.
