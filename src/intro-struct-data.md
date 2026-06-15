---
title: Introduction to Structured Data
section_number: 6.1
source_file: dcic_orig_intro-struct-data.html
prev: part_structured-data.html
up: part_structured-data.html
next: Collections_of_Structured_Data.html
---

### Introduction to Structured Data {#intro-struct-data}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.Understanding_the_.Kinds_of_.Compound_.Data%29">6.1.1<span class="hspace"> </span>Understanding the Kinds of Compound Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.A_.First_.Peek_at_.Structured_.Data%29">6.1.1.1<span class="hspace"> </span>A First Peek at Structured Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.A_.First_.Peek_at_.Conditional_.Data%29">6.1.1.2<span class="hspace"> </span>A First Peek at Conditional Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.Defining_and_.Creating_.Structured_and_.Conditional_.Data%29">6.1.2<span class="hspace"> </span>Defining and Creating Structured and Conditional Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._struct-data-eg%29">6.1.2.1<span class="hspace"> </span>Defining and Creating Structured Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.Annotations_for_.Structured_.Data%29">6.1.2.2<span class="hspace"> </span>Annotations for Structured Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.Defining_and_.Creating_.Conditional_.Data%29">6.1.2.3<span class="hspace"> </span>Defining and Creating Conditional Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.Programming_with_.Structured_and_.Conditional_.Data%29">6.1.3<span class="hspace"> </span>Programming with Structured and Conditional Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._.Extracting_.Fields_from_.Structured_.Data%29">6.1.3.1<span class="hspace"> </span>Extracting Fields from Structured Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._telling-apart-variants%29">6.1.3.2<span class="hspace"> </span>Telling Apart Variants of Conditional Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-struct-data.html#%28part._process-fields-variants%29">6.1.3.3<span class="hspace"> </span>Processing Fields of Variants</a></p></td></tr></table>
```

Earlier we had our first look at types. Until now, we have only seen
the types that Pyret provides us, which is an interesting but
nevertheless quite limited set. Most programs we write will contain
many more kinds of data.

#### Understanding the Kinds of Compound Data {#Understanding-the-Kinds-of-Compound-Data}

##### A First Peek at Structured Data {#A-First-Peek-at-Structured-Data}

There are times when a datum has many attributes, or parts. We
need to keep them all together, and sometimes take them apart. For
instance:


- An iTunes entry contains a bunch of information about a single
  song: not only its name but also its singer, its length, its genre,
  and so on.
  
  ![](itunes-1.png){width="1112" height="60"}
- Your GMail application contains a bunch of information about a
  single message: its sender, the subject line, the conversation it’s
  part of, the body, and quite a bit more.
  
  ![](gmail-1.png){width="1136" height="46"}

In examples like this, we see the need for structured data: a
single datum has structure, i.e., it
actually consists of many pieces. The number of pieces is
fixed, but may be of different kinds (some might be numbers,
some strings, some images, and different types may be mixed together
in that one datum). Some might even be other structured data:
for instance, a date usually has at least three parts, the day, month,
and year. The parts of a structured datum are called its fields.

##### A First Peek at Conditional Data {#A-First-Peek-at-Conditional-Data}

Then there are times when we want to represent different kinds of
data under a single, collective umbrella. Here are a few examples:


- A traffic light can be in different states: red, yellow, or
  green.[Yes, in some countries there are different or more
  colors and color-combinations.]{.margin-note} Collectively, they represent one
  thing: a new type called a traffic light state.
- A zoo consists of many kinds of animals. Collectively, they
  represent one thing: a new type called an animal. Some condition
  determines which particular kind of animal a zookeeper might be dealing
  with.
- A social network consists of different kinds of pages. Some
  pages represent individual humans, some places, some organizations,
  some might stand for activities, and so on. Collectively, they
  represent a new type: a social media page.
- A notification application may report many kinds of events. Some
  are for email messages (which have many fields, as we’ve discussed),
  some are for reminders (which might have a timestamp and a note), some
  for instant messages (similar to an email message, but without a
  subject), some might even be for the arrival of a package by physical
  mail (with a timestamp, shipper, tracking number, and delivery
  note). Collectively, these all represent a new type: a notification.

We call these “conditional” data because they represent an “or”: a
traffic light is red or green or yellow; a social
medium’s page is for a person or location or
organization; and so on. Sometimes we care exactly which kind of thing
we’re looking at: a driver behaves differently on different colors,
and a zookeeper feeds each animal differently. At other times, we
might not care: if we’re just counting how many animals are in the
zoo, or how many pages are on a social network, or how many unread
notifications we have, their details don’t matter. Therefore, there are
times when we ignore the conditional and treat the datum as a member
of the collective, and other times when we do care about the
conditional and do different things depending on the individual
datum. We will make all this concrete as we start to write programs.

#### Defining and Creating Structured and Conditional Data {#Defining-and-Creating-Structured-and-Conditional-Data}

We have used the word “data” above, but that’s actually been a bit
of a lie. As we said earlier, data are how we represent
information in the computer. What we’ve been discussing above is
really different kinds of information, not exactly how they are
represented. But to write programs, we must wrestle concretely with
representations. That’s what we will do now, i.e., actually show
data representations of all this information.

##### Defining and Creating Structured Data {#struct-data-eg}

Let’s start with defining structured data, such as an iTunes song
record. Here’s a simplified version of the information such an app
might store:


- The song’s name, which is a `String`{.pyret}.
- The song’s singer, which is also a `String`{.pyret}.
- The song’s year, which is a `Number`{.pyret}.

Let’s now introduce the syntax by which we can teach this to Pyret:

```pyret
data ITunesSong: song(name, singer, year) end
```
This tells Pyret to introduce a new type of data, in this case
called `ITunesSong`{.pyret}[We follow a convention that types
always begin with a capital letter.]{.margin-note}. The way we actually make one of
these data is by calling `song`{.pyret} with three parameters; for
instance:[It’s worth noting that music managers that are
capable of making distinctions between, say, Dance, Electronica, and
Electronic/Dance, classify two of these three songs by a single genre:
“World”.]{.margin-note}
<structured-examples> ::=
```pyret
song("La Vie en Rose", "Édith Piaf", 1945)
song("Stressed Out", "twenty one pilots", 2015)
song("Waqt Ne Kiya Kya Haseen Sitam", "Geeta Dutt", 1959)
```
Always follow a data definition with a few concrete instances of the
data! This makes sure you actually do know how to make data of that
form. Indeed, it’s not essential but a good habit to give names to the
data we’ve defined, so that we can use them later:

```pyret
lver = song("La Vie en Rose", "Édith Piaf", 1945)
so = song("Stressed Out", "twenty one pilots", 2015)
wnkkhs = song("Waqt Ne Kiya Kya Haseen Sitam", "Geeta Dutt", 1959)
```

In terms of the directory, structured data are no different from
simple data. Each of the three definitions above creates an entry in
the directory, as follows:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">lver</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">song("La Vie en Rose", "Édith Piaf", 1945)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">so</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">song("Stressed Out", "twenty one pilots", 2015)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">wnkkhs</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">song("Waqt Ne Kiya Kya Haseen Sitam","Geeta Dutt", 1959)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

##### Annotations for Structured Data {#Annotations-for-Structured-Data}

Recall that in [[Type Annotations](From_Repeated_Expressions_to_Functions.html##fun-annotations)] we discussed annotating our functions. Well, we
can annotate our data, too! In particular, we can annotate both the
definition of data and their creation. For the former,
consider this data definition, which makes the annotation information
we’d recorded informally in text a formal part of the program:

```pyret
data ITunesSong: song(name :: String, singer :: String, year :: Number) end
```
Similarly, we can annotate the variables bound to examples of the
data. But what should we write here?

```pyret
lver :: ___ = song("La Vie en Rose", "Édith Piaf", 1945)
```
Recall that annotations takes names of types, and the new type we’ve
created is called `ITunesSong`{.pyret}. Therefore, we should write

```pyret
lver :: ITunesSong = song("La Vie en Rose", "Édith Piaf", 1945)
```

::: {.do-now}
What happens if we instead write this?

```pyret
lver :: String = song("La Vie en Rose", "Édith Piaf", 1945)
```
What error do we get? How about if instead we write these?

```pyret
lver :: song = song("La Vie en Rose", "Édith Piaf", 1945)
lver :: 1 = song("La Vie en Rose", "Édith Piaf", 1945)
```
Make sure you familiarize yourself with the error messages that you
get.
:::

##### Defining and Creating Conditional Data {#Defining-and-Creating-Conditional-Data}

The `data`{.pyret} construct in Pyret also lets us create conditional
data, with a slightly different syntax. For instance, say we want to
define the colors of a traffic light:

```pyret
data TLColor:
  | Red
  | Yellow
  | Green
