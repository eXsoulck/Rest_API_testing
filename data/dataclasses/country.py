from typing import List
from typing import Any
from dataclasses import dataclass, field
import json
@dataclass
class Ara:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Ara':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Ara(_official, _common)

@dataclass
class CapitalInfo:
    latlng: List[float]

    @staticmethod
    def from_dict(obj: Any) -> 'CapitalInfo':
        _latlng = obj.get("latlng")
        return CapitalInfo(_latlng)

@dataclass
class Car:
    signs: List[str]
    side: str

    @staticmethod
    def from_dict(obj: Any) -> 'Car':
        _signs = obj.get("signs")
        _side = str(obj.get("side"))
        return Car(_signs, _side)

@dataclass
class CoatOfArms:
    png: str
    svg: str

    @staticmethod
    def from_dict(obj: Any) -> 'CoatOfArms':
        _png = str(obj.get("png"))
        _svg = str(obj.get("svg"))
        return CoatOfArms(_png, _svg)


@dataclass
class Flags:
    png: str
    svg: str
    alt: str

    @staticmethod
    def from_dict(obj: Any) -> 'Flags':
        _png = str(obj.get("png"))
        _svg = str(obj.get("svg"))
        _alt = str(obj.get("alt"))
        return Flags(_png, _svg, _alt)

@dataclass
class Fra:
    f: str
    m: str

    @staticmethod
    def from_dict(obj: Any) -> 'Fra':
        _f = str(obj.get("f"))
        _m = str(obj.get("m"))
        return Fra(_f, _m)


@dataclass
class Idd:
    root: str
    suffixes: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Idd':
        _root = str(obj.get("root"))
        _suffixes = obj.get("suffixes")
        return Idd(_root, _suffixes)


@dataclass
class Maps:
    googleMaps: str
    openStreetMaps: str

    @staticmethod
    def from_dict(obj: Any) -> 'Maps':
        _googleMaps = str(obj.get("googleMaps"))
        _openStreetMaps = str(obj.get("openStreetMaps"))
        return Maps(_googleMaps, _openStreetMaps)

@dataclass
class Name:
    common: str
    official: str
    nativeName: dict

    @staticmethod
    def from_dict(obj: Any) -> 'Name':
        _common = str(obj.get("common"))
        _official = str(obj.get("official"))
        _nativeName = obj.get("nativeName")
        return Name(_common, _official, _nativeName)


@dataclass
class PostalCode:
    format: str
    regex: str

    @staticmethod
    def from_dict(obj: Any) -> 'PostalCode':
        _format = str(obj.get("format"))
        _regex = str(obj.get("regex"))
        return PostalCode(_format, _regex)

@dataclass
class Country:
    name: Name
    tld: List[str] = None
    cca2: str = None
    ccn3: str = None
    cca3: str = None
    cioc: str = None
    independent: bool = None
    status: str = None
    unMember: bool = None
    currencies: dict = None
    idd: Idd = None
    capital: List[str] = None
    altSpellings: List[str] = field(default_factory=list)
    region: str = None
    subregion: str = None
    languages: dict = None
    translations: dict = None
    latlng: List[float] = field(default_factory=list)
    landlocked: bool = None
    borders: List[str] = field(default_factory=list)
    area: float = None
    demonyms: dict = None
    flag: str = None
    maps: Maps = None
    population: int = None
    gini: dict = None
    fifa: str = None
    car: Car = None
    timezones: List[str] = field(default_factory=list)
    continents: List[str] = field(default_factory=list)
    flags: Flags = None
    coatOfArms: CoatOfArms = None
    startOfWeek: str = None
    capitalInfo: CapitalInfo = None
    postalCode: PostalCode = None

    @staticmethod
    def from_dict(obj: Any) -> 'Country':
        _name = Name.from_dict(obj.get("name", {}))
        _tld = obj.get("tld", [])
        _cca2 = str(obj.get("cca2"))
        _ccn3 = str(obj.get("ccn3"))
        _cca3 = str(obj.get("cca3"))
        _cioc = str(obj.get("cioc"))
        _independent = obj.get("independent")
        _status = str(obj.get("status"))
        _unMember = obj.get("unMember")
        _currencies = obj.get("currencies")
        _idd = Idd.from_dict(obj.get("idd", {}))
        _capital = obj.get("capital")
        _altSpellings = obj.get("altSpellings")
        _region = str(obj.get("region"))
        _subregion = str(obj.get("subregion"))
        _languages = obj.get("languages")
        _translations = obj.get("translations")
        _latlng = obj.get("latlng")
        _landlocked = obj.get("landlocked")
        _borders = obj.get("borders")
        _area = obj.get("area")
        _demonyms = obj.get("demonyms")
        _flag = str(obj.get("flag"))
        _maps = Maps.from_dict(obj.get("maps", {}))
        _population = obj.get("population")
        _gini = obj.get("gini")
        _fifa = str(obj.get("fifa"))
        _car = Car.from_dict(obj.get("car", {}))
        _timezones = obj.get("timezones")
        _continents = obj.get("continents")
        _flags = Flags.from_dict(obj.get("flags", {}))
        _coatOfArms = CoatOfArms.from_dict(obj.get("coatOfArms", {}))
        _startOfWeek = str(obj.get("startOfWeek"))
        _capitalInfo = CapitalInfo.from_dict(obj.get("capitalInfo", {}))
        _postalCode = PostalCode.from_dict(obj.get("postalCode", {}))
        return Country(_name, _tld, _cca2, _ccn3, _cca3, _cioc, _independent, _status, _unMember, _currencies, _idd, _capital, _altSpellings, _region, _subregion, _languages, _translations, _latlng, _landlocked, _borders, _area, _demonyms, _flag, _maps, _population, _gini, _fifa, _car, _timezones, _continents, _flags, _coatOfArms, _startOfWeek, _capitalInfo, _postalCode)



# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
