#!/usr/bin/python3
#Title : backup.py
# Author : Raaj
#Email: rhatig@gmail.com
# Version : 1
#Copyright : Raaj
# this program will debug the command we typed for run this program it the run program button to work
import sys 
import os
import pathlib
import shutil
import smtplib
from backupcfg import jobs, backupDir , backupLog, smtp
from datetime import datetime
# def is for writelogmessage for sending message for sucess whether its working or not.
def writeLogMessage(logMessage, dateTimeStamp,isSuccess):
    try:
        file = open(backupLog, "a") 
        if isSuccess :
            file.write(f"SUCCESS {dateTimeStamp} {logMessage}\n")
        else :
            file.write(f"FAILURE {dateTimeStamp} {logMessage}\n")
            
        file.close()
        
    except :
            print("ERROR: File.") 
# Error handler is basically sends errormessage to the logmessage and dateTimeand stamp         
def errorHandler(errorMessage, dateTimeStamp) :
     
    print(errorMessage)
    writeLogMessage(errorMessage, dateTimeStamp, False) 
    sendEmail(errorMessage)

# append all error messages to email and send
def sendEmail(message):
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")
# def main will do is send to longmessage about the datetimeStamp and arg this to there.
def main () :
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")  
    argCount = len(sys.argv) 
    if not argCount == 2:
       
        errorHandler("ERROR: job not specified", dateTimeStamp)
    else:
        job = sys.argv[1]
        if not job in jobs:
           errorHandler(f"ERROR:job {job} does not exist", dateTimeStamp)
        else:
            source =jobs[job]
            if not os.path.exists(source):
                print (f"ERROR : source {source} source does not exist")
            else:
                destination = backupDir
                if not os.path.exists(destination ):
                    errorHandler(f"ERROR : destination {destination} does not exist", dateTimeStamp) 
                else: 
                 
                    srcPath = pathlib.PurePath()
                    dstLoc = destination + "/" + srcPath.name + "/" + dateTimeStamp
                    # backup directory or file as required
                    if pathlib.Path(source).is_dir():
                        shutil.copytree(source , dstLoc)
                    else:
                        shutil.copy2(source , dstLoc) 
                # Writelogmessage the f'backed up what does do is backed up the wholw file of backup file.'  
                writeLogMessage(f"backed up {source} to {dstLoc}", dateTimeStamp , True)
                      
                 
if __name__ == "__main__":
    main()
      