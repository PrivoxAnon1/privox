# privox
Open source, anonymous, privacy respecting voice exchange.

See also: 

  Website: https://privox.io

  Forum: https://app.element.io/#/room/#privox:matrix.org

  Documentation: https://privox.readthedocs.io/en/latest/


api - cgi post handlers

farm - producer farm code

producer - producer node code

test - test and benchmark code and examples

web - website oriented stuff like javascript code and html


Note: 

  The system may be run on mutliple servers or a single server.

See the file 

  farm/privox_config.py

Variables 

  PV_VALIDATE_USER_URL = ''

  PV_POST_TRANSACTION_URL = ''

Regarding this specifically, 

Note there are two files 'transaction.py' and 'validate_key.py' that you do
not need to worry about if you are not going to limit usage or provide 
validation. In that case just disable these functions in the configuration file
and the producer farm will bother with them. Also note regarding these two APIs
that APIs authenticate while producer farms authenticate and post transactions.

To disable this simply set the authenticate url and the transaction url to '' in your farm settings file.


