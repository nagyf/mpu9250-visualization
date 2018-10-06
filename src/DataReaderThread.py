import threading
import time

class DataReaderThread(threading.Thread):
    """ 
    Reads data from the sensor on a serial port on a separate thread.

    Currently it expects that Arduino sends the data line-by-line, each data field separated by a semicolon: ';'.
    The first 3 numbers must be the acceleration data, the second 3 must be the gyroscope data, and the third block
    must contain the magnetometer data.
    """

    def __init__(self, port, data):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self.port = port
        self.data = data

    def stop(self):
        """ Stops the thread """
        self._stop_event.set()

    def stopped(self):
        """ Checks if the thread is stopped or not """
        return self._stop_event.is_set()

    def run(self):
        """ Read values from the sensor until the thread is stopped """
        while(not self.stopped()):
            try:
                values = read_values(self.port)
                self.data.add_acceleration((values[0], values[1], values[2]))
                self.data.add_gyro((values[3], values[4], values[5]))
                self.data.add_mag((values[6], values[7], values[8]))
                time.sleep(0.05)
            except (ValueError, IndexError) as e:
                # TODO don't know why it's happening
                # Sometimes I get invalid data from the sensor
                print('WARNING: ', e)

def read_values(port):
    """ Reads sensor data and parses it """
    raw_line = port.readline()
    line = raw_line.decode('utf8').strip()
    values = map(lambda x: float(x), line.split(';'))
    return list(values)