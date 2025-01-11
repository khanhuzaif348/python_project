email = input("Enter Your Email: - ")
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif  i =="_" or i =="." or i=="@":
                          continue
                
                if k==1:
                    print("Wring email 5")        
            else:
                print("Wring email 4")
        else:
            print("Wrong email 3 ")
    else:
        print("wrong email 2 ")
else:
    print("Wrong Email 1")
    
