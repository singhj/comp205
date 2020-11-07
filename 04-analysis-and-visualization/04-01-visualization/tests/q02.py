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
          >>> type(fig._data_objs[0])
          <class 'plotly.graph_objs.Bar'>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ('(1,1)') in (fig._grid_str)
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

