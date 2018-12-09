import telnetlib
import time

HOST = "lab.sharontools.com"

# A default delay of 2 seconds shall be handy
time.sleep(2)


#This psswd is needed by the router (Cisco r2) and is changed from time to time.
r2password = "2903796"

tn = telnetlib.Telnet(HOST)

sharon_user = "lab"

sharon_password = "123456"

time.sleep(2)

tn.read_until(b"lab login: ")

tn.write(sharon_user.encode() + b"\n")

time.sleep(2)

tn.read_until(b"Password: ")

tn.write(sharon_password.encode() + b"\n")

# Takes time to print the device list
time.sleep(6)


# Log in the device
tn.read_until(b"choice: ")

tn.write(b"12" + b"\n")

tn.read_until(b"Password: ")

tn.write(r2password.encode() + b"\n")

time.sleep(2)

# Enter the required command
tn.read_until(b"#")

tn.write(b"show ip interface brief" + b"\n")

time.sleep(2)


tn.read_until(b"#")

tn.write(b"quit" + b"\n")

print(tn.read_all())
