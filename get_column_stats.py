import sys
import math
import argparse


def get_column_from_file(file_name, col_num):
    """
    Gets specified column from a file and returns as a Python list

    Arguments
    ---------
    file_name : str
        name of file to read from
    col_num : int
        column of data to use from specified file

    Returns
    -------
    V : list of int/floats
        list of the specific column
    """
    f = open(file_name, 'r')

    V = []

    for l in f:
        A = [int(x) for x in l.split()]
        V.append(A[col_num])

    return(V)


def calc_mean(column_list):
    """
    takes the mean of a list provided

    Arguments
    ---------
    column_list : list of int/floats

    Returns
    -------
    mean : float
    """

    mean = sum(column_list)/len(column_list)
    return(mean)


def calc_stdev(column_list):
    """
    takes the standard deviation of a provided list

    Arguments
    ---------
    column_list : list of int/floats

    Returns
    -------
    stdev : float
    """
    mean = calc_mean(column_list)
    stdev = math.sqrt(
        sum([(mean-x)**2 for x in column_list]) / len(column_list))
    return(stdev)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f',
                        '--filename',
                        required=True,
                        help='Input file with data in rows and columns',
                        type=str,
                        )
    parser.add_argument('--col_number',
                        required=True,
                        help='column number which to take the mean and std of',
                        type=int,
                        )

    # Parse Arguments from command line
    args = parser.parse_args()
    try:
        column = get_column_from_file(args.filename, args.col_number)
    except IndexError:
        print(args.filename, 'does not have a column index',
              str(args.col_number)+'!')
        sys.exit(1)
    except FileNotFoundError:
        print(args.filename,
              'could not be found! Check to see if your',
              'file is in this directory')
        sys.exit(1)
    except PermissionError:
        print(args.filename, 'could not be opened! Check',
              str(args.filename)+"'s", 'permisions!')
        sys.exit(1)

    # Do specific calculations
    mean = calc_mean(column)
    stdev = calc_stdev(column)

    # Output results
    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
