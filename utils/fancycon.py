import os
import time

try:
    import tabulate
    from pystyle import *
except:
    os.system("pip -q install pystyle tabulate")
    import tabulate
    from pystyle import *

VALID_COLOR_PRESETS = {
    ######## NORMAL COLORS ######## (normal pystyle colors)
    "red": Colors.StaticMIX((Col.red, Col.red, Col.black)),
    "pink": Colors.StaticMIX((Col.pink, Col.pink, Col.black)),
    "green": Colors.StaticMIX((Col.green, Col.green, Col.black)),
    "blue": Colors.StaticMIX((Col.blue, Col.blue, Col.black)),
    "yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.black)),
    "orange": Colors.StaticMIX((Col.orange, Col.orange, Col.black)),
    "purple": Colors.StaticMIX((Col.purple, Col.purple, Col.black)),
    "cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.black)),
    ######## PASTEL COLORS ######## (kinda like light colors)
    "pastel_red": Colors.StaticMIX((Col.red, Col.red, Col.white, Col.gray)),
    "pastel_pink": Colors.StaticMIX((Col.pink, Col.pink, Col.white, Col.gray)),
    "pastel_green": Colors.StaticMIX((Col.green, Col.green, Col.white, Col.gray)),
    "pastel_blue": Colors.StaticMIX((Col.blue, Col.blue, Col.white, Col.gray)),
    "pastel_yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.white, Col.gray)),
    "pastel_orange": Colors.StaticMIX((Col.orange, Col.orange, Col.white, Col.gray)),
    "pastel_purple": Colors.StaticMIX((Col.purple, Col.purple, Col.white, Col.gray)),
    "pastel_cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.white, Col.gray)),
    ######## NEON COLORS ######## (a little bit more saturated than normal colors)
    "neon_red": Colors.StaticMIX((Col.red, Col.red, Col.red)),
    "neon_pink": Colors.StaticMIX((Col.pink, Col.pink, Col.pink)),
    "neon_green": Colors.StaticMIX((Col.green, Col.green, Col.green)),
    "neon_blue": Colors.StaticMIX((Col.blue, Col.blue, Col.blue)),
    "neon_yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.yellow)),
    "neon_orange": Colors.StaticMIX((Col.orange, Col.orange, Col.orange)),
    "neon_purple": Colors.StaticMIX((Col.purple, Col.purple, Col.purple)),
    "neon_cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.cyan)),
    ######## EXTRA COLORS ######## (extra colors like white, black, gray)
    "white": Colors.StaticMIX((Col.white, Col.white)),
    "black": Colors.StaticMIX((Col.black, Col.black)),
    "gray": Colors.StaticMIX((Col.gray, Col.gray)),
}

RGB_VALID_COLOR_PRESETS = {
    ######## NORMAL COLORS ######## (normal pystyle colors)
    "red": Colors.StaticMIX((Col.red, Col.red, Col.black), _start=False),
    "pink": Colors.StaticMIX((Col.pink, Col.pink, Col.black), _start=False),
    "green": Colors.StaticMIX((Col.green, Col.green, Col.black), _start=False),
    "blue": Colors.StaticMIX((Col.blue, Col.blue, Col.black), _start=False),
    "yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.black), _start=False),
    "orange": Colors.StaticMIX((Col.orange, Col.orange, Col.black), _start=False),
    "purple": Colors.StaticMIX((Col.purple, Col.purple, Col.black), _start=False),
    "cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.black), _start=False),
    ######## PASTEL COLORS ######## (kinda like light colors)
    "pastel_red": Colors.StaticMIX((Col.red, Col.red, Col.white, Col.gray), _start=False),
    "pastel_pink": Colors.StaticMIX((Col.pink, Col.pink, Col.white, Col.gray), _start=False),
    "pastel_green": Colors.StaticMIX((Col.green, Col.green, Col.white, Col.gray), _start=False),
    "pastel_blue": Colors.StaticMIX((Col.blue, Col.blue, Col.white, Col.gray), _start=False),
    "pastel_yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.white, Col.gray), _start=False),
    "pastel_orange": Colors.StaticMIX((Col.orange, Col.orange, Col.white, Col.gray), _start=False),
    "pastel_purple": Colors.StaticMIX((Col.purple, Col.purple, Col.white, Col.gray), _start=False),
    "pastel_cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.white, Col.gray), _start=False),
    ######## NEON COLORS ######## (a little bit more saturated than normal colors)
    "neon_red": Colors.StaticMIX((Col.red, Col.red, Col.red), _start=False),
    "neon_pink": Colors.StaticMIX((Col.pink, Col.pink, Col.pink), _start=False),
    "neon_green": Colors.StaticMIX((Col.green, Col.green, Col.green), _start=False),
    "neon_blue": Colors.StaticMIX((Col.blue, Col.blue, Col.blue), _start=False),
    "neon_yellow": Colors.StaticMIX((Col.yellow, Col.yellow, Col.yellow), _start=False),
    "neon_orange": Colors.StaticMIX((Col.orange, Col.orange, Col.orange), _start=False),
    "neon_purple": Colors.StaticMIX((Col.purple, Col.purple, Col.purple), _start=False),
    "neon_cyan": Colors.StaticMIX((Col.cyan, Col.cyan, Col.cyan), _start=False),
    ######## EXTRA COLORS ######## (extra colors like white, black, gray)
    "white": Colors.StaticMIX((Col.white, Col.white), _start=False),
    "black": Colors.StaticMIX((Col.black, Col.black), _start=False),
    "gray": Colors.StaticMIX((Col.gray, Col.gray), _start=False),
}

