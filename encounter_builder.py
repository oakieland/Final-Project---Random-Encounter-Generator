from gui import *
from PyQt6.QtWidgets import *
from dice import *
import re

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
    def file_select(name,location)-> list:
        """
        Method to builder encounter, find its text file.
        Prefixes:
            file = the .txt file that is read.
            nara = the narration that would be read aloud.
            rule = the rules related to the above narration.
        :return: output, 3 strings in a list are outputted: The name, narration and rules.
        """
        # Convert name to file
        filename = str(name).lower().replace(" ", "_")
        filelocation = str(location).lower().replace(" ", "_")

        # Makes sure the file doesn't crash if the txt. file goes missing.
        try:
            file_encounter = open(f'encounters/{filelocation}/{filename}.txt', errors="ignore").readlines()
        except FileNotFoundError:
            return [name, f"", f"<b>Error.</b><br> Please add {filename}.txt to {filelocation} folder."]

        # The file mirrors itself, half would be the narration and the other half the rules.
        size = (len(file_encounter) // 2)

        # Make sure the file doesn't crash if the text file doesn't have content
        try:
            choice = read_roller(1, size)
        except ValueError:
            return [name, f"", f"<b>Error.</b><br> {filename}.txt is empty."]
        except IndexError:
            return [name, f"", f"<b>Error.</b><br> {filename}.txt doesn't have enough information."]

        # Take the rules and narration from the file.
        narration = (file_encounter[choice]).strip()
        description = file_encounter[choice + size]

        output = [name, narration, description]
        return output

    @staticmethod
    def encounter_setup() -> list:
        """
        Method to choose "Space and Marching Order" and "Illumination"
        Prefixes:
        :return: output, 2 lines from space_and_marching_order.txt and illumination.txt
        """
        # Space and Marching Order
        space_and_marching_order = Encounter.file_select("Space and Marching Order","")

        # Illumination
        illumination = Encounter.file_select("Illumination","")

        output = [space_and_marching_order[1], space_and_marching_order[2], illumination[1], illumination[2]]
        return output

    @staticmethod
    def encounter_generator(name,location) -> list:
        """
        Method to choose "Terrain", "Filler" or "Creature"
        :return: output, 3 strings in a list are outputted: The name, narration and rules.
        """
        encounter: list = Encounter.file_select(name, location)

        f_Title:str = encounter[0]

        f_Narration:str = encounter[1]
        strip_Narration = f_Narration.strip()
        roll_Narration = eval(f'f"{strip_Narration}"')

        f_Description:str = encounter[2]
        strip_Description = f_Description.strip()
        roll_Description = eval(f'f"{strip_Description}"')

        output = [f_Title,roll_Narration,roll_Description]

        return output
