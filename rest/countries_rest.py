from data.dataclasses.country import Country
from rest.rest_client import RestClient


class CountriesRest(RestClient):
    """
    Countrie API service
    """
    BASE_URL = "https://restcountries.com/v3.1/"

    def get_country_by_name(self, country_name, expected_status_code=200) -> Country:
        self._log.info("Getting country by name")
        response = self._get(f"name/{country_name}", expected_status_code=expected_status_code)
        if response:
            return Country.from_dict(response[0])
        raise ValueError(f"Country with name {country_name} not found")

    def get_country_by_code(self, country_code, expected_status_code=200) -> Country:
        self._log.info("Getting country by code")
        response = self._get(f"alpha/{country_code}", expected_status_code=expected_status_code)
        if response:
            return Country.from_dict(response[0])
        raise ValueError(f"Country with code {country_code} not found")

    def get_countries_by_codes(self, country_codes, expected_status_code=200) -> list:
        self._log.info("Getting countries by codes")
        response = self._get(f"alpha?codes={country_codes}", expected_status_code=expected_status_code)
        if response:
            return [Country.from_dict(country) for country in response]
        raise ValueError(f"Countries with codes {country_codes} not found")

    def get_countries_by_currency(self, currency, expected_status_code=200) -> list:
        self._log.info("Getting countries by currency")
        response = self._get(f"currency/{currency}", expected_status_code=expected_status_code)
        if response:
            return [Country.from_dict(country) for country in response]
        raise ValueError(f"Countries with currency {currency} not found")

    def get_countries_by_language(self, language, fields=None, expected_status_code=200) -> list:
        self._log.info("Getting countries by language")

        url = f"lang/{language}"
        if fields:
            url += f"?fields={','.join(fields)}"

        response = self._get(url, expected_status_code=expected_status_code)
        if response:
            return [Country.from_dict(country) for country in response]
        raise ValueError(f"Countries with language {language} not found")