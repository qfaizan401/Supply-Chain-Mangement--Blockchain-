def create_timestamp ():
    import datetime
    timestamp = datetime.datetime.now() .strftime('%Y-%m-%d  %H:%M:%S')
    return timestamp

def current_transection ():
    user_input = {}
    user_input['timestamp'] = create_timestamp()
    user_input['product_id'] = int(input('Enter Product ID:\n'))
    user_input['product_serial'] = input('Enter Product Serial:\n')
    user_input['from'] = input('From:\n')
    user_input['to'] = input('To:\n')
    user_input['massage'] = input('Type your massage:\n')
    user_input['Flag'] = input('T: Ture\nF: False\n')
    return user_input

def create_block (stage_input, product_id):
    with open(product_id,'w') as f:
        f.write(f'Block_Created [{create_timestamp()}]')
        f.write('\n')
        f.write(str(stage_input))
    return

def manufacturer ():
    manufacturer_id = input('Enter your ID:')
    manufacturer_password = input('Enter your Password:')
    if manufacturer_id == 'demo_manufacturer' and manufacturer_password == 'demo_manufacturer':
        print('Initialized Chain...\nInitialized Ledger...')
        manufacturer_input = current_transection()
        create_block(manufacturer_input, product_id=manufacturer_input['product_id'])
        print(manufacturer_input)
    else:
        print('Login Incorrect')
    return

print('1: Manufacturer\n2: Tranportation\n3: Retailer')
user_profile = int(input("Select your profile\n"))

def profile_selector (user_profile):
    if user_profile == 1:
        return manufacturer()
    elif user_profile == 2:
        return tranportation()
    elif user_profile == 3:
        return retailer()

profile_selector(user_profile)