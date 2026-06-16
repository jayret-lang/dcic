---
title: Queues from Lists
section_number: 8.2
source_file: queues-from-lists.html
prev: func-as-data.html
up: part_bonus-foundations.html
next: testing.html
---

### 8.2 Queues from Lists {#queues-from-lists}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._.Using_a_.Wrapper_.Datatype%29">8.2.1<span class="hspace"> </span>Using a Wrapper Datatype</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._qfl-comb-ans%29">8.2.2<span class="hspace"> </span>Combining Answers</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._.Using_a_.Picker%29">8.2.3<span class="hspace"> </span>Using a Picker</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._qfl-tuples%29">8.2.4<span class="hspace"> </span>Using Tuples</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="queues-from-lists.html#%28part._.A_.Picker_.Method%29">8.2.5<span class="hspace"> </span>A Picker Method</a></p></td></tr></table>
```

Suppose you have a list. When you take its first element, you get the
element that was most recently `link`{.pyret}ed to create it. The next element is the
second most recent one that was `link`{.pyret}ed, and so on. That is, the last one in is
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

#### 8.2.1 Using a Wrapper Datatype {#Using-a-Wrapper-Datatype}

Concretely, here’s how we’ll represent queues. For all the code that follows,
it’s helpful to use the Pyret type-checker to make sure we’re composing code
correctly:

```pyret
data Queue<T>:
  | queue(l :: List<T>)
end
```
With this encoding, we can start define a few helper functions: e.g., a way to
construct an empty queue and to check for emptiness:

```pyret
fun mk-mtq<T>() -> Queue<T>:
  queue(empty)
end

fun is-mtq<T>(q :: Queue<T>) -> Boolean:
  is-empty(q.l)
end
```
Adding an element to a queue is usually called “enqueueing”. It has this type:

```pyret
enqueue :: <T> Queue<T>, T -> Queue<T>
```
Here’s the corresponding implementation:

```pyret
fun enqueue(q, e):
  queue(link(e, q.l))
end
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

```pyret
qpeek :: <T> Queue<T> -> T
qrest :: <T> Queue<T> -> Queue<T>
```
Let’s write out a few examples to make sure we know how these should work:

```pyret
q_ = mk-mtq()
q3 = enqueue(q_, 3)
m43 = enqueue(q3, 4)
m543 = enqueue(m43, 5)

check:
  qpeek(q3) is 3
  qpeek(m43) is 3
  qpeek(m543) is 3
end

check:
  qrest(q3) is mk-mtq()
  qrest(m43) is enqueue(mk-mtq(), 4)
  qrest(m543) is enqueue(enqueue(mk-mtq(), 4), 5)
end
```
Now let’s implement these:

```pyret
fun qpeek(q):
  if is-mtq(q):
    raise("can't peek an empty queue")
  else:
    q.l.get(q.l.length() - 1)
  end
end

fun qrest(q):
  fun safe-rest(l :: List<T>) -> List<T>:
    cases (List) l:
      | empty => raise("can't dequeue an empty queue")
      | link(f, r) => r
    end
  end
  queue(safe-rest(q.l.reverse()).reverse())
end
```

#### 8.2.2 Combining Answers {#qfl-comb-ans}

However, it would be nice if we could obtain both the oldest element and the
rest of the queue at once, if we want them both. That means the single function
would need to return two values; since a function can return only one value at
a time, it would need to use a data structure to hold both of
them. Furthermore, note that both `qpeek`{.pyret} and `qrest`{.pyret} above have the
possibility of not having any more elements! We might as well reflect that too
in the type. Thus we end up with a type that looks like

```pyret
data Dequeued<T>:
  | none-left
  | elt-and-q(e :: T, q :: Queue<T>)
end
```

::: {.exercise}
Write out the function to use this return type.
:::

