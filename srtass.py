#!/usr/bin/env python3

import argparse

# local import:
from tools.timecodes import main

parser = argparse.ArgumentParser(
    description="""Changes subtitle timecodes.
    Supported formats: .ass and .srt""")
parser.add_argument(
    'file', help="""Path to subtitles file, that need to be changed.""")
parser.add_argument(
    '-s', '--seconds', type=int, default=0,
    help="""The seconds for which the timecode needs to be corrected.
    Like: 2 or -12.""")
parser.add_argument(
    '-ml', '--milliseconds', type=int, default=0,
    help="""The milliseconds for which the timecode needs to be corrected.""")
parser.add_argument(
    '-min', '--minutes', type=int, default=0,
    help="""The minutes for which the timecode needs to be corrected.""")
args = parser.parse_args()
file = args.file
seconds = args.seconds
milliseconds = args.milliseconds
minutes = args.minutes

main(file, seconds, milliseconds, minutes)
