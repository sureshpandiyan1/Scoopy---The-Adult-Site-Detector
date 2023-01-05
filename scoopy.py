import runpy, time
from tkinter import *


scoopy = """
   _____                                                                                                    
  / ___/_________  ____  ____  __  __                                                                       
  \__ \/ ___/ __ \/ __ \/ __ \/ / / /                                                                       
 ___/ / /__/ /_/ / /_/ / /_/ / /_/ /                                                                        
/____/\___/\____/\____/ .___/\__, /                                                                         
  ________           /_/_   /____/      ____     _____ _ __          ____       __            __            
 /_  __/ /_  ___     /   | ____/ /_  __/ / /_   / ___/(_) /____     / __ \___  / /____  _____/ /_____  _____
  / / / __ \/ _ \   / /| |/ __  / / / / / __/   \__ \/ / __/ _ \   / / / / _ \/ __/ _ \/ ___/ __/ __ \/ ___/
 / / / / / /  __/  / ___ / /_/ / /_/ / / /_    ___/ / / /_/  __/  / /_/ /  __/ /_/  __/ /__/ /_/ /_/ / /    
/_/ /_/ /_/\___/  /_/  |_\__,_/\__,_/_/\__/   /____/_/\__/\___/  /_____/\___/\__/\___/\___/\__/\____/_/     
                                                                                                            
scoopy - The Adult Site Detector is very useful to detect a user where addicted by adult site or not.it's highly
very useful for parents who want to monitor a kids were addicted in a adult site. even you can use this to 
analyze behaviour of employee at companies too

Created By Suresh P | Copyright @ Scoopy - The Adult Site Detector
"""


print("scoopy process starting....")
runpy.run_module("comps_scoopy")
print("next processing about the sites what they use..\n \nCHECK SEXUAL ADDICTED OR NOT ? \n")
runpy.run_module("comps_fdrdr")