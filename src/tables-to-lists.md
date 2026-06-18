---
title: From Tables to Lists
section_number: 5.1
source_file: tables-to-lists.html
prev: part_lists.html
up: part_lists.html
next: processing-lists.html
---

```{=html}
<a name="(part._tables-to-lists)"></a>
```

### 5.1 From Tables to Lists {#tables-to-lists}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._table-stat-qs%29">5.1.1<span class="hspace"> </span>Basic Statistical Questions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Extracting-a-Column-from-a-Table%29">5.1.2<span class="hspace"> </span>Extracting a Column from a Table</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Understanding-Lists%29">5.1.3<span class="hspace"> </span>Understanding Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._lists-generic-data%29">5.1.3.1<span class="hspace"> </span>Lists as Anonymous Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Creating-Literal-Lists%29">5.1.3.2<span class="hspace"> </span>Creating Literal Lists</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Operating-on-Lists%29">5.1.4<span class="hspace"> </span>Operating on Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Built-In-Operations-on-Lists-of-Numbers%29">5.1.4.1<span class="hspace"> </span>Built-In Operations on Lists of Numbers</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Built-In-Operations-on-Lists-in-General%29">5.1.4.2<span class="hspace"> </span>Built-In Operations on Lists in General</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._An-Aside-on-Naming-Conventions%29">5.1.4.3<span class="hspace"> </span>An Aside on Naming Conventions</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Getting-Elements-By-Position%29">5.1.4.4<span class="hspace"> </span>Getting Elements By Position</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Transforming-Lists%29">5.1.4.5<span class="hspace"> </span>Transforming Lists</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._lists-recap%29">5.1.4.6<span class="hspace"> </span>Recap: Summary of List Operations</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Lambda--Anonymous-Functions%29">5.1.5<span class="hspace"> </span>Lambda: Anonymous Functions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="tables-to-lists.html#%28part._Combining-Lists-and-Tables%29">5.1.6<span class="hspace"> </span>Combining Lists and Tables</a></p></td></tr></table>
```

Previously [[Introduction to Tabular Data](intro-tabular-data.html)] we began to process
collective data in the form of tables. Though we saw
several powerful operations that let us quickly and easily ask
sophisticated questions about our data, they all had two things in
common. First, all were operations by rows. None of the operations
asked questions about an entire column at a time. Second, all the
operations not only consumed but also produced tables. However, we
already know [[Getting Started](getting-started.html)] there are many other kinds
of data, and sometimes we will want to compute one of them. We will
now see how to achieve both of these things, introducing an important
new type of data in the process.

```{=html}
<a name="(part._table-stat-qs)"></a>
```

#### 5.1.1 Basic Statistical Questions {#table-stat-qs}

There are many more questions we might want to ask of our events data. For
instance:


- The most-frequently used discount code.

- The average number of tickets per order.

- The largest ticket order.

- The most common number of tickets in an order.

- The collection of unique discount codes that were used (many
  might have been available).

- The collection of distinct email addresses associated with
  orders, so we can contact customers (some customers may have placed
  multiple orders).

- Which school lead to the largest number of orders with a
  `"STUDENT"`{.jayret} discount.

Notice the kinds of operations that we are talking about: computing
the maximum, minimum, average, median, and other basic
statistics.[Jayret has several built-in
statistics functions in the
[math](https://jayret-lang.github.io/docs/math.html)
and
[statistics](https://jayret-lang.github.io/docs/statistics.html)
packages.]{.margin-note}

::: {.do-now}
Think about whether and how you would express these questions with the
operations you have already seen.
:::

In each of these cases, we need to perform a computation on a single
column of data (even in the last question about the `"STUDENT"`{.jayret}
discount, as we would filter the table to those rows, then do a
computation over the `email`{.jayret} column). In order to capture these
in code, we need to extract a column from the table.

For the rest of this chapter, we will work with a cleaned copy of the
`event-data`{.jayret} from the previous chapter. The cleaned data, which
applies the transformations at the end of the previous chapter, is in
a different tab of the same Google Sheet as the other versions of the
event data.

```jayret
import gdrive-sheets
import data-source
ssid = "1Ks4ll5_8wyYK1zyXMm_21KORhagSMZ59dcr7i3qY6T4";
cleaned-data = load-table name ,email ,tickcount ,discount ,delivery ,zip source: load-spreadsheet(ssid).sheet-by-name("Cleaned", true) sanitize name using string-sanitizer sanitize email using string-sanitizer sanitize tickcount using num-sanitizer sanitize discount using string-sanitizer sanitize delivery using string-sanitizer sanitize zip using string-sanitizer;
```

```{=html}
<a name="(part._Extracting-a-Column-from-a-Table)"></a>
```

#### 5.1.2 Extracting a Column from a Table {#Extracting-a-Column-from-a-Table}

Our collection of table functions includes one that we haven’t yet
used, called `select-columns`{.jayret}. As the name suggests, this
function produces a new table containing only certain columns from an
existing table. Let’s extract the `tickcount`{.jayret} column so we can
compute some statistics over it. We use the following expression:

```jayret
select-columns(cleaned-data, ["tickcount"]);
```

![](tickcount-column.png){width="94" height="295"}

This focuses our attention on the numeric ticket sales, but we’re still stuck
with a column in a table, and none of the other tables
functions let us do the kinds of computations we might want over these
numbers. Ideally, we want the collection of numbers on their own, without being
wrapped up in the extra layer of table cells.

In principle, we could have a collection of operations on a single
column. In some languages that focus solely on tables, such as
[SQL](https://en.wikipedia.org/wiki/SQL),
this is what you’ll find. However, in Jayret we have many more
kinds of data than just columns (as we’ll soon see [[Introduction to Structured Data](intro-struct-data.html)], we can even
create our own!), so it makes sense to leave the gentle cocoon of
tables sooner or later. An extracted column is a more basic kind of
datum called a list, which can be used to represent a sequence
of data outside of a table.

Just as we have used the notation `.row-n`{.jayret} to pull a single row
from a table, we use a similar dot-based notion to pull out a single
column. Here’s how we extract the `tickcount`{.jayret} column:

```jayret
cleaned-data.get-column("tickcount");
```

In response, Jayret produces the following value:

```jayret
[2, 1, 5, 0, 3, 10, 3];
```

Now, we seem to have only the values that were in the cells in the
column, without the enclosing table. Yet the numbers are still bundled
up, this time in the `[...]`{.jayret} notation. What is that?

```{=html}
<a name="(part._Understanding-Lists)"></a>
```

#### 5.1.3 Understanding Lists {#Understanding-Lists}

A list has much in common with a single-column table:


- The elements have an order, so it makes sense to talk about the
  “first”, “second”, “last”—and so on—element of a list.

- All elements of a list are expected to have the same type.

The crucial difference is that a list does not have a “column name”;
it is anonymous. That is, by itself a list does not describe
what it represents; this interpretation is done by our program.

```{=html}
<a name="(part._lists-generic-data)"></a>
```

##### 5.1.3.1 Lists as Anonymous Data {#lists-generic-data}

This might sound rather abstract—and it is—but this isn’t actually
a new idea in our programming experience. Consider a value like
`3`{.jayret} or `-1`{.jayret}: what is it? It’s the same sort of thing: an
anonymous value that does not describe what it represents; the
interpretation is done by our program. In one setting `3`{.jayret} may
represent an age, in another a play count; in one setting `-1`{.jayret}
may be a temperature, in another the average of several
temperatures. Similarly with a string: Is `"project"`{.jayret} a noun (an
activity that one or more people perform) or a verb (as when we
display something on a screen)? Likewise with images and so on. In
fact, tables have been the exception so far in having description
built into the data rather than being provided by a program!

This genericity is both a virtue and a problem. Because, like
other anonymous data, a list does not provide any interpretation of
its use, if we are not careful we can accidentally mis-interpret the
values. On the other hand, it means we can use the same datum in
several different contexts, and one operation can be used in many
settings.

Indeed, if we look at the list of questions we asked earlier, we see
that there are several common operations—maximum, minimum, average,
and so on—that can be asked of a list of values without regard for
what the list represents (heights, ages, playcounts). In fact, some
are specific to numbers (like average) while some (like maximum) can
be asked of any type on which we can perform a comparison (like
strings).

```{=html}
<a name="(part._Creating-Literal-Lists)"></a>
```

##### 5.1.3.2 Creating Literal Lists {#Creating-Literal-Lists}

We have already seen how we can create lists from a table, using
`get-column`{.jayret}. As you might expect, however, we can also create lists
directly:

```jayret
[1, 2, 3];
[-1, 5, 2.3, 10];
["a", "b", "c"];
["This", "is", "a", "list", "of", "words"];
```
Of course, lists are values so we can name them using variables—

```jayret
shopping-list = ["muesli", "fiddleheads"];
```
—pass them to functions (as we will soon see), and so on.

::: {.do-now}
Based on these examples, can you figure out how to create an empty
list?
:::

As you might have guessed, it’s `[]`{.jayret} (the space isn’t
necessary, but it’s a useful visual reminder of the void).

```{=html}
<a name="(part._Operating-on-Lists)"></a>
```

#### 5.1.4 Operating on Lists {#Operating-on-Lists}

```{=html}
<a name="(part._Built-In-Operations-on-Lists-of-Numbers)"></a>
```

##### 5.1.4.1 Built-In Operations on Lists of Numbers {#Built-In-Operations-on-Lists-of-Numbers}

Jayret handily provides a useful set of operations we can already
perform on lists. [The
[lists
documentation](https://jayret-lang.github.io/docs/lists.html) describes these operations.]{.margin-note} As you might have
guessed, we can already compute most of the answers we’ve asked for
at the start of the chapter. First we need to include some libraries that contain useful
functions:

```jayret
import math as M
import statistics as S

