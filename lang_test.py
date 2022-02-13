# references
# https://docs.python.org/3/
# https://www.w3schools.com/python/
# https://pythonguides.com/python-get-all-files-in-directory/
# https://stackoverflow.com/questions/24332996/import-json-data-into-python

import os
import json

# define location of the language files
path = "languageFiles"

# parse json data from master file
master = json.load(open("languageFiles/master_enum.json"))

# create list of all language files in the designated folder
lang_file_objects = []

for root, directories, file in os.walk(path):
	for file in file:
		if(file.startswith("lang_") and file.endswith(".json")):
			lang_file_objects.append({"data":json.load(open("languageFiles/" + file)), "filename":file})

# create list of enums that should be in a language file
master_enums = []

for i in master:
    for j in i["enums"]:
        master_enums.append({"name":j["name"],"screen":i["name"]})

# create list of enums in master file that are missing from a language file
def findMissingEnums(lang):
    # clear
    lang_enums = []

    # get enums from current language file
    for i in lang["data"]:
        lang_enums.append(i["enum"])

    # clear
    missing_enums = []

    # make list of enums that are in the master file
    # but missing from the current language file
    for i in master_enums:
        if i["name"] not in lang_enums:
            missing_enums.append(i)

    # display missing enum's information
    for i in missing_enums:
        print(i["name"] + "    " + i["screen"] + "    (" + lang["filename"] + ")")

# check each language file against the master file
for i in lang_file_objects:
    findMissingEnums(i)