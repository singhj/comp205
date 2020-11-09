#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ppl.shape
          (20, 11)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(ppl)
          <class 'pandas.core.frame.DataFrame'>
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

