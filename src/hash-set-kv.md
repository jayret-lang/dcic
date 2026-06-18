---
title: Hashes, Sets, and Key-Values
section_number: 18.4
source_file: hash-set-kv.html
prev: union-find.html
up: part_sets.html
next: orderability.html
---

```{=html}
<a name="(part._hash-set-kv)"></a>
```

### 18.4 Hashes, Sets, and Key-Values {#hash-set-kv}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._hash-string%29">18.4.1<span class="hspace"> </span>A Hash Function for Strings</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._.Sets_from_.Hashing%29">18.4.2<span class="hspace"> </span>Sets from Hashing</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._.Arrays%29">18.4.3<span class="hspace"> </span>Arrays</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._hash-tables%29">18.4.4<span class="hspace"> </span>Sets from Hashing and Arrays</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._.Collisions%29">18.4.5<span class="hspace"> </span>Collisions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._.Resolving_.Collisions%29">18.4.6<span class="hspace"> </span>Resolving Collisions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._hash-comp%29">18.4.7<span class="hspace"> </span>Complexity</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._bloom-filters%29">18.4.8<span class="hspace"> </span>Bloom Filters</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="hash-set-kv.html#%28part._.Generalizing_from_.Sets_to_.Key-.Values%29">18.4.9<span class="hspace"> </span>Generalizing from Sets to Key-Values</a></p></td></tr></table>
```

We have seen several solutions to set membership
[[Several Variations on Sets](part_sets.html)]. In particular, trees
[[Making Sets Grow on Trees](sets-from-trees.html)] gave us logarithmic complexity for
insection and membership.
Now we will see one more implementation of sets, with different
complexity. To set this up, we assume you are familiar with the
concept of hashing [[Converting Values to Ordered Values](orderability.html##hashing-values)], which we saw
was useful for constructing search trees. Here, we
will use it to construct sets in a very different way.
We will then generalize sets to another important data
structure: key-value repositories. But first…

```{=html}
<a name="(part._hash-string)"></a>
```

#### 18.4.1 A Hash Function for Strings {#hash-string}

As we have seen in [Converting Values to Ordered Values](orderability.html##hashing-values), we have multiple
strategies for converting arbitrary values into numbers, which we will
rely on here. Therefore, we could write this material around numbers
alone. To make the examples more interesting, and to better illustrate
some real-world issues, we will instead use strings. To hash them, we
will use `hash-of`{.pyret}, defined there, which simply adds up a
string’s code points.

We use this function for multiple reasons. First, it is sufficient to
illustrate some of the consequences of hashing. Second, in practice,
when built-in hashing does not suffice, we do write (more complex
versions of) functions like it. And finally, because it’s all laid
bare, it’s easy for us to experiment with.

```{=html}
<a name="(part._Sets-from-Hashing)"></a>
```

#### 18.4.2 Sets from Hashing {#Sets-from-Hashing}

Suppose we are given a set of strings. We can hash each element of
that set. Each string is now mapped to a number. Each of these numbers
is a member of the set; every other number is not a member of this
set.

Therefore, a simple representation is to just store this list of numbers. For instance, we can store the list
`[list: "Hello", "World!", "🏴‍☠️"] as [list: 500, 553, 195692]`{.pyret}.

Unfortunately, this does not help very much. Insertion can be done in
constant time, but checking membership requires us to traverse the
entire list, which takes linear time in the worst case. Alternatively,
maybe we have some clever scheme that involves sorting the list. But
note:


- inserting the element can now take as much as linear time; or,

- we store the elements as a tree instead of a list, but then
  
  1. we have to make sure the tree is balanced, so

  2. we will have essentially reconstructed the BBST.

In other words, we are recapitulating the discussion from
[Representing Sets as Lists](sets-from-lists.html) and [Making Sets Grow on Trees](sets-from-trees.html).

Notice that the problem here is traversal: if we have to visit
more than a constant number of elements, we have probably not
improved anything over the BBST. So, given a hash, how can we perform
only a constant amount of work? For that, lists and trees don’t work:
they both require at least some amount of (non-constant) traversal to
get to an arbitrary element. Instead we need a different data
structure…

```{=html}
<a name="(part._Arrays)"></a>
```

#### 18.4.3 Arrays {#Arrays}

Arrays are another linear data structure, like lists. There are two
key differences between lists and arrays that reflect each one’s
strength and weakness.

The main benefit to arrays is that we can access any element in the
array in constant time. This is in contrast to lists where, to
get to the \(n\)th element, we have to first traverse the previous
\(n-1\) elements (using successive `rest`{.pyret}s).

However, this benefit comes at a cost. The reason arrays can support
constant-time access is because the size of an array is fixed
at creation time. Thus, while we can keep extending a list using link,
we cannot grow the size of an array “in place”; rather, we must make
a new array and copy the entire array’s content into the new array,
which takes linear time. (We can do a better job of this by using
[Halloween Analysis](amortized-analysis.html), but there is no real free ride.)

The arrays in Jayret are
[documented here](https://jayret-lang.github.io/docs/latest/arrays.html).
While not necessary in principle, it is conventional to think of
arrays as data structures that support mutation, and that is how we
will use them here.

```{=html}
<a name="(part._hash-tables)"></a>
```

#### 18.4.4 Sets from Hashing and Arrays {#hash-tables}

Okay, so now we have a strategy. When we want to insert a string into
the set, we compute its hash, go to the corresponding location in the
array, and record the presence of that string. If we want to check for
membership, we similarly compute its hash and see whether the
corresponding location has been set. Traditionally, each location in
the array is called a bucket, and this data structure is called
a hashtable.

```jayret
BUCKET-COUNT = 1000;
buckets = array-of(false, BUCKET-COUNT);
Object insert(String s) {
    h = hash-of(s);
    return buckets.set-now(h, true);
}
Object is-in(String s) {
    h = hash-of(s);
    return buckets.get-now(h);
}
```

Observe that if this were to work, we would have constant time
insertion and membership checking. Unfortunately, two things make this
plan untenable in general.

```{=html}
<a name="(part._Collisions)"></a>
```

#### 18.4.5 Collisions {#Collisions}

First, our choice of hash function. For the above scheme to work, two
different strings have to map to two different locations.

::: {.do-now}
Is the above hash function invertible?
:::

We just need to find two strings that have the same hash. Given the
definition of `hash-of`{.pyret}, it’s easy to see that any rearrangement of the
letters produces the same hash:

::: {.pyret-repl}
```jayret
hash-of("Hello");
```
``` output
500
```
:::

::: {.pyret-repl}
```jayret
hash-of("olleH");
```
``` output
500
```
:::

Similarly, this test suite passes:

```jayret
@Check void test() {
    assertEquals(hash-of("Hello"), hash-of("olleH"));
    assertEquals(hash-of("Where"), hash-of("Weird"));
    assertEquals(hash-of("Where"), hash-of("Wired"));
    assertEquals(hash-of("Where"), hash-of("Whine"));
}
```

When multiple values hash to the same location, we call this a
hash collision.

Hash-collisions are problematic! With the above hash function, we get:

```jayret
@Check void test() {
    insert("Hello");
    assertEquals(is-in("Hello"), true);
    assertEquals(is-in("Where"), false);
    assertEquals(is-in("elloH"), true);
}
```
where two of these tests are desirable but the third is definitely not.

Note that collisions are virtually inevitable. If we have uniformly
distributed data, then collisions show up sooner than we might
expect.[This follows from the reasoning behind what is
known as the
[birthday problem](http://en.wikipedia.org/wiki/Birthday_problem),
commonly presented as how many people need to be in a room before the
likelihood that two of them share a birthday exceeds some
percentage. For the likelihood to exceed half we need just 23 people!]{.margin-note}
Therefore, it is wise to prepare for the possibility of collisions.

The key is to know something about the distribution of hash
values. For instance, if we knew our hash values are all multiples of
10, then using a table size of 10 would be a terrible idea (because
all elements would hash to the same bucket, turning our hash table
into a list). In practice, it is common to use uncommon prime numbers
as the table size, since a random value is unlikely to have it as a
divisor. This does not yield a theoretical improvement (unless you can
make certain assumptions about the input, or work through the math
very carefully), but it works well in practice.[In
particular, since the typical hashing function uses memory addresses
for objects on the heap, and on most systems these addresses are
multiples of 4, using a prime like 31 is often a fairly good bet.]{.margin-note}

While collisions are probabilistic, and depend on the choice of hash
function, we have an even more fundamental and unavoidable reason for
collisions. We have to store an array of the largest possible hash
size. However, not only can hash values be very large (try to run
`insert("🏴‍☠️")`{.pyret} and see what happens), there isn’t even an a priori
limit to the size of a hash. This fundamentally flies in the face of
arrays, which must have a fixed size.

To handle arbitrarily large values, we:


- use an array size that is reasonable given our memory
  constraints

- use the remainder of the hash relative to the array’s
  size to find the bucket

That is:

```jayret
Object insert(String s) {
    h = hash-of(s);
    return buckets.set-now(num-remainder(h, BUCKET-COUNT), true);
}
Object is-in(String s) {
    h = hash-of(s);
    return buckets.get-now(num-remainder(h, BUCKET-COUNT));
}
```
This addresses the second problem: we can also store the pirate flag:

```jayret
@Check void test() {
    assertEquals(is-in("🏴‍☠️"), false);
    insert("🏴‍☠️");
    assertEquals(is-in("🏴‍☠️"), true);
}
```
Observe, however, we have simply created yet another source of
collisions: the remainder computation. If we have 10 buckets, then the
hashes 5, 15, 25, 35, … all refer to the same bucket. Thus, there are
two sources of collision, and we have to deal with them both.

```{=html}
<a name="(part._Resolving-Collisions)"></a>
```

#### 18.4.6 Resolving Collisions {#Resolving-Collisions}

Surprisingly or disappointingly, we have a very simple solution to the
collision problems. Each bucket is not a single Boolean value, but
rather a list of the actual values that hashed to that bucket. Then,
we just check for membership in that list.

First, we will abstract over finding the bucket number in
`insert`{.pyret} and `is-in`{.pyret}:

```jayret
Object index-of(String s) {
    return num-remainder(hash-of(s), BUCKET-COUNT);
}
```
Next, we change what is held in each bucket: not a Boolean, but rather
a list of the actual strings:

```jayret
buckets = array-of(empty, BUCKET-COUNT);
```
Now we can write the more nuanced membership checker:

```jayret
Object is-in(String s) {
    b = index-of(s);
    return member(buckets.get-now(b), s);
}
```
Similarly, when inserting, we first make sure the element isn’t already there (to avoid the complexity problems caused by having duplicates), and only then insert it:

```jayret
Object insert(String s) {
    b = index-of(s);
    l = buckets.get-now(b);
    when (not(member(l, s))) {
        buckets.set-now(b, link(s, l));
    }
}
```
Now our tests pass as intended:

```jayret
@Check void test() {
    insert("Hello");
    assertEquals(is-in("Hello"), true);
    assertEquals(is-in("Where"), false);
    assertEquals(is-in("elloH"), false);
}
```

```{=html}
<a name="(part._hash-comp)"></a>
```

#### 18.4.7 Complexity {#hash-comp}

Now we have yet another working implementation for (some primitives
of) sets. The use of arrays supposedly enables us to get constant-time
complexity. Yet we should feel at least some discomfort. After all,
the constant time applied when the arrays contained only Boolean
values. However, that solution was weak in two ways: it could not
handle hash-collisions by non-invertible hash functions, and it
required potentially enormous arrays. If we relaxed either assumption,
the implementation was simply wrong, in that it was easily
fooled by values that caused collisions either through hashing or
through computing the remainder.

The solution we have shown above is called hash chaining, where
“chain” refers to the list stored in each bucket. The benefit of
hash-chaining is that insertion can still be constant-time: it takes a
constant amount of time to find a bucket, and inserting can be as
cheap as link. Of course, this assumes that we don’t mind duplicates;
otherwise we will pay the same price we saw earlier in
[Representing Sets as Lists](sets-from-lists.html). But lookup takes time linear in the
size of the bucket (which, with duplicates, could be arbitrarily
larger relative to the number of distinct elements). And even if we
check for duplicates, we run the risk that most or even all the
elements could end up in the same bucket (e.g., suppose the elements
are `"Where"`{.pyret}, `"Weird"`{.pyret}, `"Wired"`{.pyret},
`"Whine"`{.pyret}). In that case, our sophisticated implementation
reduces to the list-based representation and its complexity!

There’s an additional subtlety here. When we check membership of the
string in the list of strings, we have to consider the cost of
comparing each pair of strings. In the worst case, that is
proportional to the length of the shorter string. Usually this is
bounded by a small constant, but one can imagine settings where this
is not guaranteed to be true. However, this same cost has to be borne
by all set implementations; it is not a new complexity introduced
here.

Thus, in theory, hash-based sets can support insertion and membership
in as little as constant time, and (ignoring the cost of string
comparisons) as much as linear time, where “linear” has the same
caveats about duplicates as the list-based representation. In many
cases—depending on the nature of the data and parameters set for the
array—they can be much closer to constant time. As a result, they
tend to be very popular in practice.

```{=html}
<a name="(part._bloom-filters)"></a>
```

#### 18.4.8 Bloom Filters {#bloom-filters}

Another way to improve the space and time complexity is to relax the
properties we expect of the operations. Right now, set membership
gives perfect answers, in that it answers `true`{.pyret} exactly when the
element being checked was previously inserted into the set. But
suppose we’re in a setting where we can accept a more relaxed notion
of correctness, where membership tests can “lie” slightly in one
direction or the other (but not both, because that makes the
representation almost useless). Specifically, let’s say that “no
means no” (i.e., if the set representation says the element isn’t
present, it really isn’t) but “yes sometimes means no” (i.e., if the
set representation says an element is present, sometimes it
might not be). In short, if the set says the element isn’t in it, this
should be guaranteed; but if the set says the element is present,
it may not be. In the latter case, we either need some
other—more expensive—technique to determine truth, or we might
just not care.

Where is such a data structure of use? Suppose we are building a Web
site that uses password-based authentication. Because many passwords
have been leaked in well-publicized breaches, it is safe to assume
that hackers have them and will guess them. As a result, we want to
not allow users to select any of these as passwords. We could use a
hash-table to reject precisely the known leaked passwords. But for
efficiency, we could use this imperfect hash instead. If it says
“no”, then we allow the user to use that password. But if it says
“yes”, then either they are using a password that has been leaked,
or they have an entirely different password that, purely by accident,
has the same hash value, but no matter; we can just disallow that
password as well.[A related use is for filtering out
malicious Web sites. The URL shortening system, bitly,
[uses it for this purpose](http://word.bitly.com/post/28558800777/dablooms-an-open-source-scalable-counting-bloom).
It’s also used by ad networks; here’s a
[talk](https://youtu.be/T3Bt9Tn6P5c?si=t8U33orccRCgkSw0&t=1277)
(the segment from about 20m to about 45m) about that.
 But sometimes, a Bloom filter is overkill,
 as this Cloudflare blog post
 [discusses](https://blog.cloudflare.com/when-bloom-filters-dont-bloom/)…]{.margin-note}

Another example is in updating databases or memory stores. Suppose we
have a database of records, which we update frequently. It is often
more efficient to maintain a journal of changes: i.e., a list
that sequentially records all the changes that have occurred. At some
interval (say overnight), the journal is “flushed”, meaning all
these changes are applied to the database proper. But that means every
read operation has become highly inefficient, because it has to check
the entire journal first (for updates) before accessing the
database. Again, here we can use this faulty notion of a hash table:
if the hash of the record locator says “no”, then the record
certainly hasn’t been modified and we go directly to the database; if
it says “yes” then we have to check the journal.

We have already seen a simple example implementation of this idea
earlier, when we used a single array, with modular arithmetic, to
represent the set. When an element was not present in the array, we
knew for a fact that it was definitely not present. When the array
indicated an element was present, we couldn’t be sure that what was
present was the exact value we were looking for. To get around this
uncertainty, we used chaining.

However, there is something else we could have done. Chaining costs
both space (to store all the actual values) and time (to look through
all the values). Suppose, instead, a bucket is only a Boolean
value. This results in a slightly useful, but potentially very
inaccurate, data structure; furthermore, it exhibits correlated
failure tied to the modulus.

But suppose we have not only one array, but several! When an element
is added to the set, it is added to each array; when checking for
membership, every array is consulted. The set only answers
affirmatively to membership if all the arrays do so.

Naturally, using multiple arrays offers absolutely no advantage if the
arrays are all the same size: since both insertion and lookup are
deterministic, all will yield the same answer. However, there is a
simple antidote to this: use different array sizes. In particular, by
using array sizes that are relatively prime to one another, we
minimize the odds of a clash (only hashes that are the product of all
the array sizes will fool the array).

This data structure, called a Bloom Filter, is a
probabilistic data structure. Unlike our earlier set data
structure, this one is not guaranteed to always give the right answer;
but contrary to the
[☛ space-time tradeoff](glossary.html#%28elem._glossary-space-time._tradeoff%29), we
save both space and time by changing the
problem slightly to accept incorrect answers. If we know something
about the distribution of hash values, and we have some acceptable
bound of error, we can design hash table sizes so that with high
probability, the Bloom Filter will lie within the acceptable error
bounds.

```{=html}
<a name="(part._Generalizing-from-Sets-to-Key-Values)"></a>
```

#### 18.4.9 Generalizing from Sets to Key-Values {#Generalizing-from-Sets-to-Key-Values}

Above, we focused on sets: that is, a string effectively mapped to a
Boolean value, indicating whether it was present or not. However,
there are many settings where it is valuable to associate one value
with another. For instance, given an identity number we might want to
pull up a person’s records; given a computer’s name, we might want to
retrieve its routing information; given a star’s catalog entry, we
might want its astronomical information. This kind of data structure
is so ubiquitous that it has several names, some of which are more
general and some implying specific implementations: key-value
store, associative array, hash map, dictionary,
etc.

In general, the names “key-value” and “dictionary” are useful
because they suggest a behavioral interface. In contrast,
associative array implies the use of arrays, and hash table suggests
the use of an array (and of hashing). In fact, real systems use a
variety of implementation strategies, including balanced binary search
trees. The names “key-value” and “dictionary” avoid commitment to
a particular implementation. Here, too, “dictionary” evokes a common
mental image of unique words that map to descriptions. The term “key
value” is even more technically useful because keys are meant to all
be distinct (i.e., no two different key-value pairs can have the same
key; alternatively, one key can map to only one value). This makes
sense because we view this as a generalization of sets, so the keys
are the set elements, which must necessarily have no duplicates; the
values take the place of the Boolean.

To extend our set representation to handle a dictionary or key-value
store, we need to make a few changes. First, we introduce the
key-value representation:

```jayret
data KV {
}
```
Each bucket is still an empty list, but we understand it to be a list of key-value pairs.

Previously, we only had `is-in`{.pyret} to check whether an element was
present in a set or not. That element is now the key, and we could
have a similar function to check whether the key is present. However,
we rarely want to know just that; in fact, because we already know the
key, we usually want the associated value.

Therefore, we can just have this one function:[We use Jayret’s naming convention of `-now`{.pyret} to indicate that this result might change later.]{.margin-note}

```jayret
/* contract: getkv-now :: Object */;
```
Of course, `getkv-now`{.pyret} may fail: the key may not be present. That is,
it has become a partial function [[Partial Domains](partial-domains.html)]. We
therefore have all the usual strategies for dealing with partial
functions. Here, for simplicity we choose to return an error if the
key is not present, but all the other strategies we discuss for
handling partiality are valid (and often better in a robust
implementation).

Similarly, we have:

```jayret
/* contract: setkv-now :: Object */;
```
This is the generalization of `insert`{.pyret}. However, `insert`{.pyret}
had no reason to return an error: inserting an element twice was
harmless. However, because keys must now be associated with only one
value, insertion has to check whether the key is already present, and
signal an error otherwise. In short, it is also
partial.[This is not partial due to a mathematical reason,
but rather because of state: the same key may have been inserted
previously.]{.margin-note}

Once we have agreed on this interface, getting a value is a natural
extension of checking for membership:

```jayret
Object getkv-now(k) {
    b = index-of(k);
    r = find((kvp) -> kvp.key == k, buckets.get-now(b));
    return switch (r) {
        case None: yield raise("getkv-now can't find " + k);
        case Some(v): yield v.value;
    }
}
```
Having found the index, we look in the bucket for whether any
key-value pair has the desired key. If it does, then we return the
corresponding value. Otherwise, we error.

Inserting a key-value pair similarly generalizes adding an element to the set:

```jayret
Object setkv-now(k, v) {
    b = index-of(k);
    keys = map(_.key, buckets.get-now(b));
    return if (member(keys, k)) {
        return raise("setkv-now already has a value for key " + k);
    } else {
        return buckets.set-now(b, link(kv(k, v), buckets.get-now(b)));
    }
}
```
Once again, we check the bucket for whether the key is already
present. If it is, we choose to halt with an error. Otherwise, we make
the key-value pair and link it to the existing bucket contents, and
modify the array to refer to the new list.

::: {.exercise}
Do the above pair of functions do all the necessary error-checking?
:::

::: {.exercise}
Above, `setkv-now`{.pyret} raises an error if a key already has a name associated with it.
A natural variation is to instead override the associated value, so that
the new value is now associated with that key. Modify the implementation to do that
instead, and make sure you test it thoroughly! Note that you may need to modify the
`KV`{.pyret} datatype also.
:::

This concludes our brief tour of sets (yet again!) and key-value
stores or dictionaries. We have chosen to implement both using arrays,
which required us to employ hashes. For more on string dictionaries,
see the
[Jayret
documentation](https://jayret-lang.github.io/docs/latest/string-dict.html). Observe that Jayret offers two kinds of dictionaries:
one mutable (like we have shown here) and one (the default)
functional.
