available_currencies = {
    'USD': {'rate': 1, 'name' : 'United States Dolloar'},
    'PHP': {'rate': 55.80, 'name' : 'Philippine Peso'},
    'SGD': {'rate': 1.35, 'name' : 'Singapore Dollar'},
    'EUR': {'rate': 0.92, 'name' : 'Euro'}
}

def get_currencies():
    for currency_code, currency_info in available_currencies.items():
        name = currency_info.get('name')
        print(f"{currency_code} - {name}")

def get_source_currency():
    while True:
        source_currency = input("Enter the source currency: ").upper()
        if source_currency not in available_currencies:
            print("Invalid source currency! (ex.SGD)")
        else:
            break  
    return source_currency

def get_target_currency():
    while True:        
        target_currency = input("Enter the target currency: ").upper()
        if target_currency not in available_currencies:
            print("Invalid target currency! (ex.SGD)")
        else:
            break  
    return target_currency

def convert_currency(source_currency, target_currency):       
    while True:
        amount_str = input("Enter the amount to convert: ")
        # Check if the input is a positive number
        if amount_str.replace('.', '').isdigit() and amount_str.count('.') <= 1:
            amount = float(amount_str)
            if amount >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        else:
            print("Invalid input. Please enter a valid number.")
        
    rate_from = float(available_currencies[source_currency]['rate'])
    rate_to = float(available_currencies[target_currency]['rate'])

    converted_amount = (amount / rate_from) * rate_to
    print(f"{amount} {source_currency} = {converted_amount:.2f} {target_currency}")

get_currencies()
source_currency = get_source_currency()
target_currency = get_target_currency()
convert_currency(source_currency, target_currency)