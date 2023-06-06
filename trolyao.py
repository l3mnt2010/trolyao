import speech_recognition
import pyttsx3
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain =""
with  speech_recognition.Microphone() as mic:
    print(" Robot: I am listening")
    audio = robot_ear.listen(mic)
    print("Robot:...")
try:
    you = robot_ear.recognize_google(audio)
except:
       you = ""
print("you: " +  you)


## print("hieu") 

if you =="":
    robot_brain ="I can't hear you,repeat again"
if you =="hello":
    robot_brain ="Hello how are you today"
if you =="today":
    today = date.today()
    robot_brain = today.strftime(" %B %d, %Y")
if you == "time":
 now =datetime.now()
 robot_brain =now.strftime("%H hours %M minutes %S seconds")
if you =="how are you":
    robot_brain ="I'm fine thank you and you!"
print("Robot:" + robot_brain)


## print("noi")
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()