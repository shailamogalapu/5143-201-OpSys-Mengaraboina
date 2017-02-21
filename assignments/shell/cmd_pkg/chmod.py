#!/usr/bin/env python
import os
import sys
def chmod(_flag1,_flag2):
	permission=int(_flag1,8)
        print permission
        os.chmod(_flag2,permission)
        print("changed permission of")
        print(_flag2)
