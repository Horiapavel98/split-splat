# Split-Splat (split by # of characters)


## Description

Tired of reading `.txt` files with lines that are too long so you have to
scroll right to be able to read the whole line? Raw data deserves better!

The solution is here: Split-Splat is a tool that helps you arrange the text
files and data that you collect into readable `.txt` files.

## Dependencies

The only requirement for running Split-Splat is Python version 3.x.x. This is the version used to build the current version of this tool:

    Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

## Running locally

    usage: split_splat.py [-h] [-c CHARACTERS] [-r RENAME] filename

This tool requires one positional argument: name of the target file.
The other optional arguments is the number of characters to have per
line and the name of the new file.

    Required: filename
    Default: characters/line, new file name

@Horiapavel98