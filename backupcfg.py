#!/usr/bin/python3

jobs = {"job1" : "/home/ec2-user/environment/ictpng302-vetdss/test/file1",
        "job2" : "/home/ec2-user/environment/ictpng302-vetdss/test/dir1",
        "job3" : "/home/ec2-user/environment/ictpng302-vetdss/test/dir200"}
        
backupDir = "/home/ec2-user/environment/ictpng302-vetdss/backups"

backupLog = "/home/ec2-user/environment/ictpng302-vetdss/backup.log"

smtp = {"sender": "rhatig@gmail.com",
        "recipient": "rhatig@gmail.com",
        "server": "smtp.gmail.com",
        "port": 587,
        "user": "rhatig@gmail.com", # need to specify a gmail email address with an app password setup
        "password": "xfsxzvwkwlrpregi"}   # need a gmail app password     

