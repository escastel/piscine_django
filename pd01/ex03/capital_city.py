import sys

def capital_city(state):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if (states.get(state)):
        key = states.get(state)
        print(capital_cities.get(key))
    else:
        print("Unknown state")

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    capital_city(sys.argv[1])

if __name__ == '__main__':
    main()