from fastapi import FastAPI, Request
from pydantic import BaseModel
import datetime

app = FastAPI()

class IPLogEntry(BaseModel):
    ip_address: str
    timestamp: datetime.datetime
    caller_url: str

ip_log: list[IPLogEntry] = []

# @app.middleware("http")
# async def log_client_ip(request: Request, call_next):
#     # Get client's IP address
#     client_ip = request.client.host
#     # Log the IP address with current timestamp
#     ip_log.append(IPLogEntry(ip_address=client_ip, timestamp=datetime.datetime.now()))
#     response = await call_next(request)
#     return response

@app.get("/ip-log", response_model=list[IPLogEntry])
async def get_ip_log():
    """
    Retrieve the list of logged IP addresses and their timestamps.
    """
    return ip_log

@app.get("/show-my-ip", response_model=IPLogEntry)
async def show_my_ip(request: Request):
    """
    Log the client's IP address and return it.
    """
    # Get client's IP address
    client_ip = request.client.host
    
    # Log the IP address with current timestamp
    ip_log.append(IPLogEntry(ip_address=client_ip, timestamp=datetime.datetime.now(), caller_url=str(request.url)))

    return IPLogEntry(ip_address=client_ip, timestamp=datetime.datetime.now(), caller_url=str(request.url))

@app.get("/")
async def root():
    return {"message": "Welcome to the IP Logger API"}
