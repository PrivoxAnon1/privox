#
# stick any manifest constants shared by the 
# system in here. use PV_ convention for
# pseudo namespacing.
#

PRODUCER_FARM_AUTH_KEY = 'YourFarmName'


# public facing apis. these are what our users hit
PV_TRANSACTION_URL_STT = ''
PV_TRANSACTION_URL_TTS = ''

# location of socket servers.
# this is used by the cgi scripts 
# and the client endpoints
PV_TTS_SOCKET_SERVER_IP = ''
PV_TTS_SOCKET_SERVER_PORT = 0
PV_STT_SOCKET_SERVER_IP = ''
PV_STT_SOCKET_SERVER_PORT = 0

# validate response shared with cgi script
PV_USER_KEY_NOT_FOUND = -1

# where to validate a user key
PV_VALIDATE_USER_URL = ''

# where to post json results transactions 
PV_POST_TRANSACTION_URL = ''

# various keys and identifiers
PV_STT_PRODUCER_FARM_AUTH_KEY = ''
PV_TTS_PRODUCER_FARM_AUTH_KEY = ''

# operational values
PV_STT_CLIENT_TIME_OUT = 20
PV_TTS_CLIENT_TIME_OUT = 20

# socket server constants
PV_AUTH_RESPONSE_SIZE = 17
PV_DEFAULT_SOCKET_HOST = '0.0.0.0'
PV_DEFAULT_SOCKET_PORT_STT = 1776
PV_DEFAULT_SOCKET_PORT_TTS = 1777

STT_CLIENT_REQUEST_TIMEOUT = 60
TTS_CLIENT_REQUEST_TIMEOUT = 60
