#!/usr/bin/env python3

import argparse
from tools.timecodes import timecode

parser = argparse.ArgumentParser(description="""Changes subtitle timecodes.
Supported formats: .ass and .srt""")
parser.add_argument('old_file', help="""Path to subtitles file, that need do be
changed.""")
parser.add_argument('-f', '--file', help="""
Name and path to new file with changed timecodes. If not specified - will be
created in current working directory.""")
parser.add_argument('-s', '--seconds', type=int, default=0, help="""The
seconds for which the timecode needs to be corrected. Like: 2 or -12.""")
parser.add_argument('-ml', '--milliseconds', type=int, default=0, help="""
The milliseconds for which the timecode needs to be corrected.""")
parser.add_argument('-min', '--minutes', type=int, default=0, help="""
The minutes for which the timecode needs to be corrected.""")
args = parser.parse_args()
old_file = args.old_file
new_file = args.file
seconds = args.seconds
milliseconds = args.milliseconds
minutes = args.minutes
if not new_file:
    new_file = '_' + old_file

timecode(old_file, new_file, seconds, milliseconds, minutes)
