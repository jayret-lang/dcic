---
title: Cyclic Data
section_number: 12.4
source_file: unified-cyclic-data.html
prev: unified-lists-memory.html
up: part_state.html
next: part_python-state.html
---

```{=html}
<a name="(part._unified-cyclic-data)"></a>
```

### 12.4 Cyclic Data {#unified-cyclic-data}

```{=html}
<table cellpadding="0" cellspacing="0"><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="unified-cyclic-data.html#%28part._Creating-Cyclic-Data%29">12.4.1<span class="hspace"> </span>Creating Cyclic Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="unified-cyclic-data.html#%28part._Testing-Cyclic-Data%29">12.4.2<span class="hspace"> </span>Testing Cyclic Data</a></p></td></tr><tr><td><p><span class="hspace">    </span><a class="toclink" data-pltdoc="x" href="unified-cyclic-data.html#%28part._Cycles-in-Practice%29">12.4.3<span class="hspace"> </span>Cycles in Practice</a></p></td></tr></table>
```

```{=html}
<a name="(part._Creating-Cyclic-Data)"></a>
```

#### 12.4.1 Creating Cyclic Data {#Creating-Cyclic-Data}

Earlier [[Aliasing](mutating-structures.html#mult-bank-acct)], we introduced the idea of aliased
bank accounts, where multiple customers can operate the same
account. Sometimes, a bank wants to keep track of all the customers
who have access to a given account. For instance, when the account
balance runs low, it would want to notify all the customers who have
access to it.

Therefore, each account needs to maintain a list of its
customers. Because the set of owners can change over time, we make
that field mutable in Jayret:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">@dataclass
class Account:
    id: int
    balance: int
    owners: list # of Customer

@dataclass
class Customer:
    name: str
    acct: Account
</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">data Account:
    account(id :: Number,
      ref balance :: Number,
      ref owners :: List&lt;Customer&gt;)
end

data Customer:
    cust(name :: String,
      acct :: Account)
end</code></pre></div></div></p></td></tr></table>
```
If you look closely, you’ll see that `Account`{.jayret} refers to
`Customer`{.jayret} (specifically, a list of them) and in turn
`Customer`{.jayret} refers to `Account`{.jayret}. This could get interesting.

Previously, we could create an account with one customer as follows:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena = Customer("Elena", Account(8404, 500))</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena = cust("Elena", account(8404, 500))</code></pre></div></div></p></td></tr></table>
```
How do we do that now? Every `Account`{.jayret} requires a list of its
`Customer`{.jayret}s. We need to write

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena = Customer("Elena", Account(8404, 500, [_____]))</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena = cust("Elena", account(8404, 500, [list: _____]))</code></pre></div></div></p></td></tr></table>
```
But what goes in `_____`{.jayret}? It needs to refer to the very customer
account that we are presently creating.

Another way to think about writing this is:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1 = Account(8404, 500, [_____])
elena = Customer("Elena", acct1)</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1 = account(8404, 500, [list: _____])
elena = cust("Elena", acct1)</code></pre></div></div></p></td></tr></table>
```
This hasn’t solved our fundamental problem—we still need to fill in
`_____`{.jayret}—but at least we now have names to refer to entities. We
would like to be able to write

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1 = Account(8404, 500, [elena])
elena = Customer("Elena", acct1)</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1 = account(8404, 500, [list: elena])
elena = cust("Elena", acct1)</code></pre></div></div></p></td></tr></table>
```
But when we try to run this, both Python and Jayret will give us an
error. That is because they try to evaluate the right-hand-side of the
first line to create an account, whose heap address will be bound in
the directory to `acct1`{.jayret}. To do so, they must evaluate that
account-creation expression. In doing so, they look up the name
`elena`{.jayret}. However, `elena`{.jayret} has not yet been bound in the
directory. Therefore, they produce an error.

Observe that we can’t just reverse the order of these two bindings. If
we try that, we end up with the same problem: we try to create a
customer that refers to `acct1`{.jayret}. But we haven’t yet defined
`acct1`{.jayret}, producing the same error.

The problem is we are trying to create cyclic data. The two data
refer to one another. We could already sense that this might happen
from the data definitions, and now we must confront it. The problem is
that we have to create some value first, and we can’t produce
either one correctly since each one depends on the other.

As you might guess, we have to compromise. We have to construct one of
the data first, and when we do so, it might not be entirely
accurate. Then we create the other, and then modify the first
one to have the correct contents.

In our case, the Jayret version makes clear what order to use in
creating the data. Nothing in a `Customer`{.jayret} is mutable (nor needs
to be), whereas the list of account owners is (and should be, because
the set of customers can grow). Therefore, we can write:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1 = Account(8404, 500, [])</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1 = account(8404, 500, empty)</code></pre></div></div></p></td></tr></table>
```
Note that at this point, this is actually accurate! There are no
owners of this account.

Now we create Elena’s account:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena = Customer("Elena", acct1)</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">elena = cust("Elena", acct1)</code></pre></div></div></p></td></tr></table>
```
At this point, our memory looks like this:[For simplicity,
we will show the list of owners inside the account instead of
putting it in its own memory location(s).]{.margin-note}

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1002</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500, [])</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", <span class="heapref sink">1001</span>)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```

Now things are slightly inaccurate: the account at 1001
does have an owner, which is not yet reflected. So we
have to update it to reflect that:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumn"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p><span style="font-weight: bold">Jayret</span></p></td></tr><tr><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1.owners = [elena]</code></pre></div></div></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1!{owners: [list: elena]}</code></pre></div></div></p></td></tr></table>
```
We can legitimately do this now because `elena`{.jayret} is bound in the
dictionary. Furthermore, it is bound to something useful: Elena’s
customer information. So now the values are properly set up: Elena’s
customer information refers to the account, and the account refers to
Elena’s customer information:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1002</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500, [<span class="heapref sink">1002</span>])</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", <span class="heapref sink">1001</span>)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```
This is the cycle in “cyclic”: 1001 depends on 1002
and 1002 depends on 1001.

Observe that if we introduce another customer, Jorge, who shares the same
account, we can update the account to reflect that also:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jorge = Customer("Jorge", acct1)</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">jorge = cust("Jorge", acct1)</code></pre></div></div></p></td></tr></table>
```
Again, the information in `acct1`{.jayret} is inaccurate because it does
not reflect the new owner. We can modify it in a similar way:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1.owners = acct1.owners + [jorge]</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">acct1!{owners: acct1!owners + [list: jorge]}</code></pre></div></div></p></td></tr></table>
```
So now our memory would look like this:

```{=html}
<div class="HeapExpr"><div class="EnvPart"><p>Directory</p><ul><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">acct1</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1001</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">elena</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1002</span></div></p></li><li><p><div class="SIntrapara"><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">jorge</code></pre></div></div></p></div><div class="SIntrapara"><span class="hspace"> </span>→<span class="hspace"> </span><span class="heapref sink">1003</span></div></p></li></ul></div><div class="HeapPart"><p>Heap</p><ul><li><p><span class="heapref source">1001</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Account(8404, 500, [<span class="heapref sink">1002</span>, <span class="heapref sink">1003</span>])</code></span></p></li><li><p><span class="heapref source">1002</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Customer("Elena", <span class="heapref sink">1001</span>)</code></span></p></li><li><p><span class="heapref source">1003</span>:<span class="hspace"> </span><span class="sourceCode" title="Jayret"><code class="sourceCode" data-lang="jayret">Customer("Jorge", <span class="heapref sink">1001</span>)</code></span></p></li></ul></div><p></p><div class="clear"></div></div>
```

::: {.do-now}
We wrote slightly different code when adding Jorge’s account than when
adding Elena’s account. Is one better than the other?
:::

The code for Elena’s addition ignored whatever owners there previously
were. That is, it would only work correctly in a setting where there
were no other owners. The code for Jorge’s addition takes into account
all the previous owners. Therefore, Elena’s code was perfectly fine
for illustrating the simple first case, but Jorge’s code is more
general in that it will work in all settings (including when the prior
list of owners is empty).

::: {.exercise}
Write a function that takes care of adding a customer to an account.
:::

```{=html}
<a name="(part._Testing-Cyclic-Data)"></a>
```

#### 12.4.2 Testing Cyclic Data {#Testing-Cyclic-Data}

When you want to write a test involving circular data, you can’t write
out the circular data manually. For example, imagine that we wanted
to write out `acct1`{.jayret} from earlier:

```{=html}
<table cellpadding="0" cellspacing="0" class="TwoColumnAsRows"><tr><td><p><span style="font-weight: bold">Python</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Python"></span><div class="sourceCode"><pre class="sourceCode" data-lang="text/x-python"><code class="sourceCode" data-lang="text/x-python">assert(acct1 = Account(8404, 500, [Customer("Elena", Account(8404, 500, …)]))</code></pre></div></div></p></td></tr><tr><td><p><span style="font-weight: bold">Jayret</span></p></td><td><p></p></td></tr><tr><td><p></p></td><td><p><div class="sourceCodeWrapper"><span class="sourceLangLabel" data-label="Jayret"></span><div class="sourceCode"><pre class="sourceCode" data-lang="jayret"><code class="sourceCode" data-lang="jayret">check:
  acct1 is
    account(8404, 500, [list: cust("Elena", account(8404, 500, …))])
end</code></pre></div></div></p></td></tr></table>
```
However, because of the circularity, we can’t finish writing down the
data. We can’t just leave part of it unspecified with `…`{.jayret}.

This leaves us with two choices:

You have two options: write tests in terms of the names of data,
or write tests on the components of the data.

Here’s an example that illustrates both. After setting up the account,
we might want to check that the owner of the new account is the new
customer:

```python
assert(new_acct.owner is new_cust)
```

Here, rather than write out the `Customer`{.python} explicitly, we use the name
of the existing item in the directory. This doesn’t require you to write
ellipses. We also focused on just the `owner`{.python} component, as a part of
the `Account`{.python} value that we expected to change.

```{=html}
<a name="(part._Cycles-in-Practice)"></a>
```

#### 12.4.3 Cycles in Practice {#Cycles-in-Practice}

Cyclic data show up in many settings in real programs. Whenever two
data are interrelated, and we have good reason to want to get from
either one to the other, they have the potential to have references to
each other, which can lead to cycles. Sometimes the connection can be
to provide updates, as above; other times it can simply be for
navigational convenience.

Consider the Document Object Model (DOM), which is the data structure
that represents every Web page in a Web browser. Programmers usually
think of the DOM hierarchically, as a tree, because every note refers
to all the nodes that constitute it: e.g., a page has references to
each of its paragraphs, a list has references to each list item, and
so forth. However, every one of these elements also has a reference to
its parent. This way, a program can conveniently traverse “downward”
or “upward”.

Programming with cyclic data introduces complications. If we traverse
the data naïvely, we would go into an infinite loop. Rather, we have
to keep track of the data we have previously visited, and make sure we
don’t visit them again (see [The Size of a DAG](size-of-dag.html)). Indeed, cyclic
data are graphs [[Graphs](part_graphs.html)], so issues in processing graphs
become relevant here.

One interesting question that programming languages face is, how do
you print cyclic data? For instance, what happens if the
programmer writes

```jayret
acct1;
```
? To print the account we must print its owners; to print each owner,
we must print their account; to print that account…

::: {.do-now}
Try it out in both Python and Jayret!
:::

Different programming languages handle this problem in different
ways. Some languages will go into an infinite loop trying to print
cyclic data. Both Python and Jayret handle this more
intelligently. Determining even whether a datum is cyclic is an
interesting question, which we take up in [Detecting Cycles](cycle-detection.html).
