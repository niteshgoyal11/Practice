import configparser
config = configparser.ConfigParser()
config.read("file.log")
print(config.sections())
print(config.get("telnet", "telnet_ip"))

import hashlib
hashlib.md5(raw.encode('utf-8')).hexdigest()