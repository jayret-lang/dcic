---
title: Equality, Ordering, and Hashing
section_number: 18.5
source_file: orderability.html
prev: hash-set-kv.html
up: part_sets.html
next: sets-case-study.html
---

```{=html}
<a name="(part._orderability)"></a>
```

### 18.5 Equality, Ordering, and Hashing {#orderability}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="orderability.html#%28part._hashing-values%29">18.5.1<span class="hspace"> </span>Converting Values to Ordered Values</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="orderability.html#%28part._hash-in-practice%29">18.5.2<span class="hspace"> </span>Hashing in Practice</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="orderability.html#%28part._eq-ord%29">18.5.3<span class="hspace"> </span>Equality and Ordering</a></p></td></tr></table>
```

```{=html}
<a name="(part._hashing-values)"></a>
```

#### 18.5.1 Converting Values to Ordered Values {#hashing-values}

In [Making Sets Grow on Trees](sets-from-trees.html), we noted that a single comparison needs
to eliminate an entire set of values. With numbers, we were able to
accomplish that easily: every bigger or smaller number was excluded by
a comparison. But what if the data in the set are not actually
numbers? Then we have to convert an arbitrary datum into a datatype that
permits such comparison. This is known as hashing.

A hash function consumes an arbitrary value and produces a comparable
representation of it (its hash)—most commonly (but not
strictly necessarily), a number. A hash function must naturally be
deterministic: a fixed value should always yield the same hash
(otherwise, we might conclude that an element in the set is not
actually in it, etc.). Particular uses may need additional properties,
as we discuss in [Equality and Ordering](orderability.html##eq-ord).

Let us now consider how one can compute hashes. If the input datatype
is a number, it can serve as its own hash. Comparison simply uses
numeric comparison (e.g., `<`{.jayret}). Then, transitivity of `<`{.jayret}
ensures that if an element \(A\) is less than another element \(B\),
then \(A\) is also less than all the other elements bigger than
\(B\).

Suppose instead the input is a string. We can of course use the
principle above for strings: e.g., replacing number inequality with
string inequality. Strings have a lexicographic (or
“alphabetic”) ordering that permit them to be treated similar to
numbers.

But what if we are handed more complex datatypes?

Before we answer that, consider that in practice numbers are more
efficient to compare than strings (since comparing two numbers is very
nearly constant time). Thus, although we could use strings directly,
it may be convenient to find a numeric representation of
strings. We convert each character of the string
into a number, e.g., using its
[code point](https://en.wikipedia.org/wiki/Code_point).
Based on that, here are two different hash functions:


1. Consider a list of primes as long as the string. Raise each
  prime by the corresponding number, and multiply the result. For
  instance, if the string is represented by the character codes
  `[6, 4, 5]`{.jayret} (the first character has code `6`{.jayret}, the second
  one `4`{.jayret}, and the third `5`{.jayret}), we get the hash
  
  ```jayret
num-expt(2, 6) * num-expt(3, 4) * num-expt(5, 5);
  ```
  or `16200000`{.jayret}.
2. Simply add together all the character codes. For the above
  example, this would correspond to the has
  
  ```jayret
