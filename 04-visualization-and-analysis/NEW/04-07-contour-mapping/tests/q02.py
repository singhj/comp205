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
          >>> type(our_vars)
          list
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ("UNIX TIME") in str(our_vars)
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> ("ALT") in str(our_vars)
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

