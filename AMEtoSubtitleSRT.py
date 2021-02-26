
# created by Simon Duschl, ARRI, sduschl@arri.de | Arnold & Richter Cinetechnik, Munich (c) 2021
# Read CSV from ARRI Meta Extract and write the values from a given column frame accurate into a SRT Subtitle File.
# e.g. frame accurate Focus Distance information. The SRT can be used in many post production tools.
# external module "timecode" is used -> https://pypi.org/project/timecode/#description

from pathlib import Path
from timecode import Timecode
import csv


#set variables (not necessarily needed)

counter = 0
source_tc = "01:00:00:00"
clip_name = "A001C001_210222_MN99"
focus_dis = 1.123
frame_duration = 1

#open CSV file from ARRI Meta Extract
with open('F003C005_190925_MN99.mxf.csv', 'rt') as f:

    # Skip first line of CSV (if any)
    next(f, None)

    # Read DATA from CSV
    data = csv.reader(f, delimiter='\t')
    for row in data:

        # Counter for SRT Subtitle
        counter += 1

        # Set clip name = from CSV ARRI Clip Name
        clip_name = row[2]

        # Set Source TC from CSV Source TC
        source_tc = row[1]

        # Use external module for Timecode calculation / is set to 24fps!
        source_tc = Timecode('24', source_tc)

        # Source Time Code OUT is one frame more as Source Time Code IN
        out_source_tc = Timecode('24', source_tc + frame_duration)

        # Convert TC Seconds to Milliseconds
        source_tc.set_fractional(True)
        out_source_tc.set_fractional(True)

        # Set Focus Distance from CSV Focus Distance
        focus_dis = row[4]

        # Write everything in a SRT formatted Subtitle File
        file1 = open(clip_name + '.srt', 'a')
            # noinspection PyTypeChecker
        file1.write(f"{str(counter)}\n")
        file1.write(f"{str(source_tc)}" + " " + "-->" + " " + f"{str(out_source_tc)}\n")
        file1.write(f"{str(focus_dis)}\n\n")

        file1.close()


