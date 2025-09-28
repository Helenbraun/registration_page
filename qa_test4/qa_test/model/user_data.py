from dataclasses import dataclass
from enum import Enum

class Subjects(Enum):
    math = "Maths"
    chemistry = "Chemistry"
    english = "English"
    biology = "Biplpgy"

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subject: Subjects
    hobby: str
    upload_filename: str
    currentAddress: str
    state: str
    city:str
