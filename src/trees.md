---
title: Trees
section_number: 7.1
source_file: trees.html
prev: part_trees.html
up: part_trees.html
next: part_bonus-foundations.html
---

```{=html}
<a name="(part._trees)"></a>
```

### 7.1 Trees {#trees}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._ancestor-trees%29">7.1.1<span class="hspace"> </span>Data Design Problem – Ancestry Data</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._compute-parents-table%29">7.1.1.1<span class="hspace"> </span>Computing Genetic Parents from an Ancestry Table</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Computing_.Grandparents_from_an_.Ancestry_.Table%29">7.1.1.2<span class="hspace"> </span>Computing Grandparents from an Ancestry Table</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._ancestor-tree%29">7.1.1.3<span class="hspace"> </span>Creating a Datatype for Ancestor Trees</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Programs_to_.Process_.Ancestor_.Trees%29">7.1.2<span class="hspace"> </span>Programs to Process Ancestor Trees</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Summarizing_.How_to_.Approach_.Tree_.Problems%29">7.1.3<span class="hspace"> </span>Summarizing How to Approach Tree Problems</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="trees.html#%28part._.Study_.Questions%29">7.1.4<span class="hspace"> </span>Study Questions</a></p></td></tr></table>
```

```{=html}
<a name="(part._ancestor-trees)"></a>
```

#### 7.1.1 Data Design Problem – Ancestry Data {#ancestor-trees}

Imagine that we wanted to manage ancestry information for
purposes of a medical research study. Specifically, we want to record
people’s birthyear, eye colors, and genetic parents. Here’s a
sample table of such data, with one row for each person:

```jayret
ancestors = table: name ,birthyear ,eyecolor ,female-parent ,male-parent row: "Anna" ,1997 ,"blue" ,"Susan" ,"Charlie" row: "Susan" ,1971 ,"blue" ,"Ellen" ,"Bill" row: "Charlie" ,1972 ,"green" ,"" ,"" row: "Ellen" ,1945 ,"brown" ,"Laura" ,"John" row: "John" ,1922 ,"brown" ,"" ,"Robert" row: "Laura" ,1922 ,"brown" ,"" ,"" row: "Robert" ,1895 ,"blue" ,"" ,"";
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
(we’ll call it `parents-of`{.jayret}). Since this sounds like a routine
table program, we can use it for a bit of review:

```{=html}
<a name="(part._compute-parents-table)"></a>
```

##### 7.1.1.1 Computing Genetic Parents from an Ancestry Table {#compute-parents-table}

How do we compute a list of someone’s genetic parents? Let’s sketch a
task plan for that:

- filter the table to find the person

- extract the name of the female parent

- extract the name of the male parent

- make a list of those names

These are tasks we have seen before, so we can translate this
plan directly into code:

```jayret
List<Object> parents-of(Table anc-table, String who) {
    // Return list of names of known parents of given name
    matches = filter-with(anc-table, (r) -> r["name"] == who);
    return if (matches.length() > 0) {
        person-row = matches.row-n(0);
        return [person-row["female-parent"], person-row["male-parent"]];
    } else {
        return empty;
    }
} where {
    
}
```

::: {.do-now}
Are you satisfied with this program? With the examples included in the
`where`{.jayret} block? Write down any critiques you have.
:::

There are arguably some issues here. How many of these did you catch?

- The examples are weak: none of them consider people for
  whom we are missing information on at least one parent.

- The list of names returned in the case of an unknown parent
  includes the empty string, which isn’t actually a name. This could
  cause problems if we use this list of names in a subsequent
  computation (such as to compute the names of someone’s grandparents).

- If empty strings are not part of the output list, then we’d get
  the same result from asking for the parents of `"Robert"`{.jayret} (who is
  in the table) as for `"Kathi"`{.jayret} (who is not). These are
  fundamentally different cases, which arguably demand different
  outputs so we can tell them apart.

To fix these problems, we need to remove the empty strings from the
produced list of parents and return something other than the
`empty`{.jayret} list when a name is not in the table. Since the output of
this function is a list of strings, it’s hard to see what to return
that couldn’t be confused for a valid list of names. Our solution for
now is to have Jayret throw an error (like the ones you get when Jayret
is not able to finish running your program). Here’s a solution that
handles both problems:

```jayret
List<Object> parents-of(Table anc-table, String who) {
    // Return list of names of known parents of given name
    matches = filter-with(anc-table, (r) -> r["name"] == who);
    return if (matches.length() > 0) {
        person-row = matches.row-n(0);
        names = [person-row["female-parent"], person-row["male-parent"]];
        return L.filter((n) -> not(n == ""), names);
    } else {
        return raise("No such person " + who);
    }
} where {
    
}
```

