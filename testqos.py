from zmqbroker import *
import time

llim=0
ulim=5
slp=20

while True:
  for level in range(llim,ulim):
     print "Setting level to %d " % level
     zmqSender("QOSQ").tx("qoslevel=%d" % level)
     time.sleep(slp)
  for level in range(ulim,llim,-1):
     print "Setting level to %d " % level
     zmqSender("QOSQ").tx("qoslevel=%d" % level)
     time.sleep(slp)

