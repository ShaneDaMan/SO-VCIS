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
    elif inputone == "BANNG":
        print("")
        print("BANNG2 8L/8R: SKNNR")
        print("BANNG2 9L/9R/10: GRITZ")
        print("BANNG2 26L/26R: SNUFY")
        print("BANNG2 27R/27L: SLAWW")
        print("BANNG2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "CUTTN":
        print("")
        print("CUTTN2 8L/8R: HRSHL")
        print("CUTTN2 9L/9R/10: GRITZ")
        print("CUTTN2 26L/26R: SNUFY")
        print("CUTTN2 27R/27L: SLAWW")
        print("CUTTN2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "GAIRY":
        print("")
        print("GAIRY2 8L/8R: RONII")
        print("GAIRY2 9L/9R: LIDAS")
        print("GAIRY2 10: GRITZ")
        print("GAIRY2 26L/26R: MPASS")
        print("GAIRY2 27R/27L: FUTBL")
        print("GAIRY2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "HAALO":
        print("")
        print("HAALO2 8L/8R: SKNNR")
        print("HAALO2 9L/9R/10: GRITZ")
        print("HAALO2 26L/26R: SNUFY")
        print("HAALO2 27R/27L: SLAWW")
        print("HAALO2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "JACCC":
        print("")
        print("JACCC2 8L/8R: RONII")
        print("JACCC2 9L/9R: LIDAS")
        print("JACCC2 10: GRITZ")
        print("JACCC2 26L/26R: MPASS")
        print("JACCC2 27R/27L: FUTBL")
        print("JACCC2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "KAJIN":
        print("")
        print("KAJIN2 8L/8R: HRSHL")
        print("KAJIN2 9L/9R/10: GRITZ")
        print("KAJIN2 26L/26R: SNUFY")
        print("KAJIN2 27R/27L: SLAWW")
        print("KAJIN2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "NASSA":
        print("")
        print("NASSA2 8L/8R: HRSHL")
        print("NASSA2 9L/9R/10: GRITZ")
        print("NASSA2 26L/26R: SNUFY")
        print("NASSA2 27R/27L: SLAWW")
        print("NASSA2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "PADGT":
        print("")
        print("PADGT2 8L/8R: RONII")
        print("PADGT2 9L/9R/10: PICKT")
        print("PADGT2 26L/26R: MPASS")
        print("PADGT2 27R/27L/28: CPARK")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "PENCL":
        print("")
        print("PENCL2 8L/8R: RONII")
        print("PENCL2 9L/9R/10: PICKT")
        print("PENCL2 26L/26R: MPASS")
        print("PENCL2 27R/27L/28: CPARK")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "PHIIL":
        print("")
        print("PHIIL2 8L/8R: RONII")
        print("PHIIL2 9L/9R: LIDAS")
        print("PHIIL2 10: GRITZ")
        print("PHIIL2 26L/26R: MPASS")
        print("PHIIL2 27R/27L: FUTBL")
        print("PHIIL2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "PLMMR":
        print("")
        print("PLMMR2 8L/8R: RONII")
        print("PLMMR2 9L/9R: LIDAS")
        print("PLMMR2 10: GRITZ")
        print("PLMMR2 26L/26R: MPASS")
        print("PLMMR2 27R/27L: FUTBL")
        print("PLMMR2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "POUNC":
        print("")
        print("POUNC2 8L/8R: HRSHL")
        print("POUNC2 9L/9R/10: GRITZ")
        print("POUNC2 26L/26R: SNUFY")
        print("POUNC2 27R/27L: SLAWW")
        print("POUNC2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "SMKEY":
        print("")
        print("SMKEY2 8L/8R: RONII")
        print("SMKEY2 9L/9R/10: PICKT")
        print("SMKEY2 26L/26R: MPASS")
        print("SMKEY2 27R/27L/28: CPARK")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "SMLTZ":
        print("")
        print("SMLTZ2 8L/8R: SKNNR")
        print("SMLTZ2 9L/9R/10: GRITZ")
        print("SMLTZ2 26L/26R: SNUFY")
        print("SMLTZ2 27R/27L: SLAWW")
        print("SMLTZ2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "VARNM":
        print("")
        print("VARNM2 8L/8R: RONII")
        print("VARNM2 9L/9R/10: PICKT")
        print("VARNM2 26L/26R: MPASS")
        print("VARNM2 27R/27L/28: CPARK")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "VRSTY":
        print("")
        print("VRSTY2 8L/8R: SKNNR")
        print("VRSTY2 9L/9R/10: GRITZ")
        print("VRSTY2 26L/26R: SNUFY")
        print("VRSTY2 27R/27L: SLAWW")
        print("VRSTY2 28: WLSON")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "WIGLE":
        print("")
        print("WIGLE2 8L/8R: TUANN")
        print("WIGLE2 9L/9R: LIDAS")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "ZELAN":
        print("")
        print("ZELAN4 27R: CPARK")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "BANKR":
        print("")
        print("BANKR2 - Descend via")
        print("BANKR2 South: DEELX @ 12k & 250kt")
        print("BANKR2 North: BLNCE @ 9k & 210kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "BTSEY":
        print("")
        print("BTSEY2: BTSEY @ 11k & 250kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "CHPTR":
        print("")
        print("CHPTR3 South: CHPTR @ 11k & 250kt")
        print("CHPTR3 North: CHPTR @ 14k & 250kt")
        print("CHPTR3 Props: CHPTR @ 7k")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "CHSLY":
        print("")
        print("CHSLY4 - Descend via")
        print("CHSLY4 South: HEELZ @ 6k & 210kt")
        print("CHSLY4 Rwy23: JEPHS @ 6k & 230kt")
        print("CHSLY4 North: EPAYE @ 6k & 210kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "FILPZ":
        print("")
        print("FILPZ3 - Descend via")
        print("FILPZ3 South: FISHN @ 7k & 210kt")
        print("FILPZ3 North: VALLL @ 6k & 210kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "JONZE":
        print("")
        print("JONZE2 - Descend via")
        print("JONZE2 South: JRDEN @ 6k & 210kt")
        print("JONZE2 North: CHELE @ 7k & 210kt")
        print("JONZE2 Rwy23: WOOOO @ 7k & 210kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "LIINN":
        print("")
        print("LIINN3 Jets: LIINN @ 11k & 250kt")
        print("LIINN3 Props: LIINN @ 9k")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "MAJIC":
        print("")
        print("MAJIC4 Jets: MAJIC @ 13k & 250kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "MLLET":
        print("")
        print("MLLET2 - Descend via")
        print("MLLET2 South: MLLET @ 14k & 250kt")
        print("MLLET2 North: MLLET @ 12k & 250kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "PARQR":
        print("")
        print("PARQR3 - Descend via")
        print("PARQR3 South: CAMPR @ 9k & 220kt")
        print("PARQR3 North: THACK @ 12k & 250kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "RASLN":
        print("")
        print("RASLN3 Jets South: RASLN @ 14k & 250kt")
        print("RASLN3 Jets North: RASLN @ 11k & 250kt")
        print("RASLN3 Props South: RASLN @ 10k")
        print("RASLN3 Props North: RASLN @ 8k")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "STOCR":
        print("")
        print("STOCR3 South: HANDO @ 8k & 210kt")
        print("STOCR3 Rwy23: JRUTT @ 6k & 210kt")
        print("STOCR3 North: GATEE @ 6k & 210kt")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    elif inputone == "UNARM":
        print("")
        print("UNARM6 Jets: UNARM @ 11k & 250kt")
        print("UNARM6 Props: UNARM @ 7k")
        print("")
        inputsix = input("Press ENTER to return to menu: ")
        menu()
    else:
        print("Invalid entry")
        time.sleep(3)
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
        elif report == "routine":
            report = "UA "
        elif report == "Urgent":
            report = "UUA "
        elif report == "urgent":
            report = "UUA "
        if saident != "":
            ident = saident + " "
        if location != "":
            loc = "/OV " + location
        else:
            loc = ""
        if time != "":
            ti = "/TM " + time
        else:
            ti = ""
        if altitude != "":
            alt = "/" + altitude
        else:
            alt = ""
        if type != "":
            actype = "/TP " + type
        else:
            actype = ""
        if sky != "":
            skyc = "/SK " + sky
        else:
            skyc = ""
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