VALID_MENUTYPES = [
    "double_outline",
    "rounded_outline",
    "simple_outline",
    "heavy_outline",
]

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

def get_color_config(return_type="variable") -> list:
    
    if all([bool(primaryColor), bool(secondaryColor), bool(terciaryColor), bool(timeColor), bool(dataColor)]) == False:
            raise ValueError("Colors are not set. Please set colors using setcolors() function.")
    
    if return_type.lower() == "variable":
        temp_color_list = [primaryColor, secondaryColor, terciaryColor, timeColor, dataColor, reset]
        
        return temp_color_list
    
    elif return_type.lower() == "hex":
        temp_color_list = [rgb_primaryColor, rgb_secondaryColor, rgb_terciaryColor, rgb_timeColor, rgb_dataColor, rgb_reset]
        
        for color in temp_color_list:
                
            temp_color_list[temp_color_list.index(color)] = '#{:02x}{:02x}{:02x}'.format(int(color[0]), int(color[1]), int(color[2]))
            
        return temp_color_list
    
    elif return_type.lower() == "rgb":
        temp_color_list = [rgb_primaryColor, rgb_secondaryColor, rgb_terciaryColor, rgb_timeColor, rgb_dataColor, rgb_reset]
        
        for color in temp_color_list:
            temp_color_list[temp_color_list.index(color)] = color
                
        return temp_color_list
                
                

class setcolors:
    
    def __init__(self, color_preset:str ="white"):
        global primaryColor, secondaryColor, terciaryColor, timeColor, dataColor, red, green, blue, purple, yellow, orange, reset
        global rgb_primaryColor, rgb_secondaryColor, rgb_terciaryColor, rgb_timeColor, rgb_dataColor, rgb_reset
        
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
        
        rgb_primaryColor = RGB_VALID_COLOR_PRESETS[color_preset].split(";")
        rgb_secondaryColor = Colors.StaticMIX((Col.black, Col.white, VALID_COLOR_PRESETS[color_preset], Col.white), _start=False).split(";")
        rgb_terciaryColor = Colors.StaticMIX((Col.black, Col.black, Col.white, Col.white), _start=False).split(";")
        rgb_timeColor = Colors.StaticMIX((Col.gray, VALID_COLOR_PRESETS[color_preset], Col.gray, VALID_COLOR_PRESETS[color_preset], Col.white), _start=False).split(";")
        rgb_dataColor = Colors.StaticMIX((Col.gray, VALID_COLOR_PRESETS[color_preset], VALID_COLOR_PRESETS[color_preset], Col.black, Col.white), _start=False).split(";")
        rgb_reset = [255, 255, 255]
 
