import os
import json
import win32gui
import threading

try:
    from tkinter import *
    from queue import Queue
    import customtkinter as ctk
    from threading import Thread
    from tkinter import messagebox
    from PIL import ImageTk, Image
except:
    setup.installdeps()
    from tkinter import *
    from queue import Queue
    import customtkinter as ctk
    from threading import Thread
    from tkinter import messagebox
    from PIL import ImageTk, Image
    

ASSET_PATH = f"..\\assets" if not os.path.exists(f"{os.getcwd()}\\assets") else f"{os.getcwd()}\\assets"

IMAGE_LIST = {
    "logo": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "logo.png")), size=(80, 80)),
    "aim_tab": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "aim_tab.png")), size=(20, 20)),
    "visuals_tab": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "visuals_tab.png")), size=(20, 20)),
    "spoofer_tab": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "spoofer_tab.png")), size=(20, 20)),
    "config_tab": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "config_tab.png")), size=(20, 20)),
    "support_tab": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "support_tab.png")), size=(20, 20)),
    "unknowncheats": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "unknowncheats.png")), size=(32, 32)),
    "discord": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "discord.png")), size=(32, 32)),
    "github": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "github.png")), size=(32, 32)),
    "youtube": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "youtube.png")), size=(32, 32)),
}

CREDITS_ASSETS = {
    "takkeshi": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "takkeshi.png")), size=(32, 32)),
    "nian": ctk.CTkImage(Image.open(os.path.join(ASSET_PATH, "nian.png")), size=(32, 32)),
}	

CREDITS_LINKS = {
    "takkeshi": "https://www.youtube.com/@takkeshi_dev",
    "nian": "https://www.youtube.com/@o2nian93"
}

SUPPORT_LINKS = {
    "discord": "https://discord.gg/invite",
    "unknowncheats": "https://www.unknowncheats.me/forum/other-games/623903-osussit-external-aimassist-osu.html#post3995987",
    "github": "https://github.com/LUXTACO/Osussist-External-AimAssist",
    "youtube": "https://www.youtube.com/@takkeshi_dev",
}

TEXT_STYLE = {
    "Bold17": ("Comfortaa", 17, "bold"),
    "Bold16": ("Comfortaa", 16, "bold"),
    "Normal16": ("Comfortaa", 16),
    "Normal15": ("Comfortaa", 15),
    "Normal14": ("Comfortaa", 14),
    "Normal12": ("Comfortaa", 12),
    "Normal10": ("Comfortaa", 10),
}

def alert(title: str, message: str):
    return messagebox.showinfo(title, message)

def webbrowser(url: str):
    os.system(f"start {url}")
    
def is_in_focus():
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower().startswith("osussist")
    except:
        return False

class Spawn:
    
    global ASSET_PATH
    
    def __init__(self, linker_instance: classmethod, version: str, queue: classmethod):
        
        self.settings = linker_instance
        self.queue = queue
        self.value_th = None
        
        self.get_gui_style()
        self.get_values()
        
        self.tk = ctk.CTk()
        self.tk.title(f"Osussist | By: Takkeshi | v{version}")
        self.tk.iconbitmap(f"{ASSET_PATH}\\logo.ico")
        self.tk.geometry("700x500")
        self.tk.resizable(False, False)
        
        self.nav_frame = ctk.CTkFrame(self.tk, corner_radius=0)
        self.nav_frame.pack(side=LEFT, fill=Y)
        
        self.logo_display = ctk.CTkLabel(self.nav_frame, corner_radius=0, image=IMAGE_LIST["logo"], text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_display.pack(side=TOP, fill=X, padx=20, pady=20)
        self.separator_frame = ctk.CTkFrame(self.nav_frame, corner_radius=0, fg_color="#323232", height=2, width=50)
        self.separator_frame.pack(side=TOP, fill=X)
        
        self.aim_button = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="| AIM ", font=TEXT_STYLE["Bold16"], fg_color=self.navColor
                                        , hover_color=self.primaryColor, image=IMAGE_LIST["aim_tab"], anchor="w", command=lambda: GuiHandler.aim_tab(self))
        self.aim_button.pack(side=TOP, fill=X)
        self.visuals_button = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="| VISUALS ", font=TEXT_STYLE["Bold16"], fg_color=self.navColor
                                            , hover_color=self.primaryColor, image=IMAGE_LIST["visuals_tab"], anchor="w", command=lambda: GuiHandler.visuals_tab(self))
        self.visuals_button.pack(side=TOP, fill=X)
        self.spoofer_button = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="| SPOOFER ", font=TEXT_STYLE["Bold16"], fg_color=self.navColor
                                            , hover_color=self.primaryColor, image=IMAGE_LIST["spoofer_tab"], anchor="w", command=lambda: GuiHandler.spoofer_tab(self))
        self.spoofer_button.pack(side=TOP, fill=X)
        
        self.support_button = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="| SUPPORT ", font=TEXT_STYLE["Bold16"], fg_color=self.navColor
                                            , hover_color=self.primaryColor, image=IMAGE_LIST["support_tab"], anchor="w", command=lambda: GuiHandler.support_tab(self))
        self.support_button.pack(side=BOTTOM, fill=X)
        self.config_button = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="| CONFIG ", font=TEXT_STYLE["Bold16"], fg_color=self.navColor
                                           , hover_color=self.primaryColor, image=IMAGE_LIST["config_tab"], anchor="w", command=lambda: GuiHandler.config_tab(self))
        self.config_button.pack(side=BOTTOM, fill=X)

        self.main_frame = ctk.CTkFrame(self.tk, corner_radius=0, fg_color="transparent")
        self.main_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        
        self.content_frame = ctk.CTkFrame(self.main_frame, corner_radius=0)
        self.content_frame.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=20)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(6, weight=1)
        
        GuiHandler.aim_tab(self)
        self.content_frame.pack_propagate()
        self.main_frame.pack_propagate()
        self.nav_frame.pack_propagate()
        self.tk.mainloop()
        
    def get_gui_style(self):
        
        self.navColor = "#2b2b2b"
        self.navColor2 = "#3b3b3b"
        self.frameColor = "#353535"
        self.frameColor2 = "#282828"
        
        color_name = self.settings.get().menu["color"]
        
        setcolors(color_name)
        self.primaryColor, self.secondaryColor, self.tertiaryColor, self.timeColor, self.dataColor, self.reset = get_color_config("hex")
    
    def get_values(self):
        
        try:
            self.queue.queue.clear()
        except:
            print("Queue is empty!")
        
        self.aim_settings = self.settings.get().aim
        self.visuals_settings = self.settings.get().visuals
        self.detection_settings = self.settings.get().detection
        #//self.spoofer_settings = self.settings.get().spoofer
        #//self.support_settings = self.settings.get().support
        #//self.config_settings = self.settings.get().config
        
        def th():
            while True:
                self.queue.put((self.aim_settings, self.visuals_settings, self.detection_settings))
                time.sleep(0.5)
            
        self.value_th = threading.Thread(target=th).start()

    def update_nav(self):
            
            self.get_gui_style()
            
            self.aim_button.configure(fg_color=self.navColor, hover_color=self.primaryColor)
            self.visuals_button.configure(fg_color=self.navColor, hover_color=self.primaryColor)
            self.spoofer_button.configure(fg_color=self.navColor, hover_color=self.primaryColor)
            self.config_button.configure(fg_color=self.navColor, hover_color=self.primaryColor)
            self.support_button.configure(fg_color=self.navColor, hover_color=self.primaryColor)
    
