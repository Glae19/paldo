if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "7494737749:AAG5Et7FuBX5B6Hua62xUsEDuvewfjT3D-k"
    OWNER_ID = "5344116851"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "@its_megm"

    # RECOMMENDED
    import os

# Retrieve environment variables
username = os.getenv('DATABASE_USERNAME')
password = os.getenv('DATABASE_PASSWORD')
host = os.getenv('DATABASE_HOST')
port = os.getenv('DATABASE_PORT')
database = os.getenv('DATABASE_NAME')

# Construct the connection URI
SQLALCHEMY_DATABASE_URI = f'postgresql://svc-4hvxba:un12f7EE1eho3hHRzNqCDoUVkRBfGXq9@e4twmj.stackhero-network.com:7016/ah-postgresql-stackhero-shallow-07146'
    # Example of consistent indentation
  class Development:
    DEBUG = True
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist

    LOAD = ['module1' 'module2']
    NO_LOAD = 'module3'
    WEBHOOK = False
    URL = http://e4twmj.stackhero-network.com:8443/

    # OPTIONAL
    SUDO_USERS = 5344116851
    SUPPORT_USERS = 5344116851
    WHITELIST_USERS = 5344116851
    DONATION_LINK = @its_megm
    CERT_PATH = "C:\Users\user\Downloads\isrgrootx1.pem"
    PORT = 7016
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    BMERNU_SCUT_SRELFTI = 0

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
