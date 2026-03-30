#!/usr/bin/python3

def generate_html(elements):
    periods = organize_by_period(elements)
    
    html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla Periódica de Elementos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        table {
            border-collapse: collapse;
            margin: 20px auto;
            background-color: transparent;
        }
        td {
            width: 100px;
            height: 120px;
            padding: 10px;
            text-align: center;
            vertical-align: top;
        }
        h4 {
            margin: 3px 0;
            font-size: 16px;
        }
        ul {
            margin: 3px 0;
            padding-left: 13px;
            font-size: 14px;
            list-style-type: none;
        }
        li {
            margin: 1px 0;
        }
    </style>
</head>
<body>
    <h1>Periodic Table of the Elements</h1>
    <table>
"""
    
    for period in sorted(periods.keys()):
        html += "        <tr>\n"
        for pos in range(18):
            if pos in periods[period]:
                elem = periods[period][pos]
                color = get_element_color(elem['number'])
                html += f"""            <td style="border: 1px solid black; background-color: {color}">
                <h4>{elem['name']}</h4>
                <ul>
                    <li>No {elem['number']}</li>
                    <li>{elem['small']}</li>
                    <li>{elem['molar']}</li>
                    <li>{elem['electron']} electron</li>
                </ul>
            </td>
"""
            else:
                html += '            <td style="border: none;"></td>\n'
        html += "        </tr>\n"
    
    html += """    </table>
</body>
</html>
"""
    return html

def get_element_color(number):
    number = int(number)

    if number in [2, 10, 18, 36, 54, 86, 118]:
        return "#91dfff"
    
    if number in [9, 17, 35, 53, 85, 117]:
        return "#F991FF"
    
    if number in [1, 6, 7, 8, 15, 16, 34]:
        return "#AB91FF"
    
    if number in [5, 14, 32, 33, 51, 52, 84]:
        return "#92FF9F"
    
    if number in [13, 31, 49, 50, 58, 81, 82, 83, 113, 114, 115, 116]:
        return "#FFF991"
    
    if ((21 <= number <= 30) or (39 <= number <= 48) or (71 <= number <= 80) or (103 <= number <= 112)):
        return "#ECFF91"
    
    if number in [4, 12, 20, 38, 56, 88]:
        return "#FFDF91"
    
    if number in [3, 11, 19, 37, 55, 87]:
        return "#FFC591"

    return "#FFFFFF"


def organize_by_period(elements):
    periods = {}
    
    for elem in elements:
        number = int(elem['number'])
        
        if number <= 2:
            period = 1
        elif number <= 10:
            period = 2
        elif number <= 18:
            period = 3
        elif number <= 36:
            period = 4
        elif number <= 54:
            period = 5
        elif number <= 86:
            period = 6
        else:
            period = 7
        
        if period not in periods:
            periods[period] = {}
        
        position = int(elem['position'])
        periods[period][position] = elem
    
    return periods

def write_html_file(html):
    try:
        with open("periodic_table.html", 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Archivo periodic_table.html generado exitosamente")
    except Exception as e:
        print(f"Error escribiendo archivo: {e}")

def read_periodic_table(filename):
    elements = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(' = ')
                name = parts[0]
                attrs = {}
                for attr in parts[1].split(', '):
                    key, value = attr.split(':')
                    attrs[key.strip()] = value.strip()
                attrs['name'] = name
                elements.append(attrs)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    return elements

def periodic_table():
    elements = read_periodic_table('periodic_table.txt')
    if elements is None:
        return
    
    html = generate_html(elements)
    write_html_file(html)

if __name__ == '__main__':
    periodic_table()
