# Importing Modules
import os
import functions.details as details
import functions.setup as setup
import functions.signup as signup
import functions.forgotpass as forgotpass
import functions.forgotuname as forgotuname

datafolder = "data"
rootfolder = os.getcwd()
login = False

logincmd = ["1 Login ✅", "2 Sign Up 📜", "3 Forgot Password 🙄", "4 Forgot Username 🙄", "5 Exit ➡"]
setup.runsetup()


valTrue = True

while valTrue:
    
    cmd = int(input(f"❗ Type The Number Besides The Command To Execute The Command \n\t{logincmd[0]}\n\t{logincmd[1]} \n\t{logincmd[2]} \n\t{logincmd[3]} \n\t{logincmd[4]}\n"))
    
    if int(cmd) == 1:
                
        name = details.name().lower()
        uname = details.username().lower()
        os.chdir(datafolder)
        
        
        if os.path.exists(name):
                    password = details.password()
                    os.chdir(name)
                    with open(uname, "r") as x:
                        match = x.read()
                    if password in match:
                        print("✅ Login Successful")
                        login = True
                        os.chdir(rootfolder)
                        valTrue = False
                    else:
                        print("❌ Password doesn't matched try again")
                        os.chdir(rootfolder)
                                
        elif os.path.exists(name) == False:
                    print("❌ No Account was created with this name try again or sign up")
                    os.chdir(rootfolder)

    elif int(cmd) == 2:
        
        signup.signup()
   
    elif int(cmd) == 3:
        
        forgotpass.forgotpass()
        
    elif int(cmd) == 4:
        forgotuname.forgotuname()
    elif int(cmd) == 5:
        exit()
    else:
        print("❌ Unknown Command Choosen")


