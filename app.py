import func
from colorama import Fore as f,init
init(autoreset=True)
print(f.CYAN+'''

 $$$$$$\                                  $$\     $$\   $$\ $$\   $$\     
$$  __$$\                                 $$ |    $$ | $$  |\__|  $$ |    
$$ /  \__| $$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$\   $$ |$$  / $$\ $$$$$$\   
\$$$$$$\  $$  _____|$$  __$$\ $$ |  $$ |\_$$  _|  $$$$$  /  $$ |\_$$  _|  
 \____$$\ $$ /      $$ /  $$ |$$ |  $$ |  $$ |    $$  $$<   $$ |  $$ |    
$$\   $$ |$$ |      $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |\$$\  $$ |  $$ |$$\ 
\$$$$$$  |\$$$$$$$\ \$$$$$$  |\$$$$$$  |  \$$$$  |$$ | \$$\ $$ |  \$$$$  |
 \______/  \_______| \______/  \______/    \____/ \__|  \__|\__|   \____/ 
                                                                          
                                                                          
                                                                          
''')
print(f.GREEN+'''
                                  MENU
__________________________________________________________________________

[1] WHOIS Search
[2] Nameserver Search
[3] Sundomain Enumeration
[4] Geolocation By IP
[5] Detect IP Type
[6] Exit
''')
try:
  opt=int(input(f.GREEN+"Enter your option: "))
except:
  opt=0
if opt<=6 and opt!=0:
  if opt==1:
   url=input(f.GREEN+"Enter domain: ")
   func.whois_search(url)
  elif opt==2:
    url=input(f.GREEN+"Enter domain: ")
    func.ns(url)
  elif opt==3:
    url=input(f.GREEN+"Enter domain: ")
    func.scan(url)
  elif opt==4:
    ip=input(f.GREEN+"Enter IP: ")
    func.geo(ip)
    pass
  elif opt==5:
    ip=input(f.GREEN+"Enter IP: ")
    func.isvpn(ip)
  else:
    print(f.RED+"Exiting...")
    exit()
else:
  print(f.RED+"Bad Input")
