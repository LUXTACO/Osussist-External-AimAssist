import os
import time
from pystyle import *

VALID_COLOR_PRESETS = {
    ######## NORMAL COLORS ######## (normal pystyle colors)
    "red": Colors.StaticMIX((Col.red, Col.red, Col.black)),
    "green": Colors.StaticMIX((Col.green, Col.green, Col.black)),
    "blue": Colors.StaticMIX((Col.blue, Col.blue, Col.black)),
    "yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.black)),
    "orange": Colors.StaticMIX((Col.orange, Col.orange, Col.black)),
    "purple": Colors.StaticMIX((Col.purple, Col.purple, Col.black)),
    "cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.black)),
    ######## PASTEL COLORS ######## (kinda like light colors)
    "pastel_red": Colors.StaticMIX((Col.red, Col.red, Col.white, Col.gray)),
    "pastel_green": Colors.StaticMIX((Col.green, Col.green, Col.white, Col.gray)),
    "pastel_blue": Colors.StaticMIX((Col.blue, Col.blue, Col.white, Col.gray)),
    "pastel_yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.white, Col.gray)),
    "pastel_orange": Colors.StaticMIX((Col.orange, Col.orange, Col.white, Col.gray)),
    "pastel_purple": Colors.StaticMIX((Col.purple, Col.purple, Col.white, Col.gray)),
    "pastel_cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.white, Col.gray)),
    ######## NEON COLORS ######## (a little bit more saturated than normal colors)
    "neon_red": Colors.StaticMIX((Col.red, Col.red, Col.red)),
    "neon_green": Colors.StaticMIX((Col.green, Col.green, Col.green)),
    "neon_blue": Colors.StaticMIX((Col.blue, Col.blue, Col.blue)),
    "neon_yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.yellow)),
    "neon_orange": Colors.StaticMIX((Col.orange, Col.orange, Col.orange)),
    "neon_purple": Colors.StaticMIX((Col.purple, Col.purple, Col.purple)),
    "neon_cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.cyan)),
}

VALID_PRINT_TYPES = [
    "error",
    "info",
    "warning",
    "debug",
    "session",
    "critical",
]

def get_time():
    return time.strftime("%H:%M:%S")

class setcolors:
    
    def __init__(self, color_preset):
        global primaryColor, secondaryColor, terciaryColor, timeColor, dataColor, red, green, blue, purple, yellow, orange, reset
        
        if color_preset in VALID_COLOR_PRESETS:
            self.color_preset = VALID_COLOR_PRESETS[color_preset]
        else:
            raise ValueError(f"Invalid color preset: {color_preset}, valid presets: {VALID_COLOR_PRESETS.items}")
        
        primaryColor = VALID_COLOR_PRESETS[color_preset]
        secondaryColor = Colors.StaticMIX((Col.black, Col.white, VALID_COLOR_PRESETS[color_preset], Col.white))
        terciaryColor = Colors.StaticMIX((Col.black, Col.black, Col.white, Col.white))
        timeColor = Colors.StaticMIX((Col.gray, VALID_COLOR_PRESETS[color_preset], Col.gray, VALID_COLOR_PRESETS[color_preset], Col.white))
        dataColor = Colors.StaticMIX((Col.gray, VALID_COLOR_PRESETS[color_preset], VALID_COLOR_PRESETS[color_preset], Col.black, Col.white))
        red = Colors.StaticMIX((Col.red, Col.red, Col.white, Col.white))
        green = Colors.StaticMIX((Col.green, Col.green, Col.white, Col.white))
        blue = Colors.StaticMIX((Col.blue, Col.blue, Col.white, Col.white))
        purple = Colors.StaticMIX((Col.purple, Col.purple, Col.white, Col.white))
        yellow = Colors.StaticMIX((Col.yellow, Col.yellow, Col.white, Col.white))
        orange = Colors.StaticMIX((Col.orange, Col.orange, Col.white, Col.white))
        reset = Colors.reset
 
