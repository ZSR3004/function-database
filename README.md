# Sequences and Functions Database: My First Programming Project

## Table of Contents

1. [About the Project](#about-the-project)  
2. [Making the Project](#making-the-project)  
3. [Function Style Guide](#function-style-guide)  
4. [Recursive Equation Style Guide](#recursive-equation-style-guide)

## About the Project

This was the very first proper coding for my Introduction to Programming course in college. I plan to come back and
update the project at some point by making it a webapp with some better visuals.

The SFProject.txt file acts as the database for the functions if you feel so inclined as to glance at it.

## Making the Project

Just clone the repository and run the `main.py` file.

## Function Style Guide

To create a function, _f(x)_, you must follow the following:

_x_ refers to a variable; only use this variable
_c_ is a constant, it can be replaced by any number
Do not include _f(x)_ or _y_, include only everything after the equals sign

Basic Operations:
Addition: +
Subtraction: -
Multiplication: *
Division: /
Factorials: factorial(_c_)

## Recursive Equation Style Guide

Recursive Sequence Style Guide:

_x_ refers to a variable; only use this variable
_c_ is a constant, it can be replaced by any number
Do not include _a(n)_, include only everything after the equals sign

Basic Operations:
Addition: +
Subtraction: -
Multiplication: *
Division: /
Factorials: factorial(_c_)

For example, the term, _a_, before the nth term would be _a(n-1)_.

Example:
The _nth_ term is the second to last term added to the third to last term: _a(n)=a(n-1)+a(n-2)_

Degree:
Degree is determined by the farthest back term called.
For example, if you are adding the last and second to last term, then the sequence is to the second degree (degree of 2)
Look for the largest number you are subtracting n from.

Example: _a(n-1)+a(n-2)*a(n-5)_; the largest number subtracting from _n_ is 5, therefore this is to the fifth degree.
