age = int(input("How old are you? "))

if(age >= 18):
    print("You can drive")
if(age<= 17):
    print("You can't drive")

permit_check = input("Do you have your permit? ")

if(permit_check == "yes"):
    print("You can drive with your parents")
if(permit_check == "no"):
    print("You can't drive with your parents")
    
drive_test_check = input("Did you pass your Driving Test? ")
if(drive_test_check == "yes"):
    print("You can drive... if you're over 18")
if(drive_test_check == "no"):
    print("You can't drive at all")

car = input("Do you have a car? ")
if(car == "yes"):
    print("You have a car to drive if you're legal")
if(car == "no"):
    print("You have no car to drive at all")

insurance_and_registration_check = input("Do you have insurance and registration? ")

if(insurance_and_registration_check == "yes"):
    print("You are street legal to drive your car")
if(insurance_and_registration_check == "no"):
    print("You are not street legal to drive your car")
    print("Congratulations!")
