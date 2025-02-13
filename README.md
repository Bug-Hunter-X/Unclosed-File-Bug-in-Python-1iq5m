# Unclosed File Bug in Python

This repository demonstrates a common error in Python: forgetting to close files after opening them with `open()`. This can lead to resource leaks and prevent other processes from accessing the file.  The provided solution showcases the proper use of `with open(...) as f:` for guaranteed file closure.

## Bug
The file `bug.py` demonstrates the error. Note the absence of a file closure.