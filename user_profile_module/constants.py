from enum import Enum


# Enums
class GenderEnum(str, Enum):
    female = "female"
    male = "male"
    other = "other"