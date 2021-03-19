# Version: 0.5.2 beta
# Last changes: 2021-03-19

# Created by Simon Duschl, ARRI, sduschl@arri.de | Arnold & Richter Cinetechnik, Munich (c) 2021
# Read CSV from ARRI Meta Extract and write the values from a given column frame accurate into a SRT Subtitle File.
# e.g. frame accurate Focus Distance information. The SRT can be used in many post production tools.
# External module "timecode" is used -> https://pypi.org/project/timecode/#description

from pathlib import Path
from timecode import Timecode
import csv

#from tkinter import *
#from tkinter import messagebox


counter = 0
source_tc = "01:00:00:00"
clip_name = "A001C001_210222_MN99"
focus_dis = 1.123
frame_duration = 1
project_speed = 24


clip_name = input("Enter ARRI Clip *.CSV (with .csv ending):")

project_speed = int(input("Project Speed of clip (24 or 25):"))



def check_user_input(input):
  if input == 24:
    # Convert it into integer
    val = int(input)
    print("Project Speed is:", val)
  elif input == 25:
    val = int(input)
    print("Project Speed is:", val)
  else:
    print("Only 24fps or 25fps are allowed!")

check_user_input(project_speed)



def convert_csv_24(project_speed_value, clip_name_convert):


  counter = 0

  #open CSV file from ARRI Meta Extract
  with open(clip_name_convert, 'rt') as f:

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
      source_tc = Timecode(project_speed_value, source_tc)

      # Source Time Code OUT is one frame more as Source Time Code IN
      out_source_tc = Timecode(project_speed_value, source_tc + frame_duration)

      # Convert TC Seconds to Milliseconds
      source_tc.set_fractional(True)
      out_source_tc.set_fractional(True)

      # Set Focus Distance from CSV Focus Distance
      focus_dis = row[4]

      # Write everything in a SRT formatted Subtitle File
      file1 = open(clip_name_convert + '.srt', 'a')
      # noinspection PyTypeChecker
      file1.write(f"{str(counter)}\n")
      file1.write(f"{str(source_tc)}" + " " + "-->" + " " + f"{str(out_source_tc)}\n")
      file1.write(f"{str(focus_dis)}\n\n")

      file1.close()

    return clip_name

convert_csv_24(project_speed, clip_name)

print("Operation done! Please find your SRT file in this python code main directory!")
print(clip_name + ".srt")
