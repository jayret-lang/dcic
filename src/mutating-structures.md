---
title: Mutating Structures
section_number: 12.1
source_file: mutating-structures.html
prev: part_state.html
up: part_state.html
next: unified-equality.html
---

```{=html}
<a name="(part._mutating-structures)"></a>
```

### 12.1 Mutating Structures {#mutating-structures}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-structures.html#%28part._eg-bank-acc%29">12.1.1<span class="hspace"> </span>Example: Bank Accounts</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-structures.html#%28part._Testing-Functions-that-Mutate-Structures%29">12.1.2<span class="hspace"> </span>Testing Functions that Mutate Structures</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-structures.html#%28part._mult-bank-acct%29">12.1.3<span class="hspace"> </span>Aliasing</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="mutating-structures.html#%28part._structure-mut-dir%29">12.1.4<span class="hspace"> </span>Structure Mutation and the Directory</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="mutating-structures.html#%28part._heap-intro%29">12.1.4.1<span class="hspace"> </span>Introducing the Heap</a></p></td></tr><tr><td><p><span class="hspace">      </span><a class="toclink" data-pltdoc="x" href="mutating-structures.html#%28part._basic-data-heap%29">12.1.4.2<span class="hspace"> </span>Basic Data and the Heap</a></p></td></tr></table>
```

We will now study a new kind of data and the programming style that
accompanies it. This will give us both great power and great
responsibility. We will develop this idea in both Jayret and Python,
both because the core concept arises in both (indeed in nearly all)
languages and
because their contrast is instructive.

```{=html}
<a name="(part._eg-bank-acc)"></a>
```

#### 12.1.1 Example: Bank Accounts {#eg-bank-acc}

Imagine that we want to represent bank accounts, where each account
has a (unique) id number and a balance:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">@dataclass
class Account:
    id: int
    balance: float</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">data Account:
    account(id :: Number,
    balance :: Number)
end</code></pre></div></div></p></td></tr></table>
```

Let’s now make an account:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1 = Account(8404, 500)</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1 = account(8404, 500)</code></pre></div></div></p></td></tr></table>
```

Now let’s say we learn that the account has just
earned another 200. We could always reflect the resulting account as follows:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">Account(acct1.id, acct1.balance + 200)</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">account(acct1.id, acct1.balance + 200)</code></pre></div></div></p></td></tr></table>
```
However, this creates a new account; if we look at the current
`balance`{.jayret} of `acct1`{.jayret}, by writing `acct1.balance`{.jayret}, it is
still `500`{.jayret}. If this were our account, we would be quite sad!

Rather, we want to change the balance in the existing
account. This requires a programming feature that we have not
encountered until now: data that can be changed. Such data are called
mutable, and we explore them below. In contrast, until now we
have worked with immutable data: data that cannot be altered.

First, we have to declare that the data can be changed. In
Python, this is automatically true, always, so nothing changes. In
Jayret, however, fields cannot be changed—they are
immutable—by default. We have to explicitly say they can be
changed:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">@dataclass
class Account:
    id: int
    balance: float</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">data Account:
    account(id :: Number,
      ref balance :: Number)
end</code></pre></div></div></p></td></tr></table>
```
This Jayret definition says that `id`{.jayret} cannot be changed,
while `balance`{.jayret} can. This ensures that no programmer can
accidentally change the bank account number. In Python, every
programmer has to make sure they don’t accidentally change it.
(If we did want `id`{.jayret} to be mutable in Jayret, we would add a
`ref`{.jayret} in front of it, too.)

With this definition, making accounts looks the same (unsurprisingly
in Python, since nothing has changed):

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1 = Account(8404, 500)</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1 = account(8404, 500)</code></pre></div></div></p></td></tr></table>
```
When we view the account in Jayret, we see something
special:


![](pyret-output-caution.png){width="193" height="84"}

The yellow-and-black “caution tape” indicator is a reminder that the
value can change, so what is shown on screen may not be the current
value.

