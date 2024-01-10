import os
from fastapi import FastAPI
from data_access.local_store import LocalStoreDataAccess  

app = FastAPI()


# Use environment variable to determine the data store type (local or AWS)
data_store_type = os.environ.get("DATA_STORE_TYPE", "local")

if data_store_type == "local":
    data_access = LocalStoreDataAccess('local_store')
elif data_store_type == "aws":
    raise NotImplementedError("AWS data store not implemented yet")

# TODO: Add Auth

# Define routes and handlers
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Dealership API"}

@app.get("/config/{config_name}")
async def read_config(config_name: str):
    config_data = data_access.read_config(config_name)
    if config_data:
        return config_data
    else:
        return {"message": "Configuration not found"}

@app.post("/config/{config_name}")
async def create_config(config_name: str, data: dict):
    data_access.write_config(config_name, data)
    return {"message": f"Configuration '{config_name}' created successfully"}

@app.get("/config")
async def list_configs():
    config_list = data_access.list_configs()
    return {"configurations": config_list}
