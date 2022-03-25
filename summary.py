import os 
import pandas as pd 

mypath = "./2021record"

files =  os.listdir(mypath)


def filterfile(filename):
  name = '00.csv'
  return True if filename[10:] == name else False 


nfile = filter(filterfile, files)
vvfile = tuple(nfile)
print(len(vvfile))