class Commands:
        
    def aim_enabled_cmd(self, state: int):
        if state == 1:
            self.aim_settings["enabled"] = True
        else:
            self.aim_settings["enabled"] = False
    
    def aim_range_cmd(self, caller: str, value: (int, float)):
        
        if caller == "slider":
            try:
                self.aim_settings["range"] = int(value)
            except:
                self.aim_settings["range"] = round(value)
                
            self.range_input.delete(0, END)
            self.range_input.insert(0, self.aim_settings["range"])
        
        elif caller == "input":
            try:
                self.aim_settings["range"] = int(value)
            except:
                self.aim_settings["range"] = round(value)
                
            self.range_slider.set(self.aim_settings["range"])
            
        elif caller == "plus":
            try:
                self.aim_settings["range"] += int(value)
            except:
                self.aim_settings["range"] += round(value)
                
            self.range_input.delete(0, END)
            self.range_input.insert(0, self.aim_settings["range"])
            self.range_slider.set(self.aim_settings["range"])
        
        elif caller == "minus":
            try:
                self.aim_settings["range"] -= int(value)
            except:
                self.aim_settings["range"] -= round(value)
                
            self.range_input.delete(0, END)
            self.range_input.insert(0, self.aim_settings["range"])
            self.range_slider.set(self.aim_settings["range"])
            
        if self.aim_settings["range"] < 0:
            self.aim_settings["range"] = 0
            self.range_input.delete(0, END)
            self.range_input.insert(0, self.aim_settings["range"])
            self.range_slider.set(self.aim_settings["range"])
        elif self.aim_settings["range"] > 1000:
            self.aim_settings["range"] = 1000
            self.range_input.delete(0, END)
            self.range_input.insert(0, self.aim_settings["range"])
            self.range_slider.set(self.aim_settings["range"])
            
    def aim_strength_cmd(self, caller: str, value: (int, float)):
            
            if caller == "slider":
                try:
                    self.aim_settings["strength"] = float(value)
                except:
                    self.aim_settings["strength"] = round(value, 2)
                    
                self.strength_input.delete(0, END)
                self.strength_input.insert(0, self.aim_settings["strength"])
            
            elif caller == "input":
                try:
                    self.aim_settings["strength"] = float(value)
                except:
                    self.aim_settings["strength"] = round(value, 2)
                    
                self.strength_slider.set(self.aim_settings["strength"])
                
            elif caller == "plus":
                try:
                    self.aim_settings["strength"] += float(value)
                except:
                    self.aim_settings["strength"] += round(value, 2)
                    
                self.strength_input.delete(0, END)
                self.strength_input.insert(0, self.aim_settings["strength"])
                self.strength_slider.set(self.aim_settings["strength"])
            
            elif caller == "minus":
                try:
                    self.aim_settings["strength"] -= float(value)
                except:
                    self.aim_settings["strength"] -= round(value, 2)
                    
                self.strength_input.delete(0, END)
                self.strength_input.insert(0, self.aim_settings["strength"])
                self.strength_slider.set(self.aim_settings["strength"])
                
            if self.aim_settings["strength"] < 0:
                self.aim_settings["strength"] = 0
                self.strength_input.delete(0, END)
                self.strength_input.insert(0, float(self.aim_settings["strength"]))
                self.strength_slider.set(self.aim_settings["strength"])
            elif self.aim_settings["strength"] > 1:
                self.aim_settings["strength"] = 1
                self.strength_input.delete(0, END)
                self.strength_input.insert(0, float(self.aim_settings["strength"]))
                self.strength_slider.set(self.aim_settings["strength"])
                
    def aim_min_area_cmd(self, caller: str, value: (int, float)):
                
                if caller == "slider":
                    try:
                        self.aim_settings["min_area"] = int(value)
                    except:
                        self.aim_settings["min_area"] = round(value)
                        
                    self.min_area_input.delete(0, END)
                    self.min_area_input.insert(0, self.aim_settings["min_area"])
                
                elif caller == "input":
                    try:
                        self.aim_settings["min_area"] = int(value)
                    except:
                        self.aim_settings["min_area"] = round(value)
                        
                    self.min_area_slider.set(self.aim_settings["min_area"])
                    
                elif caller == "plus":
                    try:
                        self.aim_settings["min_area"] += int(value)
                    except:
                        self.aim_settings["min_area"] += round(value)
                        
                    self.min_area_input.delete(0, END)
                    self.min_area_input.insert(0, self.aim_settings["min_area"])
                    self.min_area_slider.set(self.aim_settings["min_area"])
                
                elif caller == "minus":
                    try:
                        self.aim_settings["min_area"] -= int(value)
                    except:
                        self.aim_settings["min_area"] -= round(value)
                        
                    self.min_area_input.delete(0, END)
                    self.min_area_input.insert(0, self.aim_settings["min_area"])
                    self.min_area_slider.set(self.aim_settings["min_area"])
                    
                if self.aim_settings["min_area"] < 0:
                    self.aim_settings["min_area"] = 0
                    self.min_area_input.delete(0, END)
                    self.min_area_input.insert(0, self.aim_settings["min_area"])
                    self.min_area_slider.set(self.aim_settings["min_area"])
                elif self.aim_settings["min_area"] > 200:
                    self.aim_settings["min_area"] = 200
                    self.min_area_input.delete(0, END)
                    self.min_area_input.insert(0, self.aim_settings["min_area"])
                    self.min_area_slider.set(self.aim_settings["min_area"])
    
    def detection_set_color(self, caller: str):
        
        if caller == "cursor":
            r = int(self.cursor_r_input.get())
            g = int(self.cursor_g_input.get())
            b = int(self.cursor_b_input.get())
            
            if any([r > 255, g > 255, b > 255]):
                return
            
            self.detection_settings["cursor"] = [r, g, b]
            self.cursor_color_square.configure(fg_color=Common.convert_color(self.detection_settings["cursor"]))
        elif caller == "hitcircle":
            r = int(self.hitcircle_r_input.get())
            g = int(self.hitcircle_g_input.get())
            b = int(self.hitcircle_b_input.get())
            
            if any([r > 255, g > 255, b > 255]):
                return
            
            self.detection_settings["hitcircle"] = [r, g, b]
            self.hitcircle_color_square.configure(fg_color=Common.convert_color(self.detection_settings["hitcircle"]))
    
    def config_selection(self, selected: str):

        try: 
            for widget in self.config_files_frame.winfo_children():
                widget.destroy()
        except:
            pass
        
        self.config_selector.set("Select Config")
        self.config_selector.configure(values=["Select Config"])
        
        if selected.lower() == "local":
            
            self.config_list = self.settings.get_local_configs()

            for config_file in self.config_list:
                file_label = ctk.CTkLabel(self.config_files_frame, corner_radius=5, text=config_file, font=TEXT_STYLE["Normal15"], fg_color=self.navColor2)
                file_label.pack(side=TOP, fill=X, pady=(5,0), padx=(5,0))
                
            self.config_selector.configure(values=self.config_list)
            
        elif selected.lower() == "cloud":
            self.file_label = ctk.CTkLabel(self.config_files_frame, corner_radius=5, text="Coming Soon", font=TEXT_STYLE["Normal15"], fg_color=self.navColor2)
            self.file_label.pack(side=TOP, fill=X, pady=(5,0), padx=(5,0))
    
    def config_actions(self, action: str, config_name: str = None):
        
        if action.lower() == "load":
            
            if self.config_selector.get() == "Select Config":
                alert("Invalid Config!", "Please select a config to load!")
                return
            
            config_name = self.config_selector.get()
            self.settings.load(config_name=config_name)
            self.get_values()
            self.get_gui_style()
            self.update_nav()
            GuiHandler.config_tab(self)
            self.config_selector.set(config_name)
        
        elif action.lower() == "save":
            
            if self.config_selector.get() == "Select Config":
                alert("Invalid Config!", "Please select a config to save!")
                return
            
            config_name = self.config_selector.get()
            
            self.settings.save(aim=self.aim_settings, visuals=self.visuals_settings, detection=self.detection_settings, config_name=self.config_selector.get())
            GuiHandler.config_tab(self)
            self.config_selector.set(config_name)
            
        elif action.lower() == "create":
            
            if config_name == "":
                alert("Invalid Config Name!", "Please enter a config name!")
                return
            
            if not config_name.endswith(".json"):
                alert("Invalid Config Name!", "Please make sure the config name ends with .json!")
                raise ValueError("Invalid Config Name!")
            
            self.settings.create(config_name.replace(" ", "_"))
            self.config_selector.set("Select Config")
            Commands.config_selection(self, "local")
            
        elif action.lower() == "reset":
            
                if self.config_selector.get() == "Select Config":
                    alert("Invalid Config!", "Please select a config to reset!")
                    return
                
                config_name = self.config_selector.get()
                self.settings.reset(config_name)
                GuiHandler.config_tab(self)
                self.config_selector.set(config_name)
            
        elif action.lower() == "delete":
            
            if self.config_selector.get() == "Select Config":
                alert("Invalid Config!", "Please select a config to delete!")
                return
            
            self.settings.delete(self.config_selector.get())
            self.config_selector.set("Select Config")
            Commands.config_selection(self, "local")
    
    def visuals_enabled_cmd(self, caller: str, state: int):
            if caller == "cursor":
                if state == 1:
                    self.visuals_settings["cursor"]["enabled"] = True
                else:
                    self.visuals_settings["cursor"]["enabled"] = False
            elif caller == "hitcircle":
                if state == 1:
                    self.visuals_settings["hitcircle"]["enabled"] = True
                else:
                    self.visuals_settings["hitcircle"]["enabled"] = False

    def visuals_set_color(self, caller: str):
        
        if caller == "cursor":
            r = int(self.cursor_r_input.get())
            g = int(self.cursor_g_input.get())
            b = int(self.cursor_b_input.get())
            
            if any([r > 255, g > 255, b > 255]):
                return
            
            self.visuals_settings["cursor"]["color"] = [r, g, b]
            self.cursor_color_square.configure(fg_color=Common.convert_color(self.visuals_settings["cursor"]["color"]))
        elif caller == "hitcircle":
            r = int(self.hitcircle_r_input.get())
            g = int(self.hitcircle_g_input.get())
            b = int(self.hitcircle_b_input.get())
            
            if any([r > 255, g > 255, b > 255]):
                return
            
            self.visuals_settings["hitcircle"]["color"] = [r, g, b]
            self.hitcircle_color_square.configure(fg_color=Common.convert_color(self.visuals_settings["hitcircle"]["color"]))

    def cursor_thickness_cmd(self, caller: str, value: (int, float)):
            
            if caller == "slider":
                try:
                    self.visuals_settings["cursor"]["thickness"] = int(value)
                except:
                    self.visuals_settings["cursor"]["thickness"] = round(value)
                    
                self.cursor_thickness_input.delete(0, END)
                self.cursor_thickness_input.insert(0, self.visuals_settings["cursor"]["thickness"])
            
            elif caller == "input":
                try:
                    self.visuals_settings["cursor"]["thickness"] = int(value)
                except:
                    self.visuals_settings["cursor"]["thickness"] = round(value)
                    
                self.cursor_thickness_slider.set(self.visuals_settings["cursor"]["thickness"])
                
            elif caller == "plus":
                try:
                    self.visuals_settings["cursor"]["thickness"] += int(value)
                except:
                    self.visuals_settings["cursor"]["thickness"] += round(value)
                    
                self.cursor_thickness_input.delete(0, END)
                self.cursor_thickness_input.insert(0, self.visuals_settings["cursor"]["thickness"])
                self.cursor_thickness_slider.set(self.visuals_settings["cursor"]["thickness"])
            
            elif caller == "minus":
                try:
                    self.visuals_settings["cursor"]["thickness"] -= int(value)
                except:
                    self.visuals_settings["cursor"]["thickness"] -= round(value)
                    
                self.cursor_thickness_input.delete(0, END)
                self.cursor_thickness_input.insert(0, self.visuals_settings["cursor"]["thickness"])
                self.cursor_thickness_slider.set(self.visuals_settings["cursor"]["thickness"])
                
            if self.visuals_settings["cursor"]["thickness"] < 0:
                self.visuals_settings["cursor"]["thickness"] = 0
                self.cursor_thickness_input.delete(0, END)
                self.cursor_thickness_input.insert(0, self.visuals_settings["cursor"]["thickness"])
                self.cursor_thickness_slider.set(self.visuals_settings["cursor"]["thickness"])
            elif self.visuals_settings["cursor"]["thickness"] > 10:
                self.visuals_settings["cursor"]["thickness"] = 10
                self.cursor_thickness_input.delete(0, END)
                self.cursor_thickness_input.insert(0, self.visuals_settings["cursor"]["thickness"])
                self.cursor_thickness_slider.set(self.visuals_settings["cursor"]["thickness"])

    def hitcircle_thickness_cmd(self, caller: str, value: (int, float)):
            
            if caller == "slider":
                try:
                    self.visuals_settings["hitcircle"]["thickness"] = int(value)
                except:
                    self.visuals_settings["hitcircle"]["thickness"] = round(value)
                    
                self.hitcircle_thickness_input.delete(0, END)
                self.hitcircle_thickness_input.insert(0, self.visuals_settings["hitcircle"]["thickness"])
            
            elif caller == "input":
                try:
                    self.visuals_settings["hitcircle"]["thickness"] = int(value)
                except:
                    self.visuals_settings["hitcircle"]["thickness"] = round(value)
                    
                self.hitcircle_thickness_slider.set(self.visuals_settings["hitcircle"]["thickness"])
                
            elif caller == "plus":
                try:
                    self.visuals_settings["hitcircle"]["thickness"] += int(value)
                except:
                    self.visuals_settings["hitcircle"]["thickness"] += round(value)
                    
                self.hitcircle_thickness_input.delete(0, END)
                self.hitcircle_thickness_input.insert(0, self.visuals_settings["hitcircle"]["thickness"])
                self.hitcircle_thickness_slider.set(self.visuals_settings["hitcircle"]["thickness"])
            
            elif caller == "minus":
                try:
                    self.visuals_settings["hitcircle"]["thickness"] -= int(value)
                except:
                    self.visuals_settings["hitcircle"]["thickness"] -= round(value)
                    
                self.hitcircle_thickness_input.delete(0, END)
                self.hitcircle_thickness_input.insert(0, self.visuals_settings["hitcircle"]["thickness"])
                self.hitcircle_thickness_slider.set(self.visuals_settings["hitcircle"]["thickness"])
                
            if self.visuals_settings["hitcircle"]["thickness"] < 0:
                self.visuals_settings["hitcircle"]["thickness"] = 0
                self.hitcircle_thickness_input.delete(0, END)
                self.hitcircle_thickness_input.insert(0, self.visuals_settings["hitcircle"]["thickness"])
                self.hitcircle_thickness_slider.set(self.visuals_settings["hitcircle"]["thickness"])
            elif self.visuals_settings["hitcircle"]["thickness"] > 10:
                self.visuals_settings["hitcircle"]["thickness"] = 10
                self.hitcircle_thickness_input.delete(0, END)
                self.hitcircle_thickness_input.insert(0, self.visuals_settings["hitcircle"]["thickness"])
                self.hitcircle_thickness_slider.set(self.visuals_settings["hitcircle"]["thickness"])
    
