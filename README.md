Make sure you have the following installed:

- python 3.x
- virtualenv

Execute these commands to run the application:
```
> virtualenv env
> source ./env/bin/activate
> pip install -r requirements.txt
> python main.py -d <device_id>
```

Where the `device_id` is the name of the serial port on which the arduino is connected. 
The easiest way to find it out is to launch the Arduino IDE and in the you search for it `Tools -> Port` menu, it will be something like `/dev/cu.usbmodem14411` on a Mac.
