How It Works
************

.. toctree::
   :maxdepth: 2

.. figure:: _static/PriVox_PVX.png
   :class: with-border

   PriVox Voice Exchange System Overview


Central to the Privox voice exchange is the notion of a producer farm. A producer farm 
is a publicly available endpoint which socket consumers and producers can connect to. 
It acts as an anonymous directory connecting producers with consumers in a random manner.

The API servers will take an inbound request and select a producer farm to deliver the 
request to. The producer farm will decide which producer node to forward the request to. Neither
endpoint knows anything about the other. 

Privox maintains a set of Privox controlled producer farms and associated static producer 
nodes, but most producer farms are user contributed as are most producer nodes.

