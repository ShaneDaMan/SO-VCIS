import time

#Variable definitions
PIREP1 = "PIREP Slot Empty"
PIREP2 = "PIREP Slot Empty"
PIREP3 = "PIREP Slot Empty"
PIREP4 = "PIREP Slot Empty"
PIREP5 = "PIREP Slot Empty"
PIREP6 = "PIREP Slot Empty"
PIREP7 = "PIREP Slot Empty"
PIREP8 = "PIREP Slot Empty"
PIREP9 = "PIREP Slot Empty"
PIREP10 = "PIREP Slot Empty"

def menu():
    import time
    global PIREP1, PIREP2, PIREP3, PIREP4, PIREP5, PIREP6, PIREP7, PIREP8, PIREP9, PIREP10
    print("")
    print("")
    print("")
    print("SO VCIS")
    print("Virtual Controlling Information System")
    print("Made by SO")
    print("")
    time.sleep(1)
    print("Select an option or enter a command")
    print("[1] PIREP System")
    print("[2] N/A")
    inputone = input("")
    if inputone == "1":
        print("")
        pirep()
    else:
        print("Invalid entry")
        time.sleep(4)
        menu()
        
def pirep():
    import time
    global PIREP1, PIREP2, PIREP3, PIREP4, PIREP5, PIREP6, PIREP7, PIREP8, PIREP9, PIREP10
    print("")
    print("")
    print("")
    print("PIREP System")
    print("[1] View PIREPs")
    print("[2] Enter PIREP")
    print("[3] Main Menu")
    inputtwo = input("")
    if inputtwo == "1":
        if PIREP1 == "PIREP Slot Empty":
            print("")
            print("No PIREPs in system")
            time.sleep(4)
            menu()
        else:
            print("")
            print(PIREP1)
            print(PIREP2)
            print(PIREP3)
            print(PIREP4)
            print(PIREP5)
            print(PIREP6)
            print(PIREP7)
            print(PIREP8)
            print(PIREP9)
            print(PIREP10)
            time.sleep(3)
            print("")
            print("[1] Delete PIREP")
            print("[2] Return to Main Menu")
            print("[3] Return to PIREP Menu")
            inputthree = input("")
            if inputthree == "1":
                print("")
                print("Which PIREP Number Would you Like to Delete?")
                inputfour = input("")
                if inputfour == "1":
                    PIREP1 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "2":
                    PIREP2 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "3":
                    PIREP3 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "4":
                    PIREP4 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "5":
                    PIREP5 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "6":
                    PIREP6 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "7":
                    PIREP7 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "8":
                    PIREP8 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "9":
                    PIREP9 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                elif inputfour == "10":
                    PIREP1 = "PIREP Slot Empty"
                    time.sleep(1)
                    print("")
                    print("PIREP Deleted")
                    time.sleep(3)
                    menu()
                else:
                    print("")
                    print("PIREP # does not exist")
                    time.sleep(4)
                    pirep()
            elif inputthree == "2":
                menu()
            elif inputthree == "3":
                pirep()
    elif inputtwo == "2":
        print("")
        if PIREP10 != "PIREP Slot Empty":
            print("Error, all PIREP Slots filled")
            time.sleep(3)
            pirep()
        print("PIREP Entry System")
        time.sleep(1)
        print("If an entry for a line is unavailable, do NOT enter anything")
        print("")
        report = input("Report Type (Routine or Urgent): ")
        saident = input("Station Identifier (ATL): ")
        location = input("Location: ")
        time = input("Time (HHMMz): ")
        altitude = input("Altitude (FL350): ")
        type = input("Aircraft Type (C172): ")
        sky = input("Sky Cover (OVC005-TOP008/SKC): ")
        vis = input("Flight Visibility and Weather: ")
        temp = input("Temperature (Celsius): ")
        wind = input("Wind: ")
        turb = input("Turbulence: ")
        ice = input("Icing: ")
        remarks = input("Remarks: ")
        if report == "Routine":
            report = "UA "
        elif report == "Urgent":
            report = "UUA "
        if saident != "":
            ident = saident + " "
        if location != "":
            loc = "/OV " + location
        if time != "":
            ti = "/TM " + time
        if altitude != "":
            alt = "/" + altitude
        if type != "":
            actype = "/TP " + type
        if sky != "":
            skyc = "/SK " + sky
        if vis != "":
            visi = "/WX " + vis
        else:
            visi = ""
        if temp != "":
            tempe = "/TA " + temp
        else:
            tempe = ""
        if wind != "":
            win = "/WV " + wind
        else:
            win = ""
        if turb != "":
            turbs = "/TB " + turb
        else:
            turbs = ""
        if ice != "":
            icing = "/IC " + ice
        else:
            icing = ""
        if remarks != "":
            remark = "/RM " + remarks
        else:
            remark = ""
        PIREP = ident + report + loc + ti + alt + actype + skyc + visi + tempe + win + turbs + icing + remark
        
        if PIREP1 == "PIREP Slot Empty":
            PIREP1 = PIREP
        elif PIREP2 == "PIREP Slot Empty":
            PIREP2 = PIREP
        elif PIREP3 == "PIREP Slot Empty":
            PIREP3 = PIREP
        elif PIREP4 == "PIREP Slot Empty":
            PIREP4 = PIREP
        elif PIREP5 == "PIREP Slot Empty":
            PIREP5 = PIREP
        elif PIREP6 == "PIREP Slot Empty":
            PIREP6 = PIREP
        elif PIREP7 == "PIREP Slot Empty":
            PIREP7 = PIREP
        elif PIREP8 == "PIREP Slot Empty":
            PIREP8 = PIREP
        elif PIREP9 == "PIREP Slot Empty":
            PIREP9 = PIREP
        elif PIREP10 == "PIREP Slot Empty":
            PIREP10 = PIREP
        print("")
        print("Process complete. PIREP generated successfully")
        print("")
        print(PIREP)
        import time
        time.sleep(2)
        print("")
        pirep()
    elif inputtwo == "3":
        time.sleep(1)
        menu()

menu()