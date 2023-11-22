import random
def dice_checker(dice_max: int, text: str) -> int:
    """
        Static method to ensure dice integrity.
        :param: dice_max: the maximum amount of dice used.
        :param: text: the textbox that can be manually entered.
        :return: the textbox as an integer or None for the randomizer.
    """
    try:
        if int(text) < 0 or int(text) > dice_max:
            raise ValueError
        elif not isinstance(text, int):
            if 1 <= int(text) <= dice_max:
                print('Successful Return')
                return int(text)
            else:
                raise KeyError

    except KeyError:
        print(f'Key Error: Must be an Integer from 1 to {dice_max}.')
    except ValueError:
        print(f'ValueError: Must be an Integer from 1 to {dice_max}.')


def roll(amount: int, sides: int) -> int:
    """
        Static method to roll a number of dice.
        :param: amount: the number of dice to roll.
        :param: sides: the number of sides on each die.
        :return: dice result
    """
    result = 0
    for x in range(0, amount):
        die_roll = random.randint(1, sides)
        result += die_roll
    return result


def read_roller(start: int, finish: int) -> int:
    """
        Static method to roll a number of dice.
        :param: amount: the number of dice to roll.
        :param: sides: the number of sides on each die.
        :return: dice result
    """
    result = random.randint(start - 1, finish - 1)
    return result