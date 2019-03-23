import json
import numpy as np

with open('./incidents.json') as f:
  data = json.loads(f.read())


src = {}
dest = []
files = []
temp = {}
cpt = 0

for each in data["tickets"]:
  if each["src_ip"] not in src :
    src[each["src_ip"]] = 1
  else :
    src[each["src_ip"]] = src[each["src_ip"]] + 1
print (max(src, key=src.get))

for each in data["tickets"]:
  temp[each["file_hash"]] = None
  if each["src_ip"] == "44.206.37.254":
    if each["dst_ip"] not in dest :
      cpt = cpt + 1
      dest.append(each["dst_ip"])
print (cpt)

nbTickets = 0
nbFiles = 0

for each in data["tickets"]:
    nbTickets += 1
    if each["file_hash"] not in files:
      files.append(each["file_hash"])
      nbFiles += 1
print (nbTickets/nbFiles)
  
