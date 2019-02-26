
import threading
from zmqbroker import *
import time

class BrokerThread(threading.Thread):
  def run(self):
    a=zmqBroker()

class zmqsub(zmqSubscriber):
  def process(self,mst,msg):
    print "timestamp=%s, msg=%s" %(mst,msg)
    zmqSender("channel:node1").tx("ModFreq:3Mhz")

class SubscriberThread(threading.Thread):
  def run(self):
    b=zmqsub("NetEvent")

class StatsThread(threading.Thread):
  def run(self):
    b=statsqsub("STATSQ")


BrokerThread().start()
SubscriberThread().start()
StatsThread().start()

while True:
  time.sleep(1)

