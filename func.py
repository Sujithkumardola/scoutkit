import requests
import json
import whois
from colorama import Fore,init
init(autoreset=True)
def whois_search(domain):
  result=whois.whois(domain)
  print(Fore.BLUE+"Domain",":",Fore.GREEN+str(result.domain_name))
  print(Fore.BLUE+"Registrar",":",Fore.GREEN+str(result.registrar))
  print(Fore.BLUE+"Updates at",":",Fore.GREEN+str(result.upadated_date))
  print(Fore.BLUE+"Created at",":",Fore.GREEN+str(result.created_date))
  print(Fore.BLUE+"Expires at",":",Fore.GREEN+str(result.expiry_date))
from threading import Thread
from queue import Queue
q = Queue()
def scan_subdomains(domain):
    global q
    while True:
        # get the subdomain from the queue
        subdomain = q.get()
        # scan the subdomain
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except:
            pass
        else:
            print(Fore.CYAN+"[+] Discovered subdomain:", url)

        # we're done with scanning that subdomain
        q.task_done()


def scanner(domain, n_threads, subdomains):
    global q

    # fill the queue with all the subdomains
    for subdomain in subdomains:
        q.put(subdomain)

    for t in range(n_threads):
        # start all threads
        worker = Thread(target=scan_subdomains, args=(domain))
        # daemon thread means a thread that will end when the main thread ends
        worker.daemon = True
        worker.start()
def scan(domain):
    wordlist = "subdomains.txt"
    num_threads = 10

    scanner(domain=domain, n_threads=num_threads, subdomains=open(wordlist).read().splitlines())
    q.join()

def geo(ip):
  url="http://ip-api.com/json/{ip}".format(ip=ip)
  resp=requests.get(url)
  resp=resp.text
  resp=json.loads(resp)
  for keys,values in resp.items():
    print(Fore.CYAN+keys,":",values)
def isvpn(ip):
  f=open("config.json","r")
  f=f.read()
  key=json.loads(f)
  key=key["vpnapi.io"]
  url="https://vpnapi.io/api/{ip}?key={key}".format(key=key,ip=ip)
  resp=requests.get(url)
  resp=resp.text
  resp=json.loads(resp)
  try:
    for keys,values in resp["security"].items():
      print(Fore.CYAN+keys,":",values)
  except:
    print(Fore.RED+"Invalid IP...")
def ns(domain):
  result=whois.whois(domain)
  ns=result.name_servers
  for i in ns:
    print(Fore.CYAN+i)
