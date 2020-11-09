#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(plotdf)
          pandas.core.frame.DataFrame
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(plotdf.columns)
          2
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> len(plotdf)
          123
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

