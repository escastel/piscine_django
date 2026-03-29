import sys

def state(capital):
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
    
    value_state = ""
    for key, value in capital_cities.items():
        if value == capital:
            value_state = key

    if not value_state:
       print("Unknown capital city")
       sys.exit(1)

    for key, value in states.items():
        if value == value_state:
            print(key)

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    state(sys.argv[1])

if __name__ == '__main__':
    main()