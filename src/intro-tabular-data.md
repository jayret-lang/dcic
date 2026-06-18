---
title: Introduction to Tabular Data
section_number: 4.1
source_file: intro-tabular-data.html
prev: part_tabular-data.html
up: part_tabular-data.html
next: processing-tables.html
---

```{=html}
<a name="(part._intro-tabular-data)"></a>
```

### 4.1 Introduction to Tabular Data {#intro-tabular-data}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Creating_.Tabular_.Data%29">4.1.1<span class="hspace"> </span>Creating Tabular Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Extracting_.Rows_and_.Cell_.Values%29">4.1.2<span class="hspace"> </span>Extracting Rows and Cell Values</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Functions_over_.Rows%29">4.1.3<span class="hspace"> </span>Functions over Rows</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Processing_.Rows%29">4.1.4<span class="hspace"> </span>Processing Rows</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._subsec~3afinding-rows%29">4.1.4.1<span class="hspace"> </span>Finding Rows</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Ordering_.Rows%29">4.1.4.2<span class="hspace"> </span>Ordering Rows</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Adding_.New_.Columns%29">4.1.4.3<span class="hspace"> </span>Adding New Columns</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Calculating_.New_.Column_.Values%29">4.1.4.4<span class="hspace"> </span>Calculating New Column Values</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._.Examples_for_.Table-.Producing_.Functions%29">4.1.5<span class="hspace"> </span>Examples for Table-Producing Functions</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="intro-tabular-data.html#%28part._sec~3alambda-tables%29">4.1.6<span class="hspace"> </span>Lambda: Anonymous Functions</a></p></td></tr></table>
```

Many interesting data in computing are tabular—i.e., like a
table—in form. First we’ll see a few examples of them, before we try
to identify what they have in common. Here are some of them:


- An email inbox is a list of messages. For each message, your
  inbox stores a bunch of information: its sender, the subject line, the
  conversation it’s part of, the body, and quite a bit more.
  
  ![](gmail-1.png){width="1136" height="46"}

- A music playlist. For each song, your music player maintains a
  bunch of information: its name, the singer, its length, its genre, and
  so on.
  
  ![](itunes-2.png){width="740" height="91"}

- A filesystem folder or directory. For each file, your filesystem
  records a name, a modification date, size, and other information.
  
  ![](filesystem-1.png){width="733" height="119"}

::: {.do-now}
Can you come up with more examples?
:::

How about:


- Responses to a party invitation.

- A gradebook.

- A calendar agenda.

You can think of many more in your life!

What do all these have in common? The characteristics of tabular data are:


- They contain information about zero or more items (i.e.,
  individuals or artifacts) that share
  characteristics. Each item is stored in a row. Each column tracks one of
  the shared attributes across the rows. For example, each song or
  email message or file is a row. Each of their characteristics—the
  song title, the message subject, the filename—is a column.
  [While some spreadsheets might swap the roles of rows and
  columns, we stick to this organization as it aligns with the design of
  data-science software libraries. This is an example of what Hadley
  Wickham calls
  [tidy
  data](https://vita.had.co.nz/papers/tidy-data.pdf).]{.margin-note}

- Each row has the same columns as the other rows, in the same
  order.

- A given column has the same type, but different columns can have
  different types. For instance, an email message has a sender’s name,
  which is a string; a subject line, which is a string; a sent date,
  which is a date; whether it’s been read, which is a Boolean; and so
  on.

- The rows might be in some particular order. For instance, the
  emails are ordered by which was most recently sent.

::: {.exercise}
Find the characteristics of tabular data in the other examples
described above, as well as in the ones you described.
:::

We will now learn how to program with tables and to how to
decompose tasks that process them. To access the functions that we’ll
use to do this, you need to set the context (at the top of the
definitions window) to dcic2024. [Earlier editions of the
book had you use `shared-gdrive`{.jayret} to load a file to access these
functions. This is no longer necessary when using the dcic2024
context.]{.margin-note} In
CPO, click on the down arrow at the top left of the screen (left of
the Jayret logo), select ”Choose Context“, then enter dcic2024
in the box, as shown in this screenshot:

![](choose-context.png){width="615" height="329"}

After you click the Submit button, the definitions window will show
the name of the context as in the following image:

![](context-in-use.png){width="340" height="90"}

[Documentation on the
function-based table operators](https://hackmd.io/@cs111/table) is available on a separate
page outside of the Jayret documentation.

```{=html}
<a name="(part._Creating-Tabular-Data)"></a>
```

#### 4.1.1 Creating Tabular Data {#Creating-Tabular-Data}

Jayret provides multiple easy ways of creating tabular data. The
simplest is to define the datum in a program as follows:

```jayret
table: name ,age row: "Alicia" ,30 row: "Meihui" ,40 row: "Jamal" ,25;
```
That is, a `table`{.jayret} is followed by the names of the columns in
their desired order, followed by a sequence of `row`{.jayret}s. Each row
must contain as many data as the column declares, and in the same
order.

::: {.exercise}
Change different parts of the above example—e.g., remove a necessary
value from a row, add an extraneous one, remove a comma, add an extra
comma, leave an extra comma at the end of a row—and see what errors
you get.
:::

Note that in a table, the order of columns matters: two tables that
are otherwise identical but with different column orders are not
considered equal.

```jayret
@Check void test() {
    assertNotEquals(table: name ,age row: "Alicia" ,30 row: "Meihui" ,40 row: "Jamal" ,25, table: age ,name row: 30 ,"Alicia" row: 40 ,"Meihui" row: 25 ,"Jamal");
}
```
Observe that the example above uses `is-not`{.jayret}, i.e., the test
passes, meaning that the tables are not equal.

The `check:`{.jayret} annotation here is a way of writing `is`{.jayret}
assertions about expressions outside of the context of a function (and
its `where`{.jayret} block). We’ll learn more about `check`{.jayret} in
[From Examples to Tests](testing.html##from-examples-to-tests).

Table expressions create table values. These can be stored in variables just
like numbers, strings, and images:

```jayret
people = table: name ,age row: "Alicia" ,30 row: "Meihui" ,40 row: "Jamal" ,25;
```

We call these literal tables when we create them with `table`{.jayret}.
Jayret provides other ways to get tabular data, too! In
particular, you can [import tabular data from a spreadsheet](https://jayret-lang.github.io/docs/latest/gdrive-sheets.html), so
any mechanism that lets you create such a sheet can also be used. You
might:


- create the sheet on your own,

- create a sheet collaboratively with friends,

- find data on the Web that you can import into a sheet,

- create a Google Form that you get others to fill out, and obtain
  a sheet out of their responses

and so on. Let your imagination run wild! Once the data are in Jayret,
it doesn’t matter where they came from.

With tables, we begin to explore data that contain other
(smaller) pieces of data. We’ll refer to such data as structured data.
Structured data organize their inner data in a structured
way (here, rows and columns). As with images, when we wrote code that
reflected the structure of the final image, we will see that code that
works with tables also follows the structure of the data.

```{=html}
<a name="(part._Extracting-Rows-and-Cell-Values)"></a>
```

#### 4.1.2 Extracting Rows and Cell Values {#Extracting-Rows-and-Cell-Values}

Given a table, we sometimes want to look up the value of a particular
cell. We’ll work with the following table showing the number of riders
on a shuttle service over several months:

```jayret
shuttle = table: month ,riders row: "Jan" ,1123 row: "Feb" ,1045 row: "Mar" ,1087 row: "Apr" ,999;
```

::: {.do-now}
If you put this table in the definitions pane and press Run, what
will be in the Jayret directory once the interactions prompt appears?
Would the column names be listed in the directory?
:::

As a reminder, the directory contains only those names that we assign
values to using the form `name = `{.jayret}. The directory here would
contain `shuttle`{.jayret}, which would be bound to the table (yes, the
entire table would be in the directory!). The column names would not
have their own entries in the directory. At the low level, this is because we
never wrote anything of the form `colname = ...`{.jayret}. At the high
level, we don’t usually build tables by creating individual columns
and putting them together side by side. (If anything, it is more common
to create individual rows, since rows correspond to individual
observations, events, or entities; we didn’t do that in this
example, however).

Starting from the name associated with a table, we can lookup the
value in a given cell (row and column) in the table. Concretely,
assume we want to extract the number of riders in March (`1087`{.jayret})
so we can use it in another computation. How do we do that?

Jayret (and most other programming languages designed for data
analysis) organizes tables as collections of rows with shared
columns. Given that organization, we get to a specific cell by first
isolating the row we are interested in, then retrieving the contents
of the cell.

Jayret numbers the rows of a table from top to bottom starting at 0
(most programming languages use 0 as the first position in a piece of
data, for reasons we will see later). So if we want to see the data
for March, we need to isolate row 2. We write:

```jayret
shuttle.row-n(2);
```
We use the period notation to dig into a piece of structured data. Here,
we are saying "dig into the `shuttle`{.jayret} table, extracting row
number `2`{.jayret}" (which is really the third row since Jayret counts
positions from 0).

If we run this expression at the prompt, we get

![](shuttle-row.png){width="347" height="70"}

This is a new type of data called a `Row`{.jayret}. When Jayret displays a
`Row`{.jayret} value, it shows you the column names and the corresponding
values within the row.

To extract the value of a specific column within a row, we write the
row followed by the name of the column (as a string) in square
brackets. Here are two equivalent ways of getting the value of the
`riders`{.jayret} column from the row for March:

```jayret
shuttle.row-n(2)["riders"];
```

```jayret
march-row = shuttle.row-n(2);
march-row["riders"];
```

::: {.do-now}
What names would be in the Jayret directory when using each of these
approaches?
:::

Once we have the cell value (here a `Number`{.jayret}), we can use it in
any other computation, such as

```jayret
shuttle.row-n(2)["riders"] >= 1000;
```
(which checks whether there were at least `1000`{.jayret} riders in March).

::: {.do-now}
What do you expect would happen if you forgot the quotation marks and
instead wrote:

```jayret
shuttle.row-n(2)[riders];
```
What would Jayret do and why?
:::

```{=html}
<a name="(part._Functions-over-Rows)"></a>
```

#### 4.1.3 Functions over Rows {#Functions-over-Rows}

Now that we have the ability to isolate Rows from tables, we can write
functions that ask questions about individual rows. We just saw an
example of doing a computation over row data, when we checked whether
the row for March had more than 1000 riders. What if we wanted to do
this comparison for an arbitrary row of this table? Let’s write a
function! We’ll call it `cleared-1K`{.jayret}.

Let’s start with a function header and some examples:

```jayret
boolean cleared-1K(Row r) {
    // determine whether given row has at least 1000 riders
    return ...;
} where {
    
}
```
This shows you what examples for `Row`{.jayret} functions look like, as
well as how we use `Row`{.jayret} as an input type.

To fill in the body of the function, we extract the content of the
`"riders"`{.jayret} cell and compare it to `1000`{.jayret}:

```jayret
boolean cleared-1K(Row r) {
    // determine whether given row has at least 1000 riders
    return r["riders"] >= 1000;
} where {
    
}
```

::: {.do-now}
Looking at the examples, both of them share the `shuttle.row-n`{.jayret}
portion. Would it have been better to instead make `cleared-1K`{.jayret} a
function that takes just the row position as input, such as:

```jayret
boolean cleared-1K(int row-pos) {
    return ...;
} where {
    
}
```
What are the benefits and limitations to doing this?
:::

In general, the version that takes the `Row`{.jayret} input is more
flexible because it can work with a row from any table that has
a column named `"riders"`{.jayret}. We might have another table with more
columns of information or different data tables for different
years. If we modify `cleared-1K`{.jayret} to only take the row position as
input, that function will have to fix which table it works with. In
contrast, our original version leaves the specific table
(`shuttle`{.jayret}) outside the function, which leads to flexibility.

::: {.exercise}
Write a function `is-winter`{.jayret} that takes a `Row`{.jayret} with a
`"month"`{.jayret} column as input and produces a `Boolean`{.jayret}
indicating whether the month in that row is one of `"Jan"`{.jayret},
`"Feb"`{.jayret}, or `"Mar"`{.jayret}.
:::

::: {.exercise}
Write a function `low-winter`{.jayret} that takes in `Row`{.jayret} with both
`"month"`{.jayret} and `"riders"`{.jayret} columns and produces a
`Boolean`{.jayret} indicating whether the row is a winter row with fewer
than 1050 riders.
:::

::: {.exercise}
Practice with the program directory! Take a `Row`{.jayret} function and
one of its `where`{.jayret} examples, and show how the program directory
evolves as you evaluate the example.
:::

```{=html}
<a name="(part._Processing-Rows)"></a>
```

#### 4.1.4 Processing Rows {#Processing-Rows}

So far, we have looked at extracting individual rows by their position
in the table and computing over them. Extracting rows by position
isn’t always convenient: we might have hundreds or thousands of rows,
and we might not know where the data we want even is in the table. We
would much rather be able to write a small program that identifies the
row (or rows!) that meets a specific criterion.

[Jayret offers three different notations for processing
tables: one uses functions, one uses methods, and one uses a SQL-like
notation. This chapter uses the function-based notation. The SQL-like
notation and the methods-based notation are shown in the Jayret
Documentation. To use the function-based notation, you’ll need to
include the file specified in the main narrative.]{.margin-note}

The rest of this section assumes that you have loaded the functions
notations for working with tables.

```{=html}
<a name="(part._subsec-finding-rows)"></a>
```

##### 4.1.4.1 Finding Rows {#subsec-finding-rows}

Imagine that we wanted to write a program to locate a row that has
fewer than `1000`{.jayret} riders from our `shuttle`{.jayret} table. With what
we’ve studied so far, how might we try to write this? We could imagine
using a conditional, like follows:

```jayret
if (shuttle.row-n(0)["riders"] < 1000) {
    return shuttle.row-n(0);
} else if (shuttle.row-n(1)["riders"] < 1000) {
    return shuttle.row-n(1);
} else if (shuttle.row-n(2)["riders"] < 1000) {
    return shuttle.row-n(2);
} else if (shuttle.row-n(3)["riders"] < 1000) {
    return shuttle.row-n(3);
} else {
    return ...;
}
// not clear what to do here
```

::: {.do-now}
What benefits and limitations do you see to this approach?
:::

There are a couple of reasons why we might not care for this
solution. First, if we have thousands of rows, this will be terribly
painful to write. Second, there’s a lot of repetition here (only the
row positions are changing). Third, it isn’t clear what to do if there
aren’t any matching rows. In addition, what happens if there are
multiple rows that meet our criterion? In some cases, we might want to
be able to identify all of the rows that meet a condition and
use them for a subsequent computation (like seeing whether some months
have more low-ridership days than others).

This conditional is, however, the spirit of what we want to do:
go through the rows of the table one at a time, identifying those that
match some criterion. We just don’t want to be responsible for
manually checking each row. Fortunately for us, Jayret knows how to do
that. Jayret knows which rows are in a given table. Jayret can pull
out those rows one position at a time and check a criterion about
each one.

We just need to tell Jayret what criterion we want to use.

As before, we can express our criterion as a function that takes a
`Row`{.jayret} and produces a `Boolean`{.jayret} (a Boolean because our
criterion was used as the question part of an `if`{.jayret} expression in
our code sketch). In this case, we want:

```jayret
boolean below-1K(Row r) {
    // determine whether row has fewer than 1000 riders
    return r["riders"] < 1000;
} where {
    
}
```

Now, we just need a way to tell Jayret to use this criterion as it
searches through the rows. We do this with a function called
`filter-with`{.jayret} which takes two inputs: the table to process and the
criterion to check on each row of the table.

```jayret
filter-with(shuttle, below-1K);
```

Under the hood, `filter-with`{.jayret} works roughly like the `if`{.jayret}
statement we outlined above: it takes each row one at a time and calls
the given criterion function on it. But what does it do with the
results?

If you run the above expression, you’ll see that `filter-with`{.jayret}
produces a table containing the matching row, not the row by
itself. This behavior is handy if multiple rows match the
criterion. For example, try:

```jayret
filter-with(shuttle, is-winter);
```
(using the `is-winter`{.jayret} function from an exercise earlier in this
chapter). Now we get a table with the three rows corresponding to winter
months. If we want to be able to name this table for use in future
computations, we can do so with our usual notation for naming values:

```jayret
winter = filter-with(shuttle, is-winter);
```

```{=html}
<a name="(part._Ordering-Rows)"></a>
```

##### 4.1.4.2 Ordering Rows {#Ordering-Rows}

Let’s ask a new question: which winter month had the fewest number
of riders?. This question requires us to identify a specific row,
namely, the winter row with the smallest value in the `"riders"`{.jayret}
column.

::: {.do-now}
Can we do this with `filter-with`{.jayret}? Why or why not?
:::

Think back to the `if`{.jayret} expression that motivated
`filter-with`{.jayret}: each row is evaluated independently of the
others. Our current question, however, requires comparing across
rows. That’s a different operation, so we will need more than
`filter-with`{.jayret}.

Tools for analyzing data (whether programming languages or
spreadsheets) provide ways for users to sort rows of a table
based on the values in a single column. That would help us here: we
could sort the winter rows from smallest to largest value in the
`"riders"`{.jayret} column, then extract the `"riders"`{.jayret} value from
the first row. First, let’s sort the rows:

```jayret
order-by(winter, "riders", true);
```

The `order-by`{.jayret} function takes three inputs: the table to sort
(`winter`{.jayret}), the column to sort on (`"riders"`{.jayret}), and a
`Boolean`{.jayret} to indicate whether we want to sort in increasing
order. (Had the third argument been `false`{.jayret}, the rows would be
sorted in decreasing order of the values in the named column.)

![](sorted-winter.png){width="178" height="151"}

In the sorted table, the row with the fewest riders is in the first
position. Our original question asked us to lookup the month with the
fewest riders. We did this earlier.

::: {.do-now}
Write the code to extract the name of the winter month with the fewest
riders.
:::

Here are two ways to write that computation:

```jayret
order-by(winter, "riders", true).row-n(0)["month"];
```

```jayret
sorted = order-by(winter, "riders", true);
least-row = sorted.row-n(0);
least-row["month"];
```

::: {.do-now}
Which of these two ways do you prefer? Why?
:::

::: {.do-now}
How does each of these programs affect the program
directory?
:::

Note that this problem asked us to combine several actions that we’ve
already seen on rows: we identify rows from within a table
(`filter-with`{.jayret}), order the rows (`order-by`{.jayret}), extract a
specific row (`row-n`{.jayret}), then extract a cell (with square brackets
and a column name). This is typical of how we will operate on tables,
combining multiple operations to compute a result (much as we did with
programs that manipulate images).

```{=html}
<a name="(part._Adding-New-Columns)"></a>
```

##### 4.1.4.3 Adding New Columns {#Adding-New-Columns}

Sometimes, we want to create a new column whose value is based on
those of existing columns. For instance, our table might reflect
employee records, and have columns named `hourly-wage`{.jayret} and
`hours-worked`{.jayret}, representing the corresponding quantities. We
would now like to extend this table with a new column to reflect each
employee’s total wage. Assume we started with the following table:

```jayret
employees = table: name ,hourly-wage ,hours-worked row: "Harley" ,15 ,40 row: "Obi" ,20 ,45 row: "Anjali" ,18 ,39 row: "Miyako" ,18 ,40;
```

The table we want to end up with is:

```jayret
employees = table: name ,hourly-wage ,hours-worked ,total-wage row: "Harley" ,15 ,40 ,15 * 40 row: "Obi" ,20 ,45 ,20 * 45 row: "Anjali" ,18 ,39 ,18 * 39 row: "Miyako" ,18 ,40 ,18 * 40;
```
(with the expressions in the `total-wage`{.jayret} column computed to
their numeric equivalents: we used the expressions here to illustrate
what we are trying to do).

Previously, when we have had a computation that we performed multiple
times, we created a helper function to do the computation.

::: {.do-now}
Propose a helper function for computing total wages given the hourly
wage and number of hours worked.
:::

Perhaps you came up with something like:

```jayret
int compute-wages(int wage, int hours) {
    return wage * hours;
}
```
which we could use as follows:

```jayret
employees = table: name ,hourly-wage ,hours-worked ,total-wage row: "Harley" ,15 ,40 ,compute-wages(15, 40) row: "Obi" ,20 ,45 ,compute-wages(20, 45) row: "Anjali" ,18 ,39 ,compute-wages(18, 39) row: "Miyako" ,18 ,40 ,compute-wages(18, 40);
```

This is the right idea, but we can actually have this function do a
bit more work for us. The `wage`{.jayret} and `hours`{.jayret} values are in
cells within the same row. So if we could instead get the current row
as an input, we could write:

```jayret
int compute-wages(Row r) {
    // compute total wages based on wage and hours worked
    return r["hourly-wage"] * r["hours-worked"];
}
```

But now, if we tried to use `compute-wages`{.jayret} inline for every row, we would be writing the same call over and over!
Adding computed columns is a sufficiently common operation that Jayret
provides a table function called `build-column`{.jayret} for this
purpose. We use it by providing the function to use to populate values
in the new column as an input:

```jayret
int compute-wages(Row r) {
    // compute total wages based on wage and hours worked
    return r["hourly-wage"] * r["hours-worked"];
}
build-column(employees, "total-wage", compute-wages);
```
This creates a new column, `total-wage`{.jayret}, whose value in each row
is the product of the two named columns in that row. Jayret will put
the new column at the right end.

```{=html}
<a name="(part._Calculating-New-Column-Values)"></a>
```

##### 4.1.4.4 Calculating New Column Values {#Calculating-New-Column-Values}

Sometimes, we just want to calculate new values for an existing
column, rather than create an entirely new column. Giving raises to
employees is one such example. Assume we wanted to give a `10%`{.jayret} raise to
all employees making less than `20`{.jayret} an hour. We could write:

```jayret
int new-rate(int rate) {
    // Raise rates under 20 by 10%
    return if (rate < 20) {
        return rate * 1.1;
    } else {
        return rate;
    }
} where {
    assertEquals(new-rate(15), 15 * 1.1);
    assertEquals(new-rate(20), 20);
    assertEquals(new-rate(18), 18 * 1.1);
}
Table give-raises(Table t) {
    // Give a 10% raise to anyone making under 20
    return transform-column(t, "hourly-wage", new-rate);
}
```
Here, `transform-column`{.jayret} takes a table, the name of an existing
column in the table, and a function to update the value. The updating
function takes the current value in the column as input and produces
the new value for the column as output.

::: {.do-now}
Run `give-raises`{.jayret} on the `employees`{.jayret} table. What wage will
show for `"Miyako"`{.jayret} in the `employees`{.jayret} table after
`give-raises`{.jayret} completes. Why?
:::

Like all other Jayret `Table`{.jayret} operations, `transform-column`{.jayret}
produces a new table, leaving the original intact. Editing the
original table could be problematic–what if you made a mistake? How
would you recover the original table in that case? In general,
producing new tables with any modifications, then creating a new name
for the updated table once you have the one you want, is a less
error-prone way of working with datasets.

```{=html}
<a name="(part._Examples-for-Table-Producing-Functions)"></a>
```

#### 4.1.5 Examples for Table-Producing Functions {#Examples-for-Table-Producing-Functions}

How do we write examples for functions that produce tables? Conceptually,
the answer is simply "make sure you got the output table that you
expected". Logistically, writing examples for table functions seems
more painful because writing out an expected output tables is more
work than simply writing the output of a function that produces
numbers or strings. What can we do to manage that complexity?

::: {.do-now}
How might you write the `where { }`{.jayret} block for `give-raises`{.jayret}?
:::

Here are some ideas for writing the examples practically:

- Simplify the input table. Rather than work with a large
  table with all of the columns you have, create a small table that has
  sufficient variety only in the columns that the function uses. For our
  example, we might use:
  
  ```jayret
