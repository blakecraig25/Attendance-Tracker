# **Project 1: Autonomous Attendance Tracker**
###### Blake Craig: Physical Computing -- Utility

### What is the Autonomous Attendance Tracker?
The Autonomous Attendance Tracker is a helpful tool for professors and teachers to track the overall attendance of a class. Meant at the beginning of class, this code will output an attendance of students with a given error threshold. This code implements motion detection features taken from a [python motion detection](https://www.youtube.com/watch?v=oxmZ9zczptg) video.

### Creator Statement:
The Autonomous Attendance Tracker is designed for the ability to provide a rough estimate for attendance, allowing professors to freely focus on their class and not on who is present. This system simply plugs into the wall and allows professors to track movement in and out of the classroom. I wanted to get rid of any manual interaction with the system because it would hinder ease and accessibility for all students and professors.

I was motivated to go through with this project because of the accountability factors this device implements. I have attended many college classes where many students were continuously absent and seeing it affect the professor’s teaching ability. I can’t deny that I understand the temptation to miss class, but I wholeheartedly believe in the value of going to class. In addition, many students will use excuses to leave class early or to distract themselves, so they don’t have to attend the “boring” or “stressful” class. This device will track that movement.

The box is designed to be small and portable, and susceptible to a large amount of light. My hardest challenge was measuring the motion detection with a lot of light. The threshold for creating motion detection was originally set extremely high to match the bright lights impacting the camera. However, I altered the code to measure the position of the rectangles per image frame, allowing only the threshold to become a mapping feature.

Although this device is meant for tracking the attendance of people at the beginning of class, the tracker can be altered to measure movement during class as well. I think this code is very low quality, but with a larger budget and more advanced code, this attendance tracker could become very effective for autonomously tracking students. In future implementations, machine learning would be nice, recognizing different features and multiple students entering at the same time. Currently, this code can only assume that one person is walking in at the same time and that the user is walking at a constant speed.


### Resources Used:
1. Raspberry Pi 3
2. 1x Buttons
3. Webcam for motion detection
4. Wires for connection
5. Wooden Box for storage
6. Power Cord for Raspberry Pi 3 (5.1 V micro USB power supply)

### Rough Outline:

[Link to Original Pitch](https://docs.google.com/presentation/d/1O95ZX5KgljtILGdT4T_9l_w7FyWo5n8bnMxUZsTnpQk/edit?usp=sharing)
![image](https://user-images.githubusercontent.com/112400887/235817887-8cc2be63-ef89-4fd0-8465-c0f245e863ea.png)


### Code:
 Description: | Code: | Instruction:
 --- | --- | --- 
 This is code for testing the webcam from you computer. | [Link to Computer Version](https://github.com/blakecraig25/Attendance-Tracker/blob/main/InputOutput.py) | This code will run the exact same as the seperated webcam and uses your computer's camera as the webcam. When you start it, it will automatically start going, so make sure that you get out of the camera angle. The webcam will establish a background image and use that pixel data to determine if there were changes, so it is important that you have a consistent background. When you are done, press the button again to close out of the program. In the same folder as this program, you will find the attendance labelled with the date of the recording.
This code is for the Raspberry Pi itself with the attached webcam.  | [Link to Rasperry Pi 3 Version](http://github.com/blakecraig25/Attendance-Tracker) | This code will run just like the computer version. Same rules apply.
 
 
### Useful Links for this project:
- [DevLogs](https://docs.google.com/document/d/1_ZYp7lE-O2B3Qo3t3RXmOEeQC7iaxt-k5I9XMCQGwAs/edit?usp=sharing)
- [GitHub Attendance Tracker Repo](https://github.com/blakecraig25/Attendance-Tracker)
- [Box Apparatus](https://en.makercase.com/#/basicbox)
- [Motion Detection Python Code video](https://www.youtube.com/watch?v=oxmZ9zczptg)

### Similar Projects:
- [Piezoelextric Sensor](https://en.wikipedia.org/wiki/Piezoelectric_sensor)
- [Jibble.io Time Tracker](https://www.jibble.io/)
- [Person Counter by PyImageSearch](https://pyimagesearch.com/2018/08/13/opencv-people-counter/)
