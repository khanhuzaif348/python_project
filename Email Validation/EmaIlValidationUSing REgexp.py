#a - z Must be small  ^ - starting symbol
# 0-9 digit
# . _ ONetime [\._]? return 0 ,1
#@ one [@]\w search 
# after regexp like we find . in last 2 , 3 position then we apply [.]\w{2,3}$ $ means last string
# . in 2nd , 3rd place
import re
email_cndn = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
usr_email = input("Enter Email: --   ")
if re.search(email_cndn,usr_email):
    print("Right Email ")
else:
    print("Oh you Enter Wrong email ")

