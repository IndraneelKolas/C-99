import os,shutil

source = 'Downloads/WhiteHat'
destination = 'C:/Indraneel'
source = source+'/'
destination = destination+'/'

listoffiles = os.listdir(source)

for i in listoffiles:
    shutil.copy((source+i), destination)