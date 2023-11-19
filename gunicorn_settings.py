import os 
import ifcfg

NETWORK_INTERFACE = os.getenv("NETWORK_INTERFACE")

ip = ifcfg.interfaces()[NETWORK_INTERFACE]["inet"]
print(ip)

bind = f"{ip}:{str(os.getenv('PORT', '18000'))}"
proc_name = "BottleImageServer"
workers = 1