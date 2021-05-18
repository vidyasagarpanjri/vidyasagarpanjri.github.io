import struct
import sys
import re
stream_file = sys.argv[1]

stream = open(stream_file,'rb').read()
obfus = re.findall(b'\x84\x03\x00\x00(.*)\x00\x00\x00\x00\x02\x18\x00\x35\x00\x00\x00',stream)
splt = (obfus[0]).decode('ascii').split("O")
list_byte=[]
print (splt[:50])
for i in splt:
    try:
        list_byte.append(int(i).to_bytes(1,'little'))
    except Exception as e:
        print (i,e)
        
with open('embedded1.exe','wb') as ebd:
    for i in list_byte:
        ebd.write(i)

    

