#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/plain")
print()

form = cgi.FieldStorage()

cname = form.getvalue("d1")

cmd = "sudo docker rm -f {} ".format(cname)
output = subprocess.getstatusoutput(cmd)
status = output[0]
out = output[1]

if status == 0:
    print("Container {0} removed successfully".format(cname))
else:
    print("Error removing Container: {0}".format(cname))

