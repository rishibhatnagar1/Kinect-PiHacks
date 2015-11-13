from SimpleCV import *
from pymouse import PyMouse
display = SimpleCV.Display()
m = PyMouse()
cam = SimpleCV.Camera()
#cam = Kinect()
normaldisplay = True


while display.isNotDone():
    img = cam.getImage()
    dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2) #give the colors farthest from black
    segmented = dist.stretch(200,255) #pushes anything rgb below 200 down to zero
    blobs = segmented.findBlobs()
    if blobs:
        #blobs.draw()
        circles = blobs.filter([b.isCircle(0.2) for b in blobs])
        if circles:
            img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.BLUE,3)			#
            m.move(circles[-1].x,circles[-1].y)
			# circles[-1] means last postition of the circle
        if normaldisplay:
            img.show()
        else:
           segmented.show()


