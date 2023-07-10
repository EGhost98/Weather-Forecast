import os 
from dotenv import load_dotenv
load_dotenv()
local_data_expiration = os.environ.get("LOCAL_DATA_EXPIRATION")
if local_data_expiration is None or local_data_expiration == "":
    local_data_expiration = 600

print(local_data_expiration)