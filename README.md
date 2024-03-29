# Best Practices

[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/best-practices-tlfobe.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/best-practices-tlfobe)

## Description

This repository will be used to demonstrate various coding best-practices we covered in CSCI7000 at CU Boulder.
The program `get_column_stats.py` takes in a data file with tab separated rows and column and returns the mean and average of a specified row.
The program `style.py` is mostly just a demonstration file for the general PEP8 style, with no significant output.

## Usage

To run the `get_column_stats.py` script in this packge, make sure you have Python 3.x and run :

```
python get_column_stats.py --filename [data_file] --col_number [column_number]
```

Where `[data_file]` is the name of the file you would like to analyze and `[column_number]` is the column in that file you would like to analyze.

## Installation

This package and its tests depend on numpy, so before running this program be sure numpy is installed on your pythn build.


To install numpy from conda run the following command :
```
conda install numpy
```

## Testing

This repository comes with a handful of useful test scripts to ensure the program is installed correcty. To run these tests run the following:


### Python Unit Tests
```
python -m unittest basics_test.py
```

### SSSHTest Functional Tests
```
bash basics_test.sh
```