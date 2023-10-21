import os
import pprint
import sys
import numpy
import cv2
#import pylibdmtx #https://libdmtx.sourceforge.net/
#from pylibdmtx.pylibdmtx import decode #as dmtxdecode

env = os.environ
#default_camera = env.get()
print("User's Environment variable:")
pprint.pprint(dict(env), width = 1)