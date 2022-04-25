from dataclasses import dataclass
import random
import csv

NUM_CUSTOMERS = 100
NUM_ORDERS = 1000

# make customers
def customer():
    '''Generates {NUM_CUSTOMERS} customers with preferences. Can range
    no preference to multiple preferences.'''

    columns = ['customer_id', 'preferences']
    # TODO: read from a preference csv instead
    options = ["dairy-free", "nut-free", "vegetarian", "vegan", "halal", "kosher"]

    with open('data/customer_preference.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for customer_id in range(1, NUM_CUSTOMERS + 1):
            num_preferences = random.choices((range(len(options))), weights=(50,35,10,2,2,1))[0] # random number but weighted
            if num_preferences == 0: preferences = ''
            else: preferences = '"' + ','.join(random.sample(options, num_preferences)) +'"'
            file.write(f'{customer_id},{preferences}\n')

# return an item
def order_item(preferences, weather, timestamp):
    '''Returns a random item that suits the inputs.'''
    
    # read from csv to create item_id :[restrictions] dict
    # TODO: make function for modularity (?)
    with open('data/item_restrictions.csv', 'r') as file:
        data = csv.reader(file)
        next(data) # skip headers
        restrictions = dict()
        for item_id, restriction in data:
            if restriction == '': restrictions[item_id] = list()
            else: restrictions[item_id] = list(restriction.split(','))

    # cross check and remove items that don't suit customer preference
    for preference in preferences:
        for item_id, restriction in restrictions.copy().items():
            if preference not in restriction: del restrictions[item_id]

    # TODO: converting the iterator to a list is a temp band-aid :') 
    # ASSUMES THAT THERES AT LEAST ONE THING AVAILABLE
    item_id = random.choice(list(restrictions.keys()))

    # while True:
        # TODO: make item_type dict while reading file & item_name 
        # TODO: add layers of random weighted choices to create patterns
        # if morning, then coffee = 7 else coffee = 5
        # if sunny then beverage = 7
        # beverages, sides, burger
        # random.choices(item_types, weights=[5,5,5,5...coffee])
        
    # grab item_name and taste_profile 
    with open('data/item.csv', 'r') as file:
        data = csv.reader(file)
        next(data) # skip headers
        for id, name, taste, type in data:
            if id == item_id:
                return(item_id, name, taste) 
    return (-1,-1,-1)

# make orders
def orders():
    '''Generates {NUM_ORDERS} orders with random customers and 
    items that suit their preferences.'''

    columns = ['order_id', 'customer_id', 'order_timestamp', 'weather', 'item_id', 'item_name', 'taste_profile']
    weathers = ['sunny', 'cloudy', 'rainy', 'snowy']

    # TODO: make function for modularity (?)
    # preference dict where customer_id : preference_list
    with open('data/customer_preference.csv', 'r') as file:
        data = csv.reader(file)
        next(data) # skip headers
        preferences = dict()
        for customer_id, pref in data:
            if pref == '': preferences[customer_id] = list()
            else: preferences[customer_id] = list(pref.split(','))

    # generate and write to order_history.csv
    with open('data/order_history.csv', 'w') as file:
        file.write(','.join(columns) + '\n')
        for order_id in range(1, NUM_ORDERS + 1):
            customer_id = str(random.randint(1, NUM_CUSTOMERS))
            timestamp = f'"{random.randint(2015, 2020)}-{random.randint(1, 12)}-{random.randint(1, 28)} {str(random.randint(0, 23)).zfill(2)}:{str(random.randint(0, 59)).zfill(2)}:{str(random.randint(0, 59)).zfill(2)}"'
            weather = random.choice(weathers)
            # TODO: put this in a for loop for random # times so orders have multiple items
            item_id, item_name, taste_profile = order_item(preferences[customer_id], weather, timestamp)
            file.write(f'{order_id},{customer_id},{timestamp},{weather},{item_id},{item_name},{taste_profile}\n')


if __name__ == '__main__':
    customer()
    orders()