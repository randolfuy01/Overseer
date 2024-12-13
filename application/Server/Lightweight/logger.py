import psutil
import time
import json
from time import sleep

class Light_weight_monitor:
    """
    Lightweight monitoring tool for server
    Supports basic monitoring of CPU, Memory, Disk, Network, and Process
        - Data is collected in real time
        - Data can be aggregated over a certain period of time
        - Data can be logged to a file
    """

    def __init__(self):
        self.cpu = 0
        self.memory = 0
        self.disk = 0
        self.network = 0
        self.process = 0

    def get_cpu(self) -> float:
        """
            Get the current CPU usage (percentage)

        Returns:
            current_cpu_usage (float): percentage of CPU used
        """
        
        current_cpu_usage = psutil.cpu_percent(interval=1)
        return current_cpu_usage

    def get_memory(self) -> float:
        """
            Get the current memory usage (percentage)

        Returns:
            current_memory_usage(float): percentage of memory used
        """
        
        current_memory_usage = psutil.virtual_memory().percent
        return current_memory_usage

    def get_disk(self) -> float:
        """ 
            Get the current disk usage (percentage)
        
        Returns:
            current_disk_usage(float): percentage of disk used
        """
        
        current_disk_usage = psutil.disk_usage("/").percent
        return current_disk_usage

    def get_network(self) -> float:
        """ 
            Get the current network usage (bytes)
            
        Returns:
            current_network_usage(float): bytes of network used
        """
        
        current_network_usage = (
            psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        )
        return current_network_usage

    def get_process(self) -> int:
        """ 
            Get the current number of processes running (int)
        
        Returns:
            current_process_usage (int): number of processes running
        """
        
        current_process_usage = len(psutil.pids())
        return current_process_usage

    def aggregator_seconds(self, time: int) -> dict:
        """
            Aggregate the monitoring data for a certain period of time

        Args:
            time (int): time to aggregate (seconds)

        Returns:
            _type_: aggregated montitoring data
        """
        timer = time
        total_cpu = 0
        total_memory = 0
        total_disk = 0
        total_network = 0
        total_process = 0

        while timer > 0:
            total_cpu += self.get_cpu()
            total_memory += self.get_memory()
            total_disk += self.get_disk()
            total_network += self.get_network()
            total_process += self.get_process()
            timer -= 1
            sleep(1)

        aggregated_data = dict(
            cpu= total_cpu / time,
            memory= total_memory / time,
            disk= total_disk / time,
            network= total_network,
            process= total_process
        )
        
        return aggregated_data

    def aggregator_minutes(self, monitor_time: int) -> dict:
        """
            Monitor the server extensively to ensure that data is being traced correctly over the span of 'time' -> minutes. 
            Returns a json file containing the aggregated time.

        Args:
            monitor_time (int): time to monitor (minutes)
        """
        
        current_time = time.time()
        end_time = current_time + monitor_time * 60
        
        graph_points_cpu = []
        graph_points_memory = []
        graph_points_disk = []
        graph_points_network = []
        graph_points_process = []        
        
        while current_time < end_time:
            self.alert("../logs/alerts.json")
            current_time = time.time()
            graph_points_cpu.append(self.get_cpu())
            graph_points_memory.append(self.get_memory())
            graph_points_disk.append(self.get_disk())
            graph_points_network.append(self.get_network())
            graph_points_process.append(self.get_process())
            time.sleep(60)
        
        aggregated_data = dict(
            cpu= graph_points_cpu,
            memory= graph_points_memory,
            disk= graph_points_disk,
            network= graph_points_network,
            process= graph_points_process
        )
        
        return aggregated_data
        
    def logger(self, data: dict, filepath: str) -> int:
        """
            Log the monitoring data to a file within the application folder
        Args:
            data (dict): monitoring data
            filename (str): name of the file to save the data
        
        Returns:
            1 on successful logging, 0 on failure
        """

        'Log the current time'
        log_time = ("Log time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        data["log_time"] = log_time
    
        'Json dump the data'
        json_data = json.dumps(data)

        'Save the data to a file'
        try:
            with open(filepath, "w") as file:
                file.write(json_data)
        except:
            print("Failed to log data")
            return 0

        return 1
    
    def alert(self, alertpath: str):
        """
            Alert the user if the server is under heavy load
            
        Args:
            alertpath (str): path to the alert file
        
        Returns:
            VOID
        """
        
        logged_alerts = []
        if self.get_cpu() > 80:
            logged_alerts.append("CPU usage is above 80 percent at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if self.get_memory() > 80:
            logged_alerts.append("Memory usage is above 80 percent at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if self.get_disk() > 80:
            logged_alerts.append("Disk usage is above 80 percent at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if self.get_network() > 1000000:
            logged_alerts.append("Network usage is above 1MB at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if self.get_process() > 100:
            logged_alerts.append("Number of processes is above 100 at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            
        json_data = json.dumps(logged_alerts)
        
        'Save the data to a file'
        
        if json_data is not None:
            try:
                with open(alertpath, "w") as file:
                    file.write(logged_alerts)
            except:
                print("Failed to log data")
                return 0
        return 1