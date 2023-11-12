import os 


bind = f"127.0.0.1:{str(os.getenv('PORT', '18000'))}"
proc_name = "BottleImageServer"
workers = 1