#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Filter list

def shorter_words(words,n):
    
    return list(filter(lambda words: len(words) < n, words))


new_words= shorter_words(['Hello', 'World', 'sum', 'determine', 'try', 'code', 'python'],6)

print(new_words)


# In[ ]:




