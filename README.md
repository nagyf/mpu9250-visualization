# Introduction
This python application can be used to process the data read by [mpu9250-arduino](https://github.com/nagyf/mpu9250-arduino) and display the sensor data using [matplotlib](https://matplotlib.org/).

# Install dependencies

Make sure you have the following installed:

- python 3.x
- virtualenv

Execute these commands to run the application:
```
> virtualenv env
> source ./env/bin/activate
> pip install -r requirements.txt
```

# Run the application

The command is: `python main.py -d <device_id> -b <data_rate> -o <test_csv_file>`

Where: 

- `device_id` is the name of the serial port on which the arduino is connected. The easiest way to find it out is to launch the Arduino IDE and in the you search for it `Tools -> Port` menu, it will be something like `/dev/cu.usbmodem14411` on a Mac.
- `baud_rate` is the data rate used to communicate on the serial port
- `test_csv_file` is the filename of a file to write data to (this parameter is optional).

Examples:

```
# Basic example
> python main.py -d /dev/cu.usbmodem14411

# Specify different data rate (the default is 115200)
> python main.py -d /dev/cu.usbmodem14411 -b 9600

# Specify an output file
> python main.py -d /dev/cu.usbmodem14411 -o data.csv
```
