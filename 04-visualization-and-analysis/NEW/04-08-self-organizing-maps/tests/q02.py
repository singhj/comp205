#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(fruit_data)
          <class 'pandas.core.frame.DataFrame'>
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> fruit_data.size
          120
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> "31.1652" in str(fruit_data.max())
          False
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> ".000012" in str(fruit_data.min())
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> len(fruit_data)
          40
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