def fancytext(print_type, exec_part, message, showTime=True):
    if print_type in VALID_PRINT_TYPES:
        print_type = print_type
        exec_part = exec_part
        message = message
    else:
        raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
    
    if print_type == VALID_PRINT_TYPES[0]:
        if showTime:
            return f"{terciaryColor}[{red}-{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{red}-{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message}{reset}"
    elif print_type == VALID_PRINT_TYPES[1]:
        if showTime:
            return f"{terciaryColor}[{green}+{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{green}+{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message}{reset}"
    elif print_type == VALID_PRINT_TYPES[2]:
        if showTime:
            return f"{terciaryColor}[{orange}!{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{orange}!{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message}{reset}"
    elif print_type == VALID_PRINT_TYPES[3]:
        if showTime:
            return f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message}{reset}"
    elif print_type == VALID_PRINT_TYPES[4]:
        if showTime:
            size = os.get_terminal_size().columns
            dash_amount = int(size) - len(f" New {self.exec_part} Session | [{get_time()}] ")
            dashes = "-" * dash_amount/2
            return f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| [{timeColor}{get_time()}{terciaryColor}] {dashes}{reset}\n"
        else:
            size = os.get_terminal_size().columns
            dash_amount = int(size) - len(f" New {self.exec_part} Session ")
            dashes = "-" * dash_amount/2
            return f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| {dashes}{reset}\n"
    elif print_type == VALID_PRINT_TYPES[5]:
        if showTime:
            return f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}"
    else:
        raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
        
class fancyprint:
    
    def __init__(self, print_type, exec_part, message, showTime=True):
        if print_type in VALID_PRINT_TYPES:
            self.print_type = print_type
            self.exec_part = exec_part
            self.message = message
        else:
            raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
        
        if self.print_type == VALID_PRINT_TYPES[0]:
            if showTime:
                print(f"{terciaryColor}[{red}-{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{red}-{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[1]:
            if showTime:
                print(f"{terciaryColor}[{green}+{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{green}+{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[2]:
            if showTime:
                print(f"{terciaryColor}[{orange}!{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{orange}!{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[3]:
            if showTime:
                print(f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[4]:
            if showTime:
                size = os.get_terminal_size().columns
                dash_amount = int(size) - len(f" New {self.exec_part} Session | [{get_time()}] ")
                dashes = "-" * dash_amount/2
                print(f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| [{timeColor}{get_time()}{terciaryColor}] {dashes}{reset}\n")
            else:
                size = os.get_terminal_size().columns
                dash_amount = int(size) - len(f" New {self.exec_part} Session ")
                dashes = "-" * dash_amount/2
                print(f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| {dashes}{reset}\n")
        elif self.print_type == VALID_PRINT_TYPES[5]:
            if showTime:
                print(f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        else:
            raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
        
class normalprint:
    
    def __init__(self, print_type, exec_part, message, showTime=True):
        if print_type in VALID_PRINT_TYPES:
            self.print_type = print_type
            self.exec_part = exec_part
            self.message = message
        else:
            raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
        
        if self.print_type == VALID_PRINT_TYPES[0]:
            if showTime:
                print(f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {red}ERROR * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
            else:
                print(f"{red}ERROR * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[1]:
            if showTime:
                print(f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {green}INFO * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
            else:
                print(f"{green}INFO * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[2]:
            if showTime:
                print(f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {yellow}WARNING * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
            else:
                print(f"{yellow}WARNING * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[3]:
            if showTime:
                print(f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {blue}DEBUG * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
            else:
                print(f"{blue}DEBUG * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[4]:
            if showTime:
                print(f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {purple}SESSION * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
            else:
                print(f"{purple}SESSION * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[5]:
            if showTime:
                print(f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {orange}CRITICAL * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
            else:
                print(f"{orange}CRITICAL * {primaryColor} {self.exec_part} | {secondaryColor}{self.message}{reset}")
        else:
            raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")