import sys

def get_dicts():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    return states, capital_cities

def capital_city(state):
    states, capital_cities = get_dicts()

    capital = ""
    if (states.get(state)):
        key = states.get(state)
        capital = capital_cities.get(key)

    return capital
    
def rev_capital_city(capital):
    states, capital_cities = get_dicts()
    
    value_state = ""
    for key, value in capital_cities.items():
        if value == capital:
            value_state = key

    state = ""
    for key, value in states.items():
        if value == value_state:
           state = key

    return state

def all_in(str):    
    if ",," in str:
        sys.exit(1)
    
    expressions = []
    for s in str.split(","):
        if s.strip():
            expressions.append(s.strip())

    for e in expressions:
        if capital_city(e.title()):
            print (capital_city(e.title()), "is the capital of", e.title())
        elif rev_capital_city(e.title()):
            print (e.title(), "is the capital of", rev_capital_city(e.title()))
        else:
            print(e, "is neither a capital city nor a state")

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    all_in(sys.argv[1])

if __name__ == '__main__':
    main()