end
```
[Conventionally, the names of the options begin in
lower-case, but if they have no additional structure, we often
capitalize the initial to make them look different from ordinary
variables: i.e., `Red`{.pyret} rather than `red`{.pyret}.]{.margin-note}
Each `|`{.pyret} (pronounced “stick”) introduces another option. You
would make instances of traffic light colors as

```pyret
Red
Green
Yellow
```

A more interesting and common example is when each condition has some
structure to it; for instance:

```pyret
data Animal:
  | boa(name :: String, length :: Number)
  | armadillo(name :: String, liveness :: Boolean)
end
```
[“In Texas, there ain’t nothin’ in the middle of the road
except yellow stripes and a dead armadillo.”—Jim Hightower]{.margin-note}
We can make examples of them as you would expect:

```pyret
b1 = boa("Ayisha", 10)
b2 = boa("Bonito", 8)
a1 = armadillo("Glypto", true)
```
We call the different conditions variants.

::: {.do-now}
How would you annotate the three variable bindings?
:::

Notice that the distinction between boas and armadillos is lost in the
annotation.

```pyret
b1 :: Animal = boa("Ayisha", 10)
b2 :: Animal = boa("Bonito", 8)
a1 :: Animal = armadillo("Glypto", true)
```

When defining a conditional datum the first stick is actually
optional, but adding it makes the variants line up nicely. This helps
us realize that our first example

```pyret
data ITunesSong: song(name, singer, year) end
```
is really just the same as

```pyret
data ITunesSong:
  | song(name, singer, year)
