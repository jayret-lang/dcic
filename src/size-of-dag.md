---
title: The Size of a DAG
section_number: 16.2
source_file: size-of-dag.html
prev: Sharing_and_Equality.html
up: part_dags.html
next: part_graphs.html
---

### The Size of a DAG {#size-of-dag}

Let’s start by defining a function to compute the size of a tree:

```pyret
data BT:
  | mt
  | nd(v :: Number, l :: BT, r :: BT)
end

fun size-1(b :: BT) -> Number:
  cases (BT) b:
    | mt => 0
    | nd(v, l, r) => 1 + size-1(l) + size-1(r)
  end
end
```
This is straightforward enough.

But let’s say that our input isn’t actually a tree, but rather a DAG. For
instance:

```pyret
#|
     4
    / \
   2   3
    \ /
     1
|#

n1 = nd(1, mt, mt)
n2 = nd(2, mt, n1)
n3 = nd(3, n1, mt)
n4 = nd(4, n2, n3)
```
where `n4`{.pyret} is the DAG. There are two notions of size here. One is like
a “print size”: how much space will it occupy when printed. The current size
function computes that well. But another is the “allocation” size: how many
nodes did we allocate. How do we fare?

#### Stage 1 {#Stage-1}

```pyret
check:
  size-1(n1) is 1
  size-1(n2) is 2
  size-1(n3) is 2
  size-1(n4) is 4
end
```

Clearly the answer should be `4`{.pyret}: we can just read off how many `nd`{.pyret}
calls there are. And clearly the function is wrong.

The problem, of course, is that a DAG involves repeating nodes, and we
aren’t doing anything to track the repetition. So we need a stronger contract:
we’ll split the problem into two parts, a standard interface function that
takes just the DAG and returns a number, and a richer helper function, which
also takes a memory of the nodes already seen.

#### Stage 2 {#Stage-2}

```pyret
fun size-2-h(b :: BT, seen :: List<BT>) -> Number:
  if member-identical(seen, b):
    0
  else:
    cases (BT) b:
      | mt => 0
      | nd(v, l, r) =>
        new-seen = link(b, seen)
        1 + size-2-h(l, new-seen) + size-2-h(r, new-seen)
    end
  end
end
```

::: {.exercise}
Why does this code use `member-identical`{.pyret} rather than `member`{.pyret}?

Observe that if we replace every `member-identical`{.pyret} with `member`{.pyret} in
this chapter, the code still behaves the same. Why?

Make changes to demonstrate the need for `member-identical`{.pyret}.
:::

Is it odd that we return `0`{.pyret}? Not if we reinterpret what the function
does: it doesn’t count the size, it counts the additional
contribution to the size (relative to what has already been seen) of the
`BT`{.pyret} it is given. A node already in `seen`{.pyret} makes no marginal
contribution; it was already counted earlier.

Finally, we should not export such a function to the user, who has to deal with
an unwieldy extra parameter and may send something poorly-formed, thereby
causing our function to break. Instead, we should write a wrapper for it:

```pyret
fun size-2(b :: BT): size-2-h(b, empty) end
```
This also enables us to use our old tests (renamed):

```pyret
check:
  size-2(n1) is 1
  size-2(n2) is 2
  size-2(n3) is 2
  size-2(n4) is 4
end
```
Unfortunately, this still doesn’t work!

::: {.do-now}
Use Pyret’s `spy`{.pyret} construct in `size-2-h`{.pyret} to figure out why.
:::

#### Stage 3 {#Stage-3}

Did you remember to use `spy`{.pyret}? Otherwise you may very well miss the
problem! Be sure to use `spy`{.pyret} (feel free to elide the first few tests for
now) to get a feel for the issue.

As you may have noted, the problem is that we want `seen`{.pyret} to be all the
nodes ever seen. However, every time we return from one sub-computation,
we also lose track of whatever was seen during its work. Instead, we have to
also return everything that was seen, so as to properly preserve the idea that
we’re computing the marginal contribution of each node.

We can do this with the following data structure:

```pyret
data Ret: ret(sz :: Number, sn :: List<BT>) end
```
which is returned by the helper function:

```pyret
fun size-3-h(b :: BT, seen :: List<BT>) -> Ret:
  if member-identical(seen, b):
    ret(0, seen)
  else:
    cases (BT) b:
      | mt => ret(0, seen)
      | nd(v, l, r) =>
        new-seen = link(b, seen)
        rl = size-3-h(l, new-seen)
        rr = size-3-h(r, rl.sn)
        ret(1 + rl.sz + rr.sz, rr.sn)
    end
  end
end
```
Note, crucially, how the `seen`{.pyret} argument for the right branch is
`rl.sn`{.pyret}: i.e., everything that was already seen in the left branch. This
is the crucial step that avoids the bug.

