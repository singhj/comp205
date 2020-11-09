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
          >>> type(fruit)
          <class 'pandas.core.frame.DataFrame'>
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> fruit.size
          200
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> "31.1652" in str(fruit.max())
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> ".0076757" in str(fruit.min())
          True
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

