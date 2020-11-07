#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> "<plotly.validators.FramesValidator object" in str(f._frames_validator) 
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> f.layout.hovermode
          'closest'
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

