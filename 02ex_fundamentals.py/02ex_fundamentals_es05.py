#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lambda functions

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x : x[0])

print(language_scores)


# In[ ]:




