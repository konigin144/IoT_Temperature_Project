# Notes

* Use serial_reader.read() function to get temeprature as float from Arduino.
* Arduino should use ```Serial.println()``` to send temperature as float.
* Set baudrate on Arduino to match serial_reader.BAUDRATE. Use ```Serial.begin(115200)```.
* Check what device file was assigned to arduino after connecting it. New file should appear in /dev directory. Change serial_reader.PORT if needed.
* Default timeout is 1 second. Remember it when setting delay on Arduino.
