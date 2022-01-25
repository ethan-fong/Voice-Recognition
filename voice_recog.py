'''
This code is a user interface that will retrieve commands and clothing descriptions. It will output a signal to the motor detailing the amount to rotate. Speech is processed using google's API

'''
# import the speech recognition module
import speech_recognition as sr
# create the recognizer
r = sr.Recognizer()
# check audio devices
# print(sr.Microphone.list_microphone_names())
# define the microphone
mic = sr.Microphone(device_index=1)
# initialize clothing database structure
Clothing_attributes = {"black pikachu shirt": 1, "white pink shirt": 2, "white brown shirt":3, "white basketball tshirt":4, "white Puma shirt":5, "pink shoes shirt":6,\
     "black Tokyo long sleeve":7, "Grey, Basketball, Long sleeve":8, "black guess crewneck":9, "Yellow, Adidas, Hoodie":10, "Black, Essentials, Hoodie":11, "Green, Live, Hoodie":12, \
     "multicolor Adidas hoodie":13, "Brown, Essentials, Shorts":14, "white shirt":15, "Black, Puma, Shorts":16, "Black, Adidas, Shorts":17, "Blue, Adidas, Shorts":18, "Blue, Adidas, Pants":19,\
     "Grey, Nike, Pants":20, "Black, Black and white stripe, Pants":21, "black champion pants":22, "blue pants":23, "White, Nike Long, Socks": 24, "White, Adidas Short, Socks": 25,\
     "Black, Nike Long, Socks": 26, "Black, Adidas Short, Socks": 27, "Grey, Nike Long, Socks": 28, "Grey, Adidas Short, Socks": 29,"Red, Adidas Short, Socks": 30}
# calculate angle
Angle = 360/(max(Clothing_attributes.values()))
cur_angle = 0
request = ""
# main loop
while request != "end":
    print("-"*20)
    print("| start of inquiry |")
    print("-"*20)
    print("Would you like to retrieve or place clothing? ")
    input()
    # a try except loop is used here since a valueerror is raised if no input is detected
    try:
        with mic as source:
            audio = r.listen(source)
            # speech recognition using google's API
            request = r.recognize_google(audio)
    except:
        print("no input detected\n")
    else:
        # print the result
        print(request+"\n")
    possible_returns = ["place","p","pla","pl","plac","play","ace","return"]
    possible_returns2 = ["retrieve","retreat","r","re","ret","get"]
    if request.lower() in possible_returns:
        print("list some attributes of the clothing ")
        input()
        try:
            with mic as source:
                audio = r.listen(source)
                # speech recognition
                request = r.recognize_google(audio)
        except:
            print("no input detected\n")
        else:
            # print the result
            print(request+"\n")
        if request in Clothing_attributes:
            print("The wheel is currently at " + str(cur_angle) + " degrees\n")
            print("The motor will make the wheel spin " +str( abs(cur_angle%360-Clothing_attributes[request]*Angle)) + " degrees\n")
            print("the wheel will end at " +  str(Clothing_attributes[request]*Angle) + " degrees, to clothing number " + str(Clothing_attributes[request]))
            cur_angle += Clothing_attributes[request]*Angle
        else:
            print("invalid input! ")
    elif request.lower() in possible_returns2:
        print("list some attributes of the clothing ")
        input()
        try:
            with mic as source:
                audio = r.listen(source)
                # speech recognition
                request = r.recognize_google(audio)
        except:
            print("no input detected\n")
        else:
            # print the result
            print(request+"\n")
        if request in Clothing_attributes:
            print("The wheel is currently at " + str(cur_angle) + " degrees\n")
            print("The motor will make the wheel spin " +str( abs(cur_angle%360-Clothing_attributes[request]*Angle)) + " degrees\n")
            print("the wheel will end at " +  str(Clothing_attributes[request]*Angle) + " degrees, to clothing number " + str(Clothing_attributes[request]))
            cur_angle += Clothing_attributes[request]*Angle
        else:
            print("invalid input! ")
    else:
        if request != "end":
            print("invalid request! ")
    print("-"*18)
    print("| end of inquiry |")
    print("-"*18)
    print("\n")
