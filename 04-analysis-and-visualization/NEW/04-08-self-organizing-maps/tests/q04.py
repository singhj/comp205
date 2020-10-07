#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(joined_fruit)
          <class 'pandas.core.frame.DataFrame'>
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> joined_fruit.size
          400
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> 'bmu' in joined_fruit.columns
          True
          """,
          'hidden': False,
          'locked': False
        },
          
          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

