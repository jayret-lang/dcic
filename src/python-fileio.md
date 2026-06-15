---
title: File Input and Output in Python
section_number: 11.1
source_file: python-fileio.html
prev: part_python-fileio.html
up: part_python-fileio.html
next: booklet_programming-with-state.html
---

### File Input and Output in Python {#python-fileio}

In [Introduction to Pandas](python-tables-Pandas.html), we loaded data from CSV (comma-separated value) files, but we let Pandas handle the low-level details: reading files and converting their contents into DataFrames.

In this chapter, we’ll learn to read and write files using Python’s basic file operations, using a simplified CSV processor as an example.

While Pandas can certainly do all that we will do in this chapter (and more!), understanding how file operations work helps you become a more complete programmer, and to one day perhaps either create or work on libraries like Pandas.

#### Basic File Operations {#Basic-File-Operations}

Python provides built-in functions for working with files. Before you can do anything else with a file, you must "open" it:

```python
file = open('data.csv', 'r')
```

This statement opens a file named `'data.csv'`{.python} in read mode (`'r'`{.python}).
The `open`{.python} function returns a file object that we can use to read from or (if it were opened in the appropriate mode) write to the file.

::: {.do-now}
What do you think would happen if you tried to open a file that doesn’t exist? Try it and see what error message you get.
:::

Once we have a file object, we can read its contents in one of several ways:

[Important: the file object remembers where in the file it is reading.
This is how calling `.readline()`{.python} twice doesn’t return the same line, it returns one line,
and then the next. But, this also means that if you ran either `.read()`{.python} or `.readlines()`{.python},
you would have read the entire file, which means the position of the file object is now at the end, which means
calling any of the other methods would return empty results – empty strings for `.read()`{.python} or `.readline()`{.python}, and an
empty list for `.readlines()`{.python}. You can move where the file object is pointing, with `.seek()`{.python}, but how that
works is beyond our scope!]{.margin-note}
```python
# Read the entire file as one string
content = file.read()

# Or, we can read one line at a time
line = file.readline()
another_line = file.readline()

# We can also read all remaining lines into a list of strings
all_lines = file.readlines()
```

When we’re done using a file, we should always close it:

```python
file.close()
```

::: {.do-now}
Why do you think it might be important to close files when you’re done with them?
:::

Closing files is important because it frees up system resources and ensures that,
if we were writing to the file (unlike in this example, where we are only reading)
all pending writes actually get saved! However, manually remembering to close files
can be error-prone. Python provides a more reliable way using the `with`{.python}
statement:

```python
with open('data.csv', 'r') as file:
    content = file.read()
    # file is automatically closed when this block ends
```

In addition to not making us remember to close the files, it this approach also guarantees
that the file will be closed even if an error occurs while processing it.

#### Reading CSV Files Step by Step {#Reading-C-S-V-Files-Step-by-Step}

Let’s work through reading a CSV file manually, as a way to practice using files for a practical (if small) example.

Suppose we have a file called `orders.csv`{.python} with the following contents:
(You can create this file with your editor of choice – e.g., VSCode).

```{=html}
<table cellpadding="0" cellspacing="0" class="SVerbatim"><tr><td><p><span class="stt">dish,quantity,price,order_type</span></p></td></tr><tr><td><p><span class="stt">Pizza,2,25.0,dine-in</span></p></td></tr><tr><td><p><span class="stt">Salad,1,8.75,takeout</span></p></td></tr><tr><td><p><span class="stt">Burger,3,30.0,dine-in</span></p></td></tr><tr><td><p><span class="stt">Pizza,1,12.50,takeout</span></p></td></tr></table>
```

Here’s how we can read and parse this file step by step:

```python
# Step 1: Open and read the file into variable `lines`
with open('orders.csv', 'r') as file:
    lines = file.readlines()

# Step 2: Clean data: remove newline characters and split by commas
data = []
for line in lines:
    cells = line.strip().split(',')
    data.append(cells)

# Step 3: Separate header (first row) from data rows (rest of file)
header = data[0]
rows = data[1:]

print("Header:", header)
print("First row:", rows[0])
```

Let’s break down what each step does:

1. `file.readlines()`{.python} reads all lines from the file into a list of strings
2. We use a for loop to go through each line, using `line.strip()`{.python} to remove the newline character (`'\n'`{.python})
  from the end of each line and then turning the line into a list of strings by `.split(',')`{.python},
  which divides the string by the given string (which is not included).
3. We separate the first row (header) from the data rows for easier processing –
  the notation `data[1:]`{.python} is a special way of indicating we want "from index 1 until as far as the
  list goes – i.e., the end of the list.

::: {.do-now}
What would our code do if one of the cells in your CSV contained a comma?
For example, what if a dish name was "Mac and cheese, deluxe"? How could you handle this?
:::

#### Processing and Filtering Data {#Processing-and-Filtering-Data}

Once we have our data as a list of lists, we can process it using the same programming
techniques we’ve learned, by using the `.index()`{.python} method to return the numeric
offset of the given string in a list of strings – this is how we will find the columns
we are interested in, and then use that to index into the row.

For example, let’s filter for only takeout orders:

```python
# Returns the index (i.e., offset, base 0) where 'order_type' exists in the header list.
order_type_index = header.index('order_type')

# Filter for takeout orders
takeout_orders = []
for row in rows:
    if row[order_type_index] == 'takeout':
        takeout_orders.append(row)

print("Found " + str(len(takeout_orders)) + " takeout orders")
```

We can also convert data types as needed. For instance, if we want to calculate total revenue,
we need to not only find the quantity and price for each row, but convert the strings that are in
the row (since the file was all strings!) to numbers before multiplying:

```python
quantity_index = header.index('quantity')
price_index = header.index('price')

total_revenue = 0
for row in rows:
    quantity = int(row[quantity_index])
    price = float(row[price_index])
    total_revenue += quantity * price

print("Total revenue: $" + str(total_revenue))
```

::: {.do-now}
What would happen if one of the quantity cells contained invalid data, like the string "three" instead of the number 3? How could you make your code more robust to handle such errors?
:::

#### Writing CSV Files {#Writing-C-S-V-Files}

Writing CSV files follows a similar pattern. We need to:

1. Open a file in write mode
2. Convert our data to the proper string format
3. Write the strings to the file

Here’s how to write our filtered takeout orders to a new file:

```python
# Prepare data to write (header + filtered rows)
output_data = [header] + takeout_orders

# Write to file
with open('takeout_orders.csv', 'w') as file:
    for row in output_data:
        # Join the row elements with commas and add a newline
        line = ','.join(row) + '\n'
        file.write(line)
```

The key steps here are:

- `','.join(row)`{.python} combines the list elements into a single string with commas between them
- We add `'\n'`{.python} to create a new line after each row
- `file.write()`{.python} writes the string to the file

Note that we call `.write()`{.python} once for each line – we could have combined all the lines into a single
string, and only called `.write()`{.python} once, but there is no need to – just like how file objects remember
where we are reading from them, they remember where we were writing, so the next call to `.write()`{.python} will
add the next string after the previous one.

::: {.do-now}
Try writing a program that reads a CSV file, adds a new column with calculated values (like total price = quantity × price), and writes the result to a new file.
:::
