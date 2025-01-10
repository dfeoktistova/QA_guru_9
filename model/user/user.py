from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Hobbies(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


class State(Enum):
    NCR = 'NCR'
    UTTAR_PRADESH = 'Uttar Pradesh'
    HARYANA = 'Haryana'
    RAJASTHAN = 'Rajasthan'


class City_NCR(Enum):
    DELHI = 'Delhi'
    GURGAON = 'Gurgaon'
    NOIDA = 'Noida'


class City_UTTAR_PRADESH(Enum):
    AGRA = 'Agra'
    LUCKNOW = 'Lucknow'
    MERRUT = 'Merrut'


class City_HARYANA(Enum):
    KARNAL = 'Karnal'
    PANIPAT = 'Panipat'


class City_RAJASTHAN(Enum):
    JAIPUR = 'Jaipur'
    JAISELMER = 'Jaiselmer'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    user_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: str
    hobbies: Hobbies
    picture: any
    address: str
    state: State
    city: City_NCR


user = User(
    first_name='Santa',
    last_name='Claus',
    email='Santa@mail.com',
    gender=Gender.MALE,
    user_number='1234567890',
    birth_day='11',
    birth_month='April',
    birth_year='2007',
    subjects='Maths',
    hobbies=Hobbies.READING,
    picture='pic.webp',
    address='Zamshina street, 11/5',
    state=State.NCR,
    city=City_NCR.NOIDA)