Accessing an immutable field in Jayret remains the same:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1.id</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1.id</code></pre></div></div></p></td></tr></table>
```
However, accessing a mutable field looks different in Jayret:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1.balance</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1!balance</code></pre></div></div></p></td></tr></table>
```
The `!`{.jayret} is there to remind that what you are getting is the
current value of `balance`{.jayret}, and it may be different later.
Python does not offer a similar syntactic warning, but then again,
recall that every field is always mutable.

So now let’s see how to change that account balance. For simplicity,
let’s first see how to set the account balance to zero. We use slightly
different syntaxes for it in the two languages:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">acct1.balance = 0</code></span></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">acct1!{balance: 0}</code></span></p></td></tr></table>
```
In Jayret, again, we use `!`{.jayret} in the syntax for
changing the field: read it as “change the value
now!”

::: {.do-now}
You now know all the parts you need to figure out how to set
`balance`{.jayret} to be `200`{.jayret} more than its previous value.
Can you figure out how to write that?
:::

Here’s how we combine the pieces—accessing the value and then setting it:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">acct1.balance = acct1.balance + 200</code></span></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">acct1!{balance: acct1!balance + 200}</code></span></p></td></tr></table>
```
While Jayret’s syntax is a little more onerous for changing the value
of one field, it proves to be ligher-weight if we want to change
multiple fields. In Python we’d have to write `acct1.`{.jayret} for
each of them, whereas in Jayret we need only the one `acct1!`{.jayret}. So
there is a trade-off between the two syntaxes.

We hadn’t written any tests above. Suppose we had: already we might
notice something a bit odd. Say we had written

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">def test_balance():
    assert acct1.balance == 500</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">check:
  acct1!balance is 500
end</code></pre></div></div></p></td></tr></table>
```

This would pass before we performed the update, but fails after the
update is performed. In Python, tests are run when we call the testing
functions, which we typically do after loading the full file (either
by running them at the prompt or by putting our tests in a separate file).

In Jayret, tests are run as if they were written at the very bottom of
definitions. Therefore, even if the program looked like this in Jayret:

```jayret
acct1 = account(8404, 500);
@Check void test() {
    assertEquals(acct1 ! balance, 500);
}
acct1 ! {balance acct1 ! balance + 200 }
```
the test fails. Alternatively, we can write

```jayret
acct1 = account(8404, 500);
@Check void test() {
    assertEquals(acct1 ! balance, 700);
}
acct1 ! {balance acct1 ! balance + 200 }
```
and it passes, but not if we comment out the update.

In both languages, then, we see a new phenomenon: tests that are only
sometimes true. This phenomenon is called state. There is
a “state” (a collection of values for the defined names) in which
the balance is `500`{.jayret}, and another where it is `700`{.jayret}. This is
not merely limited to testing! Testing is just a reflection of what is
going on in the program as it runs. From now on, every programming
instruction will run in some state, and its actions will depend on the
other values in that state. If those values change, the same
instruction—i.e., the same piece of program text—may produce
different answers. This makes programming much harder, and we will
have to get used to the subtleties that come along with it.

```{=html}
<a name="(part._Testing-Functions-that-Mutate-Structures)"></a>
```

#### 12.1.2 Testing Functions that Mutate Structures {#Testing-Functions-that-Mutate-Structures}

Our example of adding funds to an account corresponds to making a
deposit into a bank account. Let’s turn our balance-updating
expression into a function (named `deposit`{.jayret}) that takes the
deposit amount as input. Then, we’ll look at how to write tests for
that function. First, the function definition:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">def deposit(ac: Account, amt: float):
    '''add amt to the account's balance'''
    ac.balance = ac.balance + amt</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">fun deposit(ac :: Account, amt :: Number):
  doc: "add amt to the account's balance"
  ac!{balance: ac!balance + amt}
end</code></pre></div></div></p></td></tr></table>
```
How do we test this?

