### Find >100 MB file path and cat to a file 
find ./* -size +100M | cat >> .gitignore
find . -type f -newermt "2013-06-01" \! -newermt "2013-06-20"
