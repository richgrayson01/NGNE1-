import requests
import json

print "Enter the ip address of the switch"
ip=raw_input()


print "Enter VLAN to be configured"
vlanId=raw_input()


print "enter vlan for which svi has to be configured"
vlansviId=raw_input()


print "enter ip of the svi"
ip_vlanId = raw_input()


myheaders = {'content-type': 'application/json-rpc'}
url = "http://"+ip+"/ins"
username = "admin"
password = "Cisco321"


payload=[
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "vlan "+vlanId,"version": 1},"id": 2},
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "interface vlan "+str(vlansviId),"version": 1},"id": 3},
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "ip address "+str(ip_vlanId )+"/24","version": 1},"id": 4},
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "no shut","version": 1},"id": 5},
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 6}
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()
print "VLAN and SVI created"




