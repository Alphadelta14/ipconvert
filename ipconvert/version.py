"""ipconvert Version File

Only the `__version__` section of this file should be updated.

`__version__` Must be compliant with SemVer and PEP 440. Literature can be
found at http://semver.org/

NOTE:
* Only use .rcX or .devX
* You can only upload a package once per version name
"""

import re

__version__ = '0.1.0'

__version_dict__ = re.match(
    r'^(?P<major>[0-9]+)\.'
    r'(?P<minor>[0-9]+)\.'
    r'(?P<patch>[0-9]+)'
    r'(?:\.rc(?P<rc>[0-9]+))?'
    r'(?:\.dev(?P<dev>[0-9]+))?'
    r'$',
    __version__).groupdict()

__version_info__ = (
    __version_dict__['major'],
    __version_dict__['minor'],
    __version_dict__['patch']
)

__all__ = ['__version__', '__version_info__', '__version_dict__']
