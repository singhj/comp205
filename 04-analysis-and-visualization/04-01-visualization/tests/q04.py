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
          >>> "'width': 2" in str(pi._data)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> "'color': '#000000'" in str(pi._data)
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

