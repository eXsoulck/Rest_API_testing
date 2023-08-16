import pytest

from utils.json_utils import json_file_to_country, json_file_to_countries


@pytest.mark.parametrize("country_name, expected_response_file", [
    ("Ukraine", "expected_ukraine.json"),
    ("USA", "expected_usa.json"),
    ("Germany", "expected_germany.json")
])
def test_country_by_name(countries_service, country_name, expected_response_file):
    expected_country = json_file_to_country(expected_response_file)
    actual_country = countries_service.get_country_by_name(country_name)
    assert actual_country == expected_country


@pytest.mark.parametrize("country_code", ["UA", "804", "UKR"])
def test_country_by_code(countries_service, country_code):
    expected_country = json_file_to_country("expected_ukraine.json")
    actual_country = countries_service.get_country_by_code(country_code)
    assert actual_country == expected_country


@pytest.mark.parametrize("country_codes", ["UA,US,DE", "804,840,276", "UKR,USA,DEU"])
def test_countries_by_codes(countries_service, country_codes):
    expected_countries = [json_file_to_country("expected_ukraine.json"),
                          json_file_to_country("expected_usa.json"),
                          json_file_to_country("expected_germany.json")]
    actual_countries = countries_service.get_countries_by_codes(country_codes)
    for country in expected_countries:
        assert country in actual_countries


def test_countries_by_currency_ukraine(countries_service):
    expected_country = [json_file_to_country("expected_ukraine.json")]
    actual_country = countries_service.get_countries_by_currency("UAH")
    assert expected_country == actual_country


def test_countries_by_language_ukraine(countries_service):
    expected_country = [json_file_to_country("expected_ukraine.json")]
    actual_country = countries_service.get_countries_by_language("ukr")
    assert expected_country == actual_country

@pytest.mark.xfail
def test_countries_by_language_eng(countries_service):
    expected_country = json_file_to_countries("expected_country_names_by_eng_language.json")
    actual_country = countries_service.get_countries_by_language("eng", fields=["name"])
    assert actual_country == expected_country