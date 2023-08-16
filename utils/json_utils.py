import json

from data.dataclasses.country import Country
from utils.file_utils import read_test_data_file


def json_to_country(json_str) -> Country:
    """Convert JSON string to Country object."""
    country_dict = json.loads(json_str)
    return Country.from_dict(country_dict)


def json_file_to_country(file_path) -> Country:
    """Convert JSON file to Country object."""
    json_str = read_test_data_file(file_path)
    return json_to_country(json_str)


def json_file_to_countries(file_path) -> list:
    """Convert JSON file to list of Country objects."""
    json_str = read_test_data_file(file_path)
    json_dict = json.loads(json_str)
    return [Country.from_dict(country) for country in json_dict]


def str_to_json(json_str):
    """Convert string to JSON object."""
    return json.loads(json_str)