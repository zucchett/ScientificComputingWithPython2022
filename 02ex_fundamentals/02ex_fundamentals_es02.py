#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:43:57 2022

@author: alessandra
"""

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

ans1 = [x*x for x in range(10) if x % 2 == 1]
print(ans)
print(ans1)