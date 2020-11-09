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
          >>> type(resp)
          string
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> resp == "n"
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

