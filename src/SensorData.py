import threading

class SensorData:
    """ Thread safe class to store data read from the sensor """

    def __init__(self):
        self.lock = threading.Lock()
        self.gyro = []
        self.acceleration = []
        self.mag = []
    
    def add_gyro(self, data):
        with self.lock:
            self.gyro.append(data)
    
    def get_gyro(self):
        with self.lock:
            return list(self.gyro)

    def add_acceleration(self, data):
        with self.lock:
            self.acceleration.append(data)

    def get_acceleration(self):
        with self.lock:
            return list(self.acceleration)

    def add_mag(self, data):
        with self.lock:
            self.mag.append(data)

    def get_mag(self):
        with self.lock:
            return list(self.mag)
