#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import Ice 
Ice.loadSlice('ImageICE.ice')
Ice.updateModules()

import ImageICE
import numpy as np
import threading, time
from datetime import datetime

class image_converter:
  def __init__(self):
    cv2.namedWindow("Image window", 1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image_raw",Image,self.callback)
    self.lock = threading.Lock()

  def callback(self,data):
    try:
      self.lock.acquire(); 
      self.img = self.bridge.imgmsg_to_cv2(data, "bgr8")   
      self.lock.release();
    except CvBridgeError, e:
      print e
#    print data.height, data.width, data.step, data.encoding
    cv2.imshow("Image window", self.img)
    cv2.waitKey(3)

  def getImage(self):
    self.lock.acquire();
    imagen_result = self.img.copy()
    self.lock.release();
    return imagen_result

class ImageProvider(ImageICE.ImageProvider):
    def __init__(self):
        self.ic = image_converter()
    def getImageData(self, current=None):
        img = self.ic.getImage()
#        img = cv2.imread("lena.png");
        data = ImageICE.ImageDescription()
        data.width = img.shape[0]
        data.height = img.shape[1]
        ret, buf = cv2.imencode(".jpg", img, [1, 55]);
        data.sizeCompress = buf.shape[0]
        data.imageData = buf
        return data

class Server(Ice.Application):
    def run(self, args):
        if len(args) > 1:
            print(self.appName() + ": too many arguments")
            return 1

        object = ImageProvider()

        adapter = self.communicator().createObjectAdapter("ImageServer")
        adapter.add(object, self.communicator().stringToIdentity("ImageServer"))
        adapter.activate()
        rospy.init_node('image_converter', anonymous=True)
        try:
           rospy.spin()
        except KeyboardInterrupt:
           print "Shutting down"
        self.communicator().waitForShutdown()
        return 0
"""
def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
  cv2.destroyAllWindows()
"""
if __name__ == '__main__':
#   sys.stdout.flush()
#   app = Server()
#   sys.exit(app.main(sys.argv, "config.server"))
#   main(sys.argv)
   sys.stdout.flush()
   app = Server()
   sys.exit(app.main(sys.argv, "config.server"))

