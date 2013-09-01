#!/usr/bin/env python

import os
import shutil
import subprocess

PROJECT_BASE_PATH = '../project/'
TEMPLATE_BASE_PATH = '../Templates'

#device selection menu creator
def createDeviceSelect(deviceList):
    TEMPLATE_STR = '_Template'
    deviceMenu = list()
    deviceMenu.append('Please Select the the device family:\n')
    [deviceMenu.append(deviceList[deviceList.index(row)]) for row in deviceList]
    for row in deviceMenu:
        if deviceMenu.index(row):
            deviceMenu[deviceMenu.index(row)] = row.replace(TEMPLATE_STR, '')
    for row in deviceMenu:
        if deviceMenu.index(row):
            choiceNb = str(deviceMenu.index(row))
            deviceMenu[deviceMenu.index(row)] = choiceNb + ': ' + row
    return deviceMenu

#display device families offered to the user
def displayDeviceMenu(deviceMenu):
    for row in deviceMenu:
        print row

#read the device family choice of the user
def readDeviceChoice(deviceMenu):
    familyChoice = raw_input('\nDevice family:')
    inputIsGood = 0
    while not inputIsGood:
        if familyChoice.isdigit():
            choice = int(familyChoice)
            if choice >= 1 and choice <= len(deviceMenu) - 1:
                inputIsGood = 1
            else:
                displayDeviceMenu(deviceMenu)
                familyChoice = raw_input('\nPlease enter one of the number assossiated to the list above:')
        else:
            displayDeviceMenu(deviceMenu)
            familyChoice = raw_input('\nPlease enter one of the number assossiated to the list above:')
    return choice

#ask the new project name
def askProjectName():
    projectName = raw_input('Enter the new project name:')
    return projectName

#create the ignore paturn of a specific directory in the template tree
def ignorePaturn(dirName, dirContent):
    IGNORED = ['.git', 'README.md', 'Debug', 'Release', 'documentation']
    ignoreList = list()
    for row in dirContent:
        if not row.find(IGNORED[0]) or not row.find(IGNORED[1]) or not row.find(IGNORED[2]) or not row.find(IGNORED[3]) or not row.find(IGNORED[4]):
            ignoreList.append(row)
    return ignoreList

#copy files from template directory
def copyFiles(projectName, baseTemplate):
    print ' -Copying the tree.'
    try:
        shutil.copytree(TEMPLATE_BASE_PATH + '/' + baseTemplate, PROJECT_BASE_PATH + projectName, ignore = ignorePaturn)
    except:
        print 'Project already existing.'
        exit()

#update project metadata file
def updateMetadataFile(projectName, baseTemplate, metadataFile):
    projectFile = open(PROJECT_BASE_PATH + projectName + '/' + metadataFile, "r")
    metadata = projectFile.readlines()
    projectFile.close()
    for row in metadata:
        metadata[metadata.index(row)] = row.replace(baseTemplate, projectName)
    projectFile = open(PROJECT_BASE_PATH + projectName + '/' + metadataFile, "w")
    projectFile.writelines(metadata)
    projectFile.close()

#update project metadata
def updateMetadata(projectName, baseTemplate):
    PROJECT_META = '.project'
    PROJECT_CONF = '.cproject'
    print ' -Updating the project metadata.'
    updateMetadataFile(projectName, baseTemplate, PROJECT_META)
    updateMetadataFile(projectName, baseTemplate, PROJECT_CONF)
    os.rename(PROJECT_BASE_PATH + projectName + '/' + baseTemplate + '.launch', PROJECT_BASE_PATH + projectName + '/' + projectName + '.launch')
    updateMetadataFile(projectName, baseTemplate, projectName + '.launch')

#create the new project
def createNewProject(projectName, baseTemplate):
    print 'Creating Project: ' + projectName + ' using ' + baseTemplate + ' template.'
    copyFiles(projectName, baseTemplate)
    updateMetadata(projectName, baseTemplate)
    print 'Project ' + projectName + ' created.'

#create the remote repository
def createRemoteRep(projectName):
    print 'Creating remote reprository: ' + projectName + '.'
    print ' -Creating Readme file.'
    
    print ' -Creating the repository'

    print ' -Adding all files to the repository.'

    print ' -Doing the first commit.'

    print ' -Linking to remote repository.'

    print ' -Pushing the new project.'

    print 'Remote repository ' + projectName + ' created.'

#*******************************************************************************
# Main Script Follow
#*******************************************************************************

print 'STM32 Project Creator.\n'

#chosing the device
deviceList = os.listdir(TEMPLATE_BASE_PATH)
deviceMenu = createDeviceSelect(deviceList)
displayDeviceMenu(deviceMenu)
deviceChoice = readDeviceChoice(deviceMenu)

#asking the name of the new project
projectName = askProjectName()

#creating the new project
templateBase = deviceList[deviceChoice - 1]
createNewProject(projectName, templateBase)





