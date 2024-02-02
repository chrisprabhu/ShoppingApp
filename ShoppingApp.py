users = {
        'chris': {
            'type': 'admin',
            'password': 'chris'
        },       
        'sarah' : {        
            'type': 'customer',
            'password': 'sarah'
        }
        }

user_name = input('Please enter username: ')
user_type = ''

for user in users:
    if user_name in users:
        user_type = users[user_name]['type']
        print('found user: ' + user_name + ' of type: ' + user_type)
        user_password = input('Enter password:')
        
        if users[user_name]['password'] == user_password:
            print('Welcome!')
            break
        else:
            print('Incorrect Password. Exiting.')
            exit()

if not user_type:
    print('user not found')
    exit()
    
    



