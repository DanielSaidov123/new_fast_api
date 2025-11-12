import json
import os

DATA_PATH = "data.json"

# כתוב פונקציה שקוראת את תוכן הקובץ JSON
def read_data():
    if not os.path.exists(DATA_PATH):
        return []
    try:
        with open(DATA_PATH,"r")as r:
            text=json.load(r)
        return text
    except:
        print(" קובץ קיים אבל לא טוב")

# כתוב פונקציה ששומרת נתונים לקובץ JSON
def write_data(data):
    with open(DATA_PATH,"w") as w:
        json.dump(data,w,indent=3)