def norm(var):
    res = [i / sum(var) for i in var]
    print(res)
    return res

demo_tuple = (2, 4.5, 5, 7)
norm(demo_tuple)