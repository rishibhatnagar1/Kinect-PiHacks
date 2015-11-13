from freenect import sync_get_depth as get_depth #Uses freenect to get depth information from the Kinect
import numpy as np #Imports NumPy
import cv,cv2 #Uses both of cv and cv2
import pygame
constList = lambda length, val: [val for _ in range(length)]

''' function to find the contours etc '''
class BlobAnalysis:
    def __init__(self,BW): #Constructor. BW is a binary image in the form of a numpy array
        self.BW = BW
        cs = cv.FindContours(cv.fromarray(self.BW.astype(np.uint8)),cv.CreateMemStorage(),mode = cv.CV_RETR_EXTERNAL) #Finds the contours
        counter = 0
        """
        These are dynamic lists used to store variables
        """
        centroid = list()
        cHull = list()
        contours = list()
        cHullArea = list()
        contourArea = list()
        while cs: #Iterate through the CvSeq, cs.
            if abs(cv.ContourArea(cs)) > 2000: #Filters out contours smaller than 2000 pixels in area
                contourArea.append(cv.ContourArea(cs)) #Appends contourArea with newest contour area
                m = cv.Moments(cs) #Finds all of the moments of the filtered contour
                try:
                    m10 = int(cv.GetSpatialMoment(m,1,0)) #Spatial moment m10
                    m00 = int(cv.GetSpatialMoment(m,0,0)) #Spatial moment m00
                    m01 = int(cv.GetSpatialMoment(m,0,1)) #Spatial moment m01
                    centroid.append((int(m10/m00), int(m01/m00))) #Appends centroid list with newest coordinates of centroid of contour
                    convexHull = cv.ConvexHull2(cs,cv.CreateMemStorage(),return_points=True) #Finds the convex hull of cs in type CvSeq
                    cHullArea.append(cv.ContourArea(convexHull)) #Adds the area of the convex hull to cHullArea list
                    cHull.append(list(convexHull)) #Adds the list form of the convex hull to cHull list
                    contours.append(list(cs)) #Adds the list form of the contour to contours list
                    counter += 1 #Adds to the counter to see how many blobs are there
                except:
                    pass
            cs = cs.h_next() #Goes to next contour in cs CvSeq
        """
        Below the variables are made into fields for referencing later
        """
        self.centroid = centroid
        self.counter = counter
        self.cHull = cHull
        self.contours = contours
        self.cHullArea = cHullArea
        self.contourArea = contourArea
        print "Here bro"

"""
The function below is a basic mean filter. It appends a cache list and takes the mean of it.
It is useful for filtering noisy data
cache is a list of floats or ints and val is either a float or an int
it returns the filtered mean
"""
def cacheAppendMean(cache, val):
    cache.append(val)
    del cache[0]
    return np.mean(cache)

def hand_tracker():
    (depth,_) = get_depth()
    print type(depth)
    cHullAreaCache = constList(5,12000) #Blank cache list for convex hull area
    areaRatioCache = constList(5,1) #Blank cache list for the area ratio of contour area to convex hull area
    centroidList = list() #Initiate centroid list
    #RGB Color tuples
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    PURPLE = (255,0,255)
    BLUE = (0,0,255)
    WHITE = (255,255,255)
    YELLOW = (255,255,0)
    pygame.init() #Initiates pygame    
    xSize,ySize = 640,480 #Sets size of window
    screen = pygame.display.set_mode((xSize,ySize),pygame.RESIZABLE) #creates main surface
    screenFlipped = pygame.display.set_mode((xSize,ySize),pygame.RESIZABLE) #creates surface that will be flipped (mirror display)
    screen.fill(BLACK) #Make the window black
    print "Initiated"
    done = False #Iterator boolean --> Tells programw when to terminate
    dummy = False #Very important bool for mouse manipulation
    #while not done:
	#screen.fill(BLACK)
    #(depth,_) = get_depth() #Get the depth from the kinect 
    depth = depth.astype(np.float32) #Convert the depth to a 32 bit float
    _,depthThresh = cv2.threshold(depth, 600, 255, cv2.THRESH_BINARY_INV) #Threshold the depth for a binary image. Thresholded at 600 arbitary units
    _,back = cv2.threshold(depth, 900, 255, cv2.THRESH_BINARY_INV) #Threshold the background in order to have an outlined background and segmented foreground
    blobData = BlobAnalysis(depthThresh) #Creates blobData object using BlobAnalysis class
    print blobData
    blobDataBack = BlobAnalysis(back) #Creates blobDataBack object using BlobAnalysis class
    for cont in blobDataBack.contours: #Iterates through contours in the background
        #The below line has to be changed with display.
        pygame.draw.lines(screen,YELLOW,True,cont,3) #Colors the binary boundaries of the background yellow
        print "blogFound"
    
    for i in range(blobData.counter): #Iterate from 0 to the number of blobs minus 1
        pygame.draw.circle(screen,BLUE,blobData.centroid[i],10) #Draws a blue circle at each centroid
        centroidList.append(blobData.centroid[i]) #Adds the centroid tuple to the centroidList --> used for drawing
        pygame.draw.lines(screen,RED,True,blobData.cHull[i],3) #Draws the convex hull for each blob
        pygame.draw.lines(screen,GREEN,True,blobData.contours[i],3) #Draws the contour of each blob
        for tips in blobData.cHull[i]: #Iterates through the verticies of the convex hull for each blob
            pygame.draw.circle(screen,PURPLE,tips,5) #Draws the vertices purple
            #Mouse Try statement
    
        for cent in centroidList:
            pygame.draw.circle(screen,BLUE,cent,10)
    
        
        pygame.display.set_caption('Kinect Tracking') #Makes the caption of the pygame screen 'Kinect Tracking'
        del depth #Deletes depth --> opencv memory issue
        screenFlipped = pygame.transform.flip(screen,1,0) #Flips the screen so that it is a mirror display
        screen.blit(screenFlipped,(0,0)) #Updates the main screen --> screen
        pygame.display.flip() #Updates everything on the window
        
        #Mouse Try statement
        try:
            centroidX = blobData.centroid[0][0]
            centroidY = blobData.centroid[0][1]
            print centroidX
            print centroidY
            
        except: #There may be no centroids and therefore blobData.centroid[0] will be out of range
            pass
            
        for e in pygame.event.get(): #Itertates through current events
            if e.type is pygame.QUIT: #If the close button is pressed, the while loop ends
                done = True
try: #Kinect may not be plugged in --> weird erros
    hand_tracker()
except: #Lets the libfreenect errors be shown instead of python ones
    pass
































