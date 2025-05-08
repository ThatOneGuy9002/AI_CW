import pymongo
import uuid

from datetime import datetime

myClient = pymongo.MongoClient("mongodb+srv://users:FFSUZvTMuNC972xZ@aicw2.uta66cx.mongodb.net/?retryWrites=true&w=majority&appName=AICW2")

db = myClient["chatbotDB"]
stations = db["stations"]
messages = db["conversation_history"]

def get_history(conversation_id):
    history = messages.find({"conversation_id": conversation_id}).sort("timestamp", 1)
    return [
        {
            "role": h.get("role", "user"),
            "text": h.get("text", ""),
            "timestamp": h.get("timestamp")
        }
        for h in history
    ]

def create_message(role, text, conversation_id):
    messages.insert_one({
        "conversation_id": conversation_id,
        "role": role,
        "text": text,
        "timestamp": datetime.utcnow()
    })

# Convo functions

def get_convos():
    return messages.distinct("conversation_id")

def delete_convo(id):
    messages.delete_many({"conversation_id": id})
    

# stations.insert_one({
#     "code": "NRW",
#     "name": "Norwich",
#     "location": {"lat" : 52.62, "lon": 1.29}
# })

# station = stations.find_one({"code": "NRW"})
# print(station["name"])  # Output: Norwich