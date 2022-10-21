import random
import sys
import logging

logging.basicConfig(level=logging.INFO)

def obfuscate(file,string):
        code=open(file).read()
        list = []
        for line in code:
            list.append(ord(line))
        obfuscated=[]
        for i in list:
            obfuscated.append(string.replace("'","").replace('"','')*i)

        contents=f'd={obfuscated};exec("".join([chr(len(i)) for i in d]))'

        with open(file.replace('.py','_obf.py'),'w') as f:
            f.write(contents)

try:
    obfuscate(sys.argv[1],sys.argv[2])
except Exception:
    print("[!] USAGE: obf.py <filename> 'character'\n")
