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

        encounter_setup: dict = Encounter.encounter_setup()

        # Space and Marching Order
        self.e_descn[0] = f'{encounter_setup[0]}'
        self.e_expln[0] = f'{encounter_setup[1]}'

        # Illumination
        self.e_descn[1] = f'{encounter_setup[2]}'
        self.e_expln[1] = f'{encounter_setup[3]}'

        self.gui_updater()

    def terrain_encounter(self)-> None:

        # Get Dice Roll and/or check Textbox for manual input.
        d20: int = roll(1, 20)
        text = self.d20_terrain.text()

        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        match d20:
            case 1:
                terrain: dict = Encounter.terrain("Boneyard")
            case 2:
                terrain: dict = Encounter.terrain("Cliff and Ladder")
            case 3:
                terrain: dict = Encounter.terrain("Crystal Clusters")
            case 4:
                terrain: dict = Encounter.terrain("Fungus Cavern")
            case 5:
                terrain: dict = Encounter.terrain("Gas Leak")
            case 6:
                terrain: dict = Encounter.terrain("Gorge")
            case 7:
                terrain: dict = Encounter.terrain("High Ledge")
            case 8:
                terrain: dict = Encounter.terrain("Horrid Sounds")
            case 9:
                terrain: dict = Encounter.terrain("Lava Swell")
            case 10:
                terrain: dict = Encounter.terrain("Muck Pit")
            case 11:
                terrain: dict = Encounter.terrain("Rockfall")
            case 12:
                terrain: dict = Encounter.terrain("Rope Bridge")
            case 13:
                terrain: dict = Encounter.terrain("Ruins")
            case 14:
                terrain: dict = Encounter.terrain("Shelter")
            case 15:
                terrain: dict = Encounter.terrain("Sinkhole")
            case 16:
                terrain: dict = Encounter.terrain("Slime or Mold")
            case 17:
                terrain: dict = Encounter.terrain("Steam Vent")
            case 18:
                terrain: dict = Encounter.terrain("Underground Stream")
            case 19:
                terrain: dict = Encounter.terrain("Warning Sign")
            case 20:
                terrain: dict = Encounter.terrain("Webs")

        self.e_title[1] = terrain[0]
        self.e_descn[2] = terrain[1]
        self.e_expln[2] = terrain[2]

        self.gui_updater()

    def creature_encounter(self)-> None:

        # Get Dice Roll and/or check Textbox for manual input.
        d20: int = roll(1, 20)
        text = self.d20_creature.text()

        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        match d20:
            case 1:
                creature: dict = Encounter.creature("Ambusher")
            case 2:
                creature: dict = Encounter.creature("Ambusher and Lair")
            case 3:
                creature: dict = Encounter.creature("Carrion Crawler")
            case 4:
                creature: dict = Encounter.creature("Escaped Slaves")
            case 5:
                creature: dict = Encounter.creature("Escaped Slaves")
            case 6:
                creature: dict = Encounter.creature("Fungi")
            case 7:
                creature: dict = Encounter.creature("Fungi")
            case 8:
                creature: dict = Encounter.creature("Giant Fire Beetles")
            case 9:
                creature: dict = Encounter.creature("Giant Fire Beetles")
            case 10:
                creature: dict = Encounter.creature("Giant Rocktopus")
            case 11:
                creature: dict = Encounter.creature("Giant Rocktopus")
            case 12:
                creature: dict = Encounter.creature("Mad Creature")
            case 13:
                creature: dict = Encounter.creature("Ochre Jelly")
            case 14:
                creature: dict = Encounter.creature("Raiders")
            case 15:
                creature: dict = Encounter.creature("Raiders")
            case 16:
                creature: dict = Encounter.creature("Scouts")
            case 17:
                creature: dict = Encounter.creature("Society of Brilliance")
            case 18:
                creature: dict = Encounter.creature("Spore Servants")
            case 19:
                creature: dict = Encounter.creature("Traders")
            case 20:
                creature: dict = Encounter.creature("Traders with Steeds")

        self.e_title[0] = creature[0]
        self.e_descn[3] = creature[1]
        self.e_expln[3] = creature[2]

        self.gui_updater()

    def generate_everything(self):
        # Get Dice Roll and/or check Textbox for manual input.
        d20: int = roll(1, 20)
        text = self.d20_terrain.text()

        if not text == '':
            validator: int = dice_checker(20, text)
            if validator is not None:
                d20: int = validator
                print(d20)

        self.generate_features()

        if d20 <= 13:
            pass

        elif d20 == 14 or d20 == 15:
            self.terrain_encounter()

        elif d20 == 16 or d20 == 17:
            self.creature_encounter()

        elif d20 >= 18:
            self.terrain_encounter()
            self.creature_encounter()

    def clear_everything(self)-> None:
        self.e_title: list = Madlibs.TITLE
        self.e_descn: list = Madlibs.DESCRIPTION
        self.e_expln: list = Madlibs.EXPLANATION
        self.title.setText(f'')
        self.description.setText(f'')
        self.explanation.setText(f'')

    def gui_updater(self)-> None:
        if self.e_title[0] != "" and self.e_title[1] != "":
            new_title = ' in the '.join(self.e_title)
            self.title.setText(f'<font size="10">{new_title}</font>')
        else:
            new_title = ''.join(self.e_title)
            self.title.setText(f'<font size="10">{new_title}</font>')

        new_descn = ' '.join(self.e_descn)
        self.description.setText(f'{new_descn}')

        new_expln = '<br><br>'.join(self.e_expln)
        self.explanation.setText(f'{new_expln}')


def main():
    application = QApplication([])
    window = Madlibs()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