Because of this richer return type, we have to extract the actual answer for
the purpose of testing:

```pyret
fun size-3(b :: BT): size-3-h(b, empty).sz end

check:
  size-3(n1) is 1
  size-3(n2) is 2
  size-3(n3) is 2
  size-3(n4) is 4
end
```

::: {.exercise}
Must `seen`{.pyret} be a list? What else can it be?
:::

#### Stage 4 {#Stage-4}

Observe that the `Ret`{.pyret} data structure is only of local interest. It’s
purely internal to the `size-3-h`{.pyret} function; even `size-3`{.pyret} ignores one
half, and it will never be seen by the rest of the program. That is a good use
of tuples, as we have seen before: [Using Tuples](queues-from-lists.html##qfl-tuples)!

```pyret
fun size-4-h(b :: BT, seen :: List<BT>) -> {Number; List<BT>}:
  if member-identical(seen, b):
    {0; seen}
  else:
    cases (BT) b:
      | mt => {0; seen}
      | nd(v, l, r) =>
        new-seen = link(b, seen)
        {lsz; lsn} = size-4-h(l, new-seen)
        {rsz; rsn} = size-4-h(r, lsn)
        {1 + lsz + rsz; rsn}
    end
  end
end

fun size-4(b :: BT): size-4-h(b, empty).{0} end

check:
  size-4(n1) is 1
  size-4(n2) is 2
  size-4(n3) is 2
  size-4(n4) is 4
end
```

The notation `{0; seen}`{.pyret} makes an actual tuple; `{Number; List<BT>}`{.pyret}
declares the contract of a tuple. Also, `.{0}`{.pyret} extracts the
`0`{.pyret}th element (the leftmost one) of a tuple.

#### Stage 5 {#Stage-5}

Notice that we have the two instances of the code `{0; seen}`{.pyret}. Do they
have to be that? What if we were to return `{0; empty}`{.pyret} instead in both
places? Does anything break?

We might expect it to break in the case where `member-identical`{.pyret} returns
`true`{.pyret}, but perhaps not in the `mt`{.pyret} case.

::: {.do-now}
Make each of these changes. Does the outcome match your expectations?
:::

Curiously, no! Making the change in the `mt`{.pyret} case has an effect but making
it in the `member-identical`{.pyret} case doesn’t! This almost seems
counter-intuitive. How can we diagnose this?

::: {.do-now}
Use `spy`{.pyret} to determine what is going on!
:::

Okay, so it seems like returning `empty`{.pyret} when we revisit a node doesn’t
seem to do any harm. Does that mean it’s okay to make that change?

Observe that nothing has actually depended on that seen-list being
`empty`{.pyret}. That’s why it appears to not matter. How can we make it matter?
By making it “hurt” the computation by visiting a previously seen, but now
forgotten, node yet again. So we need to visit a node at least three times: the
first time to remember it; the second time to forget it; and a third time to
incorrectly visit it again. Here’s a DAG that will do that:

```pyret
#|
    10
    / \
   11 12
  / \ /
 13<--
|#

n13 = nd(13, mt, mt)
n11 = nd(11, n13, n13)
n12 = nd(12, n13, mt)
n10 = nd(10, n11, n12)

check:
  size-4(n10) is 4
end
```
Sure enough, if either tuple now returns `empty`{.pyret}, this test
fails. Otherwise it succeeds.

#### What We’ve Learned {#What-We-e2-80-99ve-Learned}

We have learned three important principles here:


- A pattern for dealing with programs that need “memory”. This is called
  threading (not in the sense of “multi-threading”, which is a kind of
  parallel computation, but rather the pattern of how the seen list gets passed
  through the program).
- A good example of the use of tuples: local, where the documentation
  benefit of datatypes isn’t necessary (and the extra datatype probably just
  clutters up the program), as opposed to distant, where it is. In general, it’s
  always okay to make a new datatype; it’s only sometimes okay to use tuples in
  their place.
- An important software-engineering principle, called
  mutation testing. This is an odd name because it would seem to be the
  name of a technique to test programs. Actually, it’s a technique to test
  test suites. You have a tested program; you then “mutate” some part of
  your program that you feel must change the output, and see whether any tests
  break. If no tests break, then either you’ve misunderstood your program or,
  more likely, your test suite is not good enough. Improve your test suite to
  catch the error in your program, or convince yourself the change didn’t matter.
  
  There are mutation testing tools that will randomly try to alter your program
  using “mutant” strategies—e.g., replacing a `+`{.pyret} with a `-`{.pyret}—and
  re-run your suites, and then report back on how many potential mutants the
  suites actually caught. But we can’t and shouldn’t only rely on tools; we can
  also apply the principle of mutation testing by hand, as we have above. At the
  very least, it will help us understand our program better!

#### More on Value Printing: An Aside from Racket {#More-on-Value-Printing-An-Aside-from-Racket}

Earlier, we talked about how the standard recursive size can still be thought
of as a “size of printed value” computation. However, that actually depends on
your language’s value printer.

In Racket, you can turn on (it’s slightly more expensive, so off by default) a
value-printer that shows value sharing: Language | Choose Language … | Show
Details | Show sharing in values. So if we take the data definition above and
translate it into Racket structures

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">(struct mt () #:transparent)</span></p></td></tr><tr><td><p><span class="stt">(struct nd (v l r) #:transparent)</span></p></td></tr></table>
```
and then construct (almost) the same data as in the first example:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">(define n1 (nd 1 (mt) (mt)))</span></p></td></tr><tr><td><p><span class="stt">(define n2 (nd 2 (mt) n1))</span></p></td></tr><tr><td><p><span class="stt">(define n3 (nd 3 n1 (mt)))</span></p></td></tr><tr><td><p><span class="stt">(define n4 (nd 4 n2 n3))</span></p></td></tr></table>
```
and then ask Racket to print it, we get:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">&gt; n4</span></p></td></tr><tr><td><p><span class="stt">(nd 4 (nd 2 (mt) #0=(nd 1 (mt) (mt))) (nd 3 #0# (mt)))</span></p></td></tr></table>
```
The #0= notation is the moral equivalent of saying, “I’m going to refer to
this value again later, so let’s call it the 0th value” and #0# is saying “Here
I’m referring to the aforementioned 0th value”.

(Yes, there can be more than one shared value in an output, so each is given a
different “name”. We’ll see that in a moment.)

The later example above translates to

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">(define n13 (nd 13 (mt) (mt)))</span></p></td></tr><tr><td><p><span class="stt">(define n11 (nd 11 n13 n13))</span></p></td></tr><tr><td><p><span class="stt">(define n12 (nd 12 n13 (mt)))</span></p></td></tr><tr><td><p><span class="stt">(define n10 (nd 10 n11 n12))</span></p></td></tr></table>
```
which prints as

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">&gt; n10</span></p></td></tr><tr><td><p><span class="stt">(nd 10 (nd 11 #0=(nd 13 (mt) (mt)) #0#) (nd 12 #0# (mt)))</span></p></td></tr></table>
```
So it is possible for a language to reflect the sharing in its output. It’s
just that most programming languages choose to not do that, even optionally.

Remember the “almost” above? What was that about?

In Racket, we’ve made a new instance of mt over and over. We can more
accurately reflect what is happening in Pyret by instantiating it only once:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">(struct mt () #:transparent)</span></p></td></tr><tr><td><p><span class="stt">(define the-mt (mt))</span></p></td></tr><tr><td><p><span class="stt">(struct nd (v l r) #:transparent)</span></p></td></tr></table>
```
We then rewrite the earlier example to use that one instance only:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">(define n1 (nd 1 the-mt the-mt))</span></p></td></tr><tr><td><p><span class="stt">(define n2 (nd 2 the-mt n1))</span></p></td></tr><tr><td><p><span class="stt">(define n3 (nd 3 n1 the-mt))</span></p></td></tr><tr><td><p><span class="stt">(define n4 (nd 4 n2 n3))</span></p></td></tr></table>
```
And now when we print it:

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">&gt; n4</span></p></td></tr><tr><td><p><span class="stt">(nd 4 (nd 2 #0=(mt) #1=(nd 1 #0# #0#)) (nd 3 #1# #0#))</span></p></td></tr></table>
```
And now you can see there are two different shared values, one is the single
instance of mt, the other is the nd with 1 in it. Thus, Racket
uses both #0= / #0# and #1= / #1#. Notice how all the
leaves are sharing the same mt instance. (The numbering is picked in the
order in which nodes are encountered while traversing, which is why the nd
instance was #0 the previous time and is #1 this time.)
