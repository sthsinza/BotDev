<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/Botdev.png height="228" width="980">

[![button](https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/back_button.png)](https://github.com/BotDevLLC/BotDevCurriculum/blob/master/Curriculum/Week_1/readme.md)

# VITAL INFORMATION
Subject(s):  Robotics

Topic or Unit: Communication with the STEMBot

Grade/Level: 8th grade

Time Allotment: 30 minutes

Standards:           3.4.5. A3. Identify network communication technologies

3.4.6. D2. Use computers appropriately to access and organize and apply information 


  3.4.7.E4.  Illustrate how information can be acquired and sent through a variety of technological sources, including print and electronic media.  
  
  15.4.12.F. Compare and contrast network environments, including the function of network devices and connectivity issues.
  
Unit Goal(s):  
1.	Understand what VNC Viewer is and the purpose of it
2.	Understand internet protocol addressing (IP Address)
3.	By the end of lesson, students will be able to utilize VNC to remotely operate the raspberry pi

Objective(s):    
1.	To be able to follow steps to install VNC Viewer 
2.	Connect to the STEMBot through a reliable internet connection
Assessment(s):   
1.	Open a LibreOffice Write (word) document on the desktop of a Raspberry Pi.  Have each student connect to the Raspberry Pi via VNC and write their name on the document.  Be prepared, more than one person may edit the document at once, so antics will ensue.    


# INSTRUCTIONAL PROCEDURES 
  # A.	Anticipatory Set: 
  The Raspberry Pi is a low cost, credit-card sized computer that plugs into a computer monitor or TV and uses a standard keyboard and mouse. We can use a Virtual Network Computing (VNC) connection to connect to the Raspberry Pi, so that the Raspberry Pi does not need a monitor or keyboard. If a computer doesn’t have its own monitor, and input devices (such as a keyboard) we call it a “headless client.”  Using a VNC to turn another computer into the monitor and keyboard of the Raspberry Pi, we will use it as a headless client.
  
  # B. Body: 
Before beginning both the Raspberry Pi and your host computer must be on the same internet connection!
1.	Plug in Raspberry Pi to monitor, keyboard and a mouse. Open the terminal by choosing Menu > Accessories > Terminal)
<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%201.png>

2.	Type ipconfig to check the IP address of the Raspberry Pi
<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%202.png>
3.	Check the IP address of the Raspberry Pi at the wlan0 part that shows inet followed by an IP Address... normally something similar to 192.168.1.101
<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%203.png>

4.	Ensure that VNC is enabled on your Raspberry Pi.  Click on the raspberry logo in the upper left corner and select Preferences > Raspberry Pi Configuration.  Click on the second tab in the window that pops up and make sure that the radio button next to Enable to the right of VNC is selected.
<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%204.png>


5.	Download Real VNC Viewer from your browser by clicking download VNC Viewer and run the executable file
<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%205.png>

6.	Run the executable file to install the program on your device. Open the program once completed.
<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%206.png>

7.	Enter the IP Address of the Raspberry Pi in the VNC Viewer at the top bar to connect to it. You will be prompted to enter a username and password.

Username: pi
Password: raspberry

<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%207.png>


8.	An alternative to using ifconfig to get its IP address -which requires a monitor and keyboard-, is to use the Smart Phone App “ Fing” that can be downloaded on the App store and Play store.  Simply connect your phone to the same Wi-Fi, open the app and scan the network.  Then look for your Raspberry Pi’s name and the IP address will be next to it.
<img src=https://raw.githubusercontent.com/BotDevLLC/BotDevCurriculum/master/Pictures/pic%208.png>



# MATERIALS AND RESOURCES
* Computers with internet connection
* HDMI cord
* STEMBot(Raspberry Pi)
* Monitor
* Keyboard and mouse



