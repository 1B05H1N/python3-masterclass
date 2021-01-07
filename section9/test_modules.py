"""
Modules and Folders
In Python you also have the possibility to define modules with the help of a folder. 

In this lesson you will learn how to

define modules with the help of a folder, and thus structure your module better
understand what's up with the __init\.py
"""

from hellom import file
file.f()

from hellom import *
file.f()

import hellom
hellom.file.f()

# import whole folder and creating __init__.py file and using above syntax