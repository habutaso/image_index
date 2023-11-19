import os 
import ifcfg

from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

NETWORK_INTERFACE = os.getenv("NETWORK_INTERFACE")

ip = ifcfg.interfaces()[NETWORK_INTERFACE]["inet"]
print(ip)

bind = f"{ip}:{str(os.getenv('PORT', '18000'))}"
proc_name = "BottleImageServer"
workers = 1