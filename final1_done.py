import pyttsx3   
import pprint, webbrowser

def SpeakText(command):
    engine = pyttsx3.init("sapi5")
    engine.say(command)
    engine.runAndWait()

SpeakText("Welcome to the R N S I T website. How may I help you?")

while True:
    SpeakText("If you want faculty details, type 'faculty'. Or. If you want a map of the campus, type 'map'. Or. If you want to exit, type 'exit'.")
    print("\nIf you want faculty details, type 'faculty'.")
    print("(OR)")
    print("If you want a map of the campus, type 'map'.")
    print("(OR)")
    print("If you want to exit, type 'exit'.")
    start = input().strip().lower()

    if start == "faculty":
        #This code is to find a faculty member in the campus and gives details of the faculty member.

        #As the person who stores values in the 'details' dict, avoid initials or middle/last names.
        #All dept names should be small case, with no space between the words (if there are many).
        #Write only short form of the depts (The ones seen on the board on each building).
        details = {"chemistry" : {"pradeepa" : ["7411966337", "Admin block, Ground Floor, Chemistry Lab 1"]},
                "math" : {"dhruvatara" : ["99863029808", "Admin Block 201"],
                            "ambika" : ["9900217382", "Admin Block 201"],
                            "chinni krishna" : ["9880030017", "Admin Block 201"]},
                "mechanical" : {"thippeswamy" : ["9743135140", "Mechanical Block, Second Floor, Staff Room 1"],
                                "rakesh" : ["8892101582", "Mechanical Block, Second Floor, Staff Room"]},
                "cse" : {"likitha" : ["8105587509", "CSE Block, Second Floor, Staff Room 1"]},
                "english" : {"nandakishore" : ["9206513281", "Mechanical Block, Second Floor, Staff Room 2"]},
                "ece" : {"anuradha" : ["9739007711", "ECE Block,First Floor, Staff Room 1"]},
                "electrical" : {"rakesh" : ["8880164513", "Mechanical Block, Ground floor, Staff room"]},
                "civil" : {"apoorva" : ["944776646", "Civil Block, First Floor, Staff Room 2"]},
                "sfh" : {"rohini" : ["7259913110", "Mechanical Block, Second Floor, Staff Room 2"]}}


        SpeakText("I will guide you to a faculty member you are in need of. If you know the faculty member's name, type 'Y'. If you don't, type 'N'.")
        print("\nI will guied you to a faculty member you are in need of.")
        print("Do you know the faculty member's name? Y/N")
        x=input().strip().lower()

        if x == "y":
            try:
                SpeakText("Please type their first name. Also, please be specific in spelling and capitalization of letters.")
                print("\nPlease type their first name. (Please be specific in spelling and capitalization of letters.)")
                name = input().strip().lower()
                global found
                found = False
                for dept,value in details.items():
                    for person in value.items():
                        if name == person[0]:
                                    print("Phone number:", person[1][0])
                                    print("Where can you find them?", person[1][1], sep="\n")
                                    SpeakText("Their phone number is")
                                    SpeakText(person[1][0])
                                    SpeakText("and you can find them in")          
                                    SpeakText(person[1][1])
                                    found = True         
                           
                if not found:
                    raise Exception("name DNE")
            except Exception:
                SpeakText("I don't know that person. Do you have a typo?")
                print("I don't know that person. Do you have a typo?")                          


        elif x == "n":
            depts = details.keys()
            depts = list(depts)
            depts = ", ".join(depts).upper()
            SpeakText("The departments are")
            SpeakText(depts)
            print("The departments are:", depts)
            SpeakText("Which department are you looking for? Type out the department's name.")
            print("\nWhich department are you looking for?")
            dept = input().lower().strip().replace(" ", "")
            if dept in details:
                for name, info in details[dept].items():
                    print("Faculty name:", name.title(), "\n", "Phone number:", info[0], "\n", "Where can you find them?\n", info[1])
                    SpeakText("The faculty's name is")
                    SpeakText(name)
                    SpeakText("Their phone number is")
                    SpeakText(info[0])
                    SpeakText("You can find them in")
                    SpeakText(info[1])
            else:
                print("\nI don't know that department.")
                print("(Try giving the proper name (the one seen on the building) or aviod spelling errors. )")
                SpeakText("I don't know that department. Try giving the proper name or aviod spelling errors.")


    elif start == "map":
        places =["ECE Department",
                "CSE/MCA/ISE Department",
                "Admin block",
                "Mechanical/EEE Department",
                "MBA Block",
                "Pre University College",
                "Temple",
                "Library",
                "International School",
                "First Grade College",
                "School of Architecture",
                "Civil Department",
                "Canteen/Basketball Court"]

        SpeakText("The places are")
        SpeakText(places)
        pprint.pprint(places)
        SpeakText("Type out the place you want to go to.")
        finish = input("Where do you want to go?\n").lower().strip()

        if finish.startswith("ece"):
            webbrowser.open('https://www.google.com/maps/place/RNSIT+ECE+Department/@12.9022257,77.518045,20.33z/data=!4m6!3m5!1s0x3bae3fa739575fab:0x53974a7440469464!8m2!3d12.9024388!4d77.5178569!16s%2Fg%2F11bxdt1c14?entry=ttu')
        elif finish.startswith("cse") or finish.startswith("mca") or finish.startswith("ise"):
            webbrowser.open("https://www.google.com/maps/place/RNSIT+CSE+Department/@12.9022257,77.518045,20.33z/data=!4m6!3m5!1s0x3bae3fa747acf84b:0x97a5cf1952c2fe3a!8m2!3d12.9019973!4d77.5178519!16s%2Fg%2F11b7q9g03p?entry=ttu")
        elif finish.startswith("admin"):
            webbrowser.open("https://www.google.com/maps/place/RNS+INSTITUTE+OF+TECHNOLOGY/@12.9022257,77.518045,20.33z/data=!4m6!3m5!1s0x3bae3fa7243af9c3:0x9bed6669a38d1c3!8m2!3d12.9021902!4d77.518582!16s%2Fm%2F07kddf8?entry=ttu")
        elif finish.startswith("mech") or finish.startswith("eee"):
            webbrowser.open("https://www.google.com/maps/place/RNSIT+Mechanical+Dept./@12.9013514,77.5190162,20z/data=!4m6!3m5!1s0x3bae3fa6d4e243d3:0x857ce2d11b1b940!8m2!3d12.9016162!4d77.5189767!16s%2Fg%2F11bxdrl85x?entry=ttu")
        elif finish.startswith("mba"):
            webbrowser.open("https://www.google.com/maps/place/RNSIT+MBA+and+research+centre/@12.9010992,77.5185178,20.33z/data=!4m6!3m5!1s0x3bae3fa0d7d6f24d:0xf8b6576063c073b9!8m2!3d12.9009783!4d77.5187923!16s%2Fg%2F11bzztz89m?entry=ttu")
        elif finish.startswith("pre"):
            webbrowser.open("https://www.google.com/maps/place/RNS+Pre+University+College/@12.900507,77.5184921,20.33z/data=!4m6!3m5!1s0x3bae3fa0d8fbb8bf:0xb74976d4132e9065!8m2!3d12.9003387!4d77.5186649!16s%2Fg%2F1hc4583yp?entry=ttu")
        elif finish.startswith("temple"):
            webbrowser.open("https://www.google.com/maps/place/RNSIT+Temple/@12.9002323,77.5181558,20.33z/data=!4m6!3m5!1s0x3bae3fa0e86e08b9:0xabf65109195df971!8m2!3d12.8999404!4d77.5184225!16s%2Fg%2F11g6bjd9mf?entry=ttu")
        elif finish.startswith("library"):
            webbrowser.open("https://www.google.com/maps/place/RNSIT+LIBRARY/@12.9005289,77.5179113,20.33z/data=!4m6!3m5!1s0x3bae3f9dbd74e2af:0x790d3b9130cdea51!8m2!3d12.9007367!4d77.5177735!16s%2Fg%2F11vdvgyjxt?entry=ttu")
        elif finish.endswith("school"):
            webbrowser.open("https://www.google.com/maps/place/RNS+International+School/@12.9006213,77.516487,20z/data=!4m6!3m5!1s0x3bae3f00546b0855:0x80762482e618725c!8m2!3d12.9006213!4d77.5167416!16s%2Fg%2F11c542bw5l?entry=ttu")
        elif finish.startswith("first"):
            webbrowser.open("https://www.google.com/maps/place/RNS+FIRST+GRADE+COLLEGE/@12.901141,77.517641,20z/data=!4m6!3m5!1s0x3bae3fa4199cfb2b:0x2f21b3f01b7af967!8m2!3d12.9010727!4d77.5175276!16s%2Fg%2F11cn8sj6wz?entry=ttu")
        elif finish.endswith("architecture"):
            webbrowser.open("https://www.google.com/maps/place/RNS+School+Of+Architecture/@12.901141,77.517641,20z/data=!4m6!3m5!1s0x3bae3fa74a9b8047:0x6b77c45151eb9d5f!8m2!3d12.9013727!4d77.5175806!16s%2Fg%2F11f2sg_k8m?entry=ttu")
        elif finish.startswith("civil"):
            webbrowser.open("https://www.google.com/maps/place/Civil+Department,+RNSIT/@12.9016341,77.5174507,20z/data=!4m6!3m5!1s0x3bae3fe2bc21df53:0xae4f4342d8e1d687!8m2!3d12.9017141!4d77.5175117!16s%2Fg%2F11k60hgr9y?entry=ttu")
        elif finish.startswith("canteen") or finish.startswith("basket"):
            webbrowser.open("https://www.google.com/maps/place/RNSIT+Canteen/@12.9020237,77.5190292,20z/data=!4m6!3m5!1s0x3bae3fa6d909c9ad:0x336c875e790592f5!8m2!3d12.9022332!4d77.5191591!16s%2Fg%2F1wf3710k?entry=ttu")
        else:
            SpeakText("I don't know the place you are taliking about.Please use given names and spellings.")
            print("I don't know the place you are taliking about.")
            print("Please use given names and spellings.")
        break

    elif start == "exit":
        break

print("\nIt was wonderful interacting with you.")
SpeakText("It was wonderful interacting with you.")
            