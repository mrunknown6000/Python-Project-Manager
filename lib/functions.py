from re import template
from alive_progress import alive_bar
from lib.config import *
from time import sleep
import os


def checkRequirement(templateHeader, templateVariant):
    template = templateConfig[templateVariant][templateHeader]
    requirementTitle = template['requirement']
    executableRequirement = template['checkRequirement']
    os.system('cls')

    print('Checking For Needed Requirement...')
    sleep(2)
    print(f'Checking These Following Requirement: {requirementTitle}')
    result = []
    sleep(2)

    for i in executableRequirement:
        if os.system(i) == 0:
            # Successful Checkup
            result.append(True)
        else:
            result.append(False)
    for i in result:
        if i == True:
            # Failed Requirement Test
            os.system("cls")
            print('''YAY, Your System Met The Requirement For This Template. 
            \n You will be redirected to the next section in 3 seconds...''')
            sleep(3)
            return True
        # Successful Requirement Test
    else:
        return False

# Executing Commands


def progressExecution(templateName, templateDir, templateInstaller):

    # Loading Batch Script
    executionOrder = f"cd {templateInstaller} && installer.bat {templateDir} {templateName}"

    # Execution of Commands
    for i in range(100):
        # Use If i for certain % for more specific
        if i == 5:
            print('Preparing Installation')
        if i == 10:
            print('Installation Is Now Ready!')
            sleep(1)
            print('Initializing Batch Installer...')
            if os.system(executionOrder) == 1:
                print('ERROR: An Error Occurred While Using Batch Installer, Please Try Again Later')
        if i == 80:
            print('Installation Is Completed! YAY')
        yield

# Main thread of project generation


def executionMainThread(name, prgdir, installer):
    '''Executing Project Generation from selected Configuration'''
    print('Initializing Project...')
    sleep(2)
    print('Loading Current Template')

    # !: FIX THIS!!! COMPLETE DEBUG 
    # Generating Loading Bar
    with alive_bar(100) as bar:
        for i in progressExecution(name, prgdir, installer):
            bar()

# Load the parents' category from template.config.json


def categorizedTemplate(templateRoot):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    outputReturn = []
    for i in templateKeys:
        outputReturn.append(templateRoot[i]["name"])
    return outputReturn

# Load the requirements needed from modules


def templateLoader(templateRoot, templateName):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    for i in templateKeys:
        if templateRoot[i]["name"] == templateName:
            return i
    else:
        return None