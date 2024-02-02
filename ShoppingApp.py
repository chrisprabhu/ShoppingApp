users = [{
        'name': 'chris',
        'type': 'admin'
    },
    {
        'name': 'sarah',
        'type': 'customer'
    }]

user_name = input('Please enter username: ')
user_type = ''

for user in users:
    if user['name'] == user_name:
        user_type = user['type']
        print('found user: ' + user_name + ' of type: ' + user_type)
        break

if not user_type:
    print('user not found')
    exit()


