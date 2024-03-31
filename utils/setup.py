import os
import time

LIBRARIES = {
    ######## *Osu.py Libs ########
    "opencv-python": "cv2",
    "dxcam[cv2]": "dxcam", 
    "pywin32": "win32gui", 
    "keyboard": "keyboard", 
    "numpy" : "numpy",
    "numba": "numba",
    "https://github.com/qb-0/pyMeow/releases/download/1.53.36/pyMeow-1.53.36.zip": "pyMeow",
    ######## *Gui.py Libs ######## 
    "customtkinter": "customtkinter",
    "pillow": "PIL",
}

def installdeps():
    
    global LIBRARIES
    
    try:
        for lib in LIBRARIES:
            try:
                __import__(LIBRARIES[lib])
                print(f"[{time.strftime('%H:%M:%S')}] Already installed {lib}!")
            except:	
                print(f"[{time.strftime('%H:%M:%S')}] Installing {lib}...")
                os.system(f"pip -q install {lib}")
                try:
                    __import__(LIBRARIES[lib])
                    print(f"[{time.strftime('%H:%M:%S')}] Succesfully installed {lib}!")
                except:	
                    print(f"[{time.strftime('%H:%M:%S')}] Failed to install {lib}!")
                    print(f"[{time.strftime('%H:%M:%S')}] Please install {lib} manually!")
        return True             
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Failed to install libraries! {e}")
        return False
                    
                    
if __name__ == "__main__":
    check = installdeps()
    if check:
        print(f"[{time.strftime('%H:%M:%S')}] Installed all libraries!")