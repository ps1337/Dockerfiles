#!/bin/bash

# The directory of the file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Save the users UID for later
UID_=$(id -u)

sudo docker run \
    -it \
    --rm \
    --name=bibtex2pdf \
    --env UID_=$UID_ \
    -v $DIR/bib.bibtex:/tmp/bib.bibtex \
    -v $DIR/data:/home/chrome/bibtex-downloads \
    ps1337/bibtex2pdf \
    bash -c "usermod -u $UID_ chrome && su -c 'python /home/chrome/bibtex2pdf.py /tmp/bib.bibtex /home/chrome/bibtex-downloads' chrome"
