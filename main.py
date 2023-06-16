import glob, urllib, requests, json, os

black   = "\033[0;30m"
red     = "\033[0;31m"
green   = "\033[0;32m"
yellow  = "\033[0;33m"
white   = "\033[0;37m"
nocolor = "\033[0m"
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    
def getUser():
    return os.environ['USERPROFILE'].replace("C:\\Users\\", "")

list_of_files = glob.glob("C:\\Users\\" + getUser() + "\\AppData\\Local\\Roblox\\logs" + "\*.log")
latest_file = max(list_of_files, key=os.path.getctime)
fin = open(latest_file, "rt", encoding = "ISO-8859-1")

ip = ""
port = ""

for line in fin:
    text = find_between(line, "serverId:", "\n").strip()
    if len(text) > 0 and text.strip() and text != "" and text.find("|") > 0:
        ip = text.split("|")[0]
        port = text.split("|")[1]

print(FAIL + "IP: " + ip)
print(OKBLUE + "Port: " + port)

response = urllib.request.urlopen("http://ip-api.com/json/" + ip)
data = json.loads(response.read())

print(OKGREEN + "Region: " + data["timezone"])
input()

fin.close()
