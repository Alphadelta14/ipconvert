
from ipconvert.backend.vbulletin import VBulletin
from ipconvert.config import config_register

config_register('backend', 'vbulletin')


def get(config):
    """Gets a backend based on the configuration
    """
    if config['backend'] == 'vbulletin':
        return VBulletin(config)
    else:
        raise ValueError('Unknown backend')
