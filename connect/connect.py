import configparser
import pexpect
import time
config = configparser.ConfigParser()
config.read("config")
IP = config.get("telnet", "ip")
print(IP)
value = config.items("telnet")
print(value)

expected = [
            "is being used by",
            "Connection closed by foreign host",
            "login:",
            "[Pp]assword:",
            "Login incorrect",
            "# ",
            "No session killed",
        ]

obj = pexpect.spawn("telnet 172.16.251.31 2009", maxread=8192)

obj.sendline("")
result = obj.expect(expected, timeout=3)
#print(result, "dsfgds")
#print(obj.buffer)
obj.sendline("1")
#obj.expect("#")
#print(obj.buffer)
time.sleep(3)

#obj.buffer = bytes()
#print("awesrdfdse", obj.buffer)
try:
    obj.expect("Asdfgdsad", timeout=2)

except pexpect.TIMEOUT:
    pass
print("buffer is", obj.buffer)
time.sleep(2)
obj.sendline("showpilot")

obj.expect("#")
obj.expect("#")
time.sleep(1)
print("before is ", obj.before.decode("utf-8", "ignore"))
print("after is ", obj.after)
print(obj.buffer)


