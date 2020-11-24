test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> predicted_targets.shape
          (20,)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(predicted_targets)
          <class 'numpy.ndarray'>
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
