# Global variables
a_list = [1, 2, 3]
new_list = []


def f(a_list):
    for i in range(5):
        new_list.append(i)
    return new_list


ans = f(a_list)
print(ans)
print(new_list)  # a_list has been changed
