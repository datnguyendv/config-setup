from .cli import parse_args
from .config_loader import load_config
from .command_builder import run_playbooks
from .constants import VALID_ACTIONS

import sys


def main():
    options = parse_args()
    if options.action not in VALID_ACTIONS:
        print("ERROR: Unknown action.")
        sys.exit(2)

    config, playbooks, exporter_groups = load_config(options.input)
    run_playbooks(options, playbooks, exporter_groups)


if __name__ == "__main__":
    main()