class GuiHandler:
    
    def aim_tab(self):
        
        Common.reset_window(self)
        
        ####### Aim Assist #######
        
        self.aim_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor)
        self.aim_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,0), padx=(20,20))
        
        self.aim_title = ctk.CTkLabel(self.aim_frame, corner_radius=0, text="Aim Assist", font=TEXT_STYLE["Bold17"], fg_color=self.primaryColor)
        self.aim_title.pack(side=TOP, fill=X)
        
        self.aim_content_holder = ctk.CTkFrame(self.aim_frame, corner_radius=0, fg_color="transparent")
        self.aim_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
        self.aim_content_holder.grid_columnconfigure(4, weight=1)
        self.aim_content_holder.grid_rowconfigure(4, weight=1)

        ########################################################################################################################################################################################################################

        self.aim_enabled = ctk.CTkCheckBox(self.aim_content_holder, corner_radius=10, text="Enabled", font=TEXT_STYLE["Normal15"], fg_color=self.primaryColor
                                           , hover_color=self.primaryColor, command=lambda: Commands.aim_enabled_cmd(self, self.aim_enabled.get()))
        self.aim_enabled.grid(row=0, column=0, sticky="w", padx=(5,5), pady=(5,0))
        
        if self.aim_settings["enabled"]:
            self.aim_enabled.select()
        
        ########################################################################################################################################################################################################################
        
        self.range_slider = ctk.CTkSlider(self.aim_content_holder, from_=0, to=1000, orientation=HORIZONTAL, progress_color=self.primaryColor, bg_color=self.frameColor2
                                          , button_color=self.dataColor, hover=False, number_of_steps=1000, command=lambda x: Commands.aim_range_cmd(self, "slider", x))
        self.range_slider.grid(row=1, column=0, sticky="w", padx=(5,5))
        
        self.range_input = ctk.CTkEntry(self.aim_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.range_input.grid(row=1, column=1, sticky="w")
        
        self.range_minus = ctk.CTkButton(self.aim_content_holder, width=30, corner_radius=10, text="-", fg_color=self.frameColor2, hover_color=self.navColor
                                         , command=lambda: Commands.aim_range_cmd(self, "minus", 1))
        self.range_minus.grid(row=1, column=2, sticky="w", padx=(5,0))
        
        self.range_plus = ctk.CTkButton(self.aim_content_holder, width=30, corner_radius=10, text="+", fg_color=self.frameColor2, hover_color=self.navColor
                                        , command=lambda: Commands.aim_range_cmd(self, "plus", 1))
        self.range_plus.grid(row=1, column=3, sticky="w", padx=(5,0))
        
        self.range_label = ctk.CTkLabel(self.aim_content_holder, corner_radius=0, text="Base FOV", font=TEXT_STYLE["Normal15"])
        self.range_label.grid(row=1, column=4, sticky="w", padx=(5,0), pady=(5,10))
        
        self.range_input.insert(0, self.aim_settings["range"])
        self.range_input.bind("<Return>", lambda x: Commands.aim_range_cmd(self, "input", self.range_input.get()))
        self.range_slider.set(self.aim_settings["range"])
        
        ########################################################################################################################################################################################################################
        
        self.strength_slider = ctk.CTkSlider(self.aim_content_holder, from_=0, to=1, orientation=HORIZONTAL, progress_color=self.primaryColor, bg_color=self.frameColor2
                                             , button_color=self.dataColor, hover=False, number_of_steps=100, command=lambda x: Commands.aim_strength_cmd(self, "slider", x))
        self.strength_slider.grid(row=2, column=0, sticky="w", padx=(5,5))
        
        self.strength_input = ctk.CTkEntry(self.aim_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.strength_input.grid(row=2, column=1, sticky="w")
        
        self.strength_minus = ctk.CTkButton(self.aim_content_holder, width=30, corner_radius=10, text="-", fg_color=self.frameColor2, hover_color=self.navColor
                                            , command=lambda: Commands.aim_strength_cmd(self, "minus", 0.01))
        self.strength_minus.grid(row=2, column=2, sticky="w", padx=(5,0))
        
        self.strength_plus = ctk.CTkButton(self.aim_content_holder, width=30, corner_radius=10, text="+", fg_color=self.frameColor2, hover_color=self.navColor
                                           , command=lambda: Commands.aim_strength_cmd(self, "plus", 0.01))
        self.strength_plus.grid(row=2, column=3, sticky="w", padx=(5,0))
        
        self.strength_label = ctk.CTkLabel(self.aim_content_holder, corner_radius=0, text="Strength", font=TEXT_STYLE["Normal15"])
        self.strength_label.grid(row=2, column=4, sticky="w", padx=(5,0), pady=(5,10))
        
        self.strength_input.insert(0, self.aim_settings["strength"])
        self.strength_input.bind("<Return>", lambda x: Commands.aim_strength_cmd(self, "input", self.strength_input.get()))
        self.strength_slider.set(self.aim_settings["strength"])
        
        ########################################################################################################################################################################################################################
        
        self.min_area_slider = ctk.CTkSlider(self.aim_content_holder, from_=0, to=200, orientation=HORIZONTAL, progress_color=self.primaryColor, bg_color=self.frameColor2
                                             , button_color=self.dataColor, hover=False, number_of_steps=1000, command=lambda x: Commands.aim_min_area_cmd(self, "slider", x))
        self.min_area_slider.grid(row=3, column=0, sticky="w", padx=(5,5))
        
        self.min_area_input = ctk.CTkEntry(self.aim_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.min_area_input.grid(row=3, column=1, sticky="w")
        
        self.min_area_minus = ctk.CTkButton(self.aim_content_holder, width=30, corner_radius=10, text="-", fg_color=self.frameColor2, hover_color=self.navColor
                                            , command=lambda: Commands.aim_min_area_cmd(self, "minus", 1))
        self.min_area_minus.grid(row=3, column=2, sticky="w", padx=(5,0))
        
        self.min_area_plus = ctk.CTkButton(self.aim_content_holder, width=30, corner_radius=10, text="+", fg_color=self.frameColor2, hover_color=self.navColor
                                           , command=lambda: Commands.aim_min_area_cmd(self, "plus", 1))
        self.min_area_plus.grid(row=3, column=3, sticky="w", padx=(5,0))
        
        self.min_area_label = ctk.CTkLabel(self.aim_content_holder, corner_radius=0, text="Min Area", font=TEXT_STYLE["Normal15"])
        self.min_area_label.grid(row=3, column=4, sticky="w", padx=(5,0), pady=(5,10))
        
        self.min_area_input.insert(0, self.aim_settings["min_area"])
        self.min_area_input.bind("<Return>", lambda x: Commands.aim_min_area_cmd(self, "input", self.min_area_input.get()))
        self.min_area_slider.set(self.aim_settings["min_area"])
        
        ########################################################################################################################################################################################################################
        
        ####### Detection #######
        
        self.detection_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor)
        self.detection_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,20), padx=(20,20))
        
        self.detection_title = ctk.CTkLabel(self.detection_frame, corner_radius=0, text="Detection", font=TEXT_STYLE["Bold17"], fg_color=self.primaryColor)
        self.detection_title.pack(side=TOP, fill=X)
        
        self.detection_content_holder = ctk.CTkFrame(self.detection_frame, corner_radius=0, fg_color="transparent")
        self.detection_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
        self.detection_content_holder.grid_columnconfigure(5, weight=1)
        
        ########################################################################################################################################################################################################################
        
        self.cursor_r_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="R", font=TEXT_STYLE["Normal10"])
        self.cursor_r_label.grid(row=0, column=0, sticky="we", padx=(5,5))
        self.cursor_r_input = ctk.CTkEntry(self.detection_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.cursor_r_input.grid(row=1, column=0, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_g_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="G", font=TEXT_STYLE["Normal10"])
        self.cursor_g_label.grid(row=0, column=1, sticky="we", padx=(5,5))
        self.cursor_g_input = ctk.CTkEntry(self.detection_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.cursor_g_input.grid(row=1, column=1, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_b_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="B", font=TEXT_STYLE["Normal10"])
        self.cursor_b_label.grid(row=0, column=2, sticky="we", padx=(5,5))
        self.cursor_b_input = ctk.CTkEntry(self.detection_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.cursor_b_input.grid(row=1, column=2, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_button = ctk.CTkButton(self.detection_content_holder, width=50, corner_radius=10, text="Set", fg_color=self.frameColor2, hover_color=self.navColor
                                             , command=lambda: Commands.detection_set_color(self, "cursor"))
        self.cursor_button.grid(row=1, column=3, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="Cursor Color", font=TEXT_STYLE["Normal15"])
        self.cursor_label.grid(row=1, column=4, sticky="w", padx=(5,0), pady=(5,10))
        
        self.cursor_color_square = ctk.CTkFrame(self.detection_content_holder, corner_radius=0, fg_color="", height=25, width=25, border_color=self.frameColor2, border_width=2)
        self.cursor_color_square.grid(row=1, column=5, sticky="w", padx=(20,5), pady=(5,10))
        
        self.cursor_color_square.configure(fg_color=Common.convert_color(self.detection_settings["cursor"]))
        self.cursor_r_input.insert(0, self.detection_settings["cursor"][0])
        self.cursor_g_input.insert(0, self.detection_settings["cursor"][1])
        self.cursor_b_input.insert(0, self.detection_settings["cursor"][2])
        
        ########################################################################################################################################################################################################################
        
        self.hitcircle_r_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="R", font=TEXT_STYLE["Normal10"])
        self.hitcircle_r_label.grid(row=2, column=0, sticky="we", padx=(5,5))
        self.hitcircle_r_input = ctk.CTkEntry(self.detection_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.hitcircle_r_input.grid(row=3, column=0, sticky="w", padx=(5,5))
        
        self.hitcircle_g_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="G", font=TEXT_STYLE["Normal10"])
        self.hitcircle_g_label.grid(row=2, column=1, sticky="we", padx=(5,5))
        self.hitcircle_g_input = ctk.CTkEntry(self.detection_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.hitcircle_g_input.grid(row=3, column=1, sticky="w", padx=(5,5))
        
        self.hitcircle_b_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="B", font=TEXT_STYLE["Normal10"])
        self.hitcircle_b_label.grid(row=2, column=2, sticky="we", padx=(5,5))
        self.hitcircle_b_input = ctk.CTkEntry(self.detection_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.hitcircle_b_input.grid(row=3, column=2, sticky="w", padx=(5,5))
        
        self.hitcircle_button = ctk.CTkButton(self.detection_content_holder, width=50, corner_radius=10, text="Set", fg_color=self.frameColor2, hover_color=self.navColor
                                           , command=lambda: Commands.detection_set_color(self, "hitcircle"))
        self.hitcircle_button.grid(row=3, column=3, sticky="w", padx=(5,5))
        
        self.hitcircle_label = ctk.CTkLabel(self.detection_content_holder, corner_radius=0, text="Hitcircle Color", font=TEXT_STYLE["Normal15"])
        self.hitcircle_label.grid(row=3, column=4, sticky="w", padx=(5,0), pady=(5,10))
        
        self.hitcircle_color_square = ctk.CTkFrame(self.detection_content_holder, corner_radius=0, fg_color="", height=25, width=25, border_color=self.frameColor2, border_width=2)
        self.hitcircle_color_square.grid(row=3, column=5, sticky="w", padx=(20,5))
        
        self.hitcircle_color_square.configure(fg_color=Common.convert_color(self.detection_settings["hitcircle"]))
        self.hitcircle_r_input.insert(0, self.detection_settings["hitcircle"][0])
        self.hitcircle_g_input.insert(0, self.detection_settings["hitcircle"][1])
        self.hitcircle_b_input.insert(0, self.detection_settings["hitcircle"][2])
        
        ########################################################################################################################################################################################################################
        
        self.aim_frame.pack_propagate()
        self.detection_frame.pack_propagate()
        self.aim_button.configure(fg_color=self.primaryColor)
        
    def visuals_tab(self):
        
        Common.reset_window(self)
        
        self.cursor_visuals_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor)
        self.cursor_visuals_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,0), padx=(20,20))
        
        self.cursor_visuals_title = ctk.CTkLabel(self.cursor_visuals_frame, corner_radius=0, text="Cursor", font=TEXT_STYLE["Bold17"], fg_color=self.primaryColor)
        self.cursor_visuals_title.pack(side=TOP, fill=X)
        
        self.cursor_visuals_content_holder = ctk.CTkFrame(self.cursor_visuals_frame, corner_radius=0, fg_color="transparent")
        self.cursor_visuals_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
        self.cursor_visuals_content_holder.grid_columnconfigure(5, weight=1)
        
        
        self.cursor_enabled = ctk.CTkCheckBox(self.cursor_visuals_content_holder, corner_radius=10, text="Enabled", font=TEXT_STYLE["Normal15"], fg_color=self.primaryColor
                                           , hover_color=self.primaryColor, command=lambda: Commands.visuals_enabled_cmd(self, "cursor", self.cursor_enabled.get()))
        self.cursor_enabled.grid(row=0, column=0, sticky="w", padx=(5,5), pady=(5,10), columnspan=2)
        
        if self.visuals_settings["cursor"]["enabled"]:
            self.cursor_enabled.select()
        
        ########################################################################################################################################################################################################################
        
        self.slider_holder = ctk.CTkFrame(self.cursor_visuals_content_holder, corner_radius=0, fg_color="transparent")
        self.slider_holder.grid(row=1, column=0, sticky="w", padx=(0,0), pady=(0,0), columnspan=100)
        self.slider_holder.grid_columnconfigure(5, weight=1)
        
        self.cursor_thickness_slider = ctk.CTkSlider(self.slider_holder, from_=0, to=10, orientation=HORIZONTAL, progress_color=self.primaryColor, bg_color=self.frameColor2
                                          , button_color=self.dataColor, hover=False, number_of_steps=10, command=lambda x: Commands.cursor_thickness_cmd(self, "slider", x))
        self.cursor_thickness_slider.grid(row=1, column=0, sticky="w", padx=(5,5))
        
        self.cursor_thickness_input = ctk.CTkEntry(self.slider_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.cursor_thickness_input.grid(row=1, column=1, sticky="w")
        
        self.cursor_thickness_minus = ctk.CTkButton(self.slider_holder, width=30, corner_radius=10, text="-", fg_color=self.frameColor2, hover_color=self.navColor
                                         , command=lambda: Commands.cursor_thickness_cmd(self, "minus", 1))
        self.cursor_thickness_minus.grid(row=1, column=2, sticky="w", padx=(5,0))
        
        self.cursor_thickness_plus = ctk.CTkButton(self.slider_holder, width=30, corner_radius=10, text="+", fg_color=self.frameColor2, hover_color=self.navColor
                                        , command=lambda: Commands.cursor_thickness_cmd(self, "plus", 1))
        self.cursor_thickness_plus.grid(row=1, column=3, sticky="w", padx=(5,0))
        
        self.cursor_thickness_label = ctk.CTkLabel(self.slider_holder, corner_radius=0, text="Thickness", font=TEXT_STYLE["Normal15"])
        self.cursor_thickness_label.grid(row=1, column=4, sticky="w", padx=(5,0), pady=(5,5))
        
        self.cursor_thickness_input.insert(0, self.visuals_settings["cursor"]["thickness"])
        self.cursor_thickness_input.bind("<Return>", lambda x: Commands.cursor_thickness_cmd(self, "input", self.cursor_thickness_input.get()))
        self.cursor_thickness_slider.set(self.visuals_settings["cursor"]["thickness"])
        
        ########################################################################################################################################################################################################################
        
        self.cursor_r_label = ctk.CTkLabel(self.cursor_visuals_content_holder, corner_radius=0, text="R", font=TEXT_STYLE["Normal10"])
        self.cursor_r_label.grid(row=2, column=0, sticky="we", padx=(5,5))
        self.cursor_r_input = ctk.CTkEntry(self.cursor_visuals_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.cursor_r_input.grid(row=3, column=0, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_g_label = ctk.CTkLabel(self.cursor_visuals_content_holder, corner_radius=0, text="G", font=TEXT_STYLE["Normal10"])
        self.cursor_g_label.grid(row=2, column=1, sticky="we", padx=(5,5))
        self.cursor_g_input = ctk.CTkEntry(self.cursor_visuals_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.cursor_g_input.grid(row=3, column=1, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_b_label = ctk.CTkLabel(self.cursor_visuals_content_holder, corner_radius=0, text="B", font=TEXT_STYLE["Normal10"])
        self.cursor_b_label.grid(row=2, column=2, sticky="we", padx=(5,5))
        self.cursor_b_input = ctk.CTkEntry(self.cursor_visuals_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.cursor_b_input.grid(row=3, column=2, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_button = ctk.CTkButton(self.cursor_visuals_content_holder, width=50, corner_radius=10, text="Set", fg_color=self.frameColor2, hover_color=self.navColor
                                             , command=lambda: Commands.visuals_set_color(self, "cursor"))
        self.cursor_button.grid(row=3, column=3, sticky="w", padx=(5,5), pady=(5,10))
        
        self.cursor_label = ctk.CTkLabel(self.cursor_visuals_content_holder, corner_radius=0, text="Cursor Color", font=TEXT_STYLE["Normal15"])
        self.cursor_label.grid(row=3, column=4, sticky="w", padx=(5,0), pady=(5,10))
        
        self.cursor_color_square = ctk.CTkFrame(self.cursor_visuals_content_holder, corner_radius=0, fg_color="", height=25, width=25, border_color=self.frameColor2, border_width=2)
        self.cursor_color_square.grid(row=3, column=5, sticky="w", padx=(20,5), pady=(5,10))
        
        self.cursor_color_square.configure(fg_color=Common.convert_color(self.visuals_settings["cursor"]['color']))
        self.cursor_r_input.insert(0, self.visuals_settings["cursor"]['color'][0])
        self.cursor_g_input.insert(0, self.visuals_settings["cursor"]['color'][1])
        self.cursor_b_input.insert(0, self.visuals_settings["cursor"]['color'][2])
        
        ########################################################################################################################################################################################################################
        
        self.hitcircle_visuals_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor)
        self.hitcircle_visuals_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,20), padx=(20,20))
        
        self.hitcircle_visuals_title = ctk.CTkLabel(self.hitcircle_visuals_frame, corner_radius=0, text="Hitcircle", font=TEXT_STYLE["Bold17"], fg_color=self.primaryColor)
        self.hitcircle_visuals_title.pack(side=TOP, fill=X)
        
        self.hitcircle_visuals_content_holder = ctk.CTkFrame(self.hitcircle_visuals_frame, corner_radius=0, fg_color="transparent")
        self.hitcircle_visuals_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
        self.hitcircle_visuals_content_holder.grid_columnconfigure(5, weight=1)
        
        hitcircle_enabled = ctk.CTkCheckBox(self.hitcircle_visuals_content_holder, corner_radius=10, text="Enabled", font=TEXT_STYLE["Normal15"], fg_color=self.primaryColor
                                             , hover_color=self.primaryColor, command=lambda: Commands.visuals_enabled_cmd(self, "hitcircle", hitcircle_enabled.get()))
        hitcircle_enabled.grid(row=0, column=0, sticky="w", padx=(5,5), pady=(5,10), columnspan=2)
        
        if self.visuals_settings["hitcircle"]["enabled"]:
            hitcircle_enabled.select()
        
        ########################################################################################################################################################################################################################
        
        self.slider_holder = ctk.CTkFrame(self.hitcircle_visuals_content_holder, corner_radius=0, fg_color="transparent")
        self.slider_holder.grid(row=1, column=0, sticky="w", padx=(0,0), pady=(0,0), columnspan=100)
        self.slider_holder.grid_columnconfigure(5, weight=1)
        
        self.hitcircle_thickness_slider = ctk.CTkSlider(self.slider_holder, from_=0, to=10, orientation=HORIZONTAL, progress_color=self.primaryColor, bg_color=self.frameColor2
                                          , button_color=self.dataColor, hover=False, number_of_steps=10, command=lambda x: Commands.hitcircle_thickness_cmd(self, "slider", x))
        self.hitcircle_thickness_slider.grid(row=1, column=0, sticky="w", padx=(5,5))
        
        self.hitcircle_thickness_input = ctk.CTkEntry(self.slider_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.hitcircle_thickness_input.grid(row=1, column=1, sticky="w")
        
        self.hitcircle_thickness_minus = ctk.CTkButton(self.slider_holder, width=30, corner_radius=10, text="-", fg_color=self.frameColor2, hover_color=self.navColor
                                         , command=lambda: Commands.hitcircle_thickness_cmd(self, "minus", 1))
        self.hitcircle_thickness_minus.grid(row=1, column=2, sticky="w", padx=(5,0))
        
        self.hitcircle_thickness_plus = ctk.CTkButton(self.slider_holder, width=30, corner_radius=10, text="+", fg_color=self.frameColor2, hover_color=self.navColor
                                        , command=lambda: Commands.hitcircle_thickness_cmd(self, "plus", 1))
        self.hitcircle_thickness_plus.grid(row=1, column=3, sticky="w", padx=(5,0))
        
        self.hitcircle_thickness_label = ctk.CTkLabel(self.slider_holder, corner_radius=0, text="Thickness", font=TEXT_STYLE["Normal15"])
        self.hitcircle_thickness_label.grid(row=1, column=4, sticky="w", padx=(5,0), pady=(5,5))
        
        self.hitcircle_thickness_input.insert(0, self.visuals_settings["hitcircle"]["thickness"])
        self.hitcircle_thickness_input.bind("<Return>", lambda x: Commands.hitcircle_thickness_cmd(self, "input", self.hitcircle_thickness_input.get()))
        self.hitcircle_thickness_slider.set(self.visuals_settings["hitcircle"]["thickness"])
        
        ########################################################################################################################################################################################################################
        
        self.hitcircle_r_label = ctk.CTkLabel(self.hitcircle_visuals_content_holder, corner_radius=0, text="R", font=TEXT_STYLE["Normal10"])
        self.hitcircle_r_label.grid(row=2, column=0, sticky="we", padx=(5,5))
        self.hitcircle_r_input = ctk.CTkEntry(self.hitcircle_visuals_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.hitcircle_r_input.grid(row=3, column=0, sticky="w", padx=(5,5), pady=(5,10))
        
        self.hitcircle_g_label = ctk.CTkLabel(self.hitcircle_visuals_content_holder, corner_radius=0, text="G", font=TEXT_STYLE["Normal10"])
        self.hitcircle_g_label.grid(row=2, column=1, sticky="we", padx=(5,5))
        self.hitcircle_g_input = ctk.CTkEntry(self.hitcircle_visuals_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.hitcircle_g_input.grid(row=3, column=1, sticky="w", padx=(5,5), pady=(5,10))
        
        self.hitcircle_b_label = ctk.CTkLabel(self.hitcircle_visuals_content_holder, corner_radius=0, text="B", font=TEXT_STYLE["Normal10"])
        self.hitcircle_b_label.grid(row=2, column=2, sticky="we", padx=(5,5))
        self.hitcircle_b_input = ctk.CTkEntry(self.hitcircle_visuals_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal10"], width=45)
        self.hitcircle_b_input.grid(row=3, column=2, sticky="w", padx=(5,5), pady=(5,10))
        
        self.hitcircle_button = ctk.CTkButton(self.hitcircle_visuals_content_holder, width=50, corner_radius=10, text="Set", fg_color=self.frameColor2, hover_color=self.navColor
                                             , command=lambda: Commands.visuals_set_color(self, "hitcircle"))
        self.hitcircle_button.grid(row=3, column=3, sticky="w", padx=(5,5), pady=(5,10))
        
        self.hitcircle_label = ctk.CTkLabel(self.hitcircle_visuals_content_holder, corner_radius=0, text="Hitcircle Color", font=TEXT_STYLE["Normal15"])
        self.hitcircle_label.grid(row=3, column=4, sticky="w", padx=(5,0), pady=(5,10))
        
        self.hitcircle_color_square = ctk.CTkFrame(self.hitcircle_visuals_content_holder, corner_radius=0, fg_color="", height=25, width=25, border_color=self.frameColor2, border_width=2)
        self.hitcircle_color_square.grid(row=3, column=5, sticky="w", padx=(20,5), pady=(5,10))
        
        self.hitcircle_color_square.configure(fg_color=Common.convert_color(self.visuals_settings["hitcircle"]['color']))
        self.hitcircle_r_input.insert(0, self.visuals_settings["hitcircle"]['color'][0])
        self.hitcircle_g_input.insert(0, self.visuals_settings["hitcircle"]['color'][1])
        self.hitcircle_b_input.insert(0, self.visuals_settings["hitcircle"]['color'][2])
        
        self.visuals_button.configure(fg_color=self.primaryColor)
        
    def spoofer_tab(self):
            
            Common.reset_window(self)
            
            self.spoofer_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor)
            self.spoofer_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,20), padx=(20,20))
            
            self.spoofer_title = ctk.CTkLabel(self.spoofer_frame, corner_radius=0, text="Coming Soon", font=TEXT_STYLE["Bold17"], fg_color=self.primaryColor)
            self.spoofer_title.pack(side=TOP, fill=X)
            
            self.spoofer_content_holder = ctk.CTkFrame(self.spoofer_frame, corner_radius=0, fg_color="transparent")
            self.spoofer_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
            self.spoofer_content_holder.grid_columnconfigure(4, weight=1)
            self.spoofer_content_holder.grid_rowconfigure(4, weight=1)
            
            self.coming_soon = ctk.CTkLabel(self.spoofer_content_holder, corner_radius=10, text="This feature is coming soon!", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor2)
            self.coming_soon.pack(side=TOP, fill=X, pady=(10,0), padx=(5,5))
            
            self.osussist_logo = ctk.CTkLabel(self.spoofer_content_holder, corner_radius=0, image=IMAGE_LIST["logo"], text="", font=ctk.CTkFont(size=15, weight="bold"))
            self.osussist_logo.pack(side=TOP, fill=X, pady=(10,0))
            
            self.spoofer_button.configure(fg_color=self.primaryColor)
        
    def config_tab(self):
        
        Common.reset_window(self)
        
        self.config_frame = ctk.CTkFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor)
        self.config_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,20), padx=(20,20))
        
        self.config_title = ctk.CTkLabel(self.config_frame, corner_radius=0, text="Config", font=TEXT_STYLE["Bold17"], fg_color=self.primaryColor)
        self.config_title.pack(side=TOP, fill=X)
        
        self.config_content_holder = ctk.CTkFrame(self.config_frame, corner_radius=0, fg_color="transparent")
        self.config_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
        self.config_content_holder.grid_columnconfigure(1, weight=1)
        self.config_content_holder.grid_rowconfigure(2, weight=1)
        
        ########################################################################################################################################################################################################################
        
        self.config_options = ctk.CTkSegmentedButton(self.config_content_holder, corner_radius=10, fg_color=self.frameColor2, selected_color=self.primaryColor, selected_hover_color=self.primaryColor, font=TEXT_STYLE["Normal15"]
                                                     , values=["Local", "Cloud"], command=lambda x: Commands.config_selection(self, x))
        self.config_options.grid(row=0, column=0, sticky="we", padx=(5,5), pady=(5,0))
        self.config_options.set("Local")
        
        self.config_files_frame = ctk.CTkScrollableFrame(self.config_content_holder, corner_radius=0, fg_color=self.frameColor2, height=290, width=230)
        self.config_files_frame.grid(row=1, column=0, sticky="we", padx=(5,5), pady=(5,5))
        
        self.config_selector = ctk.CTkComboBox(self.config_content_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal15"], values=[], width=20)
        self.config_selector.grid(row=2, column=0, sticky="we", padx=(5,5), pady=(0,5))
        self.config_selector.set("Select Config")
        
        ########################################################################################################################################################################################################################
        
        self.button_holder = ctk.CTkFrame(self.config_content_holder, corner_radius=0, fg_color="transparent")
        self.button_holder.grid(row=0, column=1, rowspan=5, sticky="n", padx=(5,5), pady=(0,0))
        
        self.save_button = ctk.CTkButton(self.button_holder, corner_radius=10, text="Save", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor2, hover_color=self.navColor
                                         , command=lambda: Commands.config_actions(self, "save"))
        self.save_button.pack(side=TOP, fill=X, pady=(10,5))
        
        self.load_button = ctk.CTkButton(self.button_holder, corner_radius=10, text="Load", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor2, hover_color=self.navColor
                                            , command=lambda: Commands.config_actions(self, "load"))
        self.load_button.pack(side=TOP, fill=X, pady=(10,5))
        
        self.reset_button = ctk.CTkButton(self.button_holder, corner_radius=10, text="Reset", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor2, hover_color=self.navColor
                                            , command=lambda: Commands.config_actions(self, "reset"))
        self.reset_button.pack(side=TOP, fill=X, pady=(10,5))
        
        self.delete_button = ctk.CTkButton(self.button_holder, corner_radius=10, text="Delete", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor2, hover_color=self.navColor
                                            , command=lambda: Commands.config_actions(self, "delete"))
        self.delete_button.pack(side=TOP, fill=X, pady=(10,5))
        
        self.create_input = ctk.CTkEntry(self.button_holder, corner_radius=10, fg_color=self.frameColor2, font=TEXT_STYLE["Normal15"], width=20)
        self.create_input.pack(side=TOP, fill=X, pady=(115,5))
        self.create_input.insert(0, "config.json")
        
        self.create_button = ctk.CTkButton(self.button_holder, corner_radius=10, text="Create", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor2, hover_color=self.navColor
                                            , command=lambda: Commands.config_actions(self, "create", self.create_input.get()))
        self.create_button.pack(side=TOP, fill=X, pady=(10,5))
        
        ########################################################################################################################################################################################################################
        
        Commands.config_selection(self, "Local")
        self.config_content_holder.pack_propagate()
        self.config_button.configure(fg_color=self.primaryColor)

    def support_tab(self):
        
        Common.reset_window(self)
        
        self.support_frame = ctk.CTkScrollableFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor, label_text="Support", label_font=TEXT_STYLE["Bold17"]
                                                    , label_fg_color=self.primaryColor)
        self.support_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,0), padx=(20,20))
        
        self.support_content_holder = ctk.CTkFrame(self.support_frame, corner_radius=0, fg_color="transparent")
        self.support_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
        self.support_content_holder.grid_columnconfigure(0, weight=1)
        self.support_content_holder.grid_columnconfigure(1, weight=1)
        self.support_content_holder.grid_rowconfigure(0, weight=1)
        self.support_content_holder.grid_rowconfigure(1, weight=1)
        
        self.discord_frame = ctk.CTkFrame(self.support_content_holder, corner_radius=10, fg_color=self.navColor)
        self.discord_frame.grid(row=0, column=0, padx=(15,5), pady=(5,5), sticky="we")
        self.discord_logo = ctk.CTkLabel(self.discord_frame, corner_radius=0, image=IMAGE_LIST["discord"], text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.discord_logo.place(relx=0.5, rely=0.05, anchor="n")
        self.discord_label = ctk.CTkLabel(self.discord_frame, corner_radius=0, text="Osussist Discord", font=TEXT_STYLE["Normal15"])
        self.discord_label.place(relx=0.5, rely=0.21, anchor="n")
        self.discord_subtitle = ctk.CTkLabel(self.discord_frame, corner_radius=0, text="Join the Osussist Discord server\nand ask for help or report a bug", font=TEXT_STYLE["Normal10"])
        self.discord_subtitle.place(relx=0.5, rely=0.4, anchor="n")
        self.discord_button = ctk.CTkButton(self.discord_frame, corner_radius=10, text="Join", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor, hover_color=self.frameColor2
                                             , command=lambda: webbrowser(SUPPORT_LINKS["discord"]))
        self.discord_button.place(relx=0.5, rely=0.95, anchor="s")
        
        self.unknowncheats_frame = ctk.CTkFrame(self.support_content_holder, corner_radius=10, fg_color=self.navColor)
        self.unknowncheats_frame.grid(row=0, column=1, padx=(5,0), pady=(5,5), sticky="we")
        self.unknowncheats_logo = ctk.CTkLabel(self.unknowncheats_frame, corner_radius=0, image=IMAGE_LIST["unknowncheats"], text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.unknowncheats_logo.place(relx=0.5, rely=0.05, anchor="n")
        self.unknowncheats_label = ctk.CTkLabel(self.unknowncheats_frame, corner_radius=0, text="UnknownCheats", font=TEXT_STYLE["Normal15"])
        self.unknowncheats_label.place(relx=0.5, rely=0.21, anchor="n")
        self.unknowncheats_subtitle = ctk.CTkLabel(self.unknowncheats_frame, corner_radius=0, text="Check out the Osussist thread and\nleave a comment or a plus rep", font=TEXT_STYLE["Normal10"])
        self.unknowncheats_subtitle.place(relx=0.5, rely=0.4, anchor="n")
        self.unknowncheats_button = ctk.CTkButton(self.unknowncheats_frame, corner_radius=10, text="Visit", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor, hover_color=self.frameColor2
                                                  , command=lambda: webbrowser(SUPPORT_LINKS["unknowncheats"]))
        self.unknowncheats_button.place(relx=0.5, rely=0.95, anchor="s")
        
        self.github_frame = ctk.CTkFrame(self.support_content_holder, corner_radius=10, fg_color=self.navColor)
        self.github_frame.grid(row=1, column=0, padx=(15,5), pady=(5,5), sticky="we")
        self.github_logo = ctk.CTkLabel(self.github_frame, corner_radius=0, image=IMAGE_LIST["github"], text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.github_logo.place(relx=0.5, rely=0.05, anchor="n")
        self.github_label = ctk.CTkLabel(self.github_frame, corner_radius=0, text="GitHub", font=TEXT_STYLE["Normal15"])
        self.github_label.place(relx=0.5, rely=0.21, anchor="n")
        self.github_subtitle = ctk.CTkLabel(self.github_frame, corner_radius=0, text="Check out the source code and\nand contribute to the project", font=TEXT_STYLE["Normal10"])
        self.github_subtitle.place(relx=0.5, rely=0.4, anchor="n")
        self.github_button = ctk.CTkButton(self.github_frame, corner_radius=10, text="Contribute", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor, hover_color=self.frameColor2
                                            , command=lambda: webbrowser(SUPPORT_LINKS["github"]))
        self.github_button.place(relx=0.5, rely=0.95, anchor="s")
        
        self.youtube_frame = ctk.CTkFrame(self.support_content_holder, corner_radius=10, fg_color=self.navColor)
        self.youtube_frame.grid(row=1, column=1, padx=(5,0), pady=(5,5), sticky="we")
        self.youtube_logo = ctk.CTkLabel(self.youtube_frame, corner_radius=0, image=IMAGE_LIST["youtube"], text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.youtube_logo.place(relx=0.5, rely=0.05, anchor="n")
        self.youtube_label = ctk.CTkLabel(self.youtube_frame, corner_radius=0, text="YouTube", font=TEXT_STYLE["Normal15"])
        self.youtube_label.place(relx=0.5, rely=0.21, anchor="n")
        self.youtube_subtitle = ctk.CTkLabel(self.youtube_frame, corner_radius=0, text="Some video install guides and in depth\ntutorials on how to make your own\ncomputer vision cheat", font=TEXT_STYLE["Normal10"])
        self.youtube_subtitle.place(relx=0.5, rely=0.4, anchor="n")
        self.youtube_button = ctk.CTkButton(self.youtube_frame, corner_radius=10, text="Subscribe", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor, hover_color=self.frameColor2
                                            , command=lambda: webbrowser(SUPPORT_LINKS["youtube"]))
        self.youtube_button.place(relx=0.5, rely=0.95, anchor="s")
        
        ########################################################################################################################################################################################################################
        
        self.credits_frame = ctk.CTkScrollableFrame(self.content_frame, corner_radius=0, fg_color=self.frameColor, label_text="Credits", label_font=TEXT_STYLE["Bold17"]
                                                    , label_fg_color=self.primaryColor)
        self.credits_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(20,20), padx=(20,20))
        
        self.credits_content_holder = ctk.CTkFrame(self.credits_frame, corner_radius=0, fg_color="transparent")
        self.credits_content_holder.pack(side=TOP, fill=BOTH, expand=True, pady=(10,0))
        self.credits_content_holder.grid_columnconfigure(0, weight=1)
        self.credits_content_holder.grid_columnconfigure(1, weight=1)
        self.credits_content_holder.grid_rowconfigure(0, weight=1)
        self.credits_content_holder.grid_rowconfigure(1, weight=1)
        
        self.takkeshi_frame = ctk.CTkFrame(self.credits_content_holder, corner_radius=10, fg_color=self.navColor)
        self.takkeshi_frame.grid(row=0, column=0, padx=(15,5), pady=(5,5), sticky="we")
        self.takkeshi_logo = ctk.CTkLabel(self.takkeshi_frame, corner_radius=0, image=CREDITS_ASSETS["takkeshi"], text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.takkeshi_logo.place(relx=0.5, rely=0.05, anchor="n")
        self.takkeshi_label = ctk.CTkLabel(self.takkeshi_frame, corner_radius=0, text="Takkeshi", font=TEXT_STYLE["Normal15"])
        self.takkeshi_label.place(relx=0.5, rely=0.21, anchor="n")
        self.takkeshi_subtitle = ctk.CTkLabel(self.takkeshi_frame, corner_radius=0, text="Osussist Developer", font=TEXT_STYLE["Normal10"])
        self.takkeshi_subtitle.place(relx=0.5, rely=0.4, anchor="n")
        self.takkeshi_button = ctk.CTkButton(self.takkeshi_frame, corner_radius=10, text="Visit", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor, hover_color=self.frameColor2
                                            , command=lambda: webbrowser(CREDITS_LINKS["takkeshi"]))
        self.takkeshi_button.place(relx=0.5, rely=0.95, anchor="s")
        
        self.nian_frame = ctk.CTkFrame(self.credits_content_holder, corner_radius=10, fg_color=self.navColor)
        self.nian_frame.grid(row=0, column=1, padx=(5,0), pady=(5,5), sticky="we")
        self.nian_logo = ctk.CTkLabel(self.nian_frame, corner_radius=0, image=CREDITS_ASSETS["nian"], text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.nian_logo.place(relx=0.5, rely=0.05, anchor="n")
        self.nian_label = ctk.CTkLabel(self.nian_frame, corner_radius=0, text="Nian", font=TEXT_STYLE["Normal15"])
        self.nian_label.place(relx=0.5, rely=0.21, anchor="n")
        self.nian_subtitle = ctk.CTkLabel(self.nian_frame, corner_radius=0, text="Osussist Beta Tester", font=TEXT_STYLE["Normal10"])
        self.nian_subtitle.place(relx=0.5, rely=0.4, anchor="n")
        self.nian_button = ctk.CTkButton(self.nian_frame, corner_radius=10, text="Visit", font=TEXT_STYLE["Normal15"], fg_color=self.frameColor, hover_color=self.frameColor2
                                            , command=lambda: webbrowser(CREDITS_LINKS["nian"]))
        self.nian_button.place(relx=0.5, rely=0.95, anchor="s")

        self.support_frame.pack_propagate()
        self.credits_frame.pack_propagate()
        self.support_button.configure(fg_color=self.primaryColor)
        
class Common:
    
    def reset_window(self):
        try:
            for widget in self.content_frame.winfo_children():
                widget.destroy()
        except Exception as e:
            print(f"{type(e)} - {e}")

        try:
            for widget in self.nav_frame.winfo_children():
                widget.configure(fg_color=self.navColor)
        except Exception as e:
            print(f"{type(e)} - {e}")
        
        self.separator_frame.configure(fg_color="#323232")
        
    def convert_color(color: list):
        return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"

if __name__ == '__main__':
    print("This is a module, not a script!")
    
    import linker
    import setup
    from fancycon import *
    
    queue = Queue()
    
    Spawn(linker.Config("C:\\Users\\maxar\\OneDrive\\Escritorio\\Trabajo\\Takkeshi_Code\\Projects\\OsuCheats\\AimAssistV2\\configs\\default.json", "C:\\Users\\maxar\\OneDrive\\Escritorio\\Trabajo\\Takkeshi_Code\\Projects\\OsuCheats\\AimAssistV2\\configs\\"), "2.0.0", queue)

else:
    import utils.setup as setup
    from utils.fancycon import *
