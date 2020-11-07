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
          >>> type(pi)
          <class 'plotly.graph_objs._figure.Figure'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> "['Red', 'Blue', 'Yellow', 'Purple', 'Green', 'White']" in str(pi._data_objs)
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

