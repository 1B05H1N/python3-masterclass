"""
In Python you have the possibility to pack code into modules, which you can use in different place

In this lesson: 

you create a small module
and import this module into the notebook.  
"""

import hello

hello.world()

hello.mars()

from hello import world, mars

world()
mars()

from hello import *

world()
mars()
pluto()