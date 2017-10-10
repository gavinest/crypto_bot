import os
import dotenv

class passwordVault(object):
    HOME = os.getenv('HOME')
    FILEPATH = 'crypto_bot/.env'

    _SECRETS = dotenv.get_variables(os.path.join(HOME, FILEPATH))

    @classmethod
    def get(cls, name):
        return cls._SECRETS[name]

if __name__ == '__main__':
    p = passwordVault
