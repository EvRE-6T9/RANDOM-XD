import os, sys
os.system("git pull")
try:
    __import__("AXSMATAL").ariyan()
except Exception as e:
    exit(str(e))