The `raise`{.jayret} construct tells Jayret to halt the program and produce
an error message. The error message does not have to match the
expected output type of the program. If you run this function with a
name that is not in the table, you’ll see an error appear in the
interactions pane, with no result returned.

Within the `where`{.jayret} block, we see how to check whether an
expression will yield an error: instead of using `is`{.jayret} to check
the equality of values, we use `raises`{.jayret} to check whether the
provided string is a sub-string of the actual error produced by the
program.

```{=html}
<a name="(part._Computing-Grandparents-from-an-Ancestry-Table)"></a>
```

##### 7.1.1.2 Computing Grandparents from an Ancestry Table {#Computing-Grandparents-from-an-Ancestry-Table}

Once we have the `parents-of`{.jayret} function, we should be able to
compute the grandparents by computing parents of parents, as follows:

```jayret
List<Object> grandparents-of(Table anc-table, String who) {
    // compute list of known grandparents in the table
    // glue together lists of mother's parents and father's parents
    plist = parents-of(anc-table, who);
    return // gives a list of two names
    parents-of(anc-table, plist.first) + parents-of(anc-table, plist.rest.first);
} where {
    
}
```

::: {.do-now}
Look back at our sample ancestry tree: for which people would this
correctly compute the list of grandparents?
:::

This grandparents-of code works fine for someone who has both
parents in the table. For someone without two parents, however, the
`plist`{.jayret} will have fewer than two names, so the expression
`plist.rest.first`{.jayret} (if not `plist.first`{.jayret}) will yield an
error.

Here’s a version that checks the number of parents before computing
the set of grandparents:

```jayret
List<Object> grandparents-of(Table anc-table, String who) {
    // compute list of known grandparents in the table
    // glue together lists of mother's parents and father's parents
    plist = parents-of(anc-table, who);
    return // gives a list of two names
    if (plist.length() == 2) {
        return parents-of(anc-table, plist.first) + parents-of(anc-table, plist.rest.first);
    } else if (plist.length() == 1) {
        return parents-of(anc-table, plist.first);
    } else {
        return empty;
    }
} where {
    
}
```

What if we now wanted to gather up all of someone’s ancestors? Since
we don’t know how many generations there are, we’d need to use
recursion. This approach would also be expensive, since we’d end up
filtering over the table over and over, which checks every row of the
table in each use of `filter`{.jayret}.

Look back at the ancestry tree picture. We don’t do any complicated
filtering there – we just follow the line in the picture immediately
from a person to their mother or father. Can we get that idea in code
instead? Yes, through datatypes.

```{=html}
<a name="(part._ancestor-tree)"></a>
```

##### 7.1.1.3 Creating a Datatype for Ancestor Trees {#ancestor-tree}

For this approach, we want to create a datatype for Ancestor Trees
that has a variant (constructor) for setting up a person. Look
back at our picture – what information makes up a person? Their
name, their mother, and their father (along with birthyear and
eyecolor, which aren’t shown in the picture). This suggests the following
datatype, which basically turns a row into a person value:

```jayret
data AncTree {
    Person(String name, int birthyear, String eye, ________ mother, ________ father);
}
```

For example, anna’s row might look like:

```jayret
# TODO(pyret2jayret): parse failed (no shifts)
anna-row = person("Anna", 1997, "blue", ???, ???)
```

What type do we put in the blanks? A quick brainstorm yields
several ideas:


- `person`{.jayret}

- `List < person >`{.jayret}

- some new datatype

- `AncTree`{.jayret}

- `String`{.jayret}

Which should it be?

If we use a `String`{.jayret}, we’re back to the table row, and we don’t
end up with a way to easily get from one person to another. We should
therefore make this an `AncTree`{.jayret}.

```jayret
data AncTree {
    Person(String name, int birthyear, String eye, AncTree mother, AncTree father);
}
```

::: {.do-now}
Write the `AncTree`{.jayret} starting from `Anna`{.jayret} using this definition.
:::

Did you get stuck? What do we do when we run out of known people? To
handle that, we must add an option in the `AncTree`{.jayret} definition to
capture people for whom we don’t know anything.

```jayret
data AncTree {
    NoInfo;
    Person(String name, int birthyear, String eye, AncTree mother, AncTree father);
}
```

Here’s Anna’s tree written in this datatype:

```jayret
anna-tree = person("Anna", 1997, "blue", person("Susan", 1971, "blue", person("Ellen", 1945, "brown", person("Laura", 1920, "blue", noInfo, noInfo), person("John", 1920, "green", noInfo, person("Robert", 1893, "brown", noInfo, noInfo))), person("Bill", 1946, "blue", noInfo, noInfo)), person("Charlie", 1972, "green", noInfo, noInfo));
```

We could also have named each person data individually.