Observe that this also follows our principle of making exceptional behavior
manifest in the return type: [The Option Type](partial-domains.html##pd-option), and especially in
[Summary](partial-domains.html##pd-summary).

::: {.exercise}
Write out the function using this return type.
:::

#### 8.2.3 Using a Picker {#Using-a-Picker}

Does `Dequeued`{.pyret} look familiar? Of course it should! It’s basically the
same as the pickers used for sets in Pyret: [Picking Elements from Sets](Collections_of_Structured_Data.html##coll-sd-pick). If we make
queues provide the same operations, we can reuse the `Pick`{.pyret} library
already built into the language, and reuse any code that is written expecting
the picker interface.

To do so, first we need to import the picker library:

```pyret
include pick
```
Then we can write:

```pyret
dequeue :: <T> Queue<T> -> Pick<T, Queue<T>>
```
Here are some examples showing how it would work:

```pyret
check:
  dequeue(q_) is pick-none
  dequeue(q3) is pick-some(3, mk-mtq())
  dequeue(m43) is pick-some(3, enqueue(mk-mtq(), 4))
  dequeue(m543) is pick-some(3, enqueue(enqueue(mk-mtq(), 4), 5))
end
```
And here’s the corresponding code:

```pyret
fun dequeue<T>(q):
  rev = q.l.reverse()
  cases (List) rev:
    | empty => pick-none
    | link(f, r) =>
      pick-some(f, queue(r.reverse()))
  end
end
```
In terms of big-O complexity, this is a dreadfully inefficient implementation,
causing two reversals on every `qrest`{.pyret} or `dequeue`{.pyret}. To see how to do
better, and to conduct a more sophisticated analysis, see
[An Example: Queues from Lists](amortized-analysis.html##queue-data-structure).

One thing to note is that by providing only a picker interface, we’re slightly
changing the meaning of queues. The picker interface in Pyret is designed for
sets, which don’t have a notion of order. But queues are, of course, very much
an ordered datatype; order is why they exist. So by providing only a
picker interface, we don’t offer the very guarantee that queues are designed
for. Therefore, we should provide a picker in addition to an ordered
interface, rather than in place of one.

At this point we’re done with the essential content, but here are two more
parts that you may find interesting.

#### 8.2.4 Using Tuples {#qfl-tuples}

Earlier, we created the `Dequeued`{.pyret} datatype to represent the return value
from the dequeue. Indeed, it is often useful to create datatypes of this sort
to document functions and make sure the types can be meaningfully interpreted
even when their values flow around the code some distance from where they were
created.

Sometimes, however, we want to create a compound datum in a special
circumstance: it represents the return value of a function, and that return
value will not live for very long, i.e., it will be taken apart as soon as it
has returned and only the constituent parts will be used thereafter. In such
situations, it can feel like a burden to create a new datatype for such a
fleeting purpose. For such cases, Pyret has a built-in generic datatype called
the tuple.

Here are some examples of tuples, which illustrate their syntax; note that each
position (separated by `;`{.pyret}) takes an expression, not only a
constant value:

```pyret
{1; 2}
{3; 4; 5}
{1 + 2; 3}
{6}
{}
```
We can also pull values out of tuples as follows:

```pyret
{a; b} = {1; 2}
```
Evaluate `a`{.pyret} and `b`{.pyret} and see what they are bound to.

```pyret
{c; d; e} = {1 + 2; 6 - 2; 5}
```
Similarly, see what `c`{.pyret}, `d`{.pyret}, and `e`{.pyret} are bound to.

::: {.exercise}
What happens if we use too few or too many variables? Try out the following in
Pyret and see what happens:

```pyret
{p; q} = {1}
{p} = {1; 2}
{p} = 1
```
:::

::: {.do-now}
What happens if instead we write this?

```pyret
p = {1; 2}
```
:::

This binds `p`{.pyret} to the entire tuple.

::: {.exercise}
How might we pull apart the constituents of `p`{.pyret}?
:::

Now that we have tuples, we can write dequeue as:

```pyret
fun dequeue-tuple<T>(q :: Queue<T>) -> {T; Queue<T>}:
  rev = q.l.reverse()
  cases (List) rev:
    | empty => raise("can't dequeue an empty queue")
    | link(f, r) =>
      {f; queue(r.reverse())}
  end
end

check:
  dequeue-tuple(q3) is {3; mk-mtq()}
  dequeue-tuple(m43) is {3; enqueue(mk-mtq(), 4)}
  dequeue-tuple(m543) is {3; enqueue(enqueue(mk-mtq(), 4), 5)}
end
```
And here’s how we can use it more generally:

```pyret
fun q2l<T>(q :: Queue<T>) -> List<T>:
  if is-mtq(q):
    empty
  else:
    {e; rq} = dequeue-tuple(q)
    link(e, q2l(rq))
  end
end

check:
  q2l(mk-mtq()) is empty
  q2l(q3) is [list: 3]
  q2l(m43) is [list: 3, 4]
  q2l(m543) is [list: 3, 4, 5]
end
```
You should feel free to use tuples in your programs provided you follow the
rules above for when tuples are applicable. In general, tuples can cause a
reduction in readability, and increase the likelihood of errors (because tuples
from one source aren’t distinguishable from those from another source). Use
them with caution!

#### 8.2.5 A Picker Method {#A-Picker-Method}

Second, and this is truly optional: you may have noticed earlier that `Set`{.pyret}s had a
built-in `pick`{.pyret} method. We have a function, but not method,
that picks. Now we’ll see how we can write this as a method:

```pyret
data Queue<T>:
  | queue(l :: List<T>) with:
    method pick(self):
      rev = self.l.reverse()
      cases (List) rev:
        | empty => pick-none
        | link(f, r) =>
          pick-some(f, queue(r.reverse()))
      end
    end
end
```
This is a drop-in replacement for our previous definition of `Queue`{.pyret},
because we’ve added a method but left the general datatype structure intact, so
all our existing code will still work. In addition, we can rewrite `q2l`{.pyret} in terms
of the picker interface:

```pyret
fun q2lm<T>(c :: Queue<T>) -> List<T>:
  cases (Pick) c.pick():
    | pick-none => empty
    | pick-some(e, r) => link(e, q2lm(r))
  end
end

check:
  q2lm(m543)
end
```
We can also write generic programs over data that support the Pick interface. For instance, here’s a function that will convert anything satisfying that interface into a list:

```pyret
fun pick2l<T>(c) -> List<T>:
  cases (Pick) c.pick():
    | pick-none => empty
    | pick-some(e, r) => link(e, pick2l(r))
  end
end
```
For instance, it works on both sets and our new `Queue`{.pyret}s:

```pyret
import sets as S    # put this at the top of the file

check:
  pick2l([S.set: 3, 4, 5]).sort() is [list: 3, 4, 5]
  pick2l(m543) is [list: 3, 4, 5]
end
```

::: {.exercise}
Do you see why we invoked `sort`{.pyret} in the test above?
:::

The only weakness here is that for this last part (making the function
generic), we have to transition out of the type-checker, because `pick2l`{.pyret}
cannot be typed by the current Pyret type checker. It requires a feature that
the type checker does not (yet) have.
