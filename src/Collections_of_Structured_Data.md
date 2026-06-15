---
title: Collections of Structured Data
section_number: 6.2
source_file: Collections_of_Structured_Data.html
prev: intro-struct-data.html
up: part_structured-data.html
next: part_trees.html
---

### Collections of Structured Data {#Collections-of-Structured-Data}

As we were looking at structured data [[Introduction to Structured Data](intro-struct-data.html)],
we came across several situations where we have not one but many data:
not one song but a playlist of them, not one animal but a zoo full of
them, not one notification but several, not just one message (how we
wish!) but many in our inbox, and so on. In general, then, we rarely
have just a single structured datum: [One notable exception:
consider the configuration or preference information for a
system. This might be stored in a file and updated through a user
interface. Even though there is (usually) only one configuration at a
time, it may have so many pieces that we won’t want to clutter our
program with a large number of variables; instead, we might create a
structure representing the configuration, and load just one instance
of it. In effect, what would have been unconnected variables
now become a set of linked fields.]{.margin-note} if we know we have only
one, we might just have a few separate variables representing the
pieces without going to the effort of creating and taking apart a
structure. In general, therefore, we want to talk about
collections of structured data. Here are more examples:


- The set of messages matching a tag.
- The list of messages in a conversation.
- The set of friends of a user.

::: {.do-now}
How are collective data different from structured data?
:::

In structured data, we have a fixed number of possibly
different kinds of values. In collective data, we have a
variable number of the same kind of value. For instance, we
don’t say up front how many songs must be in a playlist or how many
pages a user can have; but every one of them must be a song or a
page. (A page may, of course, be conditionally defined, but
ultimately everything in the collection is still a page.)

