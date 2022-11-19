#!/usr/bin/env python
# coding: utf-8

# In[23]:


from Question import question


# In[24]:


Question_prompt = [
    "How many days do we have in a week?\n (a) six\n (b) seven\n (c) eight\n",
    "How many letters are there in the English alphabet?\n (a) 24\n (b) 26\n (c) 28\n",
    "Which animal is called King of Jungle?\n (a) lion\n (b) tiger\n (c) deer\n",
    "Which is the tallest animal on the earth?\n (a) lion\n (b) tiger\n (c) giraffe\n",
    "How many hours are there in two days?\n (a) 12\n (b) 24\n (c) 48\n",
]


# In[25]:


questions = [question(Question_prompt[0], 'b'),
             question(Question_prompt[1], 'b'),
             question(Question_prompt[2], 'a'),
             question(Question_prompt[3], 'c'),
             question(Question_prompt[4], 'c'),
]


# In[26]:


def run_test(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print('You have got ', score, '/', len(questions), 'corrected')


# In[28]:


run_test(questions)


# In[ ]:




