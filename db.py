import pymongo
from datetime import datetime

myClient = pymongo.MongoClient("mongodb+srv://users:FFSUZvTMuNC972xZ@aicw2.uta66cx.mongodb.net/?retryWrites=true&w=majority&appName=AICW2")

db = myClient["chatbotDB"]
stations = db["stations"]
messages = db["conversation_history"]

def create_message(role, text):
    messages.insert_one({
        "role": role,
        "text": text,
        "timestamp": datetime.utcnow()
    })

def get_history():
    history = messages.find().sort("timestamp" , 1)
    return [{"role": h["role"], "text":h["text"]} for h in history]

# stations.insert_one({
#     "code": "NRW",
#     "name": "Norwich",
#     "location": {"lat" : 52.62, "lon": 1.29}
# })

# station = stations.find_one({"code": "NRW"})
# print(station["name"])  # Output: Norwich