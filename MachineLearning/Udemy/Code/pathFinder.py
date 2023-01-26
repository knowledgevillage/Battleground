# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:32:47 2022

@author: Shubham Tiwari
"""
import os
from os import path
from os import walk
from os import pardir
import logging as lg

def get(fileName):
    lg.debug('get funcation called succesfully')
    
    fname=fileName
    #print(fname)
    
    #get current working directory
    cwd=os.getcwd()
    #print(cwd)
    
    
    #get parent directory name
    pdir=path.abspath(path.join(cwd, pardir))
    
    # lets find the file 
    for root, dir, files in walk(pdir):
        for name in files:
            if name==fname:
                finalPath=path.abspath(path.join(root, name))
                
    #print(finalPath)
    lg.debug('returns the file path')
    return finalPath
    
    
    
#trgtFile=get('Data.csv')

#print(trgtFile)