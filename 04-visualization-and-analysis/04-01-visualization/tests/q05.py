#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> "'coloraxis': 'coloraxis'" in str(ir._data_objs)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> "'hovertemplate': 'sepal_width=%{x}<br>sepal_length=%{marker.color}'" in str(ir._data_objs)
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

