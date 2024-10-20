# DECO3500
### cox
1. Download the required packages using `python -m pip install pygame pyserial`.
2. Search for and open "Device Manager" to check the ports if you're on Windows.
* ![image](https://github.com/user-attachments/assets/c2bd94f3-81cb-4ded-a3a1-6d2682410539)
3. On Mac or Linux, use the command `dmesg | grep tty`.
4. Ensure both Arduinos are connected to your device.
5. Once connected, check again; the two new devices that appear will be the COM numbers for the Arduinos.
6. Ensure you're in the correct directory with `cd cox`.
7. Edit drum.py to ensure the COM port matches the incoming device.
8. Save the changes.
9. Run the file using `python new.py`.

### Arduino
1. connect the ultrasound sensor and LED light on the port according to the script
* TRIG_PIN 9
* ECHO_PIN 10
* LED_PIN 13 
2. stick the device on the back of the rowing machine
3. connect to the device running cox 

### Unity 
1. Open the project in Unity

2. Launch Unity Hub and select the appropriate version of Unity.

3. Install any required packages:
   Go to Window > Package Manager and ensure all necessary packages are installed
4. Press Play to run the project in the Unity Editor.
