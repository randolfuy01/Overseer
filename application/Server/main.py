'''
Contributors: randolfuy01
'''

'''
Local / Package imports
'''
from Lightweight import Light_weight_monitor

''' 
Global imports
'''
from fastapi import FastAPI
import uvicorn
    
app = FastAPI()

@app.get("/light_log")
async def light_log():
    server_logger = Light_weight_monitor()
    aggregated_data = server_logger.aggregator_seconds(5)  # Ensure this is async if necessary
    return aggregated_data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
