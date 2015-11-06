This somehow magicall worked.

http://openkinect.org/wiki/Getting_Started#OS_X 

All I did was:
1. brew install libfreenect
2. freenect-glview 

The next step is to install and build: https://github.com/OpenKinect/libfreenect 
You will need to install macports , then do install xcode commandline tools and then use this command :sudo port install git-core cmake libusb libtool 
git-core will not get installed mostly, that is fine, remove that and install everything else.

Follow the fetch and build step later.

Install opencv next. Using this: http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/

For now I am only using this: https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/

brew tap homebrew/science 
brew install opencv
cd /usr/local/Cellar/opencv/2.4.9/  ther version here would be different
cat ~/.bash_profile | grep PYTHONPATH
cd /Library/Python/2.7/site-packages/
ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv2.so cv2.so
import cv

-----------
install cython - pip install cython

https://github.com/amiller/libfreenect-goodies.git test the freenect code from here

