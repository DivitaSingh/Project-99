import os
import shutil

source = input("Enter the source of the folder")
destination = input("Enter the destination of the folder")
source = source+'/'
destination = destination+'/'

listFiles = os.listdir(source)
for file in listFiles:
    shutil.copy((source+file), destination)