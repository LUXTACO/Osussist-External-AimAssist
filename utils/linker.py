import os
import json

class Config:
    
    def __init__(self, file_path: str, config_folder: str = f"{os.getcwd()}\\configs"):
        self.CONFIG_FOLDER = config_folder
        self.CONFIG_PATH = file_path
        self.config = None
        
        if not os.path.exists(self.CONFIG_PATH):
            with open(self.CONFIG_PATH, "w") as file:
                config = {
                    "menu_color": "pastel_pink",
                    "aim_assist": {
                        "enabled": True,
                        "min_area": 10,
                        "strength": 0.07,
                        "range": 400,
                        "compute": "cpu"
                    },
                    "detection": {
                        "cursor": [221,50,50],
                        "hitcircle": [237,3,205]
                    },
                    "visuals": {
                        "cursor": {
                            "enabled": True,
                            "color": [221,50,50],
                            "thickness": 2
                        },
                        "hitcircle": {
                            "enabled": True,
                            "color": [237,3,205],
                            "thickness": 2
                        }
                    },
                }
                
                json.dump(config, file, indent=4)
                
        if not os.path.exists(self.CONFIG_FOLDER):
            os.mkdir(self.CONFIG_FOLDER)
            
    def get_local_configs(self):
        unfiltered_list = os.listdir(self.CONFIG_FOLDER)
        return [file for file in unfiltered_list if file.endswith(".json")]
    
    def get(self):
        try:
            with open(self.CONFIG_PATH, "r") as file:
                self.config = json.load(file)
        except Exception as e:
            print(f"Failed to load {self.CONFIG_PATH}! {e}")
            self.config = None
        
        if self.config:
            self.aim = self.set_aim() # *Args {enabled: bool, min_area: int, strength: float, range: int}
            self.menu = self.set_menu() # *Args {color: list}
            self.visuals = self.set_visuals() # *Args {cursor: {color: list, thickness: int}, hitcircle: {color: list, thickness: int}}
            self.detection = self.set_detection() # *Args {cursor: list, hitcircle: list}
        else:
            print(f"Failed to load {self.CONFIG_PATH}!")
        
        return self   
    
    def load(self, config_name: str):
            
            if config_name in self.get_local_configs():
                self.CONFIG_PATH = f"{self.CONFIG_FOLDER}\\{config_name}"
                return self.get()
            else:
                return False
    
    def reset(self, config_name: str = None):
        
        if config_name:
            old_config = self.CONFIG_PATH
            self.CONFIG_PATH = f"{self.CONFIG_FOLDER}\\{config_name}"
        
        with open(self.CONFIG_PATH, "w") as file:
            config = {
                "menu_color": "pastel_pink",
                "aim_assist": {
                    "enabled": True,
                    "min_area": 10,
                    "strength": 0.07,
                    "range": 400,
                    "compute": "cpu"
                },
                "detection": {
                    "cursor": [221,50,50],
                    "hitcircle": [237,3,205]
                },
                "visuals": {
                    "cursor": {
                        "enabled": True,
                        "color": [221,50,50],
                        "thickness": 2
                    },
                    "hitcircle": {
                        "enabled": True,
                        "color": [237,3,205],
                        "thickness": 2
                    }
                },
            }
            
            json.dump(config, file, indent=4)
            
            if config_name:
                self.CONFIG_PATH = old_config
                
            return True
        
    def create(self, config_name: str):
            
            if config_name in self.get_local_configs():
                return False
            else:
                with open(f"{self.CONFIG_FOLDER}\\{config_name}", "w") as file:
                    config = {
                        "menu_color": "pastel_pink",
                        "aim_assist": {
                            "enabled": True,
                            "min_area": 10,
                            "strength": 0.07,
                            "range": 400,
                            "compute": "cpu"
                        },
                        "detection": {
                            "cursor": [221,50,50],
                            "hitcircle": [237,3,205]
                        },
                        "visuals": {
                            "cursor": {
                                "enabled": True,
                                "color": [221,50,50],
                                "thickness": 2
                            },
                            "hitcircle": {
                                "enabled": True,
                                "color": [237,3,205],
                                "thickness": 2
                            }
                        },
                    }
                    
                    json.dump(config, file, indent=4)
                    return True
    
    def delete(self, config_name: str):
            
            if config_name in self.get_local_configs():
                os.remove(f"{self.CONFIG_FOLDER}\\{config_name}")
                return True
            else:
                return False
    
    def save(self, aim: dict = None, menu: dict= None, visuals: dict= None, detection: dict= None, config_name: str = None):
        
        if all([aim, menu, visuals, detection]):
            pass
        else:
            if not aim:
                aim = self.set_aim()
            if not menu:
                menu = self.set_menu()
            if not visuals:
                visuals = self.set_visuals()
            if not detection:
                detection = self.set_detection()
        
        config = {
            "menu_color": menu["color"],
            "aim_assist": {
                "enabled": aim["enabled"],
                "min_area": aim["min_area"],
                "strength": aim["strength"],
                "range": aim["range"],
                "compute": aim["compute"]
            },
            "detection": {
                "cursor": detection["cursor"],
                "hitcircle": detection["hitcircle"]
            },
            "visuals": {
                "cursor": {
                    "enabled": visuals["cursor"]["enabled"],
                    "color": visuals["cursor"]["color"],
                    "thickness": visuals["cursor"]["thickness"]
                },
                "hitcircle": {
                    "enabled": visuals["hitcircle"]["enabled"],
                    "color": visuals["hitcircle"]["color"],
                    "thickness": visuals["hitcircle"]["thickness"]
                }
            },
        }
        
        if config_name:
            self.old_config = self.CONFIG_PATH
            self.CONFIG_PATH = f"{self.CONFIG_FOLDER}\\{config_name}"
        
        try:
            with open(self.CONFIG_PATH, "w") as file:
                json.dump(config, file, indent=4)
            return True
        except Exception as e:
            print(f"Failed to update {self.CONFIG_PATH}! {e}")
            return False
        
        if config_name:
            self.CONFIG_PATH = self.old_config
    
    def set_aim(self):
        
        enabled = self.config["aim_assist"]["enabled"]
        min_area = self.config["aim_assist"]["min_area"]
        strength = self.config["aim_assist"]["strength"]
        aim_range = self.config["aim_assist"]["range"]
        compute = self.config["aim_assist"]["compute"]
        
        return {"enabled": enabled, "min_area": min_area, "strength": strength, "range": aim_range, "compute": compute}
    
    def set_menu(self):
        color = self.config["menu_color"]
        return {"color": color}
    
    def set_visuals(self):
        cursor_enabled = self.config["visuals"]["cursor"]["enabled"]
        cursor_color = self.config["visuals"]["cursor"]["color"]
        cursor_thickness = self.config["visuals"]["cursor"]["thickness"]
        hitcircle_enabled = self.config["visuals"]["hitcircle"]["enabled"]
        hitcircle_color = self.config["visuals"]["hitcircle"]["color"]
        hitcircle_thickness = self.config["visuals"]["hitcircle"]["thickness"]
        return {"cursor": {"enabled": cursor_enabled, "color": cursor_color, "thickness": cursor_thickness}, "hitcircle": {"enabled": hitcircle_enabled, "color": hitcircle_color, "thickness": hitcircle_thickness}}
        
    def set_detection(self):
        cursor_color = self.config["detection"]["cursor"]
        color = self.config["detection"]["hitcircle"]
        return {"cursor": cursor_color, "hitcircle": color}
