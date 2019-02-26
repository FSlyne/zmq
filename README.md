# zmq
Lightweight broker using ZMQ

Set up
1. Start the Broker 
python broker.py

2. Start a publisher
python testqos.py

3. Start a subscriber
python testenbodeb.py

4. Start a logger
python logger.py

in any particular order.

Send a message
1. zmqSender("QOSQ").tx("qoslevel=%d" % level)

Receive a message
2. b=zmqsub("QOSQ")

