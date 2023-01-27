# privox
Open source, anonymous, privacy respecting voice exchange.

See also: 

  https://privox.io

  https://app.element.io/#/room/#privox:matrix.org


api - cgi post handlers

farm - producer farm code

producer - producer node code

test - test and benchmark code and examples

web - website oriented stuff like javascript code


Note: 

  The system may be run on mutliple servers or a single server.

See the file 

  farm/privox_config.py

Variables 

  PV_VALIDATE_USER_URL = ''
  PV_POST_TRANSACTION_URL = ''

Regarding this specifically, 

  APIs authenticate

  Producer Farms Authenticate and Post Transactions

To disable this simply set the authenticate url and the transaction url to '' in your farm settings file.


