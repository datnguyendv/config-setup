from optparse import OptionParser


def parse_args():
    usage = "usage: %prog -a <action>"
    parser = OptionParser(usage=usage)

    parser.add_option(
        "-a", "--action", help="The ansible action", dest="action", type="string"
    )
    parser.add_option(
        "-i",
        "--input",
        help="The ansible input inventory",
        dest="input",
        type="string",
        default="input.ini",
    )
    parser.add_option(
        "-u", "--user", help="The ansible remote user", dest="user", type="string"
    )

    options, args = parser.parse_args()

    if not options.action:
        parser.error("Missing action!")

    return options
