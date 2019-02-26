

from ona.zmqbroker import *
import threading

class statsqsub(zmqSubscriber):
  def process(self,mst,msg):
    global curlevel
    print "timestamp=%s, msg=%s" %(mst,msg)
    with open('/tmp/zmq.log', 'a') as ofile:
       ofile.write("timestamp=%s, msg=%s" %(mst,msg))


class StatsThread(threading.Thread):
  def run(self):
    b=statsqsub("STATSQ")

class NetEventThread(threading.Thread):
  def run(self):
    b=statsqsub("NetEvent")

class QoSThread(threading.Thread):
  def run(self):
    b=statsqsub("QOSQ")

StatsThread().start()
NetEventThread().start()
QoSThread().start()

while True:
  time.sleep(1)

