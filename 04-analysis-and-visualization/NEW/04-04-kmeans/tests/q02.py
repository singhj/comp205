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
          >>> str(pred_money) == "KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,\n    n_clusters=2, n_init=10, n_jobs=None, precompute_distances='auto',\n    random_state=0, tol=0.0001, verbose=0)"
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> str(money_loc) == '[[111.375       25.25      ]\n [  3.21052632  16.42105263]]'
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

