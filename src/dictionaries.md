---
title: Dictionaries
section_number: 9.2
source_file: dictionaries.html
prev: intro-python.html
up: part_pyret-to-python.html
next: arrays.html
---

```{=html}
<a name="(part._dictionaries)"></a>
```

### 9.2 Dictionaries {#dictionaries}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="dictionaries.html#%28part._Creating-and-Using-a-Dictionary%29">9.2.1<span class="hspace"> </span>Creating and Using a Dictionary</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="dictionaries.html#%28part._Searching-Through-the-Values-in-a-Dictionary%29">9.2.2<span class="hspace"> </span>Searching Through the Values in a Dictionary</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="dictionaries.html#%28part._Dictionaries-with-More-Complex-Values%29">9.2.3<span class="hspace"> </span>Dictionaries with More Complex Values</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="dictionaries.html#%28part._Dictionaries-versus-Dataclasses%29">9.2.4<span class="hspace"> </span>Dictionaries versus Dataclasses</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="dictionaries.html#%28part._Summary%29">Summary</a></p></td></tr></table>
```

So far, we have seen several ways to process sequential data such as
lists. In each of Jayret and Python, we can use `filter`{.python} and
`map`{.python} to perform certain operations that yield lists. In Jayret,
we used recursion to aggregate list data into a single value. In
Python, we used for-loops for this task. While we could use recursion
or for-loops for `filter`{.python} and `map`{.python} tasks as well, using
these named operators makes it easier for someone else to quickly read
your code and understand what kind of operation it is performing.

This observation raises a question though: are there other common code
patterns that get written with recursion or for-loops that would
benefit from specialized handling?

As an example, imagine that we had a dataclass for airline
flights. Each flight has its origin and destination cities, the flight
code (including the airline name and flight number), and the number of seats on the
flight. Imagine also that we have functions to look up the destination
and seating capacity of individual flights:

```python
@dataclass
class Flight:
    from_city: str
    to_city: str
    code: str
    seats: int

schedule = [Flight('NYC','PVD','CSA-342',50),
            Flight('PVD','ORD','CSA-590',50),
            Flight('NYC','ORD','CSA-723',120),
            Flight('ORD','DEN','CSA-145',175),
            Flight('BOS','ORD','CSA-647',80)]

def destination1(for_code: str, flights: list):
   '''get the destination of the flight with the given code'''
   for fl in flights:
      if fl.code == for_code:
          return fl.to_city

def capacity1(for_code: str, flights: list):
   '''get the seating capacity of the flight with the given code'''
   for fl in flights:
      if fl.code == for_code:
          return fl.seats
```

::: {.do-now}
Look at the similarity between `destination1`{.python} and
`capacity1`{.python}. How might we share the common code between these
two functions?
:::

Both `destination1`{.python} and `capacity1`{.python} traverse the list of
flights looking for the one with the given flight-code, then extract a
piece of information from that flight. The for-loop isn’t doing
anything other than looking for the desired flight data. This suggests
that a `find_flight`{.python} helper could be useful here:

```python
def find_flight(for_code: str, flights: list):
   '''return the flight with the given code'''
   for fl in flights:
      if fl.code == for_code:
          return fl

def destination2(for_code: str, flights: list):
    return find_flight(for_code, flights).to_city

def capacity2(for_code: str, flights: list):
    return find_flight(for_code, flights).seats
```

Searching for a single element from a list based on a specific piece
of information is common in many programs. This is so common, in fact,
that languages provide special data structures and operations just to
help with this task. In Python, this data structure is called a
dictionary (hashmap, hashtable, and
associative arrays are names for similar data structures in other
languages, though there are key nuances that distinguish all these variations).

```{=html}
<a name="(part._Creating-and-Using-a-Dictionary)"></a>
```

#### 9.2.1 Creating and Using a Dictionary {#Creating-and-Using-a-Dictionary}

A dictionary maps unique values (called keys) to corresponding pieces
of data for each key (called values). Here is our flight example
written instead as a dictionary instead of a list:

```python
sched_dict = {'CSA-342': Flight('NYC','PVD','CSA-342',50),
              'CSA-590': Flight('PVD','ORD','CSA-590',50),
              'CSA-723': Flight('NYC','ORD','CSA-723',120),
              'CSA-145': Flight('ORD','DEN','CSA-145',175),
              'CSA-647': Flight('BOS','ORD','CSA-647',80)
             }
