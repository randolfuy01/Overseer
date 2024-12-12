from fastapi import FastAPI
from Lightweight.monitor_server import Light_weight_monitor

app = FastAPI()

@app.get("/light_log")
async def root():
    monitor = Light_weight_monitor()
    return monitor.oversight(1)
    