In Python, this function does not return anything. In Jayret, the
update operation does return the value being updated, but in a larger
function we can’t always assume that it will be the value
returned. Therefore, we have to set up our test to assume otherwise.

In general, tests for functions that contain mutation need to have
three to four parts:


1. Setup: set up the necessary values to provide the function.

2. Call: call the function.

3. Check: check that the function had the desired behavior.

4. Teardown: restore data to their expected state.

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">def test_deposit():
    # Setup
    a1 = Account(8200, 150)

    # Call
    deposit(a1, 100)

    # Check
    assert a1.balance == 250</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">check:
  # Setup
  a1 = account(8200, 150)

  # Call
  deposit(a1, 100)

  # Check
  a1!balance is 250
end</code></pre></div></div></p></td></tr></table>
```

In this case we don’t need to perform a Teardown step because we
created data purely for testing the function. But if, for instance, we
had run the test over a dataset whose values matter, we would need to
restore the changes.

Similarly, the Setup phase needs to make sure that all data have the
right values. Until now, once created, data did not change. But now,
data may have been changed by some other mutations, and this may cause
tests to fail. Therefore, the Setup phase requires not only creating
necessary data but also setting the values of previously-created data
to be what the test expects. (Again, note that in Python it is
difficult to know which fields might have been changed, whereas in
Jayret, we only have to reset the value of mutable fields.)

::: {.exercise}
Write tests for the following function that adds interest to an account balance:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">def add_interest(ac: Account):
    '''increases the account value by 2 percent'''
    ac.balance = ac.balance * 1.02</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">fun add-interest(ac :: Account):
  doc: "increases the account value by 2 percent"
  ac!{balance: ac!balance * 1.02}
end</code></pre></div></div></p></td></tr></table>
```
:::

```{=html}
<a name="(part._mult-bank-acct)"></a>
```

#### 12.1.3 Aliasing {#mult-bank-acct}

Now let’s
suppose our bank allows accounts to be shared by multiple customers.
We should thus separate information about customers from that of
the account:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">@dataclass
class Customer:
    name: str
    acct: Account</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">data Customer:
    cust(name :: String,
      acct :: Account)
end</code></pre></div></div></p></td></tr></table>
```
Specifically, suppose we have two accounts (`acct1`{.jayret} and
`acct2`{.jayret}), where `acct1`{.jayret} is owned jointly by Elena and Jorge:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1 = Account(8404, 500)
acct2 = Account(8405, 350)
elena = Customer("Elena", acct1)
jorge = Customer("Jorge", acct1)</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1 = account(8404, 500)
acct2 = account(8405, 350)
elena = cust("Elena", acct1)
jorge = cust("Jorge", acct1)</code></pre></div></div></p></td></tr></table>
```

Now let’s say Elena earns an additional `150`{.jayret}. We want to update
the account to reflect this. How might we do it? First we have to
access the account itself: `elena.acct`{.jayret} (in both languages). Then
we would update it using the syntax above:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">a = elena.acct
a.balance = a.balance + 150</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">a = elena.acct
a!{balance: a!balance + 150}</code></pre></div></div></p></td></tr></table>
```
Sure enough, Elena’s account will now have the value of `850`{.jayret}
(the original `500`{.jayret}, the bonus of `200`{.jayret}, and now the extra
`150`{.jayret}):

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">assert elena.acct.balance == 850</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">check:
  elena.acct!balance is 850
end</code></pre></div></div></p></td></tr></table>
```
Observe that in Jayret we use `.`{.jayret} to get the account but `!`{.jayret}
to get the balance: a reminder that Elena’s account will never change
(the way we have defined the data structure), but that account’s
balance may and, indeed, does. Between the designs of Python and
Jayret, there’s a trade-off between convenience and precision.

The key question now is: what is Jorge’s balance? Put
differently, will this test pass or fail?

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">assert jorge.acct.balance == 850</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">check:
  jorge.acct!balance is 850
