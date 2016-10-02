
from ipconvert.config import config_register

config_register('vbulletin', {
    'dbtype': 'mysql',
    'dbname': 'vb_forums',
    'tableprefix': '',
    'dbuser': 'dbuser',
    'dbpass': 'p@ssw0rd',
})


class VBulletin(object):
    def __init__(self, config):
        self._config = config
        self.config = config['vbulletin']
