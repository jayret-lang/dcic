---
title: Trees
section_number: 7.1
source_file: trees.html
prev: part_trees.html
up: part_trees.html
next: part_bonus-foundations.html
---

### 7.1 Trees {#trees}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._ancestor-trees%29">7.1.1<span class="hspace"> </span>Data Design Problem – Ancestry Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._compute-parents-table%29">7.1.1.1<span class="hspace"> </span>Computing Genetic Parents from an Ancestry Table</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Computing_.Grandparents_from_an_.Ancestry_.Table%29">7.1.1.2<span class="hspace"> </span>Computing Grandparents from an Ancestry Table</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._ancestor-tree%29">7.1.1.3<span class="hspace"> </span>Creating a Datatype for Ancestor Trees</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Programs_to_.Process_.Ancestor_.Trees%29">7.1.2<span class="hspace"> </span>Programs to Process Ancestor Trees</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Summarizing_.How_to_.Approach_.Tree_.Problems%29">7.1.3<span class="hspace"> </span>Summarizing How to Approach Tree Problems</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Study_.Questions%29">7.1.4<span class="hspace"> </span>Study Questions</a></p></td></tr></table>
```

#### 7.1.1 Data Design Problem – Ancestry Data {#ancestor-trees}

Imagine that we wanted to manage ancestry information for
purposes of a medical research study. Specifically, we want to record
people’s birthyear, eye colors, and genetic parents. Here’s a
sample table of such data, with one row for each person:

```pyret
ancestors = table: name, birthyear, eyecolor, female-parent, male-parent
  row: "Anna", 1997, "blue", "Susan", "Charlie"
  row: "Susan", 1971, "blue", "Ellen", "Bill"
  row: "Charlie", 1972, "green", "", ""
  row: "Ellen", 1945, "brown", "Laura", "John"
  row: "John", 1922, "brown", "", "Robert"
  row: "Laura", 1922, "brown", "", ""
  row: "Robert", 1895, "blue", "", ""
end
```

For our research, we want to be able to answer questions such as the following:

- Who are the genetic grandparents of a specific person?
- How frequent is each eye color?
- Is one specific person an ancestor of another specific person?
- How many generations do we have information for?
- Does one’s eye color correlate with the ages of their genetic
  parents when they were born?

Let’s start with the first question:

::: {.do-now}
How would you compute a list of the known grandparents for a given
person? For purposes of this chapter, you may assume that each person
has a unique name (while this isn’t realistic in practice, it will
simplify our computations for the time being; we will revisit it later
in the chapter).

(Hint: Make a task plan. Does it suggest any particular helper functions?)
:::

Our task plan has two key steps: find the names of the genetic
parents of the named person, then find the names of the parents of
each of those people. Both steps share the need to compute the known
parents from a name, so we should create a helper function for that
(we’ll call it `parents-of`{.pyret}). Since this sounds like a routine
table program, we can use it for a bit of review:

##### 7.1.1.1 Computing Genetic Parents from an Ancestry Table {#compute-parents-table}

How do we compute a list of someone’s genetic parents? Let’s sketch a
task plan for that:

- filter the table to find the person
- extract the name of the female parent
- extract the name of the male parent
- make a list of those names

These are tasks we have seen before, so we can translate this
plan directly into code:

```pyret
fun parents-of(anc-table :: Table, who :: String) -> List<String>:
  doc: "Return list of names of known parents of given name"
  matches = filter-with(anc-table, lam(r): r["name"] == who end)
  if matches.length() > 0:
    person-row = matches.row-n(0)
    [list:
      person-row["female-parent"],
      person-row["male-parent"]]
  else:
    empty
  end
where:
  parents-of(ancestors, "Anna")
    is [list: "Susan", "Charlie"]
  parents-of(ancestors, "Kathi") is empty
