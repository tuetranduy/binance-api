from dotenv import dotenv_values

env = dotenv_values("local.env")

REST_BASE_URL = 'https://testnet.binancefuture.com'
WS_BASE_URL = 'wss://stream.binancefuture.com'
API_KEY = env.get('API_KEY')
API_SECRET = env.get('API_SECRET')
TEST_MODE = True
