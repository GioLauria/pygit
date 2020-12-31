import sys
import os
import platform
import internal_functions

if platform.system() == "Windows":
    onWindows=True
else:
    onWindows=False

numberOfArguments       = len(sys.argv)
if (numberOfArguments==1):
    internal_functions.Error
elif(numberOfArguments==2):
    detailedChanges         = sys.argv[1]
elif (numberOfArguments==4): 
    detailedChanges         = sys.argv[1]
    switch                  = sys.argv[2]
    release                 = sys.argv[3]
else:
    print ("Error !!!") 

remoteAlias             = "origin"
main_branch             = "main"

