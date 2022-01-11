Version: 0.5.3 beta
Last changes: 2022-01-11

Created by Simon Duschl, ARRI, sduschl@arri.de | Arnold & Richter Cinetechnik, Munich (c) 2021
Read CSV from ARRI Meta Extract and write the values from a given column frame accurate into a SRT Subtitle File.
e.g. frame accurate Focus Distance information. The SRT can be used in many post production tools.
External module "timecode" is used -> https://pypi.org/project/timecode/#description

Please verify that for an AME extract only Camera Clip Name, Master TC, Lens Focal Length and Lens Focus Distance is selected.
column1 = Index
column2 = Master TC
column3 = Camera Clip Name
column4 = Master TC (again)
column5 = Lens Focus Distance
column1 = Lens Focal Length

**Changelog: 0.5.3 beta**

- added user input for 24 or 25 project speed/timecode
- added user input for file name
- user can select to write Focus Distance or Focal Length to SRT file

**Important instructions:**

- works only with 24fps and 25fps timecode up to now
- Please only select these Metadata fields in the ARRI Meta Extract for the CSV export:
  + Master TC
  + Camera Clip Name
  + Lens Focus Distance

A sample CSV is also available in this project. Please verify that your generated CSV and columns are equal to this sample CSV. If there are more columns the code needs to be changed.


