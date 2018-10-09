import sys
import getopt
from src.DataReaderThread import DataReaderThread
from src.SensorData import SensorData
from src.Plotter import Plotter
from src.SerialDataInput import SerialDataInput
from src.CsvDataOutput import CsvDataOutput

def main():
    """
    The main function of the app, starts reading from the device and plotting it.

    The reading and the drawing is done on separate threads. Communication between the threads is 
    done through the SensorData class.
    """
    device, baud, outfile = parse_arguments()
    data = SensorData()
    input = SerialDataInput(device, baud)
    output = CsvDataOutput(outfile) if outfile else None
    thread = DataReaderThread(input, output, data)
    plotter = Plotter(data)

    try:
        thread.start()
        plotter.start() # Will block here until exit

        # Stop the data reading thread after matplotlib exited
        thread.stop()
    except (KeyboardInterrupt, SystemExit):
        thread.stop()
        sys.exit()

def usage():
    """ Prints usage information """
    print('main.py -d <device> -b <baud_rate> -o <output_file>')

def parse_arguments():
    """
    Parses command line arguments, returns a tuple with the device name and the baud rate.
    """
    try:
      opts, args = getopt.getopt(sys.argv[1:],'hd:b:o:',['device=','baud=', 'output='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    device = None
    baud = 115200
    outfile = None
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-d', '--device'):
            device = a
        elif o in ('-b', '--baud'):
            baud = a
        elif o in ('-o', '--output'):
            outfile = a
        else:
            assert False, 'unhandled option'
    
    return (device, baud, outfile)
