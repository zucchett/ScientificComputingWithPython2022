# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:58:31 2022

@author: Ruben
"""

import numpy as np

main=np.array([0,298,303,736,871,1175,1475,1544,1913,2448])

final=main-main[:,np.newaxis]
final_km=final/1.609344
print(final_km)