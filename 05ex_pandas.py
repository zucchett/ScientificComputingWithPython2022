import numpy as np
import pandas as pd
import bench


data = pd.read_csv("./data_000637.txt")
orbit_bx_num = 0


@bench.benchmark("Exercise #2")
def exercise2():
    global orbit_bx_num  # TODO: Fix this

    # Find the maximum value of BX in the whole dataset
    orbit_bx_num = data["BX_COUNTER"].max()
    print(f"Number of BX in a orbit: {orbit_bx_num}")


@bench.benchmark("Exercise #3")
def exercise3():
    first_orbit = data.iloc[0]["ORBIT_CNT"]
    data["TIME_NANOSEC"] = (
        ((data["ORBIT_CNT"] - first_orbit) * orbit_bx_num * 25)
        + (data["BX_COUNTER"] * 25)
        + (data["TDC_MEAS"] * 25 / 33)
    )
    print(data)


@bench.benchmark("Exercise #4")
def exercise4():
    last_nanosec = data.iloc[-1]["TIME_NANOSEC"]
    duration = pd.to_timedelta(last_nanosec)
    print(duration)


@bench.benchmark("Exercise #5")
def exercise5():
    noisy = (
        data.groupby("TDC_CHANNEL")["ORBIT_CNT"]
        .count()
        .sort_values(ascending=False)[:3]
    )
    print(f"Top-3 noisy channels: {noisy.index.tolist()}")


@bench.benchmark("Exercise #6")
def exercise6():
    non_empty_orbits = data["ORBIT_CNT"].unique()
    print(f"Number of non-empty orbits: {non_empty_orbits.size}")


@bench.benchmark("Exercise #7")
def exercise7():
    channel_139 = data.loc[data["TDC_CHANNEL"] == 139]
    non_empty_orbits = channel_139["ORBIT_CNT"].unique()
    print(f"Number of non-empty orbits in channel #139: {non_empty_orbits.size}")


@bench.benchmark("Exercise #8")
def exercise8():
    fpga1 = data.loc[data["FPGA"] == 0]
    fpga2 = data.loc[data["FPGA"] == 1]

    fpga1_tdc_count = fpga1.groupby("TDC_CHANNEL")["ORBIT_CNT"].count()
    fpga2_tdc_count = fpga2.groupby("TDC_CHANNEL")["ORBIT_CNT"].count()

    print(fpga1_tdc_count)
    print(fpga2_tdc_count)


@bench.benchmark("Exercise #9")
def exercise9():
    # TODO
    pass


exercise2()
exercise3()
exercise4()
exercise5()
exercise6()
exercise6()
exercise7()
exercise8()
exercise9()
