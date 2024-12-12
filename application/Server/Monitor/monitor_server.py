import psutil
import time


class MonitorServer:
    """
    Lightweight monitoring tool for server
    Supports basic monitoring of CPU, Memory, Disk, Network, and Process
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

    def time_batch(self, time: int) -> tuple:
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
            time.sleep(1)

        return (time, total_cpu, total_memory, total_disk, total_network, total_process)

    def oversight(self, monitor_time: int, threshold: float):
        """
            Monitor the server extensively to ensure that data is being traced correctly over the span of 'time' -> minutes. 
            Returns a json file containing the aggregated time.

        Args:
            monitor_time (int): time to monitor (minutes)
            threshold (float): Server logging to be monitored. Threshold servers as a metric for when to alert user
        """
        
        current_time = time.time()
        end_time = current_time + monitor_time * 60
        
