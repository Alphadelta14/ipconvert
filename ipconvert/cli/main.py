
import argparse
import sys

from ipconvert.backend import get as get_backend
from ipconvert.config import Configuration


def main():
    """Main entrypoint
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', default='config.ini')
    parser.add_argument('command')
    args = parser.parse_args()
    if args.command == 'generate':
        config = Configuration()
        config.save(args.config)
        return 0
    config = Configuration(args.config)
    backend = get_backend(config)
    return 0

if __name__ == '__main__':
    sys.exit(main())
