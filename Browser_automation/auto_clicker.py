from itertools import count
import time
import subprocess

for i in range(50):
      p = subprocess.Popen(["firefox", "https://bit.ly/3TrIQuq"])
      time.sleep(60) 
      p.kill()