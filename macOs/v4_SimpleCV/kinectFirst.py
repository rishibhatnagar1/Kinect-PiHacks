'''Example here: http://tutorial.simplecv.org/en/latest/examples/kinect.html '''

from SimpleCV import *
cam = Kinect()


while True:
        depth = cam.getDepth()
		filtered = depth.stretch(0,250)
        depth.show()
