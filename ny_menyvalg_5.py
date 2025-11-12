#lag en tom studieplan

from ny_emner import Studieplan, studieplan_dict

def tom_stuideplan():
    ID = input('ID: ')
    tittel = input('Tittel: ')
    studieplan = Studieplan(ID, tittel)
    studieplan_dict[ID] = studieplan
    