end
```
i.e., a conditional type with just one condition, where that one
condition is structured.

#### Programming with Structured and Conditional Data {#Programming-with-Structured-and-Conditional-Data}

So far we’ve learned how to create structured and conditional data,
but not yet how to take them apart or write any expressions that
involve them. As you might expect, we need to figure out how to


- take apart the fields of a structured datum, and
- tell apart the variants of a conditional datum.

As we’ll see, Pyret also gives us a convenient way to do both
together.

##### Extracting Fields from Structured Data {#Extracting-Fields-from-Structured-Data}

Let’s write a function that tells us how old a song is. First, let’s
think about what the function consumes (an `ITunesSong`{.pyret}) and
produces (a `Number`{.pyret}). This gives us a rough skeleton for the
function:
<song-age> ::=
```pyret
fun song-age(s :: ITunesSong) -> Number:
  <song-age-body>
end
```
We know that the form of the body must be roughly:
<song-age-body> ::=
```pyret
2016 - <get the song year>
```
We can get the song year by using Pyret’s field access, which is
a `.`{.pyret} followed by a field’s name—in this case,
`year`{.pyret}—following the variable that holds the structured
datum. Thus, we get the `year`{.pyret} field of `s`{.pyret} (the parameter
to `song-age`{.pyret}) with

```pyret
s.year
```
So the entire function body is:

```pyret
fun song-age(s :: ITunesSong) -> Number:
  2016 - s.year
end
```
It would be good to also record some examples
([<structured-examples>](intro-struct-data.html#%28elem._structured-examples%29)), giving us a comprehensive
definition of the function:

```pyret
fun song-age(s :: ITunesSong) -> Number:
  2016 - s.year
where:
  song-age(lver) is 71
  song-age(so) is 1
  song-age(wnkkhs) is 57
end
```

##### Telling Apart Variants of Conditional Data {#telling-apart-variants}

Now let’s see how we tell apart variants. For this, we again use
`cases`{.pyret}, as we saw for lists. We create one branch for each of
the variants. Thus, if we wanted to compute advice for a driver based on a
traffic light’s state, we might write:

```pyret
fun advice(c :: TLColor) -> String:
  cases (TLColor) c:
    | Red => "wait!"
    | Yellow => "get ready..."
    | Green => "go!"
  end
end
```

::: {.do-now}
What happens if you leave out the `=>`{.pyret}?
:::

::: {.do-now}
What if you leave out a variant? Leave out the `Red`{.pyret} variant,
then try both `advice(Yellow)`{.pyret} and `advice(Red)`{.pyret}.
:::

##### Processing Fields of Variants {#process-fields-variants}

In this example, the variants had no fields. But if the variant has
fields, Pyret expects you to list names of variables for those fields,
and will then automatically bind those variables—so you don’t need
to use the `.`{.pyret}-notation to get the field values.

To illustrate this, assume we want to get the name of any animal:
<animal-name> ::=
```pyret
fun animal-name(a :: Animal) -> String:
  <animal-name-body>
end
```
Because an `Animal`{.pyret} is conditionally defined, we know that we are
likely to want a `cases`{.pyret} to pull it apart; furthermore, we should
give names to each of the fields:[Note that the names of the
variables do not have to match the names of
fields. Conventionally, we give longer, descriptive names to
the field definitions and short names to the corresponding variables.]{.margin-note}

<animal-name-body> ::=
```pyret
cases (Animal) a:
  | boa(n, l) => ...
  | armadillo(n, l) => ...
end
```

In both cases, we want to return the field `n`{.pyret}, giving us the
complete function:

```pyret
fun animal-name(a :: Animal) -> String:
  cases (Animal) a:
    | boa(n, l) => n
    | armadillo(n, l) => n
  end
where:
  animal-name(b1) is "Ayisha"
  animal-name(b2) is "Bonito"
  animal-name(a1) is "Glypto"
end
```

Let’s look at how Pyret would evaluate a function call like

```pyret
animal-name(boa("Bonito", 8))
```
The argument `boa("Bonito", 8)`{.pyret} is a value. In the same way as we
substitute simple data types like strings and numbers for parameters
when we evaluate a function, we do the same thing here. After
substituting, we are left with the following expression to evaluate:

```pyret
cases (Animal) boa("Bonito", 8):
  | boa(n, l) => n
  | armadillo(n, l) => n
end
```

Next, Pyret determines which case matches the data (the first one, for
`boa`{.pyret}, in this case). It then substitutes the field names with the
corresponding components of the datum result expression for the
matched case. In this case, we will substitute uses of `n`{.pyret} with
`"Bonito"`{.pyret} and uses of `l`{.pyret} with `8`{.pyret}. In this program,
the entire result expression is a use of `n`{.pyret}, so the result of
the program in this case is `"Bonito"`{.pyret}.
