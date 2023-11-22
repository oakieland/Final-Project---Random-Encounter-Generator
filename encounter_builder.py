from gui import *
from PyQt6.QtWidgets import *
from dice import *

''' ---------------------------------------------------------------------------------------------------------------- '''
''' -------------------------------------------- Encounter Setup -------------------------------------------------- '''
''' ---------------------------------------------------------------------------------------------------------------- '''

class Encounter:
    """
        Dictionaries for space and marching order, and illumination.
        Format: Die Roll: ["Added to Description","Added to Explaination"]
        Most of the Encounters use a d20, however, I use a d6 to randomize the results slightly.
    """
    @staticmethod
    def encounter_setup() -> list:
        """
        Method to choose "Space and Marching Order" and "Illumination"
        Prefixes:
            file = the .txt file that is read.
            nara = the narration that would be read aloud.
            rule = the rules related to the above narration.
        :return: output, 2 lines from space_and_marching_order.txt and illumination.txt
        """
        # Space and Marching Order
        size = 3
        choice = read_roller(1, size)
        file_space_and_marching_order = open('encounters/space_and_marching_order.txt').readlines()
        nara_space_and_marching_order = (file_space_and_marching_order[choice]).strip()
        rule_space_and_marching_order = file_space_and_marching_order[choice + size]

        # Illumination
        size = 4
        choice = read_roller(1, size)
        file_illumination = open('encounters/illumination.txt').readlines()
        nara_illumination = (file_illumination[choice]).strip()
        rule_illumination = file_illumination[choice + size]

        output = [nara_space_and_marching_order, rule_space_and_marching_order, nara_illumination, rule_illumination]
        return output

    @staticmethod
    def terrain(name) -> list:
        """
        Method to choose Terrain, similar to the above, but less streamlined.
        Prefixes:
            file = the .txt file that is read.
            nara = the narration that would be read aloud.
            rule = the rules related to the above narration.
        :return: output, 3 strings in a list are outputted: The name, narration and rules.
        """
        # Convert name to file
        filename = str(name).lower().replace(" ", "_")

        # Makes sure the file doesn't crash if the txt. file goes missing.
        try:
            file_encounter = open(f'encounters/{filename}.txt').readlines()
        except FileNotFoundError:
            return [name, f"", f"<b>Error.</b><br> Please add {filename}.txt to encounters folder."]

        # The file mirrors itself, half would be the narration and the other half the rules.
        size = (len(file_encounter) // 2)
        choice = read_roller(1, size)

        # Take the rules and narration from the file.
        narration = (file_encounter[choice]).strip()
        description = file_encounter[choice + size]




        output = [name, narration, description]
        return output

    @staticmethod
    def creature(name) -> list:
        """
        Method to choose Creature, similar format as terrain but requires more rolls.
        Prefixes:
            file = the .txt file that is read.
            nara = the narration that would be read aloud.
            rule = the rules related to the above narration.
        :return: output, 3 strings in a list are outputted: The name, narration and rules.
        """
        # Convert name to file
        filename = str(name).lower().replace(" ", "_")

        # Makes sure the file doesn't crash if the txt. file goes missing.
        try:
            file_encounter = open(f'encounters/{filename}.txt').readlines()
        except FileNotFoundError:
            return [name, f"", f"<b>Error.</b><br> Please add {filename}.txt to encounters folder."]

        # The file mirrors itself, half would be the narration and the other half the rules.
        size = (len(file_encounter) // 2)
        choice = read_roller(1, size)

        # Take the rules and narration from the file.
        narration = (file_encounter[choice]).strip()
        description = file_encounter[choice + size]

        output = [name, narration, description]
        return output