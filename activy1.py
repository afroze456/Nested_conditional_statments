medical_cause = input("did you have a medical cause? (Y/N): ").strip().upper()
if medical_cause == "Y":
    print("you are allowed")
else:
    atten=int(input("enter in attenace of student: "))

    if atten >=75:
        print("Allowed")
    else:
        print("not allowed")