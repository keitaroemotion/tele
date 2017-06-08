#!/usr/bin/env python3

import sys
import os.path
import subprocess

ALIASES = "/usr/local/etc/tele/aliases"

def write(path, content=""):
    f = open(path, "a")
    content == "" or f.write(content + "\n")
    f.close

def read(path):
    f = open(path, "r")
    aliases = f.read().split("\n")
    f.close
    return aliases

def mkdir(path):
    directory = str(os.path.dirname(path))
    os.path.isdir(directory) or os.mkdir(directory)
    return path

os.path.exists(ALIASES) or write(mkdir(ALIASES))

def register_current_path_as_alias(path):
     key         = input("key: ") 
     pwd         = os.getcwd()
     description = input("description: ") 
     write(path, "{} {} {}".format(key, pwd, description))
     print("\nregistration finished.\n")

def first(tokens):
     return tokens.split(' ')[0]

def second(tokens):
     return tokens.split(' ')[1]

def goto_alias(path, key):
     aliases = read(path)
     print("")
     [ print(x) for x in aliases]
     if key == None:
         key = input("which one? ")
     dest = [ second(x) for x in read(path) if first(x) == key][0]
     print(dest)
     os.chdir(dest)

def pop(args, index):
     return len(args) > index and args[index] or None

option = pop(sys.argv, 1)

if option == "-h":
  print("")
  print("tele [add] .... add alias")
  print("")
elif option == "add":
  register_current_path_as_alias(ALIASES)
else:
  #
  # issue: cannot change current dir after process ends
  #
  goto_alias(ALIASES, option)


