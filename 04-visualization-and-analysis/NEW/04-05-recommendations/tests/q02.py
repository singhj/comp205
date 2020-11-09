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
          >>> 'Mike' in friend_recommendation(1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(friend_recommendation(1))
          <class 'str'>
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

