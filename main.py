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
        category = self.category
        location = str(category.currentText())

        # If dice is manually entered, check if its within range
        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        # Grab Terrain Encounter based on d20 roll
        match d20:
            case 1:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Boneyard",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 2:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Cliff and Ladder",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 3:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Crystal Clusters",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 4:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Fungus Cavern",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 5:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Gas Leak",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 6:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Gorge",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 7:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("High Ledge",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 8:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Horrid Sounds",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 9:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Lava Swell",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 10:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Muck Pit",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 11:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Rockfall",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 12:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Rope Bridge",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 13:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Ruins",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 14:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Shelter",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 15:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Sinkhole",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Webs", location)
            case 16:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Slime or Mold",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Web Break", location)
            case 17:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Steam Vent",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Web Break", location)
            case 18:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Underground Stream",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Web Break", location)
            case 19:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Warning Sign",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Web Break", location)
            case 20:
                if location == "Underdark":
                    terrain: dict = Encounter.encounter_generator("Webs",location)
                elif location == "The Silken Path":
                    terrain: dict = Encounter.encounter_generator("Web Break", location)

        # Update main list with new information
        try:
            self.e_title[1] = terrain[0]
            self.e_descn[2] = terrain[1]
            self.e_expln[2] = terrain[2]
        except UnboundLocalError:
            self.e_title[1] = ""
            self.e_descn[2] = ""
            filelocation = str(location).lower().replace(" ", "_")
            self.e_expln[3] = f"<b>Error.</b><br>Terrain doesn't exist in {filelocation} folder."

        # Update GUI
        self.gui_updater()

    def filler_encounter(self)-> None:
        """
        Generates Filler
        :param: filler uses the function of the same name in filler
        :return: None
        """
        category = self.category
        location = str(category.currentText())
        filler: dict = Encounter.encounter_generator("filler", location)

        # Filler
        self.e_descn[2] = filler[1]


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
        category = self.category
        location = str(category.currentText())

        # If dice is manually entered, check if its within range
        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        # Grab Creature Encounter based on d20 roll
        match d20:
            case 1:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Ambusher",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Cocooned Creature", location)
            case 2:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Ambusher and Lair",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Cocooned Creature", location)
            case 3:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Carrion Crawler",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Darkmantles", location)
            case 4:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Escaped Slaves",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Darkmantles", location)
            case 5:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Escaped Slaves",location)
            case 6:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Fungi",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Drow and Quaggoths", location)
            case 7:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Fungi",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Drow and Quaggoths", location)
            case 8:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Giant Fire Beetles",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Giant Spiders", location)
            case 9:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Giant Fire Beetles",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Giant Spiders", location)
            case 10:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Giant Rocktopus",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Giant Spiders", location)
            case 11:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Giant Rocktopus",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Giant Spiders", location)
            case 12:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Mad Creature",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Giant Spiders", location)
            case 13:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Ochre Jelly",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Giant Spiders", location)
            case 14:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Raiders",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Phase Spiders", location)
            case 15:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Raiders",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Phase Spiders", location)
            case 16:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Scouts",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Ettercaps", location)
            case 17:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Society of Brilliance",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Ettercaps", location)
            case 18:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Spore Servants",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Ettercaps", location)
            case 19:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Traders",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Mimic", location)
            case 20:
                if location == "Underdark":
                    creature: dict = Encounter.encounter_generator("Traders with Steeds",location)
                elif location == "The Silken Path":
                    creature: dict = Encounter.encounter_generator("Spectator", location)

        # Update main list with new information
        try:
            self.e_title[0] = creature[0]
            self.e_descn[3] = creature[1]
            self.e_expln[3] = creature[2]
        except UnboundLocalError:
            self.e_title[0] = ""
            self.e_descn[3] = ""
            filelocation = str(location).lower().replace(" ", "_")
            self.e_expln[3] = f"<b>Error.</b><br>Creature doesn't exist in {filelocation} folder."

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
            self.filler_encounter()

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
