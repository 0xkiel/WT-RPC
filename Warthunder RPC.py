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

WW2_GERMAN_ARRAY = (

    "pzkpfw",

    "panther_ii",
    "vk_3002m",
    "nbfz_vi",

    "panzerjager_",
    "jgdpz_",
    "pz_iv_l70",
    "pzsfl",
    "stug_iii_",
    "stuh_iii_",
    "sturmpanzer_",
    "sturmmorser_sturmtiger",

    "panzerwerfer_42",
    "sdkfz_",
    "flakpanzer_",
    "vsw_flak_41",
    "waffentrager_krupp_steyr",
    "panzerbefelhswagen_",

    "amd_35_kwk",
    "kv_1_kwk_40",
    "kv_2_754r",
    "t_34_747",
    "infanterie_kampfpanzer_churchill",

    "tiger_ost",
    "tiger_west",

    "us_m4a2_1944_germ",
)

WW2_SOVIET_ARRAY = (
      "bt",

      "t_26",
      "t_28",
      "t_35",
      "t_50",
      "t_60",
      "t_70",
      "t_126",
      "rbt_5",
      "smk",

      "t_34",

      "kv",

      "is",

   
      "zis",
      "su",
      "isu",

      "gaz",
      "yag",

      "zut",

      "m_8_24",
      "bm_13n",
      "bm_31_12",
      "ba",

      "a_12",
      "m3c",
      "m4a2_76w_sherman",

      "pzkpfw_iii_ausf_j_l42",
      "pzkpfw_v",
      "sdkfz_251_21_kit_3rank",

)

WW2_ITALY_ARRAY = (
      "ab",
      "as",
      "breda_52_autocannone",
      "l3_cc",
      "l6",
      "lancia3ro_100",
      "m11_39",
      "m13_40",
      "m14_41",
      "m15_42",
      "m18_hellcat",
      "m24_chaffee",
      "m26_ariete",
      "m3a3_stuart",
      "m36b1",
      "m4a4_sherman",
      "p_26_40",
      "p_40",
      "pzkpfw",
      "sahariano",
      "semovente_breda_501",
      "semovente_l40",
      "semovente_m41",
      "semovente_m42",
      "semovente_m43",
      
      "sherman_75_37",
      "sherman_vc_firefly",
      "sherman_vii",
      "stug_iii_ausf_g",
      "39m_csaba",
      "toldi_ii_a",
      "40m_turan_1",
      "41m_turan_2",
      "43m_turan_3",
      "44m_zrinyi_1",
      "40_43m_zrinyi_2",
)



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
                     if tank_name.startswith(WW2_GERMAN_ARRAY):
                          tank_name = tank_name.upper().replace("_", " ")
                          ShorterRPC("ww2ger")
                     else:                  
                        tank_name = tank_name.upper().replace("_", " ")
                        ShorterRPC("ger")
                  
       

               elif IndicatorData["type"].startswith("tankModels/ussr_") and Hangar is False:
                     tank_name = IndicatorData["type"].replace("tankModels/ussr_", "")
            
                     if tank_name.startswith(WW2_SOVIET_ARRAY):
                        tank_name = tank_name.upper().replace("_", " ")
                        ShorterRPC("ru")
                     else:                  
                        tank_name = tank_name.upper().replace("_", " ")
                        ShorterRPC("russia")
       


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
                     if tank_name.startswith(WW2_ITALY_ARRAY):
                        tank_name = tank_name.upper().replace("_", " ")
                        ShorterRPC("ww2it")
                     else:                  
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
  