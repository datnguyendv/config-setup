import glob
import os
import sys

from .constants import DEFAULT_HOST_GROUP


def run_playbooks(options, playbooks, exporter_groups):
    for playbook in playbooks:
        playbook_file = glob.glob(f"playbooks/{playbook}.*ml")[0]
        host_group = DEFAULT_HOST_GROUP

        if exporter_groups and (
            "metric_register" == playbook or "exporter" in playbook
        ):
            host_group = (
                exporter_groups.replace(",", ":").replace('"', "'").replace(" ", "")
            )

        ansible_base = f"ANSIBLE_HOST_KEY_CHECKING=False ANSIBLE_FORCE_COLOR=true"

        if options.action == "syntax-check":
            cmd = f"{ansible_base} ansible-playbook -u {options.user} -i {options.input} {playbook_file} --syntax-check --limit {host_group}"
        elif options.action == "connection-check":
            cmd = f"{ansible_base} ansible -u {options.user} -i {options.input} {host_group} -m ping"
        elif options.action == "dry-run":
            cmd = f"{ansible_base} ansible-playbook -u {options.user} -i {options.input} {playbook_file} --limit {host_group} --check --diff || true"
        elif options.action == "deploy":
            cmd = f"{ansible_base} ansible-playbook -u {options.user} -i {options.input} {playbook_file} --limit {host_group}"
        else:
            continue

        ecode = os.WEXITSTATUS(os.system(cmd))
        if ecode != 0:
            sys.exit(ecode)
