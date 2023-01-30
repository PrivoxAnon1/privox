How It Works
************

.. toctree::
   :maxdepth: 2

.. figure:: _static/PriVox_PVX.png
   :class: with-border

   PriVox Voice Exchange System Overview


Central to the Privox voice exchange is the notion of a producer farm. A producer farm 
is a publicly available endpoint which socket consumers and producers can connect to. 
It acts as an anonymous directory connecting producers with consumers in a pseudo random manner.

The API servers will take an inbound request and select a producer farm to deliver the 
request to. The producer farm will decide which producer node to forward the request to. Neither
endpoint knows anything about the other. 

Privox maintains a set of Privox controlled producer farms and associated static producer 
nodes, but most producer farms are user contributed as are most producer nodes.

When a request is received by an API server (api.privox.io/stt for example), it selects a user
powered producer farm and sends it the request. If that fails it will try a second and if that
fails, it will fallback to an organizational producer farm.

Currently the producer farm work distribution strategy is simply to spin thru the list of 
available producer nodes in an array which is organized by time connected and forward the 
request to the first idle connection found. Obviously this can be improved upon in the future
as may the API server farm selection strategy.