def fancytext(print_type:str, exec_part:str, message:str, showTime:bool=True) -> str:
    if print_type in VALID_PRINT_TYPES:
        print_type = print_type
        exec_part = exec_part
        message = message
    else:
        raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
    
    if all([bool(print_type), bool(exec_part), bool(message)]) == False:
        raise ValueError("Null values are not allowed. Please provide valid values.")
    
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
            return f"{terciaryColor}[{yellow}!{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{yellow}!{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message}{reset}"
    elif print_type == VALID_PRINT_TYPES[3]:
        if showTime:
            return f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {exec_part} {terciaryColor}|{secondaryColor} {message}{reset}"
    elif print_type == VALID_PRINT_TYPES[4]:
        if showTime:
            size = os.get_terminal_size().columns
            dash_amount = int(size) - len(f" New {self.exec_part} Session | [{get_time()}] ")
            dashes = "-" * (dash_amount // 2)
            return f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| [{timeColor}{get_time()}{terciaryColor}] {dashes}{reset}\n"
        else:
            size = os.get_terminal_size().columns
            dash_amount = int(size) - len(f" New {self.exec_part} Session ")
            dashes = "-" * (dash_amount // 2)
            return f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| {dashes}{reset}\n"
    elif print_type == VALID_PRINT_TYPES[5]:
        if showTime:
            return f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}"
        else:
            return f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}"
    else:
        raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")\
            
def normaltext(print_type:str, exec_part:str, message:str, showTime:bool=True) -> str:
    if print_type in VALID_PRINT_TYPES:
        print_type = print_type
        exec_part = exec_part
        message = message
    else:
        raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
    
    if all([bool(print_type), bool(exec_part), bool(message)]) == False:
        raise ValueError("Null values are not allowed. Please provide valid values.")
    
    if print_type == VALID_PRINT_TYPES[0]:
        if showTime:
            return f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {red}ERROR * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
        else:
            return f"{red}ERROR * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
    elif print_type == VALID_PRINT_TYPES[1]:
        if showTime:
            return f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {green}INFO * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
        else:
            return f"{green}INFO * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
    elif print_type == VALID_PRINT_TYPES[2]:
        if showTime:
            return f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {yellow}WARNING * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
        else:
            return f"{yellow}WARNING * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
    elif print_type == VALID_PRINT_TYPES[3]:
        if showTime:
            return f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {blue}DEBUG * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
        else:
            return f"{blue}DEBUG * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
    elif print_type == VALID_PRINT_TYPES[4]:
        if showTime:
            return f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {purple}SESSION * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
        else:
            return f"{purple}SESSION * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
    elif print_type == VALID_PRINT_TYPES[5]:
        if showTime:
            return f"{primaryColor}[{timeColor}{get_time()}{primaryColor}] {orange}CRITICAL * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
        else:
            return f"{orange}CRITICAL * {primaryColor} {exec_part} | {secondaryColor}{message}{reset}"
    else:
        raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")

class menus:
        
        def bar(contents:list, menu_type:str="rounded_outline", center:bool=True):
            
            if menu_type in VALID_MENUTYPES:
                contents_container = []
            else:
                raise ValueError(f"Invalid menu type: {menu_type}, valid types: {VALID_MENUTYPES}")
            
            if all([bool(contents), bool(menu_type)]) == False:
                raise ValueError("Null values are not allowed. Please provide valid values.")
                
            for content in contents:
                contents_container.append(f"{reset}{content}{primaryColor}")
                
            table = tabulate.tabulate([contents_container], tablefmt=menu_type)
            if center:
                space_size = os.get_terminal_size().columns - len(table.split("\n")[0])
                spaces = " " * int(space_size/2)
                
                table = table.replace("\n", f"\n{spaces}")
            else:
                spaces = ""
            
            print(spaces + primaryColor + table + reset + spaces)
        
        def normal(header:list, contents:list, menu_type:str="rounded_outline", center:bool=True):
            
            if menu_type in VALID_MENUTYPES:
                longest_string = len(max(contents, key=len))
                contents_container = []
            else:
                raise ValueError(f"Invalid menu type: {menu_type}, valid types: {VALID_MENUTYPES}")
            
            if all([bool(header), bool(contents), bool(menu_type)]) == False:
                raise ValueError("Null values are not allowed. Please provide valid values.")
            
            for content in contents:
                contents_container.append({f"{reset}{content}{primaryColor}"})
            
            header_spaces = " " * (int((longest_string - len(header[0]))/2))
            header = [f"{header_spaces}{reset}{header[0]}{primaryColor}"]
                
            table = tabulate.tabulate(contents_container, headers=header, tablefmt=menu_type)
            
            if center:
                space_size = os.get_terminal_size().columns - len(table.split("\n")[0])
                spaces = " " * int(space_size/2)
                table = table.replace("\n", f"\n{spaces}")
            else:
                spaces = ""
            
            print(spaces + primaryColor + table + reset)
      
