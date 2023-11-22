from gui import *
from PyQt6.QtWidgets import *
from encounter_builder import *
from dice import *


class Madlibs(QMainWindow, Ui_MainWindow):
    TITLE: list = ['', '']
    DESCRIPTION: list = ['', '', '', '']
    EXPLANATION: list = ['', '', '', '']

    def __init__(self):
        """
        Method to Initialize Encounter and GUI interface
        """
        super().__init__()
        self.setupUi(self)

        self.e_title: list = Madlibs.TITLE
        self.e_descn: list = Madlibs.DESCRIPTION
        self.e_expln: list = Madlibs.EXPLANATION

        # Generate Buttons
        self.gen_all.clicked.connect(lambda: self.generate_everything())
        self.gen_terrain.clicked.connect(lambda: self.terrain_encounter())
        self.gen_creature.clicked.connect(lambda: self.creature_encounter())
        self.gen_other.clicked.connect(lambda: self.generate_features())

        # Clear Buttons
        self.clear.clicked.connect(lambda: self.clear_everything())

    def generate_features(self)-> None:
        """
        Generates Space and Marching Order and Illumination
        :param: encounter_setup uses the function of the same name in encounter_builder
        :return: None
        """
        encounter_setup: dict = Encounter.encounter_setup()

        # Space and Marching Order
        self.e_descn[0] = f'{encounter_setup[0]}'
        self.e_expln[0] = f'{encounter_setup[1]}'

        # Illumination
        self.e_descn[1] = f'{encounter_setup[2]}'
        self.e_expln[1] = f'{encounter_setup[3]}'

        # Update GUI
        self.gui_updater()

    def terrain_encounter(self)-> None:
        """
        Generates Terrain encounter features
        :param: d20: a 20-sided die
        :param: text: the GUI text
        :return: None
        """
        # Get Dice Roll and/or check Textbox for manual input.
        d20: int = roll(1, 20)
        text = self.d20_terrain.text()

        # If dice is manually entered, check if its within range
        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        # Grab Terrain Encounter based on d20 roll
        match d20:
            case 1:
                terrain: dict = Encounter.encounter_generator("Boneyard")
            case 2:
                terrain: dict = Encounter.encounter_generator("Cliff and Ladder")
            case 3:
                terrain: dict = Encounter.encounter_generator("Crystal Clusters")
            case 4:
                terrain: dict = Encounter.encounter_generator("Fungus Cavern")
            case 5:
                terrain: dict = Encounter.encounter_generator("Gas Leak")
            case 6:
                terrain: dict = Encounter.encounter_generator("Gorge")
            case 7:
                terrain: dict = Encounter.encounter_generator("High Ledge")
            case 8:
                terrain: dict = Encounter.encounter_generator("Horrid Sounds")
            case 9:
                terrain: dict = Encounter.encounter_generator("Lava Swell")
            case 10:
                terrain: dict = Encounter.encounter_generator("Muck Pit")
            case 11:
                terrain: dict = Encounter.encounter_generator("Rockfall")
            case 12:
                terrain: dict = Encounter.encounter_generator("Rope Bridge")
            case 13:
                terrain: dict = Encounter.encounter_generator("Ruins")
            case 14:
                terrain: dict = Encounter.encounter_generator("Shelter")
            case 15:
                terrain: dict = Encounter.encounter_generator("Sinkhole")
            case 16:
                terrain: dict = Encounter.encounter_generator("Slime or Mold")
            case 17:
                terrain: dict = Encounter.encounter_generator("Steam Vent")
            case 18:
                terrain: dict = Encounter.encounter_generator("Underground Stream")
            case 19:
                terrain: dict = Encounter.encounter_generator("Warning Sign")
            case 20:
                terrain: dict = Encounter.encounter_generator("Webs")

        # Update main list with new information
        self.e_title[1] = terrain[0]
        self.e_descn[2] = terrain[1]
        self.e_expln[2] = terrain[2]

        # Update GUI
        self.gui_updater()

    def filler_encounter(self)-> None:
        """
        Generates Filler
        :param: filler uses the function of the same name in filler
        :return: None
        """
        filler: dict = Encounter.filler()

        # Filler
        self.e_descn[2] = filler[0]
        self.e_expln[2] = filler[1]

        # Update GUI
        self.gui_updater()


    def creature_encounter(self)-> None:
        """
        Generates Terrain encounter features
        :param: d20: a 20-sided die
        :param: text: the GUI text
        :return: None
        """

        # Get Dice Roll and/or check Textbox for manual input.
        d20: int = roll(1, 20)
        text = self.d20_creature.text()

        # If dice is manually entered, check if its within range
        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        # Grab Creature Encounter based on d20 roll
        match d20:
            case 1:
                creature: dict = Encounter.encounter_generator("Ambusher")
            case 2:
                creature: dict = Encounter.encounter_generator("Ambusher and Lair")
            case 3:
                creature: dict = Encounter.encounter_generator("Carrion Crawler")
            case 4:
                creature: dict = Encounter.encounter_generator("Escaped Slaves")
            case 5:
                creature: dict = Encounter.encounter_generator("Escaped Slaves")
            case 6:
                creature: dict = Encounter.encounter_generator("Fungi")
            case 7:
                creature: dict = Encounter.encounter_generator("Fungi")
            case 8:
                creature: dict = Encounter.encounter_generator("Giant Fire Beetles")
            case 9:
                creature: dict = Encounter.encounter_generator("Giant Fire Beetles")
            case 10:
                creature: dict = Encounter.encounter_generator("Giant Rocktopus")
            case 11:
                creature: dict = Encounter.encounter_generator("Giant Rocktopus")
            case 12:
                creature: dict = Encounter.encounter_generator("Mad Creature")
            case 13:
                creature: dict = Encounter.encounter_generator("Ochre Jelly")
            case 14:
                creature: dict = Encounter.encounter_generator("Raiders")
            case 15:
                creature: dict = Encounter.encounter_generator("Raiders")
            case 16:
                creature: dict = Encounter.encounter_generator("Scouts")
            case 17:
                creature: dict = Encounter.encounter_generator("Society of Brilliance")
            case 18:
                creature: dict = Encounter.encounter_generator("Spore Servants")
            case 19:
                creature: dict = Encounter.encounter_generator("Traders")
            case 20:
                creature: dict = Encounter.encounter_generator("Traders with Steeds")

        # Update main list with new information
        self.e_title[0] = creature[0]
        self.e_descn[3] = creature[1]
        self.e_expln[3] = creature[2]

        # Update GUI
        self.gui_updater()

    def generate_everything(self)-> None:
        """
        Generates Encounter features
        :param: d20: a 20-sided die
        :param: text: the GUI text
        :return: None
        """

        # Get Dice Roll and/or check Textbox for manual input.
        d20: int = roll(1, 20)
        text = self.d20_all.text()

        # If dice is manually entered, check if its within range
        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        # Generates Passage Size and Illumination without requiring a d20 roll
        self.generate_features()

        # Removes all features, then generates filler
        if d20 <= 13:
            self.e_title[1] = ''
            self.e_descn[2] = ''
            self.e_expln[2] = ''
            self.e_title[0] = ''
            self.e_descn[3] = ''
            self.e_expln[3] = ''
            self.filler_encounter()

        # Removes creatures, generates Terrain
        elif d20 == 14 or d20 == 15:
            self.e_title[0] = ''
            self.e_descn[3] = ''
            self.e_expln[3] = ''
            self.terrain_encounter()

        # Removes terrain, generates Creatures
        elif d20 == 16 or d20 == 17:
            self.e_title[1] = ''
            self.e_descn[2] = ''
            self.e_expln[2] = ''
            self.creature_encounter()

        # Generates Terrain and Creatures
        elif d20 >= 18:
            self.terrain_encounter()
            self.creature_encounter()

    def clear_everything(self)-> None:
        """
        Resets the List to its Default
        :return: None
        """
        self.e_title: list = Madlibs.TITLE
        self.e_descn: list = Madlibs.DESCRIPTION
        self.e_expln: list = Madlibs.EXPLANATION
        self.title.setText(f'')
        self.description.setText(f'')
        self.explanation.setText(f'')

    def gui_updater(self)-> None:
        """
        Updates the GUI with Encounter Information
        :return: None
        """

        # Check if there is a Creature Encounter on Terrain Encounter
        if self.e_title[0] != "" and self.e_title[1] != "":
            new_title = ' in the '.join(self.e_title)
            self.title.setText(f'<font size="10">{new_title}</font>')
        else:
            new_title = ''.join(self.e_title)
            self.title.setText(f'<font size="10">{new_title}</font>')

        # Update Description/Narration by merging list
        new_descn = ' '.join(self.e_descn)
        self.description.setText(f'{new_descn}')

        # Update Explanation by merging list, make sure new lines are added
        new_expln = '<br><br>'.join(self.e_expln)
        if new_expln.find("''<br><br>"):
            new_expln.replace("<br><br><br>","<br>")
        self.explanation.setText(f'{new_expln}')


def main():
    application = QApplication([])
    window = Madlibs()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
