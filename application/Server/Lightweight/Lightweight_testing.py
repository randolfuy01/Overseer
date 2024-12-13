import unittest
from monitor_server import Light_weight_monitor


class TestLightweightMonitor(unittest.TestCase):
    
    def setUp(self):
        self.monitor = Light_weight_monitor()
        
    def check_bounds(self, metric, value, lower_bound, upper_bound):
        ''' 
        Bound checking for metrics
        '''
        self.assertIsInstance(value, (int, float), f"{metric} value should be int or float but got {type(value).__name__}")
        self.assertGreaterEqual(value, lower_bound, f"{metric} value {value} is below the lower bound of {lower_bound}")
        self.assertLessEqual(value, upper_bound, f"{metric} value {value} exceeds the upper bound of {upper_bound}")
    
    def test_cpu(self):
        print("Testing CPU metrics...")
        cpu = self.monitor.get_cpu()
        print("Current CPU: ", cpu)
        self.check_bounds("CPU", cpu, 0, 100)
        print("CPU test passed")

    def test_memory(self):
        print("Testing Memory metrics...")
        memory = self.monitor.get_memory()
        print("Current Memory: ", memory)
        self.check_bounds("Memory", memory, 0, 100)
        print("Memory test passed")

    def test_disk(self):
        print("Testing Disk metrics...")
        disk = self.monitor.get_disk()
        print("Current Disk: ", disk)
        self.check_bounds("Disk", disk, 0, 100)
        print("Disk test passed")

    def test_network(self):
        print("Testing Network metrics...")
        network = self.monitor.get_network()
        print("Current Network: ", network)
        self.assertIsInstance(network, (int, float), f"Network value should be int or float but got {type(network).__name__}")
        self.assertGreaterEqual(network, 0, f"Network value {network} is below 0")
        print("Network test passed")

    def test_process(self):
        print("Testing Process metrics...")
        process = self.monitor.get_process()
        print("Current Processes: ", process)
        self.assertIsInstance(process, (int, float), f"Process value should be int or float but got {type(process).__name__}")
        self.assertGreaterEqual(process, 0, f"Process value {process} is below 0")
        print("Process test passed")
        
    def test_aggregator_seconds(self):
        aggregated_data: dict = self.monitor.aggregator_seconds(5)
        expected_keys = ["cpu", "memory", "disk", "network", "process"]
        self.assertIsInstance(aggregated_data, dict, "Aggregator should return a dictionary")
        for key in aggregated_data:
            if key not in expected_keys:
                self.fail(f"Unexpected key {key} in aggregated data")
            self.assertIsInstance(aggregated_data[key], (int, float), f"{key} value should be int or float but got {type(aggregated_data[key]).__name__}")
            print(f"aggregated {key}: {aggregated_data[key]}")
        print("Aggregator seconds test passed")
        
if __name__ == '__main__':
    unittest.main()
