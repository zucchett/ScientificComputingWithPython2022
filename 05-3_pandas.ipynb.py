data["abs_time_in_ns"] = data['TDC_MEAS'].transform(lambda x: x * 25/30) + data['BX_COUNTER'].transform(lambda x: x * 25) +data['ORBIT_CNT'].transform(lambda x: x * est_bx * 25)
data