schemas = {
    'User': {
      'type': 'object',
      'properties': {
        'id': {
            'type': 'string',
            'description': 'User\'s id in database',
            'default': '655d758-47325'
        },
        'email': {
          'type': 'string',
          'description': 'User\'s email',
          'default': 'mail@example.com'
        },
        'username': {
            'type': 'string',
            'description': 'User\'s username name',
            'default': 'anton'
        }
      }
    },
    'UserInput': {
        'type': 'object',
        'properties': {
            'email': {
                'type': 'string',
                'description': 'User\'s email',
                'default': 'mail@example.com'
            },
            'username': {
                'type': 'string',
                'description': 'User\'s username name',
                'default': 'anton'
            },
            'password': {
                'type': 'string',
                'description': 'User\'s password',
                'default': 'Sfdfdf45!'
            }
        }
    },
}
