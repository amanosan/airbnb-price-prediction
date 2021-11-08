import numpy as np
import pandas as pd


def not_in_list(x, lst):
    ''' check if a value is in a list
    Args:
        x: value to check
        lst: list in which to check the value
    Returns:
        bool: 1 if value is not in list, 0 otherwise
    '''
    if x in lst:
        return 0
    else:
        return 1


def negative_check(x):
    ''' to check if value is negative
    Args:
        x: value to check
    Returns:
        bool: 1 if value is negative, 0 otherwise
    '''
    if x >= 0:
        return 0
    else:
        return 1


def out_of_range(x, max_value, min_value):
    ''' check whether value is in a range
    Args:
        x: value to check in range
        max_value: upper bound of the range
        min_value: lower_bound of the range
    Returns:
        bool: 1 if out of range, 0 otherwise
    '''
    if x > max_value or x < min_value:
        return 1
    else:
        return 0


def out_of_bounding_box(latitude, longitude, bounding_box):
    ''' counting whether a location is within a bounding box
    Args:
        latitude: latitude portion of location
        longitude: longitude portion of location
        bounding_box: dictionary with max and min values to compare the location to
    Returns:
        bool: 1 if out of bounding box, 0 otherwise
    '''
    if ((latitude <= bounding_box['max_lat']) and (latitude >= bounding_box['min_lat'])) \
            and ((longitude <= bounding_box['max_long']) and (longitude >= bounding_box['min_long'])):
        return 0
    else:
        return 1
