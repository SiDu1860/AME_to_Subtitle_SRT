Version: 0.5.1 beta

Last changes: 2021-02-26

Created by Simon Duschl, ARRI, sduschl@arri.de | Arnold & Richter Cinetechnik, Munich (c) 2021 Read CSV from ARRI Meta Extract and write the values from a given column frame accurate into a SRT Subtitle File. e.g. frame accurate Focus Distance information. The SRT can be used in many post production tools. 

External module "timecode" is used -> https://pypi.org/project/timecode/#description

To generate a CSV with [ARRI Meta Extract](https://www.arri.com/en/learn-help/learn-help-camera-system/tools/arri-meta-extract) which can be read by this short python code.

**Please only select these Metadata fields in the ARRI Meta Extract for the CSV export:**
- Master TC
- Camera Clip Name
- Lens Focus Distance

A sample CSV is also available in this project. Please verify that your generated CSV and columns are equal to this sample CSV. If there are more columns the code needs to be changed. 