end</code></pre></div></div></p></td></tr></table>
```

Or even more simply: what
is the value of this program?

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jorge.acct.balance</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jorge.acct!balance</code></pre></div></div></p></td></tr></table>
```

There are two very reasonable answers here:


1. Going by our prose, Jorge’s account should also have `850`{.jayret},
  because that’s what it means to “share” an account.

2. Going by the visible code, Jorge’s account should still have
  `700`{.jayret}, because the update was made through `elena.acct`{.jayret},
  not `jorge.acct`{.jayret}.

::: {.do-now}
Run the above code and see what you get.
:::

What you find is that the above test passes: Jorge’s account also has
`850`{.jayret}. We say that `elena.acct`{.jayret} and `jorge.acct`{.jayret} are
aliases: they are two different “names” for the exact same
datum.

This is not the first time we have had shared data. However, until
now, it hasn’t mattered that the data were aliased. But now
that we have mutation, aliases matter: the balance in
`jorge.acct`{.jayret} has changed even though we never made an explicit
change using that name. It is as if `elena.acct`{.jayret} exhibited
spooky action at a distance.

Again, there is a linguistic difference here. Because all fields are
mutable in Python, you have to always be on the alert for
this. Because only `ref`{.jayret} fields are mutable in Jayret, you can be
sure that fields accessed through `.`{.jayret} will never change in value
over time or even if there are aliases, but those accessed through
`!`{.jayret} might change over time (and via aliases).

```{=html}
<a name="(part._structure-mut-dir)"></a>
```

#### 12.1.4 Structure Mutation and the Directory {#structure-mut-dir}

Now that we have the ability to mutate the contents of data, we will need to show and then revise our
notion of directories. The directories are essentially the same
between Jayret and Python, with one exception: we have different naming
conventions in the two languages. For instance, we write
`Account(8404, 500)`{.python} in Python versus `account(8404, 500)`{.jayret}
in Jayret. It would be annoying to write every one of these twice, with
the only difference being the capitalization. Therefore, where the
only difference is the naming, we will ignore this difference
and show only one version (in this case, the Python version); you
should assume that the exact same thing is true for Jayret, other than
the capitalization.

As a reminder, here are our initial definitions once again:

```python
acct1 = Account(8404, 500)
acct2 = Account(8405, 325)
elena = Customer("Elena", acct1)
jorge = Customer("Jorge", acct1)
```

::: {.do-now}
Review the following proposal for the directory contents after running
the initial definitions. Is this what you expect to see?

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", acct1)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jorge</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Jorge", acct1)</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```
:::

There’s a problem with this version, namely the use of `acct1`{.jayret} in
the values associated with `elena`{.jayret} and `jorge`{.jayret}. Remember,
the values in the directory can’t refer to names in the directory:
both Jayret and Python replace names with their values when evaluating
expressions. Here is the corresponding version of the directory that
uses the value of `acct1`{.python}:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8405, 325)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", Account(8404, 500))</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jorge</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Jorge", Account(8404, 500))</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```
Observe that this is also what you would see if you were to evaluate
the corresponding variable names.