end
```

::: {.do-now}
Are you satisfied with this program? With the examples included in the
`where`{.pyret} block? Write down any critiques you have.
:::

There are arguably some issues here. How many of these did you catch?

- The examples are weak: none of them consider people for
  whom we are missing information on at least one parent.
- The list of names returned in the case of an unknown parent
  includes the empty string, which isn’t actually a name. This could
  cause problems if we use this list of names in a subsequent
  computation (such as to compute the names of someone’s grandparents).
- If empty strings are not part of the output list, then we’d get
  the same result from asking for the parents of `"Robert"`{.pyret} (who is
  in the table) as for `"Kathi"`{.pyret} (who is not). These are
  fundamentally different cases, which arguably demand different
  outputs so we can tell them apart.

To fix these problems, we need to remove the empty strings from the
produced list of parents and return something other than the
`empty`{.pyret} list when a name is not in the table. Since the output of
this function is a list of strings, it’s hard to see what to return
that couldn’t be confused for a valid list of names. Our solution for
now is to have Pyret throw an error (like the ones you get when Pyret
is not able to finish running your program). Here’s a solution that
handles both problems:

```pyret
fun parents-of(anc-table :: Table, who :: String) -> List<String>:
  doc: "Return list of names of known parents of given name"
  matches = filter-with(anc-table, lam(r): r["name"] == who end)
  if matches.length() > 0:
    person-row = matches.row-n(0)
    names =
     [list: person-row["female-parent"],
       person-row["male-parent"]]
    L.filter(lam(n): not(n == "") end, names)
  else:
    raise("No such person " + who)
  end
where:
  parents-of(ancestors, "Anna") is [list: "Susan", "Charlie"]
  parents-of(ancestors, "John") is [list: "Robert"]
  parents-of(ancestors, "Robert") is empty
  parents-of(ancestors, "Kathi") raises "No such person"
end
```

The `raise`{.pyret} construct tells Pyret to halt the program and produce
an error message. The error message does not have to match the
expected output type of the program. If you run this function with a
name that is not in the table, you’ll see an error appear in the
interactions pane, with no result returned.

Within the `where`{.pyret} block, we see how to check whether an
expression will yield an error: instead of using `is`{.pyret} to check
the equality of values, we use `raises`{.pyret} to check whether the
provided string is a sub-string of the actual error produced by the
program.

##### 7.1.1.2 Computing Grandparents from an Ancestry Table {#Computing-Grandparents-from-an-Ancestry-Table}

Once we have the `parents-of`{.pyret} function, we should be able to
compute the grandparents by computing parents of parents, as follows:

```pyret
fun grandparents-of(anc-table :: Table, who :: String) -> List<String>:
  doc: "compute list of known grandparents in the table"
  # glue together lists of mother's parents and father's parents
  plist = parents-of(anc-table, who) # gives a list of two names
  parents-of(anc-table, plist.first) +
    parents-of(anc-table, plist.rest.first)
where:
  grandparents-of(ancestors, "Anna") is [list: "Ellen", "Bill"]
  grandparents-of(ancestors, "Laura") is [list:]
  grandparents-of(ancestors, "John") is [list: ]
  grandparents-of(ancestors, "Kathi") is [list:]
end
```

::: {.do-now}
Look back at our sample ancestry tree: for which people would this
correctly compute the list of grandparents?
:::

This grandparents-of code works fine for someone who has both
parents in the table. For someone without two parents, however, the
`plist`{.pyret} will have fewer than two names, so the expression
`plist.rest.first`{.pyret} (if not `plist.first`{.pyret}) will yield an
error.

Here’s a version that checks the number of parents before computing
the set of grandparents:

```pyret
fun grandparents-of(anc-table :: Table, who :: String) -> List<String>:
  doc: "compute list of known grandparents in the table"
  # glue together lists of mother's parents and father's parents
  plist = parents-of(anc-table, who) # gives a list of two names
  if plist.length() == 2:
    parents-of(anc-table, plist.first) + parents-of(anc-table, plist.rest.first)
  else if plist.length() == 1:
    parents-of(anc-table, plist.first)
  else: empty
  end
where:
  grandparents-of(ancestors, "Anna") is [list: "Ellen", "Bill"]
  grandparents-of(ancestors, "Laura") is [list:]
  grandparents-of(ancestors, "John") is [list: ]
  grandparents-of(ancestors, "Kathi") raises "No such person"