wages-test = table: hourly-wage row: 15 row: 20 row: 18 row: 18;
  ```
  
  ::: {.do-now}
  Would any table with a column of numbers work here? Or are there some
  constraints on the rows or columns of the table?
  :::
  
  The only constraint is that your input table has to have the column
  names used in your function.
- Remember that you can write computations in the code to
  construct tables. This saves you from doing calculations by hand.
  
  ```jayret
  assertEquals(give-raises(wages-test),
      table: hourly-wage row: 15 * 1.1 row: 20 row: 18 * 1.1 row: 18 * 1.1);
  ```
  This example shows that you can write an output table directly in the
  `where { }`{.jayret} block – the table doesn’t need to be named outside the
  function.

- Create a new table by taking rows from an existing table.
  If you were instead writing examples for a function that involves filtering out rows
  of a table, it helps to know how to create a new table using rows of
  an existing one. For example, if we were writing a function to find
  all rows in which employees were working exactly 40 hours, we’d like
  to make sure that the resulting table had the first and fourth rows of
  the `employees`{.jayret} table. Rather than write a new `table`{.jayret}
  expression to create that table, we could write it as follows:
  
  ```jayret
emps-at-40 = add-row(add-row(employees.empty(), employees.row-n(0)), employees.row-n(3));
  ```
  Here, `employees.empty()`{.jayret} creates a new, empty table with the
  same column headers as `employees`{.jayret}. We’ve already seen how
  `row-n`{.jayret} extracts a row from a table. The `add-row`{.jayret} function
  places the given row at the end of the given table.

Another tip to keep in mind: when the only thing your function does is call
a built-in function like `transform-column`{.jayret} it usually suffices
to write examples for the function you wrote to compute the new column
value. It is only when your code is combining table operations, or
doing more complex processing than a single call to a built-in table
operation that you really need to present your own examples to a
reader of your code.

```{=html}
<a name="(part._sec-lambda-tables)"></a>
```

#### 4.1.6 Lambda: Anonymous Functions {#sec-lambda-tables}

Let’s revisit the program we wrote in [Finding Rows](intro-tabular-data.html##subsec-finding-rows) for
finding all of the months in a table with fewer than 1000 riders:

```jayret
shuttle = table: month ,riders row: "Jan" ,1123 row: "Feb" ,1045 row: "Mar" ,1087 row: "Apr" ,999;
boolean below-1K(Row r) {
    // determine whether row has fewer than 1000 riders
    return r["riders"] < 1000;
} where {
    
}
filter-with(shuttle, below-1K);
```

This program might feel a bit verbose: do we really need to write a
helper function just to perform something as simple as a
`filter-with`{.jayret}? Wouldn’t it be easier to just write something like:

```jayret
filter-with(shuttle, r["riders"] < 1000);
```

::: {.do-now}
What will Jayret produce if you run this expression?
:::

Jayret will produce an `unbound;
identifier`{.jayret} error around the use
of `r`{.jayret} in this expression. What is `r`{.jayret}? We mean for `r`{.jayret}
to be the elements from `shuttle`{.jayret} in turn. Conceptually, that’s
what `filter-with`{.jayret} does, but we don’t have the mechanics right. When
we call a function, we evaluate the arguments before the body
of the function. Hence, the error regarding `r`{.jayret} being unbound.
The whole point of the `below-1K`{.jayret} helper function is to make
`r`{.jayret} a parameter to a function whose body is only evaluated once
a value for `r`{.jayret} is available.

To tighten the notation as in the one-line `filter-with`{.jayret} expression,
then, we have to find a way to tell Jayret to make a temporary function
that will get its inputs once `filter-with`{.jayret} is running. The following
notation achieves this:

```jayret
filter-with(shuttle, (r) -> r["riders"] < 1000);
```

We have written the expression as an arrow function `(r) -> ...`{.jayret}.
The parameter list `(r)`{.jayret} introduces the input `r`, and the arrow
`->`{.jayret} separates the parameters from the body expression. Such
anonymous functions are commonly called *lambdas*; they exist in many
languages but with different syntaxes.

The main difference between our original expression (using the
`below-1K`{.jayret} helper) and this new one (using arrow syntax) can be
seen through the program directory. To explain this, a little detail
about how `filter-with`{.jayret} is defined under the hood. In part, it looks
like:

```jayret
Table filter-with(Table tbl, (Row -> boolean) keep) {
    return if (keep(<row-from-table>)) {
        return ...;
    } else {
        return ...;
    }
}
```

Whether we pass `below-1K`{.jayret} or the arrow-function version to
`filter-with`{.jayret}, the `keep`{.jayret} parameter ends up referring to a
function with the same parameter and body. Since the function is only
actually called through the `keep`{.jayret} name, it doesn’t matter
whether or not a name is associated with it when it is initially
defined.

In practice, we use arrow functions when we have to pass simple (single line)
functions to operations like `filter-with`{.jayret} (or `transform-column`{.jayret},
`build-column`{.jayret}, etc). Of course, you can continue to write out names for
helper functions as we did with `below-1K`{.jayret} if that makes more sense to
you.

::: {.exercise}
Write the program to add 10 riders to each row in the `shuttle`{.jayret}
table above, using arrow syntax rather than a named helper-function.
:::