Observe that we’ve mentioned both sets and lists
above. The difference between a set and a list is that a set has no
order, but a list has an order. This distinction is not vital now but
we will return to it later [[Sets as Collective Data](Collections_of_Structured_Data.html##sets-as-collections)].

Of course, sets and lists are not the only kinds of collective data we
can have. Here are some more:


- A family tree of people.
- The filesystem on your computer.
- A seating chart at a party.
- A social network of pages.

and so on. For the most part these are just as easy to program and
manipulate as the earlier collective data once we have some
experience, though some of them [[Re-Examining Equality](Sharing_and_Equality.html##identical-eq)] can involve more subtlety.

We have already seen tables [[Introduction to Tabular Data](intro-tabular-data.html)], which are
a form of collective, structured data. Now we will look at a few more,
and how to program them.

#### Lists as Collective Data {#Lists-as-Collective-Data}

We have already seen one example of a collection in
some depth before: lists. A list is not limited to numbers or strings;
it can contain any kind of value, including structured ones. For
instance, using our examples from earlier [[Defining and Creating Structured Data](intro-struct-data.html##struct-data-eg)],
we can make a list of songs:

```pyret
song-list = [list: lver, so, wnkkhs]
```
This is a three-element list where each element is a song:

```pyret
check:
  song-list.length() is 3
  song-list.first is lver
end
```

Thus, what we have seen earlier about building functions over lists
[[Processing Lists](processing-lists.html)] applies here too. To illustrate, suppose
we wish to write the function `oldest-song-age`{.pyret}, which consumes a
list of songs and produces the oldest song in the list. (There may be
more than one song from the same year; the age—by our measure—of
all those songs will be the same. If this happens, we just pick one of
the songs from the list. Because of this, however, it would be more
accurate to say “an” rather than “the” oldest song.)

Let’s work through this with examples. To keep our examples easy to
write, instead of writing out the full data for the songs, we’ll refer
to them just by their variable names. Clearly, the oldest song in our
list is bound to `lvar`{.pyret}.

```pyret
oldest-song([list: lver, so, wnkkhs]) is lvar
oldest-song([list:       so, wnkkhs]) is wnkkhs
oldest-song([list:           wnkkhs]) is wnkkhs
oldest-song([list:                 ]) is ???
```

What do we write in the last case? Recall that we saw this problem
earlier [[`my-max`{.pyret}: Examples](processing-lists.html##my-max)]: there is no answer in the empty case. In
fact, the computation here is remarkably similar to that of
`my-max`{.pyret}, because it is essentially the same computation, just
asking for the minimum year (which would make the song the
oldest).

From our examples, we can see a solution structure echoing that of
`my-max`{.pyret}. For the empty list, we signal an error. Otherwise, we
compute the oldest song in the rest of the list, and compare its year
against that of the first. Whichever has the older year is the answer.

```pyret
fun oldest-song(sl :: List<ITunesSong>) -> ITunesSong:
  cases (List) sl:
    | empty => raise("not defined for empty song lists")
    | link(f, r) =>
      cases (List) r:
        | empty => f
        | else =>
          osr = oldest-song(r)
          if osr.year < f.year:
            osr
          else:
            f
          end
      end
  end
end
```

Note that there is no guarantee there will be only oldest song, and
this is reflected in the possibility that `osr.year`{.pyret} may
equal `f.year`{.pyret}. However, our problem statement allowed us
to pick just one such song, which is what we’ve done.

::: {.do-now}
Modify the solution above to `oldest-song-age`{.pyret}, which computes
the age of the oldest song(s).
:::

Haha, just kidding! You shouldn’t modify the previous solution at all!
Instead, you should leave it alone—it may come in handy for other
purposes—and instead build a new function to use it:

```pyret
fun oldest-song-age(sl :: List<ITunesSong>) -> Number:
  os = oldest-song(sl)
  song-age(os)
where:
  oldest-song-age(song-list) is 71
end
```

#### Sets as Collective Data {#sets-as-collections}

As we’ve already seen, for some problems we don’t care about the order
of inputs, nor about duplicates. Here are more examples where we don’t
care about order or duplicates:


- Your Web browser records which Web pages you’ve
  visited, and some Web sites use this information to color visited
  links differently than ones you haven’t seen. This color is typically
  independent of how many times you have visited the page.
- During an election, a poll agent might record that you have
  voted, but does not need to record how many times you have voted, and
  does not care about the order in which people vote.

For such problems a list is a bad fit relative to a set. Here we will
see how Pyret’s built-in sets work. In
[[Several Variations on Sets](part_sets.html)] we will see how we can build sets for
ourselves.

First, we can define sets just as easily as we can lists:

```pyret
import sets as S
song-set = [S.set: lver, so, wnkkhs]
```
Of course, due to the nature of the language’s syntax, we have to
list the elements in some order. Does it matter?

::: {.do-now}
How can we tell whether Pyret cares about the order?
:::

Here’s the simplest way to check:

```pyret
check:
  song-set2 = [S.set: so, wnkkhs, lver]
  song-set is song-set2
end
```
If we want to be especially cautious, we can write down all the other
orderings of the elements as well, and see that Pyret doesn’t
care.

::: {.exercise}
How many different orders are there?
:::

Similarly for duplicates:

```pyret
check:
  song-set3 = [S.set: lver, so, wnkkhs, so, so, lver, so]
  song-set is song-set3
  song-set3.size() is 3
end
```
We can again try several different kinds of duplication and confirm
that sets ignore them.

##### Picking Elements from Sets {#coll-sd-pick}

This lack of an ordering, however, poses a problem. With lists, it was
meaningful to talk about the “first” and corresponding “rest”. By
definition, with sets there is not “first” element. In fact, Pyret
does not even offer fields similar to `first`{.pyret} and `rest`{.pyret}. In
its place is something a little more accurate but complex.

The `.pick`{.pyret} method returns a random element of a set. It
produces a value of type `Pick`{.pyret} (which we get with `include
pick`{.pyret}). When we pick an element, there are two
possibilities. One is that the set is empty (analogous to a list being
empty), which gives us a `pick-none`{.pyret} value. The other option is
called `pick-some`{.pyret}, which gives us an actual member of the set.

The `pick-some`{.pyret} variant of `Pick`{.pyret} has two fields, not
one. To understand why takes a moment’s work. Let’s explore it by
choosing an element of a set:

```pyret
fun an-elt(s :: S.Set):
  cases (Pick) s.pick():
    | pick-none => raise("empty set")
    | pick-some(e, r) => e
  end
end
```
(Notice that we aren’t using the `r`{.pyret} field in the
`pick-some`{.pyret} case.)

::: {.do-now}
Can you guess why we didn’t write examples for `an-elt`{.pyret}?
:::

::: {.do-now}
Run `an-elt(song-set)`{.pyret}. What element do you get?

Run it again. Run it five more times.

Do you get the same element every time?
:::


No you don’t![Well, actually, it’s impossible to be certain
you don’t. There is a very, very small likelihood you get the exact
same element on every one of six runs. If it happens to you, keep
running it more times!]{.margin-note}
Pyret is designed to not always return the same element
when picking from a set. This is on purpose: it’s to drive home the
random nature of choosing from a set, and to prevent your program from
accidentally depending on a particular order that Pyret might use.

::: {.do-now}
Given that `an-elt`{.pyret} does not return a predictable element, what
(if any) tests can we write for it?
:::


Observe that though we can’t predict which element `an-elt`{.pyret} will
produce, we do know it will produce an element of the set. Therefore,
what we can write are tests that ensure the resulting element is a
member of the set—though in this case, that would not be
particularly surprising.

##### Computing with Sets {#Computing-with-Sets}

Once we have picked an element from a set, it’s often useful to obtain
the set consisting of the remaining elements. We have already seen
that choosing the first field of a `pick-some`{.pyret} is similar to
taking the “first” of a set. We therefore want a way to get the
“rest” of the set. However, we want the rest to what we obtain after
excluding this particular “first”. That’s what the second
field of a `pick-some`{.pyret} is: what’s left of the set.

Given this, we can write functions over sets that look roughly
analogous to functions over lists. For instance, suppose we want to
compute the size of a set. The function looks similar to
`my-len`{.pyret} [[Some Example Exercises](processing-lists.html##my-len)]:

```pyret
fun my-set-size(s :: S.Set) -> Number:
  cases (Pick) s.pick():
    | pick-none => 0
    | pick-some(e, r) =>
      1 + my-set-size(r)
  end
end
```
Though the process of deriving this is similar to that we used for
`my-len`{.pyret}, the random nature of picking elements makes it harder to
write examples that the actual function’s behavior will match.

#### Combining Structured and Collective Data {#Combining-Structured-and-Collective-Data}

As the above examples illustrate, a program’s data organization will
often involve multiple kinds of compound data, often deeply
intertwined. Let’s first think of these in pairs.

::: {.exercise}
Come up with examples that combine:


- structured and conditional data,
- structured and collective data, and
- conditional and collective data.

You’ve actually seen examples of each of these above. Identify them.
:::

Finally, we might even have all three at once. For instance, a
filesystem is usually a list (collective) of files and folders
(conditional) where each file has several attributes
(structured). Similarly, a social network has a set of pages
(collective) where each page is for a person, organization, or other
thing (conditional), and each page has several attributes
(structured). Therefore, as you can see, combinations of these arise
naturally in all kinds of applications that we deal with on a daily
basis.

::: {.exercise}
Take three of your favorite Web sites or apps. Identify the kinds of
data they present. Classify these as structured, conditional, and
collective. How do they combine these data?
:::

#### Data Design Problem: Representing Quizzes {#Data-Design-Problem-Representing-Quizzes}

Now that you can make collections of structured data, you can approach
creating the data and programs for fairly sophisticated
applications. Let’s try out a data-design problem, where we will focus
just on creating the data definition, but not on writing the actual
functions.

Problem Statement:
You’ve been hired to help create software for giving quizzes to
students. The software will show the student a question, read in the
student’s answer, compare the student’s answer to the expected answer
(sort of like a Pyret example!), and produce the percentage of
questions that the student got right.

Your task is to create a data definition for capturing quizzes and
expected answers. Don’t worry about representing the student
responses.

::: {.do-now}
Propose an initial data structure for quizzes. Start by identifying
the pieces you might need and trying to write some sample questions.
:::

We might imagine asking a quiz question like “what is 3 + 4?“. We
would expect the student to answer `7`{.pyret}. What would capture this?
A piece of structured data with two fields like the following:

```pyret
data Question:
  basic-ques(text :: String, expect :: ???)
end
```

What’s a good type for the expected answer? This specific problem has
a numeric answer, but other questions might have other types of
answers. `Any`{.pyret} is therefore an appropriate type for the answer.

We would also need a list of `Question`{.pyret} to form an entire quiz.

Sometimes, quiz software allows students to ask for hints.

::: {.do-now}
Assume we wanted to have some (but not all) questions with hints,
which would be text that a student could request for help with a
problem. Modify the current data definition to capture quizzes in
which some questions have hints and some do not.
:::

A quiz should still be a list of questions, but the `Question`{.pyret}
data definition needs another variant in order to handle questions
with hints. The following would work:

```pyret
data Question:
  | basic-ques(text :: String, expect :: Any)
  | hint-ques(text :: String, expect :: Any, hint :: String)
end

A quiz is a List<Question>
```

We could imagine extending this example to introduce dependencies
between questions (such as one problem building on the skills of
another), multiple choice questions, checkbox questions, and so on.

::: {.responsible-cs}
Many companies have tried to improve education through software
systems that automate tasks otherwise done by teachers. There are
systems that show students a video, then give them quizzes (akin to
what you just developed) to check what they have learned. A more
extreme version interleaves videos and quizzes, thus teaching entire
courses at scale, without the need for teacher intervention.

Massively-online courses (MOOCs) are a style of course that makes
heavy use to computer automation, to enable reaching many more
students without needing more teachers. Proponents of MOOCs and
related educational technology tools have promised game-changing
impacts of such tools, promising to extend quality education to
students around the world who otherwise might lack access to quality
teachers. Technology investors (and indeed some universities) dove in
behind these technologies, hoping for an educational revolution at
scale.

Unfortunately, research and evaluation have shown that replacing
education with automated systems, even ones with sophisticated
features based on data analysis and predictions that identify skills
that students haven’t quite mastered, doesn’t lead to the promised
gains in learning. Why? It turns out that teaching is about more than
choosing questions, gathering student work, and giving
grades. Teachers provide encouragement, reassurance, and an
understanding of an individual students’ situation. Today’s
computational systems don’t do this. The generally-accepted wisdom
around these tools (backed by three prior decades of research) is that
they are best used to complement direct instruction by a human
teacher. In such a setting, some tools have resulted in solid
performance gains on the parts of students.

The social-responsibility takeaway here is that you need to
consider all the features of the system you might be trying to
replace with a computational approach. Algorithmic quiz-taking tools
have genuine value in some specific context, but they aren’t a
replacement for all of teaching. A failure to understand the many
aspects of teaching, and which ones do and do not make it effective
for educating students, could have avoided a lot of inaccurate hype
about the promise of algorithmic instruction.
:::