end
```

What if we now wanted to gather up all of someone’s ancestors? Since
we don’t know how many generations there are, we’d need to use
recursion. This approach would also be expensive, since we’d end up
filtering over the table over and over, which checks every row of the
table in each use of `filter`{.pyret}.

Look back at the ancestry tree picture. We don’t do any complicated
filtering there – we just follow the line in the picture immediately
from a person to their mother or father. Can we get that idea in code
instead? Yes, through datatypes.

##### 7.1.1.3 Creating a Datatype for Ancestor Trees {#ancestor-tree}

For this approach, we want to create a datatype for Ancestor Trees
that has a variant (constructor) for setting up a person. Look
back at our picture – what information makes up a person? Their
name, their mother, and their father (along with birthyear and
eyecolor, which aren’t shown in the picture). This suggests the following
datatype, which basically turns a row into a person value:

```pyret
data AncTree:
  | person(
      name :: String,
      birthyear :: Number,
      eye :: String,
      mother :: ________,
      father :: ________
      )
end
```

For example, anna’s row might look like:

```pyret
anna-row = person("Anna", 1997, "blue", ???, ???)
```

What type do we put in the blanks? A quick brainstorm yields
several ideas:


- `person`{.pyret}
- `List<person>`{.pyret}
- some new datatype
- `AncTree`{.pyret}
- `String`{.pyret}

Which should it be?

If we use a `String`{.pyret}, we’re back to the table row, and we don’t
end up with a way to easily get from one person to another. We should
therefore make this an `AncTree`{.pyret}.

```pyret
data AncTree:
  | person(
      name :: String,
      birthyear :: Number,
      eye :: String,
      mother :: AncTree,
      father :: AncTree
      )
end
```

::: {.do-now}
Write the `AncTree`{.pyret} starting from `Anna`{.pyret} using this definition.
:::

Did you get stuck? What do we do when we run out of known people? To
handle that, we must add an option in the `AncTree`{.pyret} definition to
capture people for whom we don’t know anything.

```pyret
data AncTree:
  | noInfo
  | person(
      name :: String,
      birthyear :: Number,
      eye :: String,
      mother :: AncTree,
      father :: AncTree
      )
end
```

Here’s Anna’s tree written in this datatype:

```pyret
anna-tree =
  person("Anna", 1997, "blue",
    person("Susan", 1971, "blue",
      person("Ellen", 1945, "brown",
        person("Laura", 1920, "blue", noInfo, noInfo),
        person("John", 1920, "green",
          noInfo,
          person("Robert", 1893, "brown", noInfo, noInfo))),
      person("Bill", 1946, "blue", noInfo, noInfo)),
    person("Charlie", 1972, "green", noInfo, noInfo))
```

We could also have named each person data individually.

```pyret
robert-tree = person("Robert", 1893, "brown", noInfo, noInfo)
laura-tree = person("Laura", 1920, "blue", noInfo, noInfo)
john-tree = person("John", 1920, "green", noInfo, robert-tree)
ellen-tree = person("Ellen", 1945, "brown", laura-tree, john-tree)
bill-tree = person("Bill", 1946, "blue", noInfo, noInfo)
susan-tree = person("Susan", 1971, "blue", ellen-tree, bill-tree)
charlie-tree = person("Charlie", 1972, "green", noInfo, noInfo)
anna-tree2 = person("Anna", 1997, "blue", susan-tree, charlie-tree)
```

The latter gives you pieces of the tree to use as other examples, but
loses the structure that is visible in the indentation of the first
version. You could get to pieces of the first version by digging into
the data, such as writing `anna-tree.mother.mother`{.pyret} to get to the
tree starting from "Ellen".

Here’s the `parents-of`{.pyret} function written against `AncTree`{.pyret}:

```pyret
fun parents-of-tree(tr :: AncTree) -> List<String>:
  cases (AncTree) tr:
    | noInfo => empty
    | person(n, y, e, m, f) => [list: m.name, f.name]
      # person bit more complicated if parent is missing
  end
