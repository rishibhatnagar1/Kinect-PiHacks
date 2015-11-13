from freenect import sync_get_depth as get_depth #Uses freenect to get depth information from the Kinect
import numpy as np #Imports NumPy
import cv,cv2 #Uses both of cv and cv2
import pygame
constList = lambda length, val: [val for _ in range(length)]
def cacheAppendMean(cache, val):
    cache.append(val)
    del cache[0]
    return np.mean(cache)
    
def hand_tracker():
    (depth,_) = get_depth()
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
    #pygame.init() #Initiates pygame
    xSize,ySize = 640,480 #Sets size of window
    #screen = pygame.display.set_mode((xSize,ySize),pygame.RESIZABLE) #creates main surface
    #screenFlipped = pygame.display.set_mode((xSize,ySize),pygame.RESIZABLE) #creates surface that will be flipped (mirror display)
    #screen.fill(BLACK) #Make the window black
    done = False #Iterator boolean --> Tells programw when to terminate
    dummy = False #Very important bool for mouse manipulation
    while not done:
        screen.fill(BLACK) #Make the window black
        (depth,_) = get_depth() #Get the depth from the kinect 
        depth = depth.astype(np.float32) #Convert the depth to a 32 bit float
        _,depthThresh = cv2.threshold(depth, 600, 255, cv2.THRESH_BINARY_INV) #Threshold the depth for a binary image. Thresholded at 600 arbitary units
        _,back = cv2.threshold(depth, 900, 255, cv2.THRESH_BINARY_INV) #Threshold the background in order to have an outlined background and segmented foreground
        #blobData = BlobAnalysis(depthThresh) #Creates blobData object using BlobAnalysis class
        #blobDataBack = BlobAnalysis(back) #Creates blobDataBack object using BlobAnalysis class
        
        #for cont in blobDataBack.contours: #Iterates through contours in the background
        #    pygame.draw.lines(screen,YELLOW,True,cont,3) #Colors the binary boundaries of the background yellow
        #for i in range(blobData.counter): #Iterate from 0 to the number of blobs minus 1
        #    pygame.draw.circle(screen,BLUE,blobData.centroid[i],10) #Draws a blue circle at each centroid
        #    centroidList.append(blobData.centroid[i]) #Adds the centroid tuple to the centroidList --> used for drawing
        #    pygame.draw.lines(screen,RED,True,blobData.cHull[i],3) #Draws the convex hull for each blob
        #    pygame.draw.lines(screen,GREEN,True,blobData.contours[i],3) #Draws the contour of each blob
        #    for tips in blobData.cHull[i]: #Iterates through the verticies of the convex hull for each blob
        #        pygame.draw.circle(screen,PURPLE,tips,5) #Draws the vertices purple
        
        """
        #Drawing Loop
        #This draws on the screen lines from the centroids
        #Possible exploration into gesture recognition :D
        """
        #for cent in centroidList:
        #    pygame.draw.circle(screen,BLUE,cent,10)
    
        
        pygame.display.set_caption('Kinect Tracking') #Makes the caption of the pygame screen 'Kinect Tracking'
        del depth #Deletes depth --> opencv memory issue
        screenFlipped = pygame.transform.flip(screen,1,0) #Flips the screen so that it is a mirror display
        screen.blit(screenFlipped,(0,0)) #Updates the main screen --> screen
        pygame.display.flip() #Updates everything on the window
        
try: #Kinect may not be plugged in --> weird erros
    hand_tracker()
except: #Lets the libfreenect errors be shown instead of python ones
    pass