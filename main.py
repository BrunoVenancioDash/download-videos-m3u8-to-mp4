# Author: Bruno Venâncio
# data: 22/04/2022

#
# Program to download videos in format m3u8
# using ffmpeg and save in corresponding folder
#

# Libraries
import os 

def quantityName(name, count):
    msgOut = "{}_{}".format(name, str(count))
    print("msgOut: ",msgOut)
    return msgOut


def download (url, folderName, FileName):
    FileNameMp4 = folderName+"/"+FileName

    print("FileNameMp4: ",FileNameMp4)
    if (os.path.exists(FileNameMp4+".mp4")):
        count = 1

        FileNameVerify = quantityName(FileNameMp4, count)
        
        while os.path.exists(FileNameVerify+".mp4"):
            print(FileNameVerify)
            count=count+1
            FileNameVerify = quantityName(FileNameMp4, count)
        FileNameMp4=FileNameVerify

    command = "ffmpeg -i "+url+" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 "+FileNameMp4+".mp4"
    # print("command: "+command)
    try:
        os.system(command)
    except:
        print("Erro in process a download of video")        


def createFolder(folderName):
    if os.path.isdir(folderName):
        print("Folder: {} exit, non necessary create ...\n".format(folderName)) 
    else:    
        print("Folder: {} non exit, creating ...\n".format(folderName))
        os.mkdir(folderName)


# Videos to Download
files = [
   ["folder_1", "First_Video", "https://<LINK>.m3u8"],
   ["folder_1", "First_Video", "https://<LINK>.m3u8"],
   ["folder_2", "First_Video", "https://<LINK>.m3u8"]
]

#=== 

for folderName, FileName, url in files:
    
    createFolder(folderName)
    download(url, folderName, FileName)
