""" # User Login
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
            print('Welcome ' + user_name + '!')
            break
        else:
            print('Incorrect Password. Exiting.')
            exit()

if not user_type:
    print('user not found')
    exit() """
    
# Load Program
cart = []
catalog = { 
           'Boots': ['Classic Riding', 'Chelsea', 'Cowbody', 'Edgy', 'Rain', 'Heeled', 'Knee High'],
           'Coats:': ['Trench', 'Fur', 'Peacoat', 'Raincoat', 'Leather', 'Parka'],
           'Jackets' : ['Puffer', 'Blazer', 'Down', 'Fleece', 'Leather'],
           'Caps': ['Baseball', 'Beanie', 'Fedora', 'Trucker', 'Bowler']
           }

while True:
    option = input('Please choose an option: catalog, cart, add, remove, pay, logout: ')
    
    if option == 'catalog':
        print('')
        for cat in catalog:
            print(cat + ': ')
            for item in catalog[cat]:
                print(item)
            print('')
    
    



