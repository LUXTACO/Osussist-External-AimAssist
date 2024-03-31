import utils.setup as setup

try:
    import pyMeow as pm
    import utils.gui as gui
    from utils.fancycon import *
    import utils.linker as linker
    
    import os
    import cv2
    import json
    import dxcam
    import win32gui
    import win32con
    import win32api
    import keyboard
    import threading
    import numba as nb
    import numpy as np
    from queue import Queue
    from threading import Thread
except:
    setup.installdeps()
    
    import utils.gui as gui
    import utils.pyMeow as pm
    from utils.fancycon import *
    import utils.linker as linker
    
    import os
    import cv2
    import json
    import dxcam
    import win32gui
    import win32con
    import win32api
    import keyboard
    import threading
    import numba as nb
    import numpy as np
    from queue import Queue
    from threading import Thread

VERSION = "2.0.0"
CONFIG_FOLDER = f"{os.getcwd()}\\configs"
CONFIG_FILE = f"{CONFIG_FOLDER}\\default.json"
LINKER_INSTANCE = linker.Config(file_path=CONFIG_FILE, config_folder=CONFIG_FOLDER)

def info_thread():
    global aim_settings, visuals_settings, detection_settings
    
    while True:
        aim_settings, visuals_settings, detection_settings = queue.get()
    
class osu:
    
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
                x, y, w, h = cv2.boundingRect(contour)
                center_x = x + w//2
                center_y = y + h//2
                normalprint("info", "scan_screen", f"Objective at X: {center_x} Y: {center_y}")
                
                xy_coords.append((center_x, center_y))
        
        for contour in contours2:
            area = cv2.contourArea(contour)
            if area > min_area:
                x, y, w, h = cv2.boundingRect(contour)
                center_x = x + w//2
                center_y = y + h//2
                normalprint("info", "scan_screen", f"Cursor at X: {center_x} Y: {center_y}")
        
        try:       
            if center_x and center_y != None:
                cursor_coords = (center_x, center_y)
            else:
                cursor_coords = win32gui.GetCursorPos()
        except:
            cursor_coords = win32gui.GetCursorPos()
                
        return xy_coords, cursor_coords, objectives, cursor
    
class cpu:
    
    def get_move(coord_list, cursor_coords, strength, rangeVar):

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
            
            if np.sqrt((closest_coord[0] - cursor_coords[0])**2 + (closest_coord[1] - cursor_coords[1])**2) <= int(rangeVar):
                normalprint("warning", "get_move", f"Moving mouse to: {closest_coord[0]}, {closest_coord[1]}")
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x_diff, y_diff, 0, 0)
            else:
                normalprint("error", "get_move", f"Target too far away: {closest_coord[0]}, {closest_coord[1]}")
                pass

class gpu:
    
    @nb.jit(parallel=True, fastmath=True)
    def get_move(coord_list, cursor_coords, strength, rangeVar):

        try:
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
                
                if np.sqrt((closest_coord[0] - cursor_coords[0])**2 + (closest_coord[1] - cursor_coords[1])**2) <= int(rangeVar):
                    return x_diff, y_diff
                    normalprint("warning", "get_move", f"Moving mouse to: {closest_coord[0]}, {closest_coord[1]}")
                else:
                    normalprint("error", "get_move", f"Target too far away: {closest_coord[0]}, {closest_coord[1]}")
                    pass
        except:
            pass

if __name__ == "__main__":
    queue = Queue()
    
    gui_thread = threading.Thread(target=gui.Spawn, args=(LINKER_INSTANCE, VERSION, queue))
    gui_thread.start()
    
    camera = dxcam.create()
    camera.start(target_fps=140)
    
    setcolors("pastel_pink")
    
    value_thread = threading.Thread(target=info_thread)
    value_thread.start()
    
    if aim_settings["compute"] == "gpu":
        normalprint("warning", "main", "Using GPU acceleration for aim assist, not fully tested!")
        time.sleep(5)
    
    while True:
        
        gui_focus = gui.is_in_focus()
        
        frame = camera.get_latest_frame()   
            
        if aim_settings["enabled"]:
            if not gui_focus:
                xy_coords, cursor_coords, objectives, cursor = osu.scan_screen(frame, detection_settings["hitcircle"], detection_settings["cursor"], aim_settings["min_area"])
                
                if aim_settings["compute"] == "gpu":
                    x_diff, y_diff = gpu.get_move(xy_coords, cursor_coords, aim_settings["strength"], aim_settings["range"])
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x_diff, y_diff, 0, 0)
                else:
                    cpu.get_move(xy_coords, cursor_coords, aim_settings["strength"], aim_settings["range"])