import configparser


def load_config(input_file):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(input_file)

    playbooks = config.options("playbooks")
    exporter_groups = config.get("all:vars", "exporter-groups", fallback="")

    return config, playbooks, exporter_groups
