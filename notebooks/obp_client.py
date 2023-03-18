import obp_python as obp
import os
from dotenv import load_dotenv
from get_direct_login_token import createDirectLoginToken
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("obp")
logger.propagate = True
load_dotenv()

obp_host = 'https://obp-apisandbox.joinfincubator.com'
configuration = obp.Configuration()
configuration.client_side_validation = False
configuration.host = 'https://obp-apisandbox.joinfincubator.com'
username = 'FadiTannous'
password = 'cymEUh8ixKp4xWR!'
consumer_key = '51a3a09b-acb0-47ea-b0c8-05bf98b5b506'
token = createDirectLoginToken(username, password, consumer_key, configuration.host)
configuration.api_key['Authorization'] = f'DirectLogin token={token}'
client = obp.ApiClient(configuration)
api_instance = obp.APIApi(client)
user_instance = obp.UserApi(client)
empty_body = '{}' # EmptyClassJson | EmptyClassJson object that needs to be added.
api_version = 'v5.0.0' # str | eg:v2.2.0, v3.0.0


