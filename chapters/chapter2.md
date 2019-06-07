---
title: 'Chapter 2: Algebra 2'
description:
  "The all-in-one algebra 2."
prev: /chapter1
next: /chapter2
type: chapter
id: 1
---

<exercise  id="1" title="What's included in Algebra 2" >

As preparation for pre-calculus, `Algebra-2` is fun and entertaining. On another hand, it is rather more abstract than preceding materials. Sometimes, students find it non-intuitive and struggle to understand. 

In this chapter, we are going to cover materials in the following sequence.

1. Functions and treat (almost) everything as functions
2. Linear functions and absolute value functions
3. Polynomial operations and polynomial functions
4. Radical functions and complex numbers
5. Rational functions
6. Exponential functions and logarithmic functions
7. Trigonometric graphs, equations and functions
8. Sequences and Series
9. Statistics

</exercise>


<exercise id="2" title="Functions">

## A taste of function, from daily life examples.

Safely think this way, function is nothing special but a fancy name for **relation** or **mapping**. Such a relations usually involve transformations or operations. For example, the following **relations** are all legitimate functions. 

1. Given a __place__, find its __zip code__. 
2. Given a __distance__ in miles, find its value in __kilometers__.
3. Given a __person's name__, find out his or her __father's name__.

Note the way I describe those questions. There is always an input and an output. The relations between the output and the input are different. 

So there are three key elements in order to **specify** a function completely: the domain of input, the relations and the range of output. 

The code block below demonstrates how the second relation mentioned above can be represented in Python code. Can you guess the valid input domain of this Python function, which encodes the mathematical function, and the output range?

<codeblock id="02_02_01">
</codeblock>

## Let's define and represent functions.

### Function as a special kind of relation.
A function is a special kind of relation. For example, Let's use \\(x\\) to represent possible input values in domain and \\(y\\) to represent possible values in range. A function is special such that one value of \\(x\\) can't be mapped to more than one value of \\(y\\). 

Here is an intuitive example. Let's say a function does one job that is converting a distance to kilometers no matter what its original unit is. Then \\(1 mile\\) will be converted to \\(1.6 km\\). However, \\(5280 ft\\) will also be converted to \\(1.6 km\\). Two different \\(x\\) as the inputs of the function can give the same value of \\(y\\), which is totally fine. What is not ok is that \\(1 mile\\) cannot be converted to two different values of \\(y\\), say \\(2.6 km\\) and \\(1.6 km\\).

In a word, the return/output of a function is unambiguous as the input is given. 

### multiple ways of representing functions.

A function can be represented as a table, a graph, a mapping diagram or most commonly in math, a formula or equation.

#### Table

|  \\(x\\) | \\(y\\)  |
|---|---|
| -2  | 1  |
|  -1 | -1  |
|  0 |  -1 |
|  1 | 1  |
|  2 | 5  |

#### Equation and graph

You can run the following code block to get a graph. The equation that generates the graph is in a Python function. What is it, can you guess it?

<codeblock id="02_02_02">
</codeblock>

####  a mapping diagram. 

A mapping diagram represents exactly the same information as in the table. A typical mapping diagram looks like [this one](https://en.wikipedia.org/wiki/File:Injection.svg#/media/File:Injection.svg) on Wikipedia.

Now, let's go quizzy! What is the formula for the function represented in the table and the code block graphs?

<choice>
<opt correct="true" text="y = x*x + x - 1">

Yesss! You are right.

</opt>
<opt  text="y = 2*x*x - x - 2">
Even you can try, calculate first.
</opt>

<opt  text="y = x*x + x - 1">
One more time.
</opt>

<opt  text="y = x*x - 2x - 1">
Try to write down the formula and find consistency.
</opt>

</choice>

</exercise>