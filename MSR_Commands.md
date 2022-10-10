## Useful commands and snippets for finding code from the WOC

### Commands

```
# This will show the commit details, including the tree sha, authors, history
echo <commit-sha> | ~/lookup/showCnt commit 3 

# This will list all the files in the tree for a certain sha
echo <tree-sha> | ~/lookup/showCnt tree

# This will show the contents of a files
echo <file-sha> | ~/lookup/showCnt blob

# This will return the file base64 encoded on a single line
echo <file-sha> | ~/lookup/showCnt blob 1
```


### Notes

#### Possible way to Find the README (or any) files

The output of a respository's tree looks like the following code section:
```
100644;a8fe822f075fa3d159a203adfa40c3f59d6dd999;COPYRIGHT
100644;fd302b41386a29c3d19110a394b3f377d8c8a55a;Caldera-license.pdf
100644;ea1a840100ad18f66056e081616c643455d25316;LICENSE
100644;80ef82af7457a1a003c279afa4044598ddcedb8c;MAINTAINERS
100644;70402b9973a93910b0f3d59bcb1c8e7e8209112e;README
100644;7b179b8659417b13b0a3d5c5f184ed29f907b67d;README.md
...
```
The 2nd component is the file sha. We should be able to run the `tree` command and then grep on the `README.md` of the output. This should give us the following content from the tree command
```
100644;7b179b8659417b13b0a3d5c5f184ed29f907b67d;README.md
```
We can then split that line on the `;` character, which will give us the file sha. Once we have the file sha, we can run the `showCnt blob 1` command on the file to get its contents on a single line. 

This processs could be repeated for each commit we'd like to analyze, and for different files.