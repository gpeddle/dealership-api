import os
from datetime import datetime

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from backend.data.local import LocalDataStore

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",  # React's default port
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["X-Total-Count"]  # Exposes X-Total-Count header to the frontend
)

# Use environment variable to determine the data store type (local or AWS)
data_store_type = os.environ.get("DATA_STORE_TYPE", "local")

if data_store_type == "local":
    data_store = LocalDataStore('local_store')
elif data_store_type == "aws":
    raise NotImplementedError("AWS data store not implemented yet")

# TODO: Add Auth

# Define routes and handlers
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Dealership API"}

@app.get("/config/{config_name}")
async def read_config(config_name: str):
    config_data = data_store.read_config(config_name)
    if config_data:
        return config_data
    else:
        return Response(status_code=404)

@app.put("/config/{config_name}")
async def update_config(config_name: str, data: dict):
    # TODO validate the config data
    data_store.write_config(config_name, data)
    return Response(status_code=204)

@app.post("/config/{config_name}")
async def create_config(config_name: str, data: dict):
    # DO not allow creating a new config 
    # TODO handle this using http error instead of raising exception
    return Response(status_code=405)
    #raise NotImplementedError("Create config not implemented.")


@app.get("/config")
async def list_configs(response: Response):
    config_list = data_store.list_configs()
    data = []
    for config_descriptor in config_list:
        data.append(config_descriptor)
    response.headers['X-Total-Count'] = str(len(config_list)) 
    return data
