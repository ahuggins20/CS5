
# coding: utf-8

# In[27]:





# In[28]:


hidden_message('AAGGCCGCGGCCTT','GGCC')


# In[46]:


def frequent_words(text, k):
    k_mer_dict={}
    for i in range(len(text)-k+1):
        try:
            k_mer_dict[text[i:i+k]]+=1
        except:
            k_mer_dict[text[i:i+k]]=1
    max_iters=max(k_mer_dict.values())
    out=[]
    for key in k_mer_dict.keys():
        if k_mer_dict[key]==max_iters:
            out.append((key,k_mer_dict[key]))
    return out


# In[47]:





#%%
