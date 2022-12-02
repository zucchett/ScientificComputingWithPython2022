import json
import bench
import numpy as np
import pandas as pd
import struct
from pathlib import Path


@bench.benchmark("Exercise #1")
def exercise1():
    # Create a list of integers
    int_seq = list(range(0, 10))
    # Convert list to a JSON list
    json_str = json.dumps(int_seq)

    # Create a temporary file in order to wite in it
    with open("./data/data_int.txt", "w") as f:
        f.write(json_str)
        print(f"data_int.txt has been created")

    # TODO: Do the remainig parts
    mat1 = np.ndarray((5, 5))
    np.savetxt("./data/data_float.txt", mat1, delimiter=",")


@bench.benchmark("Exercise #2")
def exercise2():
    try:
        user_data = json.load(open("./data/user_data.json"))
        print("Loaded json data")
    except Exception as e:
        print(e)
        return

    fname = "./data/american_express.csv"
    f = open(fname, "w")

    header_line = ",".join(user_data[0].keys()) + "\n"
    f.write(header_line)

    for item in user_data:
        try:
            if item["CreditCardType"] != "American Express":
                continue
        except KeyError:
            continue

        csv_line = ",".join(item.values()) + "\n"
        f.write(csv_line)

    f.close()
    print(f"{fname} has been created")


@bench.benchmark("Exercise #3")
def exercise3():
    data = pd.read_csv("./data/mushrooms_categorized.csv")
    print(data)

    feature_avg = data.groupby("class").mean()
    print(feature_avg)

    fname = "./data/mushrooms_feature_avg.json"
    with open(fname, "w") as f:
        f.write(feature_avg.to_json())
        print(f"{fname} has been created")


@bench.benchmark("Exercise #4")
def exercise4():
    f = open("./data/credit_card.dat", "r")

    # A function to convert binary-string to character
    b2c = lambda x: chr(int(x, 2))

    for l in f.readlines():
        # Split the line into list of fixed 6-width tokens and
        # ignore the last token, since it's just for padding and can
        # be thrown away
        tokens = [l[i : i + 6] for i in range(0, len(l), 6)][:-1]
        card_num = "".join(map(b2c, tokens))
        print(card_num)

    f.close()


@bench.benchmark("Exercise #5")
def exercise5():

    out_name = "./data/data_000637.dat"
    # Skip if the binary file is already created
    if Path(out_name).is_file():
        print(f"Skipping, {out_name} exists")
        return

    data = pd.read_csv("./data/data_000637.txt")
    print(data)

    f = open(out_name, "wb")
    print("Converting to binary, it take a while...")
    for index, row in data.iterrows():
        head = (
            (row["HEAD"] << 62)
            + (row["FPGA"] << 58)
            + (row["TDC_CHANNEL"] << 49)
            + (row["ORBIT_CNT"] << 17)
            + (row["BX_COUNTER"] << 5)
            + row["TDC_MEAS"]
        )
        p = struct.pack("<q", head)
        f.write(p)
    f.close()

    print(f"{out_name} has been created")


exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