Now, let’s add funds to Elena’s account:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena.acct.balance = elena.acct.balance + 150</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena.acct!{balance: elena.acct!balance + 150}</code></pre></div></div></p></td></tr></table>
```

::: {.do-now}
Show how the directory changes if you run the above code.
:::

If we follow the code precisely, we might expect the following
directory, in which only the balance in Elena’s version of the account
changes.

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8405, 325)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", Account(8404, 650))</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jorge</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Jorge", Account(8404, 500))</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

We know from running the code, however, that the account is aliased,
so that the balances accessible from each of `acct`{.jayret},
`elena.acct`{.jayret}, and `jorge.acct`{.jayret} all reflect the update. This
suggests that the actual directory should look something like

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 650)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Account(8405, 325)</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", Account(8404, 650))</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jorge</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">Customer("Jorge", Account(8404, 650))</code></pre></div></div></p></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

But this is also weird. The directory represents the information that
Jayret or Python maintain about your defined names and their
values. What in the directory indicates that those three balances should
change, but not the balance of `acct2`{.jayret})? Put differently, what reflects the aliasing? Nothing!

The directory as we have used it up until now works fine for programs
without mutation. But once we have both mutation and aliasing, this
simple idea of mapping names to values breaks down because it
doesn’t capture the aliases. We need a refined representation of the
connections between names and values that does capture aliasing.

```{=html}
<a name="(part._heap-intro)"></a>
```

##### 12.1.4.1 Introducing the Heap {#heap-intro}

Our original presentation of the directory reflected the aliases that referred to a single
`Account`{.jayret} through repeated use of the name `acct1`{.jayret}. We only
lost that sharing when we replaced `acct1`{.jayret} with it’s value while
setting up the data for Elena and Jorge. The rule that names can’t
appear in the values is still important, especially in the presence of
mutation (we’ll return to this later in [Mutating Variables in Memory](mutating-variables.html##mutating-vars-memory)). But the idea
of having a single term that can be reused to reflect sharing is a
good one. Indeed, it reflects what happens inside your computer.

Every time you use a constructor to create data, your programming
environment stores it in the memory of your computer. Memory
consists of a (large) number of slots. Your newly-created datum goes
into one of these slots. Each slot is labeled with an
address. Just as a street address refers to a specific building,
a memory address refers to a specific slot where a datum is
stored. Memory slots are physical entities, not conceptual ones. A
computer with a 500GB hard drive has about 500 billion slots in which it can
store data. Not all of that memory is available to your programming
environment: your Web browser, applications, operating system, and so on all
get stored in the memory. Your programming environment does get a
portion of memory to use for storing its data. That portion is called
the heap.

When you write a statement like

```python
acct1 = Account(8404, 500)
```
your programming environment puts the new `Account`{.python} into a
physical slot in the heap, then associates the address of that
slot with the variable name in the directory. The name in the
directory doesn’t map to the value itself, but rather to the
address that holds the value. The address bridges
between the physical storage location and the conceptual name you want
to associate with the new datum. In other words, our directory really
looks like:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
Our revised version has two separate areas: the directory (mapping
names to addresses) and the heap (showing the values stored
at the
addresses). We will use four-digit numbers for addresses, prefixed
with an @ symbol (reserving numbers with fewer digits for data
values). The specific number for the initial address (here 1001) is
arbitrary. Subsequent storage of structured data values will use the
addresses in order. Let’s write out the directory and heap
contents for our initial definitions of accounts in this new format,
and see how it supports the aliasing that we intended.

First, we create both `acct1`{.jayret} and `acct2`{.jayret} in order as
follows. Note that the `Account`{.jayret} associated with name
`acct2`{.jayret} goes in address 1002.

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1002</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```

When we run

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena = Customer("Elena", acct1)</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena = customer("Elena", acct1)</code></pre></div></div></p></td></tr></table>
```
what happens? As before, we look up what the name `acct1`{.jayret} refers
to in the directory and substitute the result for the name in the
`Customer`{.jayret} data. Now,
`acct1`{.jayret} evaluates to an address, 1001. Therefore,
the `Customer`{.jayret} value in the heap contains an address:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1002</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", <span class="heapref sink">1001</span>)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
Similarly, when we run

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jorge = Customer("Jorge", acct1)</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jorge = customer("Jorge", acct1)</code></pre></div></div></p></td></tr></table>
```
the directory and heap look like this:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1002</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1003</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jorge</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1004</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">Account(8404, 500)</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">Account(8405, 3250)</code></span></p></li><li><p><span class="heapref source">1003</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">Customer("Elena", <span class="heapref sink">1001</span>)</code></span></p></li><li><p><span class="heapref source">1004</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">Customer("Jorge", <span class="heapref sink">1001</span>)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```

::: {.do-now}
Fun fact in the Web version of the book: Did you try hovering over the addresses? Try it now!
:::

With the heap articulated separately from the directory, we now see
the relationship between the `acct`{.python} fields
for the two customers and the name `acct1`{.jayret}: they refer to the same address, which in
turn means they refer to the same value. In contrast, the name
`acct2`{.jayret}, which was not aliased in the original code, refers to an
address that is not referenced anywhere else. This is the heart of
aliasing: that’s why changes made through one name also affect values
viewed through another.

::: {.do-now}
Write three distinct expressions each of which uses a different name in the
directory to return the balance in account `acct1`{.jayret}.
:::

::: {.do-now}
Would the following statement work to update the balance in Elena and
Jorge’s shared account?

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena.acct.balance = jorge.acct.balance - 50</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena.acct!{balance: jorge.acct!balance - 50}</code></pre></div></div></p></td></tr></table>
```
Does this seem like a good or bad way to do this computation? Why?
:::

