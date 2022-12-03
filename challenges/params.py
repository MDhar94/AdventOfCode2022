import os
import datetime

# LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))

LOCAL_DATA_PATH = os.environ.get("LOCAL_DATA_PATH")
LOCAL_TOKEN_PATH = os.environ.get("TOKEN_PATH")


#get current time
CURRENT_DAY_OF_MONTH = datetime.datetime.now().strftime("%d")
