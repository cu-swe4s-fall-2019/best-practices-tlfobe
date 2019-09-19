#!/bin/bash
test -e ssshtest ||  wget -q http://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Testing PEP8 style
run test_style pycodestyle style.py
assert_exit_code 0
assert_no_stdout

run test_get_column_stats_style pycodestyle get_column_stats.py
assert_exit_code 0
assert_no_stdout

# Testing general working behavior with random numbers
for i in `seq 1 10000`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done > data.txt

run test_random_stats python get_column_stats.py --f data.txt --col_number 2

assert_exit_code 0
assert_in_stdout 'mean: 16'
assert_in_stdout 'stdev: 9'
assert_stdout
assert_no_stderr


# Testing expected behavior output with numbers 1 through 10
for j in `seq 1 10`; do
    V=$j;
    (for i in `seq 1 100`; do 
        echo -e "$V\t$V\t$V\t$V\t$V";
    done )> data.txt
    run test_expected_stats python get_column_stats.py --f data.txt --col_number 2
    assert_in_stdout mean: $V.0\nstdev: 0.0
    done

# Testing error handling
run test_no_flag python get_column_stats.py
assert_no_stdout
assert_in_stderr 'arguments are required'
assert_exit_code 2

run test_incorrect_input python get_column_stats.py -f data.txt --col_number number
assert_in_stderr 'invalid int value:'
assert_exit_code 2

run test_invalid_file python get_column_stats.py -f not_a_file.txt --col_number 10
assert_no_stdout
assert_in_stderr 'Check to see if your file is in this'
assert_exit_code 1

run test_column_input python get_column_stats.py -f data.txt --col_number 10
assert_no_stdout
assert_in_stderr 'does not have a column index'
assert_exit_code 1

chmod -r data.txt

run test_file_perimission python get_column_stats.py -f data.txt --col_number 1
assert_exit_code 1
assert_in_sterr 'permisions!'


# cleanup

chmod -r data.txt
rm data.txt
rm -r ssshtest