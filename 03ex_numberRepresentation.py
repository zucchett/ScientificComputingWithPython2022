{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can solve these exercises in the room or at home. For this week, exercises have to be solved by creating a dedicated `.py` file (or files) called `03ex_numberRepresentation.py`.\n",
    "\n",
    "In case you need multiple files, name them `03ex_numberRepresentation_es01.py`, `03ex_numberRepresentation_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `03ex_numberRepresentation`. \n",
    "\n",
    "The exercises need to run without errors with `python3`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\\. **Number representation**\n",
    "\n",
    "Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).\n",
    "Determine the input type in the function, and pass another argument to choose the output representation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0x6a\n"
     ]
    }
   ],
   "source": [
    "def number_representation(number, mode):\n",
    "    base = -1\n",
    "    if mode == 'bin':\n",
    "        return bin(int(number))\n",
    "    if mode == 'dec':\n",
    "        return int(number)\n",
    "    if mode == 'hex':\n",
    "        return hex(int(number)) \n",
    "    return(int(number, base))          \n",
    "\n",
    "print(number_representation('106', 'hex'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2\\. **32-bit floating point number**\n",
    "\n",
    "Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12759040.0\n"
     ]
    }
   ],
   "source": [
    "def converter(number):\n",
    "    return(float(int(number, 2)))\n",
    "\n",
    "print(converter('110000101011000000000000'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3\\. **Underflow and overflow**\n",
    "\n",
    "Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. \n",
    "\n",
    "*Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "N=1000\n",
    "Underflow=1\n",
    "Overflow=1\n",
    "factor =2\n",
    "print(\"|n\",\"\\t\\t\",\"|Underflow\",\"\\t\\t\\t\",\"|Overflow\")\n",
    "for n in range(N):\n",
    "    Underflow=Underflow/2\n",
    "    Overflow=Overflow*2\n",
    "    print(\"|%2d\"%n,\"\\t\\t\",\"|2.5e\"%Underflow,\"|\",\"\\t\\t\",\"%2.5e\"%Overflow,\"|\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4\\. **Machine precision**\n",
    "\n",
    "Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.\n",
    "\n",
    "*Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5\\. **Quadratic solution**\n",
    "\n",
    "Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the quadratic equation $ax^2+bx+c=0$ using the standard formula:\n",
    "$$\n",
    "x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}\n",
    "$$\n",
    "\n",
    "(a) use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$\n",
    "\n",
    "(b) re-express the standard solution formula by multiplying the numerator and the denominator by $-b\\mp\\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)\n",
    "\n",
    "(c) write a function that computes the roots of a quadratic equation accurately in all cases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-9.999894245993346e-07, -999999.999999]\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "def quadratic(a, b, c):\n",
    "    delta = math.sqrt((b**2) - (4*a*c))\n",
    "    roots = []\n",
    "    roots.append((-b + delta) / (2 * a))\n",
    "    roots.append((-b - delta) / (2 * a))\n",
    "    return roots\n",
    "\n",
    "print(quadratic(0.001, 1000, 0.001))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6\\. **The derivative**\n",
    "\n",
    "Write a program that implements the function $f(x)=x(x−1)$\n",
    "\n",
    "(a) Calculate the derivative of the function at the point $x = 1$ using the derivative definition:\n",
    "\n",
    "$$\n",
    "\\frac{{\\rm d}f}{{\\rm d}x} = \\lim_{\\delta\\to0} \\frac{f(x+\\delta)-f(x)}{\\delta}\n",
    "$$\n",
    "\n",
    "with $\\delta = 10^{−2}$. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?\n",
    "\n",
    "(b) Repeat the calculation for $\\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12}$ and $10^{−14}$. How does the accuracy scale with $\\delta$?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0000999999998899\n"
     ]
    }
   ],
   "source": [
    "def f(x):\n",
    "    return x * (x - 1)\n",
    "\n",
    "def f_derivative(x, sigma = 0.0001):\n",
    "    if sigma < 0.00000000000001:\n",
    "        raise Exception('Can not devide by zero')\n",
    "    return (f(x + sigma) - f(x)) / sigma   \n",
    "\n",
    "print(f_derivative(1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7\\. **Integral of a semicircle**\n",
    "\n",
    "Consider the integral of the semicircle of radius 1:\n",
    "$$\n",
    "I=\\int_{-1}^{1} \\sqrt(1-x^2) {\\rm d}x\n",
    "$$\n",
    "which is known to be $I=\\frac{\\pi}{2}=1.57079632679...$.\n",
    "\n",
    "Alternatively we can use the Riemann definition of the integral:\n",
    "$$\n",
    "I=\\lim_{N\\to\\infty} \\sum_{k=1}^{N} h y_k \n",
    "$$\n",
    "\n",
    "with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where\n",
    "$y_k$ is the value of the function at the $k-$th slice.\n",
    "\n",
    "(a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?\n",
    "\n",
    "(b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use `timeit` to measure the time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
