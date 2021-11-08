import os
import yaml
import logging
import pandas as pd


def get_config(config_file):
    '''
    opens config file which contains parameters for this module
    and returns Python object.

    Returns:
        config: Python dictionary with config params from config file - dictionary
    '''
    current_path = os.getcwd()
    path_to_yaml = os.path.join(current_path, config_file)
    print(f"Path, path_to_yaml: {path_to_yaml}")
    try:
        with open(path_to_yaml, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f'Error reading the config file: {str(e)}')


def print_config(config):
    print('\n')
    for val in config:
        print(f"Config Value {val} --> {str(config[val])}")


def get_path():
    '''
    get path for the data files

    Returns:
        path: path for the data directory
    '''
    raw_path = os.getcwd()
    path = os.path.abspath(os.path.join(raw_path, '..', 'data'))
    return path


def ingest_data(path, input_csv, pickled_input_dataframe, save_raw_dataframe, load_from_scratch):
    ''' load data into dataframe

    Args:
        path: path containing input file
        input_csv: input file name 
        pickled_input_dataframe: pickled version of input dataframe 
    '''
    if load_from_scratch:
        unpickled_df = pd.read_csv(os.path.join(path, input_csv))
        if save_raw_dataframe:
            file_name = os.path.join(path, pickled_input_dataframe)
            print(f"File Name: {file_name}")
            unpickled_df.to_pickle(file_name)
    else:
        unpickled_df = pd.read_pickle(
            os.path.join(path, pickled_input_dataframe))
        logging.debug("Reloader Done")
    return (unpickled_df)