::: {.do-now}
Extend the most recent directory and heap contents to reflect running
the following statement:

```python
acct3 = acct1
```
Did you change the heap in the previous exercise? Should you have?
:::

Three rules guide how the directory and heap are affected by running
programs:

1. If the code construct a new piece of structured data, put the
  new piece of structured data at the next address in the heap.

2. If the code associates a name with a piece of structured data,
  the directory should map the name to the address of the datum in the
  heap.

3. If the code modifies a field within structured data, modify the
  data in the heap.

In the example above, we did not alter the heap in any way; only the
directory should be modified to reflect that `acct3`{.python} and
`acct1`{.python} are now aliases.

```{=html}
<a name="(part._basic-data-heap)"></a>
```

##### 12.1.4.2 Basic Data and the Heap {#basic-data-heap}

The above rules don’t indicate what happens when we have basic data,
such as numbers or strings, associated with names in the directory. Do
those values also get addresses in the heap?

They do not. As our example with shared accounts illustrated, we need
the heap so that updates to fields of shared data affect all aliases
(names that refer to) those data. Basic data don’t have fields, so
there is no need to put them in the heap. Here’s a concrete example:

```python
x = 4
prof = "Dr. Kumar"
```

The corresponding directory and heap contents would be as follows:

```{=html}
<div class="HeapExpr EmptyHeap"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">x</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">4</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">prof</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"Dr. Kumar"</code></span></div></p></li></ul></div><p></p><div class="clear"></div></div>
```

Notice that this particular program puts nothing in the heap:
according to our rules above, only structured data only go into the
heap. Now assume our program also had a dataclass (Python) or datatype (Jayret)
for `Office`{.python}s, with a professor’s name and room number. Here’s
another example showing a combination of basic and structured data:

```python
x = 4
prof = "Dr. Kumar"
office1 = Office("Dr. Lakshmi", 311)
office2 = Office(prof, 310 + x)
```

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">x</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span></div><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">4</code></pre></div></div></p></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">prof</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">"Dr. Kumar"</code></span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">office1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1005</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">office2</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1006</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1005</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">Office("Dr. Lakshmi", 311)</code></span></p></li><li><p><span class="heapref source">1006</span>:<span class="hspace"> </span><span class="sourceCode" title="Python"><code class="sourceCode" data-lang="text/x-python">Office("Dr. Kumar", 314)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```

Though specific language implementations can vary, this shows that
it is sufficient to think of basic data as residing
in the directory, not the heap. The
whole point of structured data is that they have both their own
identity and multiple components. The heap gives access to both
concepts. Basic data can’t be broken down (by definition). As such,
there is nothing lost by putting them only in the directory.

But what about strings? We’ve referred to them as basic data
until now, but don’t they have “components”, namely the
characters that make up the string? Yes, that is technically
accurate. However, we are treating strings as basic data because we
aren’t using operations that modify that sequence of characters. This is
a subtle point, one that usually comes up later in computer science.
This book
will leave strings in the directory, but if you are writing programs
that modify the internal characters, put them in the heap instead.
