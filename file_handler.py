#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import shutil

def copyValFile(targetdir,f,fval):
    print(targetdir)
    for files in os.listdir(targetdir):
        print(files)
        targetFile = os.path.join(targetdir,files)
        if os.path.isfile(targetFile):
            eles = files.split('-')
            seq = int(eles[1])
            if eles[0]=="w":
                seq = seq+50

            f.writelines(files+" "+str(seq)+"\n")
            if int(eles[2].split('.')[0])%5==0:
                fval.writelines(files+" "+str(seq)+"\n")
                #valdir = os.path.join(targetdir,"..","val")
                #shutil.copy(targetFile, valdir)

ff = open("train.txt","w")
fval = open("val.txt","w")
curdir = os.getcwd()
tardir = os.path.join(curdir,"train")
copyValFile(tardir,ff,fval)

ff.close()
fval.close()