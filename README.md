# AMR-Capstone
## Jetbot How-To Guide

### How to Login
- **Username:** `jetbot`
- **Password:** `jetbot`

### How to Use Jetbot Programs in Your Python Code
1. **Pull from Git**
   - Navigate to the git repository: `cd gitRepository/AMR-Capstone/AMR`
   - Pull from git: `git pull`

2. **Access Program**
   - Go to the desired program directory: `cd [directory]`
   - Open the program: `vi [your program].py`

3. **Setup Program**
   - Add the following at the top of the program:
     ```python
     import os
     import sys
     directory = '~/jetbot'
     directory = sys.path.expanduser(directory)
     sys.path.append(directory)
     from Jetbot import [program you want to use]
     ```
   - Save and close the program: Enter `:wq` and press Enter

### How to Add Code to Custom Startup Sequence
- **About Startup Sequence:** Determines what runs as soon as the robot is turned on.
- **Access Startup Program:** `cd gitRepository/AMR-Capstone/AMR`
- **Open Main Program:** Either `vi main.py` or `vi Robot_command/robot_startup.py`
- **Edit Code:** Press `i` to edit, then save and exit by pressing `Esc`, entering `:wq`, and pressing Enter

### How to Connect to WiFi
1. **List Available WiFi Networks:** `Nmcli device wifi list`
2. **Create New Connection:**
   - Without a username: `Nmcli device wifi connect <wifi> password <password>`
   - With a username and password: `sudo nmcli connection add type wifi ifname wlan0 con-name <username> ssid <wifi name> password <password>`
3. **Verify Connection:** `Nmcli connection show`
4. **Ping Test:** `Ping www.google.com` (Control + C to stop)

### How to Connect to the Robot Through Browser
- Ensure you are connected to the same WiFi as the robot.
- Enter the robot's IP address in your browser (`192.168.0.13:8888`).
- **Password:** `jetbot`

### How to Switch the Robot Into Desktop Mode
1. **Log into the Robot**
2. **Enter Commands:**
   - `sudo systemctl set-default graphical.target`
   - `sudo reboot`

### How to Switch the Robot Out of Desktop Mode
1. **Log into the Robot**
2. **Open Terminal:** Press Windows button, type "terminal", and press Enter (if no mouse is connected).
3. **Enter Commands:**
   - `sudo systemctl set-default multi-user.target`
   - `sudo reboot`

### How to Run the gitRepository main.py
1. **Log into the Robot**
2. **Execute the Script:**
   - `cd ~`
   - `sudo ./gitRepository/AMR-Capstone/startup.sh`
   - Or: `python3 gitRepository/AMR-Capstone/AMR/main.py`
  