```jayret
robert-tree = person("Robert", 1893, "brown", noInfo, noInfo);
laura-tree = person("Laura", 1920, "blue", noInfo, noInfo);
john-tree = person("John", 1920, "green", noInfo, robert-tree);
ellen-tree = person("Ellen", 1945, "brown", laura-tree, john-tree);
bill-tree = person("Bill", 1946, "blue", noInfo, noInfo);
susan-tree = person("Susan", 1971, "blue", ellen-tree, bill-tree);
charlie-tree = person("Charlie", 1972, "green", noInfo, noInfo);
anna-tree2 = person("Anna", 1997, "blue", susan-tree, charlie-tree);
```

The latter gives you pieces of the tree to use as other examples, but
loses the structure that is visible in the indentation of the first
version. You could get to pieces of the first version by digging into
the data, such as writing `anna-tree.mother.mother`{.jayret} to get to the
tree starting from "Ellen".

Here’s the `parents-of`{.jayret} function written against `AncTree`{.jayret}:

```jayret
List<Object> parents-of-tree(AncTree tr) {
    return switch (tr) {
        case NoInfo: yield empty;
        case Person(n, y, e, m, f): yield [m.name, f.name];
    }
}
// person bit more complicated if parent is missing
```

```{=html}
<a name="(part._Programs-to-Process-Ancestor-Trees)"></a>
```

#### 7.1.2 Programs to Process Ancestor Trees {#Programs-to-Process-Ancestor-Trees}

How would we write a function to determine whether anyone in the tree
had a particular name? To be clear, we are trying to fill in the
following code:

```jayret
# TODO(pyret2jayret): parse failed (no shifts)
fun in-tree(at :: AncTree, name :: String) -> Boolean:
  doc: "determine whether name is in the tree"
  ...
```

How do we get started? Add some examples, remembering to check both
cases of the `AncTree`{.jayret} definition:

```jayret
boolean in-tree(AncTree at, String name) {
    // determine whether name is in the tree
    return ...;
} where {
    
}
```

What next? When we were working on lists, we talked about
the template, a skeleton of code that we knew we could write
based on the structure of the data. The template names the pieces of
each kind of data, and makes recursive calls on pieces that have the
same type. Here’s the template over the `AncTree`{.jayret} filled in:

```jayret
boolean in-tree(AncTree at, String name) {
    // determine whether name is in the tree
    return switch (at) {
        case NoInfo: yield // comes from AncTree being data with cases
        ...;
        case Person(n, y, e, m, f): yield block {
            ...;
            in-tree(m, name);
            ...;
            return in-tree(f, name);
        };
    }
} where {
    
}
```

To finish the code, we need to think about how to fill in the
ellipses.

- When the tree is `noInfo`{.jayret}, it has no more people, so the answer
  should be false (as worked out in the examples).

- When the tree is a person, there are three possibilities: we
  could be at a person with the name we’re looking for, or the name
  could be in the mother’s tree, or the name could be in the father’s
  tree.
  
  We know how to check whether the person’s name matches the one
  we are looking for. The recursive calls already ask about the name
  being in the mother’s tree or father’s tree. We just need to combine
  those pieces into one Boolean answer. Since there are three
  possibilities, we should combine them with `||`{.jayret}

Here’s the final code:

```jayret
boolean in-tree(AncTree at, String name) {
    // determine whether name is in the tree
    return switch (at) {
        case NoInfo: yield // comes from AncTree being data with cases
        false;
        case Person(n, y, e, m, f): yield (name == n) || in-tree(m, name) || in-tree(f, name);
    }
} where {
    
}
// n is the same as at.name
// m is the same as at.mother
```

```{=html}
<a name="(part._Summarizing-How-to-Approach-Tree-Problems)"></a>
```

#### 7.1.3 Summarizing How to Approach Tree Problems {#Summarizing-How-to-Approach-Tree-Problems}

We design tree programs using the same design recipe that we covered
on lists:

::: {.strategy}
- Write the datatype for your tree, including a base/leaf case

- Write examples of your trees for use in testing

- Write the function name, parameters, and types (the `fun`{.jayret}
  line)

- Write `where`{.jayret} checks for your code

- Write the template, including the cases and recursive
  calls. Here’s the template again for an ancestor tree, for an
  arbitrary function called treeF:
  
  ```jayret
boolean treeF(String name, AncTree t) {
    return switch (anct) {
        case Unknown: yield ...;
        case Person(n, y, e, m, f): yield block {
            ...;
            treeF(name, m);
            ...;
            return treeF(name, f);
        };
    }
}
  ```
- Fill in the template with details specific to the problem

- Test your code using your examples
:::

```{=html}
<a name="(part._Study-Questions)"></a>
```

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