end
```

#### 7.1.2 Programs to Process Ancestor Trees {#Programs-to-Process-Ancestor-Trees}

How would we write a function to determine whether anyone in the tree
had a particular name? To be clear, we are trying to fill in the
following code:

```pyret
fun in-tree(at :: AncTree, name :: String) -> Boolean:
  doc: "determine whether name is in the tree"
  ...
```

How do we get started? Add some examples, remembering to check both
cases of the `AncTree`{.pyret} definition:

```pyret
fun in-tree(at :: AncTree, name :: String) -> Boolean:
  doc: "determine whether name is in the tree"
  ...
where:
  in-tree(anna-tree, "Anna") is true
  in-tree(anna-tree, "Ellen") is true
  in-tree(ellen-tree, "Anna") is false
  in-tree(noInfo, "Ellen") is false
end
```

What next? When we were working on lists, we talked about
the template, a skeleton of code that we knew we could write
based on the structure of the data. The template names the pieces of
each kind of data, and makes recursive calls on pieces that have the
same type. Here’s the template over the `AncTree`{.pyret} filled in:

```pyret
fun in-tree(at :: AncTree, name :: String) -> Boolean:
  doc: "determine whether name is in the tree"
  cases (AncTree) at:     # comes from AncTree being data with cases
    | noInfo => ...
    | person(n, y, e, m, f) => ... in-tree(m, name) ... in-tree(f, name)
  end
where:
  in-tree(anna-tree, "Anna") is true
  in-tree(anna-tree, "Ellen") is true
  in-tree(ellen-tree, "Anna") is false
  in-tree(noInfo, "Ellen") is false
end
```

To finish the code, we need to think about how to fill in the
ellipses.

- When the tree is `noInfo`{.pyret}, it has no more people, so the answer
  should be false (as worked out in the examples).
- When the tree is a person, there are three possibilities: we
  could be at a person with the name we’re looking for, or the name
  could be in the mother’s tree, or the name could be in the father’s
  tree.
  
  We know how to check whether the person’s name matches the one
  we are looking for. The recursive calls already ask about the name
  being in the mother’s tree or father’s tree. We just need to combine
  those pieces into one Boolean answer. Since there are three
  possibilities, we should combine them with `or`{.pyret}

Here’s the final code:

```pyret
fun in-tree(at :: AncTree, name :: String) -> Boolean:
  doc: "determine whether name is in the tree"
  cases (AncTree) at:     # comes from AncTree being data with cases
    | noInfo => false
    | person(n, y, e, m, f) => (name == n) or in-tree(m, name) or in-tree(f, name)
      # n is the same as at.name
      # m is the same as at.mother
  end
where:
  in-tree(anna-tree, "Anna") is true
  in-tree(anna-tree, "Ellen") is true
  in-tree(ellen-tree, "Anna") is false
  in-tree(noInfo, "Ellen") is false
end
```

#### 7.1.3 Summarizing How to Approach Tree Problems {#Summarizing-How-to-Approach-Tree-Problems}

We design tree programs using the same design recipe that we covered
on lists:

::: {.strategy}
- Write the datatype for your tree, including a base/leaf case
- Write examples of your trees for use in testing
- Write the function name, parameters, and types (the `fun`{.pyret}
  line)
- Write `where`{.pyret} checks for your code
- Write the template, including the cases and recursive
  calls. Here’s the template again for an ancestor tree, for an
  arbitrary function called treeF:
  
  ```pyret
  fun treeF(name :: String, t :: AncTree) -> Boolean:
    cases (AncTree) anct:
      | unknown => ...
      | person(n, y, e, m, f) =>
       ... treeF(name, m) ... treeF(name, f)
    end
  end
  ```
- Fill in the template with details specific to the problem
- Test your code using your examples
:::

#### 7.1.4 Study Questions {#Study-Questions}

- Think of writing in-tree on a table (using filter-by) vs writing
  it on a tree. How many times might each approach compare the name
  being sought against a name in the table/tree?
- Why do we need to use a recursive function to process the tree?
- In what order will we check the names in the tree version?

For practice, try problems such as

- How many blue-eyed people are in the tree?
- How many people are in the tree?
- How many generations are in the tree?
- How many people have a given name in a tree?
- How many people have names starting with "A"?
- ... and so on
