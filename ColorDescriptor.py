import numpy as np
import cv2
import imutils

class ColorDescriptor:
	def __init__(self, bins):
		# number of bins for the 3D histogram
		self.bins = bins
	def describe(self, image):
		# using HSV color space 
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []
		
		# computing the center of the image
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))
		
        # segmenting the image (localization)
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
			(0, cX, cY, h)]
		
		# elliptical mask = center of the image
		(axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)
		
		
		for (startX, endX, startY, endY) in segments:
			# construct a mask for each corner of the image (subtract the elliptical center from it)
			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)
			
			# extract histogram and update feature vector
			hist = self.histogram(image, cornerMask)
			features.extend(hist)
		
		hist = self.histogram(image, ellipMask)
		features.extend(hist)
		
		return features
	
	def histogram(self, image, mask):
		# extract a 3D color histogram from the masked region of the
		# image, using the supplied number of bins per channel
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
			[0, 180, 0, 256, 0, 256])
		# normalize the histogram if we are using OpenCV 2.4
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()
		# otherwise handle for OpenCV 3+
		else:
			hist = cv2.normalize(hist, hist).flatten()
		# return the histogram
		return hist
        

        