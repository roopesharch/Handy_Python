def get_color(clr):
    if clr == 'BLACK':
        return '\033[30m'
    elif clr == 'RED':
        return '\033[31m'
    elif clr == 'GREEN':
        return '\033[32m'
    elif clr == 'YELLOW':
        return '\033[33m'
    elif clr == 'BLUE':
        return '\033[34m'
    elif clr == 'MAGENTA':
        return '\033[35m'
    elif clr == 'CYAN':
        return '\033[36m'
    elif clr == 'UNDERLINE':
        return '\033[4m'
    elif clr == 'RESETUNDERLINE':
        return "\033[24m"
    elif clr == 'BLINK':
        return "\033[5m"
    elif clr == 'RESETBOLD':
        return "\033[21m"
    elif clr == 'BOLD':
        return "\033[1m"
    elif clr == 'WHITE':
        return "\033[97m"
    else:
        return '\033[0m'  # reset all

message = 'Yes i am coloured text'
colr = 'RED'
print(get_color(colr) + message)
