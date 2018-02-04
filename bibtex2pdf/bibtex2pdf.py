#!/usr/bin/python

# This downloads all shorthand links in a bibtex file.
# Be sure to use the shorthand command in the bibtex file!

# Parameters:
# 1: Path to bibtex file
# 2: Output path

# requires chrome
CHROME_EXECUTABLE = "google-chrome-stable"

import bibtexparser
import os
import sys
import subprocess

specialLinks = [".pdf", "ftp.", "ftp://", ".jpg", ".png", ".svg"]

with open(sys.argv[1]) as bibtex_file:
    bibtex_database = bibtexparser.load(bibtex_file)

for key in bibtex_database.entries_dict:
    shorthand = ""
    try:

        if "link" not in bibtex_database.entries_dict[key]:
            print("[!] " + key + " is missing a link")
            continue

        link = bibtex_database.entries_dict[key]['link']

        if "shorthand" not in bibtex_database.entries_dict[key]:
            print("[!] " + key + " is missing a shorthand")
            continue

        shorthand = bibtex_database.entries_dict[key]['shorthand']

        dirpath = sys.argv[2]

        # sync --> skip
        if os.path.isdir(dirpath + os.sep + shorthand):
            continue
        else:
            os.mkdir(dirpath + os.sep + shorthand)

        isSpecial = False
        for specialLink in specialLinks:
            if specialLink in link:
                isSpecial = True

        if not isSpecial:
            cmd = " ".join([CHROME_EXECUTABLE,
                            "--headless",
                            "--disable-gpu",
                            "--no-sandbox",
                            "--print-to-pdf=" + dirpath + os.sep + shorthand + os.sep + shorthand + ".pdf",
                            link])
        else:
            extension = "." + link.split(".")[-1]
            cmd = " ".join(
                ["wget", link, "-O " + dirpath + os.sep + shorthand + os.sep + shorthand + extension])

        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

    except Exception as e:
        print("[!] Error processing " + shorthand + ":")
        print("\t" + str(e))