```
We can then access several useful functions:

```jayret
tickcounts = cleaned-data.get-column("tickcount");
M.max(tickcounts);
// largest number in a list
M.sum(tickcounts);
// sum of numbers in a list
S.mean(tickcounts);
// mean (average) of numbers in a list
S.median(tickcounts);
// median of numbers in a list
```

The `M.`{.jayret} notation means "the function inside the library
`M`{.jayret}. The `import`{.jayret} statement in the above code gave the name
`M`{.jayret} to the `math`{.jayret} library.

```{=html}
<a name="(part._Built-In-Operations-on-Lists-in-General)"></a>
```

##### 5.1.4.2 Built-In Operations on Lists in General {#Built-In-Operations-on-Lists-in-General}

Some of the useful computations in our list at the start of the
chapter involved the `discount`{.jayret} column, which contains strings
rather than numbers. Specifically, let’s consider the following
question:

- Compute the collection of unique discount codes that were used (many
  might have been available).

None of the table functions handle a question like this. However, this
is a common kind of question to ask about a collection of values (How
many unique artists are in your playlist? How many unique faculty are
teaching courses?). As such, Jayret (as most languages) provides a way
to identify the unique elements of a list. Here’s how we get the list
of all discount codes that were used in our table:

```jayret
import lists as L
codes = cleaned-data.get-column("discount");
L.distinct(codes);
```

The `distinct`{.jayret} function produces a list of the unique values from
the input list: every value in the input list appears exactly once in
the output list. For the above code, Jayret produces:

```jayret
["BIRTHDAY", "STUDENT", "none"];
```

What if we wanted to exclude `"none"`{.jayret} from that list? After all,
`"none"`{.jayret} isn’t an actual discount code, but rather one that we
introduced while cleaning up the table. Is there a way to easily
remove `"none"`{.jayret} from the list?

There are two ways we could do it. In the Jayret lists documentation,
we find a function called `remove`{.jayret}, which removes a specific
element from a list:

::: {.pyret-repl}
<!-- TODO(verify-repl): jayret failed: exit 1: The name `L` is unbound. It is used but not previously defined. You may need to run the program, or check dashes and capitalization in the name. The name `L` is -->
```jayret
L.remove(L.distinct(codes), "none");
```
``` output
[list: "BIRTHDAY", "STUDENT"]
```
:::

But this operation should also sound familiar: with tables, we
used `filter-with`{.jayret} to keep only those elements that meet a
specific criterion. The filtering idea is so common that Jayret (and
most other languages) provide a similar operation on lists. In the
case of the discount codes, we could also have written:

```jayret
boolean real-code(String c) {
    return not(c == "none");
}
L.filter(real-code, L.distinct(codes));
```

The difference between these two approaches is that `filter`{.jayret} is
more flexible: we can check any characteristic of a list element using
`filter`{.jayret}, but `remove`{.jayret} only checks whether the entire
element is equal to the value that we provide. If instead of removing
the specific string `"none"`{.jayret}, we had wanted to remove all strings
that were in all-lowercase, we would have needed to use `filter`{.jayret}.

::: {.exercise}
Write a function that takes a list of words and removes those words in
which all letters are in lowercase. (Hint: combine
`string-to-lower`{.jayret} and `==`{.jayret}).
:::

```{=html}
<a name="(part._An-Aside-on-Naming-Conventions)"></a>
```

##### 5.1.4.3 An Aside on Naming Conventions {#An-Aside-on-Naming-Conventions}

Our use of the plural `codes`{.jayret} for the list of values in the
column named `discount`{.jayret} (singular) is deliberate. A list contains
multiple values, so a plural is appropriate. In a table, in contrast,
we think of a column header as naming a single value that appears in
a specific row. Often, we speak of looking up a value in a specific
row and column: the singular name for the column supports thinking
about lookup in an individual row.

```{=html}
<a name="(part._Getting-Elements-By-Position)"></a>
```

##### 5.1.4.4 Getting Elements By Position {#Getting-Elements-By-Position}

Let’s look at a new analysis question: the events company recently ran
an advertising campaign on `web.com`{.jayret}, and they are curious
whether it paid off. To do this, they need to determine how many sales
were made to people with `web.com`{.jayret} email addresses.

::: {.do-now}
Propose a task plan ([Task Plans](processing-tables.html#task-plans)) for this computation.
:::

Here’s a proposed plan, annotated with how we might implement each part:

1. Get the list of email addresses (use `get-column`{.jayret})

2. Extract those that came from `web.com`{.jayret} (use `L.filter`{.jayret})

3. Count how many email addresses remain (using `L.length`{.jayret},
  which we hadn’t discussed yet, but it is in the documentation)

(As a reminder, unless you immediately see how to solve a problem,
write out a task plan and annotate the parts you know how to do. It
helps break down a programming problem into more manageable parts.)

Let’s discuss the second task: identifying messages from
`web.com`{.jayret}. We know that email addresses are strings, so if we
could determine whether an email string ends in `@web.com`{.jayret},
we’d be set. You could consider doing this by looking at the last 7
characters of the email string. Another option is to use a string
operation that we haven’t yet seen called `string-split-all`{.jayret}, which
splits a string into a list of substrings around a given
character. For example:

::: {.pyret-repl}
```jayret
string-split-all("this-has-hyphens", "-");
```
``` output
[list: "this", "has", "hyphens"]
```
:::

::: {.pyret-repl}
```jayret
string-split("bonnie@jayret-lang.github.io", "@");
```
``` output
[list: "bonnie", "jayret-lang.github.io"]
```
:::

This seems pretty useful. If we split each email string around the
`@`{.jayret} sign, then we can check whether the second string in the
list is `web.com`{.jayret} (since email addresses should have only one
`@`{.jayret} sign). But how would we get the second element out of
the list produced by `string-split-all`{.jayret}? Here we dig into the
list, as we did to extract rows from tables, this time using the
`get`{.jayret} operation.

::: {.pyret-repl}
```jayret
string-split("bonnie@jayret-lang.github.io", "@").get(1);
```
``` output
"jayret-lang.github.io"
```
:::

::: {.do-now}
Why do we use `1`{.jayret} as the input to `get`{.jayret} if we want the
second item in the list?
:::

Here’s the complete program for doing this check:

```jayret
boolean web-com-address(String email) {
    // determine whether email is from web.com
    return string-split(email, "@").get(1) == "web.com";
} where {
    
}
emails = cleaned-data.get-column("email");
L.length(L.filter(web-com-address, emails));
```

::: {.exercise}
What happens if there is a malformed email address string that doesn’t
contain the `@`{.jayret} string? What would happen? What could you do
about that?
:::

```{=html}
<a name="(part._Transforming-Lists)"></a>
```

##### 5.1.4.5 Transforming Lists {#Transforming-Lists}

Imagine now that we had a list of email addresses, but instead just
wanted a list of usernames. This doesn’t make sense for our event
data, but it does make sense in other contexts (such as connecting
messages to folders organized by students’ usernames).

Specifcally, we want to start with a list of addresses such as:

```jayret
["parrot@web.com", "bonnie@jayret-lang.github.io"];
```

and convert it to

```jayret
["parrot", "bonnie"];
```

::: {.do-now}
Consider the list functions we have seen so far (`distinct`{.jayret},
`filter`{.jayret}, `length`{.jayret}) – are any of them useful for this task?
Can you articulate why?
:::

One way to articulate a precise answer to this is think in terms of
the inputs and outputs of the existing functions. Both `filter`{.jayret}
and `distinct`{.jayret} return a list of elements from the input list, not
transformed elements. `length`{.jayret} returns a number, not a list. So
none of these are appropriate.

This idea of transforming elements is similar to the
`transform-column`{.jayret} operation that we previously saw on
tables. The corresponding operation on lists is called
`map`{.jayret}. Here’s an example:

```jayret
String extract-username(String email) {
    // extract the portion of an email address before the @ sign
    return string-split(email, "@").get(0);
} where {
    
}
L.map(extract-username, ["parrot@web.com", "bonnie@jayret-lang.github.io"]);
```

```{=html}
<a name="(part._lists-recap)"></a>
```

##### 5.1.4.6 Recap: Summary of List Operations {#lists-recap}

At this point, we have seen several useful built-in functions for
working with lists:

- `/* contract: filter :: Object */`{.jayret}, which
  produces a list of elements from the input list on which the given
  function returns `true`{.jayret}.

- `/* contract: map :: Object */`{.jayret}, which
  produces a list of the results of calling the given function on each
  element of the input list.

- `/* contract: distinct :: Object */`{.jayret}, which
  produces a list of the unique elements that appear in the input list.

- `/* contract: length :: Object */`{.jayret}, which
  produces the number of elements in the input list.

Here, a type such as `List < A >`{.jayret} says that we have a list whose
elements are of some (unspecified) type which we’ll call
`A`{.jayret}. A type variable such as this is useful when we want to
show relationships between two types in a function
contract. Here, the type variable `A`{.jayret} captures that the type of
elements is the same in the input and output to `filter`{.jayret}. In
`map`{.jayret}, however, the type of element in the output list could
differ from that in the input list.

One additional built-in function that is quite useful in practice is:

- `/* contract: member :: Object */`{.jayret}, which
  determines whether the given element is in the list. We use the type
  `Any`{.jayret} when there are no constraints on the type of value provided
  to a function.

Many useful computations can be performed by combining these
operations.

::: {.exercise}
Assume you used a list of strings to represent the ingredients in a
recipe. Here are three examples:

```jayret
stir-fry = ["peppers", "pork", "onions", "rice"];
dosa = ["rice", "lentils", "potato"];
misir-wot = ["lentils", "berbere", "tomato"];
```

Write the following functions on ingredient lists:

- `recipes-uses`{.jayret}, which takes an ingredient list and an
  ingredient and determines whether the recipe uses the ingredient.

- `make-vegetarian`{.jayret}, which takes an ingredient list and replaces
  all meat ingredients with `"tofu"`{.jayret}. Meat ingredients are
  `"pork"`{.jayret}, `"chicken"`{.jayret}, and `"beef"`{.jayret}.

- `protein-veg-count`{.jayret}, which takes an ingredient list and
  determines how many ingredients are in the list that aren’t
  `"rice"`{.jayret} or `"noodles"`{.jayret}.
:::

::: {.exercise}
More challenging: Write a function that takes an
ingredient and a list of ingredient lists and produces a list of all
the lists that contain the given ingredient.

Hint: write examples first to make sense of the problem as needed.
:::

::: {.exercise}
Even more challenging: Try to write a function that takes two
ingredient lists and
returns all of the ingredients that are common to both lists. What
issue(s) or limitations do you run into?

Come back to this problem after you finish the next section.
:::

```{=html}
<a name="(part._Lambda-Anonymous-Functions)"></a>
```

```{=html}
<a name="(part._Lambda--Anonymous-Functions)"></a>
```

#### 5.1.5 Lambda: Anonymous Functions {#Lambda--Anonymous-Functions}

NOTE: if you already saw lambda (arrow-function) syntax in
[Lambda: Anonymous Functions](intro-tabular-data.html#sec-lambda-tables),
feel free to skip this section, or just do the exercises at the end. Here we
present the same concept using lists and `filter`{.jayret}, rather than tables
and `filter-with`{.jayret}.

Let’s revisit the program we wrote earlier in this chapter for
finding all of the discount codes that were used in the events table:

```jayret
boolean real-code(String c) {
    return not(c == "none");
}
L.filter(real-code, codes);
```

This program might feel a bit verbose: do we really need to write a
helper function just to perform something as simple as a
`filter`{.jayret}? Wouldn’t it be easier to just write something like:

```jayret
L.filter(not(c == "none"), codes);
```

::: {.do-now}
What will Jayret produce if you run this expression?
:::

Jayret will produce an `unbound;
identifier`{.jayret} error around the use
of `c`{.jayret} in this expression. What is `c`{.jayret}? We mean for `c`{.jayret}
to be the elements from `codes`{.jayret} in turn. Conceptually, that’s
what `filter`{.jayret} does, but we don’t have the mechanics right. When
we call a function, we evaluate the arguments before the body
of the function. Hence, the error regarding `c`{.jayret} being unbound.
The whole point of the `real-code`{.jayret} helper function is to make
`c`{.jayret} a parameter to a function whose body is only evaluated once
a value for `c`{.jayret} is available.

To tighten the notation as in the one-line `filter`{.jayret} expression,
then, we have to find a way to tell Jayret to make a temporary function
that will get its inputs once `filter`{.jayret} is running. The following
notation achieves this:

```jayret
L.filter((c) -> not(c == "none"), codes);
```

We have written the expression as an arrow function `(c) -> ...`{.jayret}.
The `(c)`{.jayret} introduces the parameter `c`, and the arrow `->` separates
the parameters from the body expression. Such anonymous functions are commonly
called *lambdas*; they exist in many languages but with different syntaxes.

The main difference between our original expression (using the
`real-code`{.jayret} helper) and this new one (using arrow syntax) can be
seen through the program directory. To explain this, a little detail
about how `filter`{.jayret} is defined under the hood. In part, it looks
like:

```jayret
List<A> filter((A -> boolean) keep, List<A> lst) {
    return if (keep(<elt-from-list>)) {
        return ...;
    } else {
        return ...;
    }
}
```

Whether we pass `real-code`{.jayret} or the arrow-function version to
`filter`{.jayret}, the `keep`{.jayret} parameter ends up referring to a
function with the same parameter and body. Since the function is only
actually called through the `keep`{.jayret} name, it doesn’t matter
whether or not a name is associated with it when it is initially
defined.

In practice, we use arrow functions when we have to pass simple (single
line) functions to operations like `filter`{.jayret} (or `map`{.jayret}). We
could have just as easily used them when we were working with tables
(`build-column`{.jayret}, `filter-with`{.jayret}, etc). Of course, you can
continue to write out names for helper functions as we did with
`real-code`{.jayret} if that makes more sense to you.

::: {.exercise}
Write the program to extract the list of usernames from a list of
email addresses using arrow syntax rather than a named helper-function.
:::

::: {.exercise}
Try again to tackle the problem from the end of the
previous section: write a function that takes two ingredient lists and
returns all of the ingredients that are common to both lists.
:::

```{=html}
<a name="(part._Combining-Lists-and-Tables)"></a>
```

#### 5.1.6 Combining Lists and Tables {#Combining-Lists-and-Tables}

The table functions we studied previously were primarily for
processing rows. The list functions we’ve learned in this chapter have
been primarily for processing columns (but there are many more uses in
the chapters ahead). If an analysis involves working with only some
rows and some columns, we’ll use a combination of both table and list
functions in our program.

::: {.exercise}
Given the events table, produce a list of names of all people who will
pick up their tickets.
:::

::: {.exercise}
Given the events table, produce the average number of tickets that
were ordered by people with email addresses that end in
`".org"`{.jayret}.
:::

Sometimes, there will be more than one way to perform a computation:

::: {.do-now}
Consider a question such as "how many people with `".org"`{.jayret} email
addresses bought more than 8 tickets". Propose multiple task plans
that would solve this problem, including which table and list
functions would accomplish each task.
:::

There are several options here:

1. Get the `event-data`{.jayret} rows with no more than 8
  tickets (using `filter-with`{.jayret}), get those rows that have
  `".org"`{.jayret} addresses (another `filter-with`{.jayret}), then ask for how
  many rows are in the table (using `<table>.length()`{.jayret}).

2. Get the `event-data`{.jayret} rows with no more than 8
  tickets and `".org"`{.jayret} address (using `filter-with`{.jayret} with a
  function that checks both conditions at once), then ask for how
  many rows are in the table (using `<table>.length()`{.jayret}).

3. Get the `event-data`{.jayret} rows with no more than 8
  tickets (using `filter-with`{.jayret}), extract the email addresses (using
  `get-column`{.jayret}), limit those to `".org"`{.jayret} (using `L.filter`{.jayret}),
  then get the length of the resulting list (using `L.length`{.jayret}).

There are others, but you get the idea.

::: {.do-now}
Which approach do you like best? Why?
:::

While there is no single correct answer, there are various
considerations:

- Are any of the intermediate results useful for other computations?
  While the second option might seem best because it filters the table
  once rather than twice, perhaps the events company has many
  computations to perform on larger ticket orders. Similarly, the
  company may want the list of email addresses on large orders for
  other purposes (the third option)

- Do you want to follow a discipline of doing operations on
  individuals within the table, extracting lists only when needed to
  perform aggregating computations that aren’t available on tables?

- Does one approach seem less resource-intensive than the other?
  This is actually a subtle point: you might be tempted to think that
  filtering over a table uses more resources than filtering over a list
  of values from one column, but this actually isn’t the case. We’ll
  return to this discussion later.

A company or project team sometimes sets design standards to help you
make those decisions. In the absence of that, and especially as you
are learning to program, consider multiple approaches when faced with
such problems, then pick one to implement. Maintaining the ability to
think flexibly about approaches is a useful skill in any form of design.

Until now we’ve only seen how to use built-in functions over
lists. Next [[Processing Lists](processing-lists.html)], we will study how to create
our own functions that process lists. Once we learn that, these list
processing functions will remain powerful but will no longer seem
quite so magical, because we’ll be able to build them for ourselves!
