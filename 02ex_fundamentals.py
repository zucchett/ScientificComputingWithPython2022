{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `02ex_fundamentals.py`.\n",
    "\n",
    "In case you need multiple files, name them `02ex_fundamentals_es01.py`, `02ex_fundamentals_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `02ex_fundamentals`. \n",
    "\n",
    "The exercises need to run without errors with `python3`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\\. **Global variables**\n",
    "\n",
    "Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 0, 1, 2, 3, 4]\n",
      "[1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "x = 5\r\n",
    "\r\n",
    "def f(alist):\r\n",
    "    l1 = alist.copy()\r\n",
    "    l1.extend([i for i in range(x)])\r\n",
    "    return l1\r\n",
    "\r\n",
    "alist = [1, 2, 3]\r\n",
    "ans = f(alist)\r\n",
    "print(ans)\r\n",
    "print(alist) # alist has been changed"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2\\. **List comprehension**\n",
    "\n",
    "Write the following expression using a list comprehension:\n",
    "\n",
    "`ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 9, 25, 49, 81]\n"
     ]
    }
   ],
   "source": [
    "print([i**2 for i in range(10) if i % 2 != 0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3\\. **Filter list**\n",
    "\n",
    "Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['php', 'javascript', 'java']\n"
     ]
    }
   ],
   "source": [
    "i=0\r\n",
    "def func(word):\r\n",
    "    global i\r\n",
    "    n = 3\r\n",
    "    if(i<n):\r\n",
    "        i+=1\r\n",
    "        return True\r\n",
    "    return False    \r\n",
    "r = filter(func, ['php', 'javascript', 'java', 'c++', 'c', 'python', 'go', 'rust', 'dart', 'swift'])\r\n",
    "print(list(r))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4\\. **Map dictionary**\n",
    "\n",
    "\n",
    "Consider the following dictionary:\n",
    "\n",
    "`lang = {\"Python\" : 3, \"Java\" : '', \"Cplusplus\" : 'test', \"Php\" : 0.7}`\n",
    "\n",
    "Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6, 4, 9, 3]\n"
     ]
    }
   ],
   "source": [
    "def f(string):\r\n",
    "    return len(string)\r\n",
    " \r\n",
    "print(list(map(f, {\"Python\" : 3, \"Java\" : '', \"Cplusplus\" : 'test', \"Php\" : 0.7})))       "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5\\. **Lambda functions**\n",
    "\n",
    "Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:\n",
    "\n",
    "`language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`\n",
    "\n",
    "*Hint*: use the method `sort()` and its argument `key` of the `list` data structure."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Cplusplus', 81), ('Java', 32), ('Php', 45), ('Python', 97)]\n"
     ]
    }
   ],
   "source": [
    "print(sorted([('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)], key = lambda x : x[0],reverse=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6\\. **Nested functions**\n",
    "\n",
    "Write two functions: one that returns the square of a number, and one that returns its cube.\n",
    "\n",
    "Then, write a third function that returns the number raised to the 6th power, using only the two previous functions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "64\n"
     ]
    }
   ],
   "source": [
    "def square(number):\r\n",
    "    return number**2\r\n",
    "\r\n",
    "def cube(number):\r\n",
    "    return number**3    \r\n",
    "\r\n",
    "def six_power(number):\r\n",
    "    return number * square(number) * cube(number)\r\n",
    "\r\n",
    "print(six_power(2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7\\. **Decorators**\n",
    "\n",
    "Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.\n",
    "\n",
    "The wrapped function should look like:\n",
    "\n",
    "```python\n",
    "@hello\n",
    "def square(x):\n",
    "    return x*x\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "incomplete input (3791764940.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [145]\u001b[1;36m\u001b[0m\n\u001b[1;33m    @hello\u001b[0m\n\u001b[1;37m           ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m incomplete input\n"
     ]
    }
   ],
   "source": [
    "def hello():\r\n",
    "    return 'Hello World!'\r\n",
    "@hello "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8\\. **The Fibonacci sequence (part 2)**\n",
    "\n",
    "Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 "
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\r\n",
    "    if n <= 1:\r\n",
    "        return n\r\n",
    "    return fibonacci(n - 1) + fibonacci(n - 2)\r\n",
    "\r\n",
    "n = 1\r\n",
    "while (n <= 20):\r\n",
    "    print(fibonacci(n), end=' ')\r\n",
    "    n += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9\\. **The Fibonacci sequence (part 3)**\n",
    "\n",
    "Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.\n",
    "\n",
    "Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:\n",
    "\n",
    "`%timeit loopFibonacci(20)`\n",
    "\n",
    "`%timeit recursiveFibonacci(20)`\n",
    "\n",
    "which one is the most efficient implementation? By how much?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time taken for normal fibonacci -> 0.00010489999976925901\n",
      "Time taken for recursive fibonacci -> 33.82432599999993\n"
     ]
    }
   ],
   "source": [
    "import timeit\r\n",
    "\r\n",
    "def fibonacci(n):\r\n",
    "    fibonacci = [1, 1]\r\n",
    "    for i in range(1, n - 1):\r\n",
    "        fibonacci.append(fibonacci[i] + fibonacci[i - 1])\r\n",
    "    return fibonacci    \r\n",
    "\r\n",
    "def recursive_fibonacci(n):\r\n",
    "    if n <= 1:\r\n",
    "        return n\r\n",
    "    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)\r\n",
    "\r\n",
    "start = timeit.default_timer()\r\n",
    "fibonacci(40)\r\n",
    "print('Time taken for normal fibonacci -> ' + str(timeit.default_timer() - start))\r\n",
    "\r\n",
    "start = timeit.default_timer()\r\n",
    "recursive_fibonacci(40)\r\n",
    "print('Time taken for recursive fibonacci -> ' + str(timeit.default_timer() - start))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10\\. **Class definition**\n",
    "\n",
    "Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.\n",
    "\n",
    "- Create appropriate methods to get and set the length of each side\n",
    "\n",
    "- Create a method `perimeter()` that returns the perimeter of the polygon\n",
    "\n",
    "- Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method\n",
    "\n",
    "Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 4, 5)\n",
      "(8, 6, 10)\n",
      "24\n",
      "[10, 8, 6]\n"
     ]
    }
   ],
   "source": [
    "class polygon:\r\n",
    "    sides = None\r\n",
    "    def __init__(self, sides:tuple) -> None:\r\n",
    "        if len(sides) < 3:\r\n",
    "            raise Exception('Sides should contain at least 3 items.')\r\n",
    "        self.sides = sides\r\n",
    "\r\n",
    "    def get_sides(self) -> tuple:\r\n",
    "        return self.sides\r\n",
    "\r\n",
    "    def set_sides(self, sides:tuple) -> None:\r\n",
    "            if len(sides) < 3:\r\n",
    "                raise Exception('Sides should contain at least 3 items.')\r\n",
    "            self.sides = sides     \r\n",
    "\r\n",
    "    def perimeter(self) -> float:\r\n",
    "        sum = 0\r\n",
    "        for item in self.sides:\r\n",
    "            sum += item\r\n",
    "        return sum    \r\n",
    "\r\n",
    "    def get_ordered_sides(self, increasing):\r\n",
    "        return sorted(self.sides, reverse=not increasing)\r\n",
    "        \r\n",
    "\r\n",
    "triangle = polygon((3, 4, 5))\r\n",
    "print(triangle.get_sides())\r\n",
    "triangle.set_sides((8, 6, 10))\r\n",
    "print(triangle.get_sides())\r\n",
    "print(triangle.perimeter())\r\n",
    "print(triangle.get_ordered_sides(False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11\\. **Class inheritance**\n",
    "\n",
    "Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.\n",
    "\n",
    "- Create a method `area()` that returns the area of the rectangle.\n",
    "\n",
    "Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "import math\r\n",
    "\r\n",
    "class polygon:\r\n",
    "    sides = None\r\n",
    "    def __init__(self, sides:tuple) -> None:\r\n",
    "        if len(sides) < 3:\r\n",
    "            raise Exception('Sides should contain at least 3 items.')\r\n",
    "        self.sides = sides\r\n",
    "\r\n",
    "    def get_sides(self) -> tuple:\r\n",
    "        return self.sides\r\n",
    "\r\n",
    "    def set_sides(self, sides:tuple) -> None:\r\n",
    "            if len(sides) < 3:\r\n",
    "                raise Exception('Sides should contain at least 3 items.')\r\n",
    "            self.sides = sides     \r\n",
    "\r\n",
    "    def perimeter(self) -> float:\r\n",
    "        sum = 0\r\n",
    "        for item in self.sides:\r\n",
    "            sum += item\r\n",
    "        return sum    \r\n",
    "\r\n",
    "    def get_ordered_sides(self, increasing):\r\n",
    "        return sorted(self.sides, reverse=not increasing)\r\n",
    "\r\n",
    "class rectangle(polygon):\r\n",
    "    def __init__(self, sides: tuple) -> None:\r\n",
    "        super().__init__(sides)\r\n",
    "\r\n",
    "        #if not(self.sides[0] == self.sides[1] and self.sides[3] == self.sides[2]) or not(self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]) or not(self.sides[0] == self.sides[3] and self.sides[1] == self.sides[2]):\r\n",
    "            #raise Exception('These number can not form rectangle')\r\n",
    "\r\n",
    "    def area(self):\r\n",
    "        return self.sides[0] + self.sides[1] + self.sides[2] + self.sides[3]\r\n",
    "\r\n",
    "\r\n",
    "r = rectangle((1, 1, 2, 2))\r\n",
    "print(r.area())"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "3d0d2e03e4ac39b2e9f98cf3c89f4c99e762ca0c0aa172029f1f7c8d57ce9469"
  },
  "kernelspec": {
   "display_name": "Python 3.10.8 64-bit",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}