6 + 4 + 5;
  ```
  or `15`{.jayret}.

The first representation is invertible, using the
[Fundamental Theorem of Arithmetic](http://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic):
given the resulting number, we can reconstruct the input unambiguously
(i.e., `16200000`{.jayret} can only map to the input above, and none other).
This is also known as the Gödel encoding. This is
computationally expensive.
The second encoding is, of course, not invertible (e.g., simply
permute the characters and, by commutativity, the sum will be the
same), but computationally much cheaper. It is also easy to implement:

```jayret
Object hash-of(String s) {
    return fold((int a, int b) -> a + b, 0, string-to-code-points(s));
}
@Check void test() {
    assertEquals(hash-of("Hello"), 500);
    assertEquals(hash-of("World!"), 553);
    assertEquals(hash-of("🏴‍☠️"), 195692);
}
```

Now let us consider more general datatypes. The principle of hashing
will be similar. If we have a datatype with several variants, we can
order the variants lexicographically, and use a numeric tag to
represent the variants, and recursively encode the datum and the
variant tag. For each field of a record, we need an ordering of the
fields—the lexicographic ordering of the field names suffices—and
must hash their contents recursively; having done so, we get in effect
a string of numbers, which we have shown how to handle.

The critical thing to remember is that we don’t actually need a
meaningful operation.[Observe that Gödel encodings
are not “meaningful”, either.]{.margin-note} We don’t actually care if a hash
function concludes that the hash of `4`{.jayret} is less than the hash of
`3`{.jayret}! All we need is a function that is


- non-trivial: not everything should be equal; and

- deterministic: every time we ask for a hash, we should get
  the same answer.

::: {.exercise}
Why do we care about these two properties? Think about what would could go
wrong if each one was violated.
:::

```{=html}
<a name="(part._hash-in-practice)"></a>
```

#### 18.5.2 Hashing in Practice {#hash-in-practice}

In practice, programmers do not want hash functions to do what we have
described above. While Gödel encoding is extremely expensive, even
computing `hash-of`{.jayret} takes time linear in the size of a string,
which can get quite expensive if strings are large or we compute
hashes often or both.

Instead, many programming languages do something very pragmatic. They
need a value that can be compared for equality and ordering
[[Equality and Ordering](orderability.html##eq-ord)]. Integers, we’ve already seen, already fit this
bill very nicely. But how to obtain an integer out of arbitrary
values, even datatype instances, quickly?

Simple: They just use the memory address of the datum. Every
value has a memory address, and the language can obtain it in constant
time by looking up the directory. Granted, these values may be
allocated anywhere with respect to each other, but that’s okay—we
only want consistency, not “meaningfulness”.

In practice, however, things are not quite so simple. For instance,
suppose we want two structurally equivalent values to have the same
hash. If they are allocated in different addresses, they will hash
differently. Therefore, many languages that use such a strategy also
allow programmers to write their own hashing functions, often to work
in conjunction with this built-in notion of hashing. These end up
looking not too different from the hashing strategies we described
above. Therefore, some of that complexity is inescapable, especially
if a programmer wants structural rather than reference
equality—which they very often do.

In the rest of this material, we will therefore continue with the
simple hash function above, for multiple reasons. First, it is
sufficient to illustrate how hashing works. Second, in practice, when
built-in hashing does not suffice, we do write (more complex versions
of) functions like the above. And finally, because it’s all laid bare,
it’s easy for us to experiment with.

```{=html}
<a name="(part._eq-ord)"></a>
```

#### 18.5.3 Equality and Ordering {#eq-ord}

What we’ve seen [[A Fine Balance: Tree Surgery](sets-from-trees.html##sets-from-balanced-trees)] for the construction of
balanced binary search trees is that we need some way of putting elements in
order. In the examples we used numbers because they’re a very friendly
datatype: they have several properties that we take for granted. However, not
all data have these properties.

The critical property that numbers have is that they are orderable. This
follows because they are comparable, and the comparison is
ternary: it produces three answers, “less than”, “equal to”, and
“greater than”.

However, not all data have this property. What are data that might not have
these properties? Actually, there are multiple possible properties here: Is
something orderable? Is something even comparable?

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p> </p></td><td><p><span class="hspace">  </span></p></td><td><p><span style="font-weight: bold">Comparable</span></p></td><td><p><span class="hspace">  </span></p></td><td><p><span style="font-weight: bold">Orderable</span></p></td></tr><tr><td><p>Numbers</p></td><td><p><span class="hspace">  </span></p></td><td><p>Yes (but not Roughnums!)</p></td><td><p><span class="hspace">  </span></p></td><td><p>Yes</p></td></tr><tr><td><p>Booleans</p></td><td><p><span class="hspace">  </span></p></td><td><p>Yes</p></td><td><p><span class="hspace">  </span></p></td><td><p>Yes</p></td></tr><tr><td><p>Data instances</p></td><td><p><span class="hspace">  </span></p></td><td><p>Yes</p></td><td><p><span class="hspace">  </span></p></td><td><p>Not by default</p></td></tr><tr><td><p>Roughnums</p></td><td><p><span class="hspace">  </span></p></td><td><p>No</p></td><td><p><span class="hspace">  </span></p></td><td><p>Yes</p></td></tr><tr><td><p>Functions</p></td><td><p><span class="hspace">  </span></p></td><td><p>Not really</p></td><td><p><span class="hspace">  </span></p></td><td><p>No</p></td></tr></table>
```

So…life is complicated.

That means you could potentially misuse a BBST on the wrong kind of
data. Ideally, we would want to know if we’re doing this. In Jayret’s type
system we chose not to build this in, but in some languages, the type system
actually lets you capture these properties.

In Haskell, for instance, there’s a mechanism called the type-class; in Java,
there are interfaces. They aren’t really the same, but they’re useful to
conflate for our purposes. Only things that meet a particular interface or type
class provide certain operations. For instance, in Haskell, if you want to use
== or /= (not equal), you have to be in the Eq
type-class. Thus the comparable datatypes above would be part of
Eq. Similarly, there’s a type-class Ord, which ensures the
availability of (and requires the implementation of) operations like <,
>, <=, and >=. In Haskell, everything that is Ord
must also be Eq, i.e., Eq is weaker than Ord (things can
be Eq without being Ord). Jayret’s Roughnums contradict that…but
Haskell is okay with it. But if you try to compare two functions in Haskell,

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">(\x -&gt; x + 1) &lt; (\x -&gt; x)</span></p></td></tr></table>
```
you get an error like

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">* No instance for (Ord (Integer -&gt; Integer))</span></p></td></tr><tr><td><p><span class="stt"></span><span class="hspace">    </span><span class="stt">arising from a use of `&lt;'</span></p></td></tr></table>
```
