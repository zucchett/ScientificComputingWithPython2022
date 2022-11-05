#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Polygon:
    def __init__(edge,edge_tuple):
        edge.edge_tuple = edge_tuple

        
    def perimeter(abc):
        print("Perimeter of the Polygon " + str(sum(abc.edge_tuple)))
        
    def getOrderedSides(abc, Ascending=True):
        a = abc.edge_tuple
        if Ascending:
            print(sorted(a,reverse=False))
        else:
            print(sorted(a,reverse=True))
            
 

p1 = Polygon((1,2,3))
p1.perimeter()
p1.getOrderedSides(Ascending=False)


# In[ ]:





# In[ ]:




