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
    Male = 1
    Female = 2


class EyeColour(Enum):
    Brown = 1
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


# Face Cards/Mystery Cards (one unique Face Card per board)

card1 = {
    "Name": "Alex",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
}

card2 = {
    "Name": "Alfred",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Ginger,
}

card3 = {
    "Name": "Anita",
    Gender: Gender.Female,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Blond,
}

card4 = {
    "Name": "Anne",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
}

card5 = {
    "Name": "Bernard",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Brown,
}

card6 = {
    "Name": "Bill",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
}

card7 = {
    "Name": "Charles",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
}

card8 = {
    "Name": "Claire",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
}

card9 = {
    "Name": "David",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
}

card10 = {
    "Name": "Eric",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
}

card11 = {
    "Name": "Frans",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
}

card12 = {
    "Name": "George",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
}

card13 = {
    "Name": "Herman",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Ginger,
}

card14 = {
    "Name": "Joe",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Blond,
}

card15 = {
    "Name": "Maria",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Brown,
}

card16 = {
    "Name": "Max",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
}

card17 = {
    "Name": "Paul",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
}

card18 = {
    "Name": "Peter",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.White,
}

card19 = {
    "Name": "Philip",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Black,
}

card20 = {
    "Name": "Richard",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.Brown,
}

card21 = {
    "Name": "Robert",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Brown,
}

card22 = {
    "Name": "Sam",
    Gender: Gender.Male,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
}

card23 = {
    "Name": "Susan",
    Gender: Gender.Female,
    EyeColour: EyeColour.Brown,
    HairColour: HairColour.White,
}

card24 = {
    "Name": "Tom",
    Gender: Gender.Male,
    EyeColour: EyeColour.Blue,
    HairColour: HairColour.Black,
}

cards = [
    card1,  card2,  card3,  card4,  card5,  card6,  card7,  card8,
    card9,  card10, card11, card12, card13, card14, card15, card16,
    card17, card18, card19, card20, card21, card22, card23, card24
]

board1 = cards
board2 = cards
mysteryCards = cards


