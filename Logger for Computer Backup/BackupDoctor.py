'''
This code was created to help assist the task of making backup of parts of your computer to multiple accounts in cloud storage and still
    keep track of what you did put in the backup, and where everything is.
This code will log everthing inside the folder "doctor room" into a .txt file inside "records", creating both folders first if necessary

A random username/password will be generated for the name of the .txt file, +1 more in the beggining of it

Use:
-Execute the BackupDoctor.py file.
-Copy and paste the path adress to which both folders will be created.
-To keep better track, copy and paste the path of the folder with the files you are making the backup
-Drag and drop the files from this folder that you want to registry before a backup to the folder "doctor room"
-Press enter if asked, and done.


Tip:
If you plan to use this script more times, you can easily hardcode the root path
of the "doctor room" and "records" folder in this code to avoid being asked every
time. (This is my personal preference as well)

'''


from random import choice, randint
import os
from GenerateRandomPasswordFromText import randomNameFromTuple as new
from GenerateRandomPasswordFromText import textToUniqueWordTuple

uniqueWords=textToUniqueWordTuple() #passwords combinations will be generated based on this variable
space='\n'+'-'*32+'\n'
space2='\n'+'='*32+'\n'
doctorroomNotPreviouslyCreated=False



#Uncomment/comment based on the one which you prefer: Asks everytime its run OR Hardcodes the path

rootPath=input('Provide the path to create the "doctor room" and "records" folder.\n')  #Asks
#rootPath=r'<Paste the path you want to create the folders here>'                       #Hardcodes 
#path example: C:\Users\<yourusername>\Downloads

originalFolder=input('To better help you remember.\nProvide the path from which these files were originally from:\n') #Asks
#originalFolder=r'<your\original\folder>' #Hardcodes



os.chdir(rootPath)
#Creating the "doctor room" and "records" folders if these do not already exists.
if not os.path.exists('doctor room'):   
    os.makedirs('doctor room')
    doctorroomNotPreviouslyCreated=True
if not os.path.exists('records'):
    os.makedirs('records')

registry=rootPath+'\\records\\'+new(uniqueWords)+'.txt'    #The .txt with all the info will be created in this path
doctorroom=rootPath+'\\doctor room'     #Everything inside this folder will be registered inside the registry



def fileIntroduction():
    try:
        with open(registry, 'a+', encoding='utf-8') as f:
            f.write(new(uniqueWords)+'\n\n\n')
            f.write('Original Folder: '+ originalFolder + space)
            print('Original Folder: '+ originalFolder + space)
            print(space)
    except Exception as e:
        print(e)


def cf(currentfolder):
    try:
        with open(registry, 'a+', encoding='utf-8') as f:
            curfol=(originalFolder+currentfolder.removeprefix(rootPath+r'\doctor room'))
            f.write(space2+'Current Folder: '+curfol+space2)
            print(space2+'Current Folder: '+curfol+space2)
    except Exception as e:
        print(e)


def register(iterator,message):
    try:
        with open(registry, 'a+', encoding='utf-8') as f:
            f.write(message)
            print(message)
            for item in iterator:
                f.write(item+'\n')
                print(item)
            f.write(space)
    except Exception as e:
        print(e)



if doctorroomNotPreviouslyCreated:
    input('\nAs the "doctor room" folder was just created now, the program paused so you can move anything you want to it.\n'
        'Press "Enter" when you\'re ready to continue.\n')

fileIntroduction()
for currentFolder, subfolder, files in os.walk(doctorroom):
    cf(currentFolder)
    register(subfolder,'Subfolders included in the backup: \n')
    register(files,'Files included in the backup: \n')
