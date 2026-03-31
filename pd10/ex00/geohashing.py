import antigravity as a
import sys

def parse_date(year, month, day):
    if month < 1 or month > 12 or day < 1:
        return False
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29

    return day <= month_days[month - 1]

def parse_float():
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except ValueError:
       print(f"\033[31mError: the first arguments must be of type float.\033[0m")
       sys.exit(1)

    return latitude, longitude

def parse_int(dtdw):
    try:
        year = int(dtdw[0])
        month = int(dtdw[1])
        day = int(dtdw[2])
    except Exception:
        print(f"\033[31mError: the third argument has no format YYYY-MM-DD-DOW.\033[0m")
        sys.exit(1)

    return year, month, day

def parse():
    latitude, longitude = parse_float()
    
    dtdw = sys.argv[3].split("-")
    if len(dtdw) != 4 or len(dtdw[0]) != 4 or len(dtdw[1]) != 2 or len(dtdw[2]) != 2:
        print(f"\033[31mError: the third argument has no format YYYY-MM-DD-DOW.\033[0m")
        sys.exit(1)
    
    year, month, day = parse_int(dtdw)
    if not parse_date(year, month, day):
        print(f"\033[31mError: the third argument has no format YYYY-MM-DD-DOW.\033[0m")
        sys.exit(1)

    try:
        float(dtdw[3])
    except ValueError:
       print(f"\033[31mError: the third argument has no format YYYY-MM-DD-DOW.\033[0m")
       sys.exit(1)
    
    datedow = "-".join(dtdw).encode()
    return latitude, longitude, datedow



def main():
    if len(sys.argv) != 4:
        print("\033[31mError: invalid number of arguments.\033[0m")
        sys.exit(1)

    latitude, longitude, datedow = parse()
    a.geohash(latitude, longitude, datedow)

if __name__ == '__main__':
    main()