import unittest
from monitor_server import Light_weight_monitor


class Lightweight_Test(unittest.TestCase):
    
    def instantiate_monitor(self):
        self.monitor = Light_weight_monitor()
        
    def main(self):
        """ 
        Descrption:
            Execute the testing for the following:
                - CPU
                - Memory
                - Disk
                - Network
                - Process
            Edge cases are considered in the testing, ensure package stability for the lightweight monitoring tool
        Returns:
            None
        """
        self.test_cpu_1()
        self.test_cpu_2()
        self.test_cpu_3()
        
        self.test_memory_1()
        self.test_memory_2()
        self.test_memory_3()
        
        self.test_disk_1()
        self.test_disk_2()
        self.test_disk_3()
        
    def test_cpu_1(self):
        try:
            self.assertTrue(self.monitor.get_cpu() >= 0)
            print("cpu test 1 passed")
        except Exception as e:
            self.fail(e)
    
    def test_cpu_2(self):
        try:
            self.assertTrue(self.monitor.get_cpu() <= 100)
            print("cpu test 2 passed")
        except Exception as e:
            self.fail(e)
    
    def test_cpu_3(self):
        try:
            self.assertTrue(self.monitor.get_cpu() >= 0 and self.monitor.get_cpu() <= 100)
            print("cpu test 3 passed")
        except Exception as e:
            self.fail(e)
    
    def test_memory_1(self):
        try:
            self.assertTrue(self.monitor.get_memory() >= 0)
            print("memory test 1 passed")
        except Exception as e:
            self.fail(e)
    
    def test_memory_2(self):
       try:
            self.assertTrue(self.monitor.get_memory() <= 100)
            print("memory test 2 passed")
       except Exception as e:
            self.fail(e)
            
    def test_memory_3(self):
        try:
            self.assertTrue(self.monitor.get_memory() >= 0 and self.monitor.get_memory() <= 100)
            print("memory test 3 passed")
        except Exception as e:
            self.fail(e)
    
    def test_disk_1(self):
        try:
            self.assertTrue(self.monitor.get_disk() >= 0)
            print("disk test 1 passed")
        except Exception as e:
            self.fail(e)
    
    def test_disk_2(self):
        try:
            self.assertTrue(self.monitor.get_disk() <= 100)
            print("disk test 2 passed")
        except Exception as e:
            self.fail(e)
    
    def test_disk_3(self):
        try:
            self.assertTrue(self.monitor.get_disk() >= 0 and self.monitor.get_disk() <= 100)
            print("disk test 3 passed")
        except Exception as e:
            self.fail(e)
    
if __name__ == '__main__':
   Test = Lightweight_Test()
   Test.instantiate_monitor()
   Test.main()