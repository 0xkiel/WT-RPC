import time 
from pypresence import Presence
import requests
import json
from json import JSONDecodeError
import socket
import ctypes
import sys
from pypresence.exceptions import DiscordNotFound

MAP_INFO = "http://localhost:8111/map_info.json"
INDICATOR = "http://localhost:8111/indicators"
CLIENT_ID = "1524869509922553946"
RPC = Presence(CLIENT_ID)
RPC.connect()

start = int(time.time())

Hanger = False
TankCheck = False
GameCheck = False
while True:
     try:

        MapData = requests.get(MAP_INFO, timeout=3).json()
        IndicatorData = requests.get(INDICATOR, timeout=3).json()

        if MapData["valid"] == False:
           RPC.update(
         large_image = "hanger", 
         details="In Hanger",
         name="WarThunder(WT)",
         start=start,
         ) 
     
        Hanger = True

        if  MapData["valid"] is True: 
            Hanger = False
     
        if IndicatorData["valid"] == False:
            TankCheck = True

        elif IndicatorData["valid"] != False:
            TankCheck = False

        if TankCheck and Hanger != True:
           RPC.update(
             large_image = "hanger", 
             state = "Using: Unknown Aircraft",
             details="In Battle",
             name="WarThunder(WT)",
             start=start,
            ) 


        if TankCheck != True:
               if IndicatorData["type"].startswith("tankModels/cn_") and Hanger is False:
                    tank_name = IndicatorData["type"].replace("tankModels/cn_", "")
                    tank_name = tank_name.upper()
                    RPC.update(
                    large_image = "hanger", 
                    small_image = "cn",
                    small_text= tank_name,
                    state = f"Using: {tank_name}",
                    details="In Battle",
                    name="WarThunder(WT)",
                    start=start,
                    )
                    time.sleep(0.01)

               elif IndicatorData["type"].startswith("tankModels/us_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/us_", "")
                     tank_name = tank_name.upper().strip()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "us",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,
              
                     )
                     time.sleep(0.01)

       

               elif IndicatorData["type"].startswith("tankModels/germ_") and Hanger is False:
                     tank_name = IndicatorData["type"].strip().replace("tankModels/germ_", "")
                     tank_nameA = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "ger",
                     small_text= tank_name,
                     state = f"Using: {tank_nameA}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,
                     
                     )
                     time.sleep(0.01)

       

               elif IndicatorData["type"].startswith("tankModels/ussr_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/ussr_", "")
                     tank_name = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "ru",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,
                     
                     )
                     time.sleep(0.01)



               elif IndicatorData["type"].startswith("tankModels/uk_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/uk_", "")
                     tank_name = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "uk",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,
              
                     )
                     time.sleep(0.01)



               elif IndicatorData["type"].startswith("tankModels/jp_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/jp_", "")
                     tank_name = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "jp",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,
                     
                     )
                     time.sleep(0.01)


               elif IndicatorData["type"].startswith("tankModels/it_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/it_", "")
                     tank_name = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "it",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,

                     )
                     time.sleep(0.01)

       
               elif IndicatorData["type"].startswith("tankModels/fr_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/fr_", "")
                     tank_name = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "fr",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,
                     
                     )
                     time.sleep(0.01)

       

               elif IndicatorData["type"].startswith("tankModels/sw_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/sw_", "")
                     tank_name = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "sw",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,

                     )
                     time.sleep(0.01)

               elif IndicatorData["type"].startswith("tankModels/il_") and Hanger is False:
                     tank_name = IndicatorData["type"].replace("tankModels/il_", "")
                     tank_name = tank_name.upper()
                     RPC.update(
                     large_image = "hanger", 
                     small_image = "il",
                     small_text= tank_name,
                     state = f"Using: {tank_name}",
                     details="In Battle",
                     name="WarThunder(WT)",
                     start=start,
                     )
                     time.sleep(0.01)

     except (ValueError, requests.exceptions.JSONDecodeError, requests.exceptions.ReadTimeout, TypeError, JSONDecodeError ):

            pass

     except requests.exceptions.ConnectionError:
            import tkinter as tk
            from tkinter import messagebox

            root = tk.Tk()
            root.withdraw()

            messagebox.showinfo("ERROR", "warthunder localhost didnt start in time rerun again terminating py")
            RPC.clear()
            sys.exit(0)
            


