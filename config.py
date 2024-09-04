# config.py

class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY =  "7494737749:AAG5Et7FuBX5B6Hua62xUsEDuvewfjT3D-k"
    OWNER_ID = "5344116851" # Kung di nimo kabalo, run ang bot ug do /id sa imong private chat with it
    OWNER_USERNAME = "@its_megm"

    # RECOMMENDED
    # Retrieve environment variables
    import os

    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_NAME = os.getenv('DATABASE_NAME')

    # Construct the connection URI
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://svc-4hvxba:un12f7EE1eho3hHRzNqCDoUVkRBfGXq9@e4twmj.stackhero-network.com:7016/ah-postgresql-stackhero-shallow-07146'

    )

class Development(Config):
    DEBUG = True
    MESSAGE_DUMP = None

    LOAD = ['module1', 'module2']
    NO_LOAD = 'module3'
    WEBHOOK = False
    URL = "http://your-development-url.com:8443/"

    # OPTIONAL
    SUDO_USERS = [5344116851]
    SUPPORT_USERS = [5344116851]
    WHITELIST_USERS = [5344116851]
    DONATION_LINK = "@its_megm"
    CERT_PATH = r"C:\Users\user\Downloads\isrgrootx1.pem"

    PORT = 7016
    DEL_CMDS = False
    STRICT_GBAN = False
    WORKERS = 8
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'
    ALLOW_EXCL = False
    BMERNU_SCUT_SRELFTI = 0

class Production(Config):
    LOGGER = False
