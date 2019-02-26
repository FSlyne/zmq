
import threading
from zmqbroker import *
import time

class zmqsub(zmqSubscriber):
  def process(self,mst,msg):
    print "timestamp=%s, msg=%s" %(mst,msg)

class SubscriberThread(threading.Thread):
  def run(self):
    b=zmqsub("channel:enodeb1")

class NetEvent(threading.Thread):
  def run(self):
    b=zmqsub("NetEvent")


SubscriberThread().start()
NetEvent().start()

while True:
  time.sleep(1)
