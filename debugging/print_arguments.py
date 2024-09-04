#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        print(sys.argv[i])
else:
    print("Uso: ./script.py [argumentos...]")