class fancyprint:
    
    def __init__(self, print_type:str, exec_part:str, message:str, showTime:bool=True):
        if print_type in VALID_PRINT_TYPES:
            self.print_type = print_type
            self.exec_part = exec_part
            self.message = message
        else:
            raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
        
        if all([bool(self.print_type), bool(self.exec_part), bool(self.message)]) == False:
            raise ValueError("Null values are not allowed. Please provide valid values.")
        
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
                print(f"{terciaryColor}[{yellow}!{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{yellow}!{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[3]:
            if showTime:
                print(f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{blue}?{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        elif self.print_type == VALID_PRINT_TYPES[4]:
            if showTime:
                size = os.get_terminal_size().columns
                dash_amount = int(size) - len(f" New {self.exec_part} Session | [{get_time()}] ")
                dashes = "-" * (dash_amount // 2)
                print(f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| [{timeColor}{get_time()}{terciaryColor}] {dashes}{reset}\n")
            else:
                size = os.get_terminal_size().columns
                dash_amount = int(size) - len(f" New {self.exec_part} Session ")
                dashes = "-" * (dash_amount // 2)
                print(f"\n{terciaryColor}{dashes} {primaryColor}New {self.exec_part} Session {terciaryColor}| {dashes}{reset}\n")
        elif self.print_type == VALID_PRINT_TYPES[5]:
            if showTime:
                print(f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message} {terciaryColor}- [{timeColor}{get_time()}{terciaryColor}]{reset}")
            else:
                print(f"{terciaryColor}[{orange}x{terciaryColor}]{primaryColor} {self.exec_part} {terciaryColor}|{secondaryColor} {self.message}{reset}")
        else:
            raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
        
class normalprint:
    
    def __init__(self, print_type:str, exec_part:str, message:str, showTime:bool=True):
        if print_type in VALID_PRINT_TYPES:
            self.print_type = print_type
            self.exec_part = exec_part
            self.message = message
        else:
            raise ValueError(f"Invalid print type: {print_type}, valid types: {VALID_PRINT_TYPES}")
        
        if all([bool(self.print_type), bool(self.exec_part), bool(self.message)]) == False:
            raise ValueError("Null values are not allowed. Please provide valid values.")
        
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
        
if __name__ == "__main__":
    print("\n\nThis is a module, not a script!\n\n")
    
    setcolors("pastel_pink")
    
    print("\n\nPrint Types: \n\n")
    
    normalprint("session", "normalprint", "This is a test message", True)
    normalprint("info", "normalprint", "This is a test message", True)
    normalprint("error", "normalprint", "This is a test message", True)
    normalprint("warning", "normalprint", "This is a test message", True)
    normalprint("debug", "normalprint", "This is a test message", True)
    normalprint("critical", "normalprint", "This is a test message", True)
    
    fancyprint("session", "fancyprint", "This is a test message", True)
    fancyprint("info", "fancyprint", "This is a test message", True)
    fancyprint("error", "fancyprint", "This is a test message", True)
    fancyprint("warning", "fancyprint", "This is a test message", True)
    fancyprint("debug", "fancyprint", "This is a test message", True)
    fancyprint("critical", "fancyprint", "This is a test message", True)
    
    print("\n\nMenus: \n\n")
    
    menus.bar(["This is a test message", "This is a test message", "This is a test message"], "rounded_outline", True)
    menus.normal(["Header"], ["This is a test message", "This is a test message", "This is a test message"], "rounded_outline", True)
    
    print("\n\nGet color config: \n\n")
    
    print(f'{get_color_config("variable")} \n')
    print(f'{get_color_config("hex")} \n')
    print(f'{get_color_config("rgb")} \n')
    