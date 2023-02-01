# privox

Open source, anonymous, privacy respecting voice exchange.

## Associated Links

  Website: https://privox.io

  Forum: https://app.element.io/#/room/#privox:matrix.org

  Documentation: https://privox.readthedocs.io/en/latest/


## Repo Structure

### api - cgi post handlers
CGI post handlers handle http post requests and select a producer farm to handle the request. They also handle any associated retry logic. These scripts are designed to be run by a webserver like apache or nginx. 


### farm - producer farm code
Socket servers which serve as an informal directrory and exchange between producers and consumers.


### producer - producer node code
Code which runs on a contributor's machine and provides computing power to the voice exchange network. producer nodes connect to producer farms and wait for transcription requests.


### test - test and benchmark code and examples
Code to test basic features and provide simple examples like a local closed caption application.


### web - website oriented stuff like javascript code and html
The website has a page which performs STT and TTS. This is that code.


## Notes 

  The system may be run on mutliple servers or a single server.

See the file 

  farm/privox_config.py


The variables 

  PV_VALIDATE_USER_URL = ''

  PV_POST_TRANSACTION_URL = ''

May be used to disable key authentication and/or transaction processing.

Note there are two files 'transaction.py' and 'validate_key.py' that you do
not need to worry about if you are not going to limit usage or provide 
validation. In that case just disable these functions in the configuration file
and the producer farm will bother with them. Also note regarding these two APIs
that APIs authenticate while producer farms authenticate and post transactions.

To disable this simply set the authenticate url and the transaction url to '' in your farm settings file.

If you want to implement validation you will need to put the 'transaction.py' file somewhere your producer farm can reach. 
This script in its current state also requires connection to a mysql database. This is the same for the 'validate_key.py' 
script. 


