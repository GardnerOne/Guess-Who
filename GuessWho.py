# Guess Who
#
# Strategy Types:
#   A: random guesses
#   B: Optimised guesses (see later)
#
# Requirements:
#   - Follows official Guess Who rules (see "/GuessWho.pdf")

from enum import Enum


class Gender(Enum):
    Male = 1,
    Female = 2


class EyeColour(Enum):
    Brown = 1,
    Blue = 2


class HairColour(Enum):
    Black = 1,
    Ginger = 2,
    Blond = 3,
    Brown = 4,
    White = 5


class HairStyle(Enum):
    Long = 1,
    Short = 2,
    Bald = 3


class FacialHair(Enum):
    NA = 1,
    Moustache = 2,
    Beard = 3


class Accessory(Enum):
    NA = 1,
    Glasses = 2,
    Hat = 3,
    Earrings = 4,
    Bows = 5


class Countenance(Enum):
    Happy = 1,
    Sad = 2


# Face Cards/Mystery Cards (one unique Face Card per board)
# TODO: Save card data as JSON and import
card1 = {
    "Name": "Alex",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.Moustache,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card2 = {
    "Name": "Alfred",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Ginger,
    HairStyle: HairStyle.Long,
    FacialHair: FacialHair.Moustache,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card3 = {
    "Name": "Anita",
    Gender: Gender.Female,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Blond,
    HairStyle: HairStyle.Long,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Bows,
    Countenance: Countenance.Happy,
    "RosyCheeks": True
}

card4 = {
    "Name": "Anne",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Earrings,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card5 = {
    "Name": "Bernard",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Brown,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Hat,
    Countenance: Countenance.Sad,
    "RosyCheeks": False
}

card6 = {
    "Name": "Bill",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
    HairStyle: HairStyle.Bald,
    FacialHair: FacialHair.Beard,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": True
}

card7 = {
    "Name": "Charles",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.Moustache,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card8 = {
    "Name": "Claire",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: [Accessory.Hat, Accessory.Glasses],
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card9 = {
    "Name": "David",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.Beard,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card10 = {
    "Name": "Eric",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Hat,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card11 = {
    "Name": "Frans",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card12 = {
    "Name": "George",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Hat,
    Countenance: Countenance.Sad,
    "RosyCheeks": False
}

card13 = {
    "Name": "Herman",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
    HairStyle: HairStyle.Bald,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card14 = {
    "Name": "Joe",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Glasses,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card15 = {
    "Name": "Maria",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Brown,
    HairStyle: HairStyle.Long,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Hat,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card16 = {
    "Name": "Max",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.Moustache,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card17 = {
    "Name": "Paul",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Glasses,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card18 = {
    "Name": "Peter",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.White,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card19 = {
    "Name": "Philip",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.Beard,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": True
}

card20 = {
    "Name": "Richard",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Brown,
    HairStyle: HairStyle.Bald,
    FacialHair: [FacialHair.Moustache, FacialHair.Beard],
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card21 = {
    "Name": "Robert",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Brown,
    HairStyle: HairStyle.Short,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.NA,
    Countenance: Countenance.Sad,
    "RosyCheeks": True
}

card22 = {
    "Name": "Sam",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
    HairStyle: HairStyle.Bald,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Glasses,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

card23 = {
    "Name": "Susan",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
    HairStyle: HairStyle.Long,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.NA,
    Countenance: Countenance.Happy,
    "RosyCheeks": True
}

card24 = {
    "Name": "Tom",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Black,
    HairStyle: HairStyle.Bald,
    FacialHair: FacialHair.NA,
    Accessory: Accessory.Glasses,
    Countenance: Countenance.Happy,
    "RosyCheeks": False
}

cards = [
    card1,  card2,  card3,  card4,  card5,  card6,  card7,  card8,
    card9,  card10, card11, card12, card13, card14, card15, card16,
    card17, card18, card19, card20, card21, card22, card23, card24
]

board1 = cards
board2 = cards
mysteryCards = cards
