# User Login
print('Welcome to the Demo Marketplace!')
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
    exit()
    
# Load Program
cart = []
catalog = { 
           'Boots': ['Classic Riding', 'Chelsea', 'Cowbody', 'Edgy', 'Rain', 'Heeled', 'Knee High'],
           'Coats': ['Trench', 'Fur', 'Peacoat', 'Raincoat', 'Leather', 'Parka'],
           'Jackets' : ['Puffer', 'Blazer', 'Down', 'Fleece', 'Leather'],
           'Caps': ['Baseball', 'Beanie', 'Fedora', 'Trucker', 'Bowler']
           }

if user_type == 'customer':
    while True:
        option = input('Please choose an option (1-6): 1. See Catalog 2. See Cart 3. Add Item 4. Update Item 5. Remove Item 5. Pay 6. Logout: ')
        
        if option == '1':
            print('Here is the catalog of available items: \n')
            for cat in catalog:
                print( ' \n' + cat + ':')
                for item in catalog[cat]:
                    print(item)
                    
        if option == '2':
            print(cart)
        
        if option == '3':
            item_name = input('Please type the name of the item you would like to add to your cart:')
            cart.append(item_name)
            
        if option == '4':
            item_name = input('Please type the name of the item you would like to remove from your cart:')
            cart.remove(item_name)
                
        if option == '5':
            input('How would you like to pay? 1. Net Banking 2. Credit Card 3. Debit Card 4. Paypal')
            print('Your order is successfully placed. You will be shortly redirected to the payment portal. Thank you for shopping with us!')
            cart = []
                    
        if option == '6':
            print('Logging Out...')
            break

if user_type == 'admin':
    
    while True:
        option = input('Please choose an option (1-6): 1. See Catalog 2. Add Product 3. Remove Product 4. Update Product 5. Add Category 6. Remove Category 7. Logout: ')
        
        if option == '1':
            print('Here is the catalog of available items: \n')
            for cat in catalog:
                print(' \n' + cat + ':')
                for item in catalog[cat]:
                    print(item)
                    
        if option == '2':
            print('Available Categories:')
            for cat in catalog:
                print(cat)
                
            prod_cat = input('Please enter which category you would like to add your product to: ')
            prod_name = input('Please type the name of the product that you would like to add:')
            
            if prod_cat in catalog:
                catalog[prod_cat].append(prod_name)
            else: 
                catalog[prod_cat] = [prod_name]
        
        if option == '3':
            prod_cat = input('Please enter the name of the category you would like to remove from:')
            prod_name = input('Please enter the name of the product you would like to remove:')

            if prod_cat in catalog and prod_name in catalog[prod_cat]:
                catalog[prod_cat].remove(prod_name)
            else:
                print('Category or Product3 not found.')

        if option == '4':
            prod_cat = input('Please enter the name of the category you would like to update: ')
            old_prod = input('Please enter the name of the product you would like to replace:')
            new_prod = input('Please enter the name of the new product:')
            for i in range(len(catalog[prod_cat])):
                if catalog[prod_cat][i] == old_prod:
                    catalog[prod_cat][i] = new_prod
            
        if option == '5':
            cat_name = input('Please enter the name of the new category that you would like to add:')
            if cat_name not in catalog:
                catalog[cat_name] = []
            
        if option == '6':
            cat_name = input('Please enter the name of the category that you would like to remove:')
            if cat_name in catalog:
                del catalog[cat_name]
                
        if option == '7':
            print('Logging Out...')
            break



