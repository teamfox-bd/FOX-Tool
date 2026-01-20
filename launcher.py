import os, sys, subprocess

BIN = "./FOX"

if not os.path.exists(BIN):
    sys.exit("FOX binary missing ❌")

subprocess.run([BIN])