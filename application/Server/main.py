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

app = FastAPI()

@app.get("/light_log")
async def root():
    server_logger = Light_weight_monitor()
    aggregated_data = server_logger.aggregator_seconds(5)
    return aggregated_data
    
    
def main():
    print("yello")
    
if __name__ == "__main__":
    main()