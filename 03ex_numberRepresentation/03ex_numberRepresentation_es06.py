def df (delta):
    def f (x):
        return x*(x-1)
    d = (f(1 + delta) - f(1)) / delta
    return d
 
d1 = 1e-2
print(d1, "\t --- ",df(d1), "\t --- e :", df(d1) - 1)
d1 = 1e-4
print(d1, "\t --- ",df(d1), "\t --- e :", df(d1) - 1)
d1 = 1e-6
print(d1, "\t --- ",df(d1), "\t --- e :", df(d1) - 1)
d1 = 1e-8
print(d1, "\t --- ",df(d1), "\t --- e :", df(d1) - 1)
d1 = 1e-10
print(d1, "\t --- ",df(d1), "\t --- e :", df(d1) - 1)
d1 = 1e-12
print(d1, "\t --- ",df(d1), "\t --- e :", df(d1) - 1)
d1 = 1e-14
print(d1, "\t --- ",df(d1), "\t --- e :", df(d1) - 1)

# As it is shown below (after run), using smaller 'delta' firstly improves the accuracy and
# function result gets closer to true value (which is 1).
# But somewhere (1e-10) decreasing delta makes bigger error and decreases accuracy.
# But why?
# If we rewrite the derivative equation for x=1, it would be df = (1 + delta) (1 + delta -1) / delta.
# When delta is not very very small, second paranteses (1 + delta -1) would be =delta, 
# so we have df = (1 + delta). And it is obvious (1 + delta) has smaller value and is closer to 1,when delta is smaller.
# But when we have a very very small value of delta, (1 + delta -1) != delta.
# In this case (1 + delta -1) ~= (1-1), and also (1 + delta)~= 1,
# so we would have df = (1 * 0) / delta. And this is completely differnet.
# And we can say in this new formula when delta gets smaller, result gets bigger, because it is denomirator.
# (This is not a correct reasin, but it is just for a better intuitive understanding).