```

The general form of a dictionary is:

```python
{key1: value1,
 key2: value2,
 key3: value3,
 ...}
```

Dictionaries are designed to enable easy lookup of values give a
key. To get the 
```python
Flight
```
 associated with key
`'CSA-145'`{.python}, we can write simply:

```python
sched_dict['CSA-145']
```

To get the number of seats on flight `'CSA-145'`{.python}, we can simply
write:

```python
sched_dict['CSA-145'].seats
```

In other words, the dictionary data structure removes the need to
traverse a list to find the `Flight`{.python} with a specific key. The
dictionary lookup operation does that work for us. Actually,
dictionaries are even more nuanced: depending on how they are
designed, dictionaries can retrieve the value for a key without
traversing all the values (or even any other value). In general,
you can assume that dictionary-based lookup is significantly faster
than a list-based one. How this works is a more advanced topic; some
of this content is explained in [SECREF].

One limitation of dictionaries is that they allow only one value per
key. Let’s consider a different example, this time one that uses
rooms in a building as keys and occupants as values:

```python
office_dict = {410: 'Farhan',
               411: 'Pauline',
               412: 'Marisol',
               413: 'Saleh'}
```

What if someone new moves into office 412? In Python, we can the value
for that key as follows:

```python
office_dict[412] = 'Zeynep'
```

Now, any use of `office_dict[412]`{.python} will evaluate to
`'Zeynep'`{.python} instead of `'Marisol'`{.python}.

```{=html}
<a name="(part._Searching-Through-the-Values-in-a-Dictionary)"></a>
```

#### 9.2.2 Searching Through the Values in a Dictionary {#Searching-Through-the-Values-in-a-Dictionary}

What if we wanted to find all of the flights with more than 100 seats?
For this, we have to search through all of the key-value pairs and
check their balances. This again sounds like we need a for-loop. What
does that look like on a dictionary though?

Turns out, it looks much like writing a for loop on a list (at least
in Python). Here’s a program that creates a list of the flights with
more than 100 seats:

```python
above_100 = []

# the room variable takes on each key in the dictionary
for flight_code in sched_dict:
    if sched_dict[flight_code].seats > 100:
        above_100.append(sched_dict[flight_code])
```

Here, the for-loop iterates over the keys. Within the loop, we use
each key to retrieve its corresponding `Flight`{.python}, perform the
balance check on the `Flight`{.python}, then put the `Flight`{.python} in
our running list if it meets our criterion.

::: {.exercise}
Create a dictionary that maps names of classrooms or meeting rooms to
the numbers of seats that they have. Write expressions to:

1. Look up how many seats are in a specific room

2. Change the capacity of a specific room to have 10 more seats
  than it did initially

3. Find all rooms that can seat at least 50 students
:::

```{=html}
<a name="(part._Dictionaries-with-More-Complex-Values)"></a>
```

#### 9.2.3 Dictionaries with More Complex Values {#Dictionaries-with-More-Complex-Values}

::: {.do-now}
A track-and-field tournament needs to manage the names of the
players on the individual teams that will be competing. For
example, “Team Red” has “Shaoming” and “Lijin”, “Team
Green” contains “Obi” and ”Chinara”, and “Team Blue” has
“Mateo” and “Sophia”. Come up with a way to organize the data that
will allow the organizers to easily access the names of the players on
each team, keeping in mind that there could be many more teams than
just the three listed here.
:::

This feels like a dictionary situation, in that we have a meaningful
key (the team name) with which we want to access values (the names of
the players). However, we have already said that dictionaries allow
only one value per key. Consider the following code:

```python
players = {}
players["Team Red"] = "Shaoming"
players["Team Red"] = "Lijin"
```

::: {.do-now}
What would be in the dictionary after running this code? If you aren’t
sure, try it out!
:::

How do we store multiple player names under the same key? The insight
here is that the collection of players, not an individual player, is
what we want to associate with the team name. We should therefore
store a list of players under each key, as follows:

```python
players = {}
players["Team Red"] = ["Shaoming", "Lijin"]
players["Team Green"] = ["Obi", "Chinara"]
players["Team Blue"] = ["Mateo", "Sophia"]
```

The values in a dictionary aren’t limited to being basic values. They
can be arbitrarily complex, including lists, tables, or even other
dictionaries (and more!). There is still only one value
per key, which is the requirement of a dictionary.

```{=html}
<a name="(part._Dictionaries-versus-Dataclasses)"></a>
```

#### 9.2.4 Dictionaries versus Dataclasses {#Dictionaries-versus-Dataclasses}

Previously, we learned about dataclasses as a way to create compound
data in Python. Here again is the `ToDoItem`{.python} dataclass that we
introduced earlier, as well as an example datum for that class:

```python
class ToDoItem:
    descr: str
    due: date
    tags: list

