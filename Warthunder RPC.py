import time 

from pypresence import Presence
from pypresence.exceptions import PipeClosed
import requests
import json
from json import JSONDecodeError
from pypresence.exceptions import DiscordNotFound

MAP_INFO = "http://localhost:8111/map_info.json"
INDICATOR = "http://localhost:8111/indicators"
CLIENT_ID = "1524869509922553946"
RPC = Presence(CLIENT_ID)
RPC.connect()    
start = int(time.time())

Hangar = False
TankCheck = False
WTloaded = False

def ShorterRPC(county):
   RPC.update(
        large_image = "hanger", 
        small_image = county,
        small_text= tank_name, 
        state = f"Using: {tank_name}", 
        details="In Battle",
        name="WarThunder(WT)",
        start=start,
   )   
   time.sleep(0.01)



while True:
     try:        

        MapData = requests.get(MAP_INFO, timeout=3).json()
        IndicatorData = requests.get(INDICATOR, timeout=3).json()

        if MapData["valid"] == False:
           RPC.update(
         large_image = "hanger", 
         details="In Hangar",
         name="WarThunder(WT)",
         start=start,
         ) 
     
        Hangar = True
     

        if  MapData["valid"] is True: 
            Hangar = False
     
        if IndicatorData["valid"] == False:
            TankCheck = True

        elif IndicatorData["valid"] != False:
            TankCheck = False

        if TankCheck and Hangar != True:
           RPC.update(
             large_image = "hanger", 
             state = "Using: Unknown Aircraft",
             details="In Battle",
             name="WarThunder(WT)",
             start=start,
            ) 


        if TankCheck != True:
               WTloaded = True
               if IndicatorData["type"].startswith("tankModels/cn_") and Hangar is False:
                    tank_name = IndicatorData["type"].replace("tankModels/cn_", "")
                    tank_name = tank_name.upper().replace("_", " ")
                    ShorterRPC("cn")
          

               elif IndicatorData["type"].startswith("tankModels/us_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/us_", "")
                     tank_name = tank_name.upper().strip().replace("_", " ")
                     ShorterRPC("us")
      
       

               elif IndicatorData["type"].startswith("tankModels/germ_") and Hangar is False:
                     tank_name = IndicatorData["type"].strip().replace("tankModels/germ_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("ger")
             
       

               elif IndicatorData["type"].startswith("tankModels/ussr_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/ussr_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("ru")
       


               elif IndicatorData["type"].startswith("tankModels/uk_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/uk_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("uk")
                 


               elif IndicatorData["type"].startswith("tankModels/jp_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/jp_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("jp")
                  

               elif IndicatorData["type"].startswith("tankModels/it_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/it_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("it")
       
       
               elif IndicatorData["type"].startswith("tankModels/fr_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/fr_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("fr")

               elif IndicatorData["type"].startswith("tankModels/sw_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/sw_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("sw")
                  
               elif IndicatorData["type"].startswith("tankModels/il_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/il_", "")
                     tank_name = tank_name.upper().replace("_", " ")
                     ShorterRPC("il")

     except DiscordNotFound:
          pass

     except (ValueError, requests.exceptions.JSONDecodeError, requests.exceptions.ReadTimeout, TypeError, JSONDecodeError, requests.exceptions.ConnectionError):
            RPC.clear()
            time.sleep(5)
            start = int(time.time())
            pass
     
     except PipeClosed:
          pass
  