import sys
sourceFileName = sys.argv[1]

#check that file is plaintext
from winmagic import magic
if magic.from_file(sourceFileName,mime = True) != 'text/plain':
    quit("Source file is not plaintext.")

#new file will be original filename + "utf"
import os
splitName = os.path.splitext(sourceFileName)
targetFileName = splitName[0] + 'utf' + splitName[1]

#detect source encoding
import cchardet as chardet
with open(sourceFileName, "rb") as f:
    msg = f.read()
    result = chardet.detect(msg)
    sourceEncoding = result.get('encoding')

#end if the source is already unicode
if sourceEncoding == 'UTF-8':
    print('Source file is already unicode. Exiting program...')
    quit()

#output UTF-8 encoded file
import codecs
BLOCKSIZE = 1048576 # or some other, desired size in bytes
with codecs.open(sourceFileName, "r", result.get('encoding')) as sourceFile:
    with codecs.open(targetFileName, "w", "utf-8") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)
