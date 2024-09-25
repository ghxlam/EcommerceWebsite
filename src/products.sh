#!/bin/bash

#make sure that quill.txt is first and staples.txt is second cli input
#checks to see if an input is provided
if [ $# -eq 0 ]; then 
    echo "No input Detected"
    exit 
fi
#makes the folder where all the xhtml files will be kept
mkdir -p xhtmlfiles
#this reads the input file with all the links for first cli input and gets their html file
counterq=1
while IFS= read -r line; do
    output_file="xhtmlfiles/q$counterq.html"
    curl -L "$line" -o "$output_file"
    sleep 3
    ((counterq++))
done < "$1"
#this goes through file by file in the directory and makes the html into xhtml
for file in xhtmlfiles/*.html; do 
    xhtml_file="${file%.html}.xhtml"
    java -jar tagsoup-1.2.1.jar "$file" > "$xhtml_file"
    rm "$file"
done
# this will call the python script and allow database insertion
for file in xhtmlfiles/*.xhtml; do 
    python3 parser.py "$file"
    rm "$file"
done
#this reads the input file with all the links for second cli input and gets their html file
counters=1
while IFS= read -r line; do
    output_file="xhtmlfiles/s$counters.html"
    curl -L "$line" -o "$output_file"
    sleep 3
    ((counters++))
done < "$2"
#this goes through file by file in the directory and makes the html into xhtml
for file in xhtmlfiles/*.html; do 
    xhtml_file="${file%.html}.xhtml"
    java -jar tagsoup-1.2.1.jar "$file" > "$xhtml_file"
    rm "$file"
done
# this will call the python script and allow database insertion
for file in xhtmlfiles/*.xhtml; do 
    python3 parser.py "$file"
    rm "$file"
done
rmdir xhtmlfiles