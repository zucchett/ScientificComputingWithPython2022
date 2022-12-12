{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `01ex_introduction.py`.\n",
    "\n",
    "In case you need multiple files, name them `01ex_introduction_es01.py`, `01ex_introduction_es02.py` and so on. \n",
    "\n",
    "The exercises need to run without errors in `python3`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\\. **The HelloWorld replacement**\n",
    "\n",
    "a) Write a program that:\n",
    "- prints the numbers from 1 to 100\n",
    "- but for multiples of three print \"`Hello`\" instead of the number and for the multiples of five print \"`World`\"\n",
    "- for numbers which are multiples of both three and five print \"`HelloWorld`\".\n",
    "\n",
    "b) Put the result in a tuple and substitute \"`Hello`\" with \"`Python`\" and \"`World`\" with \"`Works`\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range (1,101):\r\n",
    "    if i%15 == 0:\r\n",
    "        print (\"Hello World\")\r\n",
    "    elif i%3==0:\r\n",
    "        print (\"Hello\")\r\n",
    "    elif i%5==0:\r\n",
    "        print (\"World\")\r\n",
    "    else :\r\n",
    "        print (\"i\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.code.notebook.stdout": [
       "(1, 2, 'python', 4, 'works', 'python', 7, 8, 'python', 'works', 11, 'python', 13, 14, 'python works', 16, 17, 'python', 19, 'works', 'python', 22, 23, 'python', 'works', 26, 'python', 28, 29, 'python works', 31, 32, 'python', 34, 'works', 'python', 37, 38, 'python', 'works', 41, 'python', 43, 44, 'python works', 46, 47, 'python', 49, 'works', 'python', 52, 53, 'python', 'works', 56, 'python', 58, 59, 'python works', 61, 62, 'python', 64, 'works', 'python', 67, 68, 'python', 'works', 71, 'python', 73, 74, 'python works', 76, 77, 'python', 79, 'works', 'python', 82, 83, 'python', 'works', 86, 'python', 88, 89, 'python works', 91, 92, 'python', 94, 'works', 'python', 97, 98, 'python', 'works')\n"
      ]
     },
     "output_type": "unknown"
    }
   ],
   "source": [
    "result = []\r\n",
    "for i in range (1,101):\r\n",
    "    if i%15 == 0:\r\n",
    "        result.append('python works')\r\n",
    "    elif i%3==0:\r\n",
    "        result.append('python')\r\n",
    "    elif i%5==0:\r\n",
    "        result.append('works')\r\n",
    "    else :\r\n",
    "        result.append(i)\r\n",
    "print(tuple(result))        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2\\. **The swap**\n",
    "\n",
    "Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).\n",
    "\n",
    "Try to do that without using a temporary variable, exploiting the Python syntax."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "left, right = input().split(' ')\r\n",
    "print(left, right, end='=>')\r\n",
    "left, right = right, left\r\n",
    "print(left, right)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3\\. **Computing the distance**\n",
    "\n",
    "Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, where *u* and *v* are both 2-tuples *(x,y)*.\n",
    "\n",
    "Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.\n",
    "\n",
    "*Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.code.notebook.stdout": [
       "(1, 2, 'python', 4, 'works', 'python', 7, 8, 'python', 'works', 11, 'python', 13, 14, 'python works', 16, 17, 'python', 19, 'works', 'python', 22, 23, 'python', 'works', 26, 'python', 28, 29, 'python works', 31, 32, 'python', 34, 'works', 'python', 37, 38, 'python', 'works', 41, 'python', 43, 44, 'python works', 46, 47, 'python', 49, 'works', 'python', 52, 53, 'python', 'works', 56, 'python', 58, 59, 'python works', 61, 62, 'python', 64, 'works', 'python', 67, 68, 'python', 'works', 71, 'python', 73, 74, 'python works', 76, 77, 'python', 79, 'works', 'python', 82, 83, 'python', 'works', 86, 'python', 88, 89, 'python works', 91, 92, 'python', 94, 'works', 'python', 97, 98, 'python', 'works')\n"
      ]
     },
     "output_type": "unknown"
    }
   ],
   "source": [
    "import math\r\n",
    "\r\n",
    "u=(float(input()),float(input()))\r\n",
    "v=(float(input()),float(input()))\r\n",
    "d= math.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)\r\n",
    "print(d) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4\\. **Counting letters**\n",
    "\n",
    "Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.\n",
    "\n",
    "The strings are in the cell below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = \"Write a program that prints the numbers from 1 to 100. \\\n",
    "But for multiples of three print Hello instead of the number and for the multiples of five print World. \\\n",
    "For numbers which are multiples of both three and five print HelloWorld.\"\n",
    "s2 = \"The quick brown fox jumps over the lazy dog\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = \"Write a program that prints the numbers from 1 to 100. \\\r\n",
    "But for multiples of three print Hello instead of the number and for the multiples of five print World. \\\r\n",
    "For numbers which are multiples of both three and five print HelloWorld.\"\r\n",
    "s2 = \"The quick brown fox jumps over the lazy dog\"\r\n",
    "\r\n",
    "s1 , s2 = s1.lower(), s2.lower()\r\n",
    "\r\n",
    "for i in s1:\r\n",
    "    print(i , \": \",s1.count(i) + s2.count(i))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5\\. **Isolating the unique**\n",
    "\n",
    "Write a program that determines and counts the unique numbers in the list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,\n",
    " 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,\n",
    " 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,\n",
    " 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,\r\n",
    " 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,\r\n",
    " 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,\r\n",
    " 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]\r\n",
    "\r\n",
    "result = {}\r\n",
    "\r\n",
    "for i in range(len(l)):\r\n",
    "    c = 0\r\n",
    "    for j in range(len(l)):\r\n",
    "        if l[i] == l[j]:\r\n",
    "            c+=1\r\n",
    "            result[l[i]] = c\r\n",
    "#print(result)\r\n",
    "uniques = []\r\n",
    "for key, value in result.items():\r\n",
    "    if value == 1:\r\n",
    "        uniques.append(key)\r\n",
    "print(uniques)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Do the same exploiting only the Python data structures."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6\\. **Casting**\n",
    "\n",
    "Write a program that:\n",
    "* reads from command line two variables, that can be either `int`, `float`, or `str`.\n",
    "* use the `try`/`except` expressions to perform the addition of these two variables, only if possible\n",
    "* and print the result without making the code crash for all the `int`/`float`/`str` input combinations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "can not add integer to string!\n"
     ]
    }
   ],
   "source": [
    "a = input('enter your value: ')\r\n",
    "b = input('enter your value: ')\r\n",
    "try:\r\n",
    "     if not a.isnumeric() and not b.isnumeric():\r\n",
    "          c = a + b\r\n",
    "     else:\r\n",
    "          c = float(a) + float(b)\r\n",
    "except:\r\n",
    "     c = 'can not add integer to string!'\r\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "can not add integer to string!\n"
     ]
    }
   ],
   "source": [
    "a=input(\"input 1:\")\r\n",
    "b=input(\"input 2:\")\r\n",
    "try:\r\n",
    "    try:\r\n",
    "        a,b=float(a),float(b)\r\n",
    "        c=a+b\r\n",
    "        print(c)\r\n",
    "   \r\n",
    "    except: \r\n",
    "        try:\r\n",
    "            a=int(a)\r\n",
    "            print('can not add integer to string!')            \r\n",
    "        except:\r\n",
    "             b=int(b)\r\n",
    "             print('can not add integer to string!')\r\n",
    "except: \r\n",
    "    c=a+b \r\n",
    "    print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7\\. **Cubes**\n",
    "\n",
    "Create a list of the cubes of *x* for *x* in *[0, 10]* using:\n",
    "\n",
    "a) a for loop\n",
    "\n",
    "b) a list comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]\n"
     ]
    }
   ],
   "source": [
    "cubes = [i**3 for i in range(0, 11)]\n",
    "print(cubes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8\\. **List comprehension**\n",
    "\n",
    "Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]\n"
     ]
    }
   ],
   "source": [
    "a = []\n",
    "for i in range(3):\n",
    "    for j in range(4):\n",
    "        a.append((i, j))\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]\n"
     ]
    }
   ],
   "source": [
    "print([(i, j) for i in range(3) for j in range(4)])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9\\. **Nested list comprehension**\n",
    "\n",
    "> A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).\n",
    "\n",
    "Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "((3, 4, 5), (8, 6, 10), (12, 16, 20), (24, 10, 26), (32, 24, 40), (40, 42, 58), (48, 64, 80), (80, 18, 82))\n"
     ]
    }
   ],
   "source": [
    "result = []\n",
    "c, m = 0, 2\n",
    "while c < 100 :\n",
    "    for n in range(1, m) :\n",
    "        a = m * m - n * n\n",
    "        b = 2 * m * n\n",
    "        c = m * m + n * n\n",
    "        if c > 100 :\n",
    "            break\n",
    "        result.append((a, b, c))\n",
    "        m = m + 1\n",
    "print(tuple(result))        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10\\. **Normalization of a N-dimensional vector**\n",
    "\n",
    "Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.2672612419124244, 0.5345224838248488, 0.8017837257372732]\n"
     ]
    }
   ],
   "source": [
    "import math\r\n",
    "\r\n",
    "n = int(input('Enter the number of dimensions: '))\r\n",
    "vector = []\r\n",
    "square_sum = 0\r\n",
    "for i in range(n):\r\n",
    "    vector.append(int(input()))\r\n",
    "    square_sum += vector[i]**2\r\n",
    "size = math.sqrt(square_sum)\r\n",
    "for i in range(n):\r\n",
    "    vector[i] = vector[i] / size\r\n",
    "print(vector)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11\\. **The Fibonacci sequence**\n",
    "\n",
    "Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]\n"
     ]
    }
   ],
   "source": [
    "fibonacci = [1, 1]\r\n",
    "for i in range(1, 19):\r\n",
    "    fibonacci.append(fibonacci[i] + fibonacci[i - 1])\r\n",
    "print(fibonacci)    "
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
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  },
  "vscode": {
   "interpreter": {
    "hash": "ad2bdc8ecc057115af97d19610ffacc2b4e99fae6737bb82f5d7fb13d2f2c186"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}