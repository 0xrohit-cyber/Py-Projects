import subprocess
interface=input("Enter your interface : ")
mac=input("Enter your macx address : ")
subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac,shell=True)
subprocess.call("ifconfig " + interface + " up",shell=True)
print("THE MAC ADDRESS IS CHANGED TO " + mac )
print("Do you want to see your MAC ADDRESS")
print("Enter your choice (Y/N) :")
c=input("YOUR CHOICE :")
if (c=="Y"):
    print("HERE IS YOUR MAC ")
    subprocess.call("ifconfig | grep ether",shell=True)
else:
    print("OK FINE THANK YOU FOR USING THIS TOOL..........")
