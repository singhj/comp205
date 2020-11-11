#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> "{'text': 'Sepal width vs. length'}" in str(ir._layout_obj)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> "6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2, 5. , 5.9" in str(ir._data)
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

