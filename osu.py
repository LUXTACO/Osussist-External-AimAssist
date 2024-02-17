import subprocess

try:
    import os
    import cv2
    import json
    import dxcam
    import win32gui
    import win32con
    import win32api
    import keyboard
    import numpy as np
    from fancycon import *
    import asd
except:
    subprocess.run("pip install -r requirements.txt", shell=True)
    import os
    import cv2
    import json
    import dxcam
    import win32gui
    import win32con
    import win32api
    import keyboard
    import numpy as np
    from fancycon import *
    

def title():
    
    System.Clear()
    System.Title("Osussist By: Takkeshi")
    Cursor.HideCursor()
    
    title = """
                 ▄██████▄     ▄████████ ███    █▄     ▄████████    ▄████████  ▄█     ▄████████     ███     
                ███    ███   ███    ███ ███    ███   ███    ███   ███    ███ ███    ███    ███ ▀█████████▄ 
                ███    ███   ███    █▀  ███    ███   ███    █▀    ███    █▀  ███▌   ███    █▀     ▀███▀▀██ 
                ███    ███   ███        ███    ███   ███          ███        ███▌   ███            ███   ▀ 
                ███    ███ ▀███████████ ███    ███ ▀███████████ ▀███████████ ███▌ ▀███████████     ███     
                ███    ███          ███ ███    ███          ███          ███ ███           ███     ███     
                ███    ███    ▄█    ███ ███    ███    ▄█    ███    ▄█    ███ ███     ▄█    ███     ███     
                 ▀██████▀   ▄████████▀  ████████▀   ▄████████▀   ▄████████▀  █▀    ▄████████▀     ▄████▀
                                                
                                                Made By: Takkeshi"""
    
    title = Colorate.Diagonal(Colors.DynamicMIX((VALID_COLOR_PRESETS[config["menu_color"]], VALID_COLOR_PRESETS["neon_" + config["menu_color"]])), title)
    print(title)

def config():
    global config
    try:
        with open(f"{os.getcwd()}\\config.json", "r") as f:
            config = json.load(f)
            return config
    except:
        config = {
            "menu_color": "purple",
            "aim_assist": {
                "min_area": 10,
                "strength": 0.05,
                "range": 200,
                "cursor": [221,50,50],
                "color": [237,3,205]
            },
            "keybinds": {
                "exit": "q"
            }
        }
        
        with open(f"{os.getcwd()}\\config.json", "w") as f:
            json.dump(config, f, indent=4)
        return config
    
def scan_screen(frame, color_obj, color_cursor, min_area):
    
    xy_coords = []
    color_range = np.array([color_obj[0]-25, color_obj[1]-25, color_obj[2]-25]), np.array([color_obj[0]+25, color_obj[1]+25, color_obj[2]+25])
    cursor_range = np.array([color_cursor[0]-8, color_cursor[1]-8, color_cursor[2]-8]), np.array([color_cursor[0]+8, color_cursor[1]+8, color_cursor[2]+8])
    objectives = cv2.inRange(frame, color_range[0], color_range[1])
    cursor = cv2.inRange(frame, cursor_range[0], cursor_range[1])
    contours, _ = cv2.findContours(objectives, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(cursor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w//2
            center_y = y + h//2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            normalprint("info", "scan_screen", f"Objective at X: {center_x} Y: {center_y}")
            
            xy_coords.append((center_x, center_y))
    
    for contour in contours2:
        area = cv2.contourArea(contour)
        if area > min_area:
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w//2
            center_y = y + h//2
            cv2.circle(frame, (center_x, center_y), 10, (255, 255, 255), -1)
            normalprint("info", "scan_screen", f"Cursor at X: {center_x} Y: {center_y}")
     
    try:       
        if center_x and center_y != None:
            cursor_coords = (center_x, center_y)
        else:
            cursor_coords = win32gui.GetCursorPos()
    except:
        cursor_coords = win32gui.GetCursorPos()
            
    return xy_coords, cursor_coords, objectives, cursor

def get_move(coord_list, cursor_coords, strength):

    if len(coord_list) == 0:
        return
    
    closest_coord = None
    closest_coord_distance = None
    for coord in coord_list:
        distance = np.sqrt((coord[0] - cursor_coords[0])**2 + (coord[1] - cursor_coords[1])**2)
        if closest_coord_distance == None:
            closest_coord_distance = distance
            closest_coord = coord
        elif distance < closest_coord_distance:
            closest_coord_distance = distance
            closest_coord = coord
            
    if closest_coord != None:
        x_diff = round((closest_coord[0] - cursor_coords[0]) * strength)
        y_diff = round((closest_coord[1] - cursor_coords[1]) * strength)
        normalprint("info", "get_move", f"X diff: {x_diff} Y diff: {y_diff}")
        
        if np.sqrt((closest_coord[0] - cursor_coords[0])**2 + (closest_coord[1] - cursor_coords[1])**2) <= int(aim_assist["range"]):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x_diff, y_diff, 0, 0)
            normalprint("warning", "get_move", f"Moving mouse to: {closest_coord[0]}, {closest_coord[1]}")
        else:
            normalprint("error", "get_move", f"Target too far away: {closest_coord[0]}, {closest_coord[1]}")
    
    
if __name__ == "__main__":
    config = config()
    keybinds = config["keybinds"]
    aim_assist = config["aim_assist"]
    setcolors(config["menu_color"])
    title()
    camera = dxcam.create()
    camera.start(target_fps=140)

    while True:
        frame = camera.get_latest_frame()
        xy_coords, cursor_coords, objectives, cursor = scan_screen(frame, aim_assist["color"], aim_assist["cursor"], aim_assist["min_area"])
        #cv2.imshow('frame', cv2.resize(frame, (500, 300)))
        get_move(xy_coords, cursor_coords, aim_assist["strength"])

        if (cv2.waitKey(1) & 0xFF == ord(keybinds['exit'])) or keyboard.is_pressed(keybinds['exit']):
            cv2.destroyAllWindows()
            exit()
            
        xy_coords.clear()