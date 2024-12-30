import configparser
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')


def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('Given JSON not found.')
    except json.JSONDecodeError:
        raise ValueError('Invalid JSON format in given file path')
    except Exception as e:
        raise Exception(f'Error reading given file path: {e}')
    return json_data

def read_conf(session, key):
    parser = configparser.ConfigParser()
    parser.read(BASE_DIR + '/config.ini')
    return parser[session][key]

def set_conf(session, key, value):
    parser = configparser.ConfigParser()
    parser.read(BASE_DIR + '/config.ini')
    parser.set(session, key, value)
    with open(BASE_DIR + '/config.ini', 'w') as config_file_instance:
        parser.write(config_file_instance)
