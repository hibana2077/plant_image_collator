from fastapi import FastAPI
from pymongo import MongoClient
from os import getenv

app = FastAPI()
mongo = MongoClient(f"mongodb://{getenv('MONGO_INITDB_ROOT_USERNAME')}:{getenv('MONGO_INITDB_ROOT_PASSWORD')}@db:27017/")


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/photo")
async def photo(payload: dict):
    image = payload["photo"]
    time = payload["time"]
    plant_name = payload["plant_name"]
    node_name = payload["node_name"]
    if not image or not time or not plant_name:return {"message": "fail"}
    db = mongo["plant_image_collator"]
    collection = db["photo"]
    collection.insert_one({
        "image": image,
        "time": time,
        "plant_name": plant_name,
        "node_name": node_name
    })
    return {"message": "success"}

@app.post("/status")
async def status(payload: dict):
    cpu = payload["cpu"]
    memory = payload["memory"]
    time = payload["time"]
    node_name = payload["node_name"]
    if not cpu or not memory or not time or not node_name:return {"message": "fail"}
    db = mongo["plant_image_collator"]
    collection = db["status"]
    collection.insert_one({
        "cpu": cpu,
        "memory": memory,
        "time": time,
        "node_name": node_name
    })
    return {"message": "success"}

@app.post("/error")
async def error(payload: dict):
    error = payload["error"]
    time = payload["time"]
    node_name = payload["node_name"]
    if not error or not time or not node_name:return {"message": "fail"}
    db = mongo["plant_image_collator"]
    collection = db["error"]
    collection.insert_one({
        "error": error,
        "time": time,
        "node_name": node_name
    })
    return {"message": "success"}


@app.get("/photo")
async def photo():
    db = mongo["plant_image_collator"]
    collection = db["photo"]
    result = collection.find()
    return_data = []
    for item in result:
        return_data.append({
            "image": item["image"],
            "time": item["time"],
            "plant_name": item["plant_name"],
            "node_name": item["node_name"]
        })
    return return_data

@app.get("/status")
async def status():
    db = mongo["plant_image_collator"]
    collection = db["status"]
    result = collection.find()
    return_data = []
    for item in result:
        return_data.append({
            "cpu": item["cpu"],
            "memory": item["memory"],
            "time": item["time"],
            "node_name": item["node_name"]
        })
    return return_data[-500:] if len(return_data) > 500 else return_data

@app.get("/error")
async def error():
    db = mongo["plant_image_collator"]
    collection = db["error"]
    result = collection.find()
    return_data = []
    for item in result:
        return_data.append({
            "error": item["error"],
            "time": item["time"],
            "node_name": item["node_name"]
        })
    return return_data