milk = ToDoItem("buy milk", date(2020, 7, 27), ["shopping", "home"]
```

One could view the field names in the dataclass as akin to keys in a
dictionary. If we did so, we could also capture the `milk`{.python}
datum via a dictionary as follows:

```python
milk_dict = {"descr": "buy milk",
             "due": date(2020, 7, 27),
             "tags": ["shopping", "home"]
             }
```

::: {.do-now}
Create a dictionary to capture the compound datum

```python
ToDoItem("grade hwk", date(2020, 7, 27), ["teaching"])
```
:::

::: {.do-now}
Create a to-do list named `myTD_D`{.python} that contains a list of
dictionaries, rather than a list of dataclasses.
:::

Putting these two approaches side-by-side, here’s the contrast:

```python
myTD_L = [ToDoItem("buy milk", date(2020, 7, 27), ["shopping", "home"]),
          ToDoItem("grade hwk", date(2020, 7, 27), ["teaching"]),
          ToDoItem("meet students", date(2020, 7, 26), ["research"])
         ]

myTD_D = [milk_dict,
          {"descr": "grade hwk",
           "due": date(2020, 7, 27),
           "tags": ["teaching"]
          },
          {"descr": "meet students",
           "due": date(2020, 7, 26),
           "tags": ["research"]
          }
         ]
```

::: {.do-now}
What do you see as the benefits and drawbacks of each of dataclasses and
dictionaries to represent compound data?
:::

Dataclasses have a fixed number of fields, while directories allow
arbitrary numbers of keys. Dataclass fields can be annotated with
types (which most languages will check when you make new data);
dictionaries can use fixed types for each of keys and values, though
this gets restrictive when using dictionaries to capture dataclasses
with fields of different types. Dataclasses give you a function name
for creating new data, whereas with dictionaries you’d have to create
such a function on your own.

Overall, dataclasses come with more linguistic support for error
checking: you can’t supply data for the wrong number of fields or
field values of the wrong type. Dictionaries are more flexible: you
can support optional fields more easily, including adding new
fields/keys as a program runs. Each of these makes more sense in some
programming situations.

::: {.do-now}
Write a function `ToDoItem_D`{.python} that takes a description, due
date, and list of tags and returns a dictionary with keys for each
field of a to-do item.
:::

```{=html}
<a name="(part._Summary)"></a>
```

##### Summary {#Summary}

Python programmers tend to make substantial use of dictionaries. In
this chapter, we’ve seen dictionaries used in two different settings:

- one in which the keys uniquely identify different
  entities or individuals among a larger set; the values represent some
  consistent type of information about each individual. The dictionary
  overall captures information about a large population of individuals,
  each with their own key.

- one in which the keys name fields of compound data; the values
  associated with each field can have different types from the values
  for other fields. This setting corresponds to the use of dataclasses,
  in which a dictionary captures information about one individual; some
  other structure (such as a list or another dictionary) would be needed
  to hold the dictionaries for each individual.

As a general rule, it is better to use dataclasses for the second
setting when you have a fixed set of fields. The use of dictionaries
for dataclasses is somewhat associated with programming practices in
the Python community (less so in other languages). The first setting,
however, is a common use of dictionaries in nearly all languages,
especially since dictionaries are usually built to provide fast access
to the data associated with a specific key.
