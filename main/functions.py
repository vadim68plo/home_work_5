from config import DATA
import json

def load_data(path=DATA):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def all_candidates():

    '''Загружает список кандидатов'''

    candidates = load_data()
    return candidates


def candidates_id(id):

    '''Загружает список кандидатов по номеру id'''

    candidates = load_data()

    for candidat in candidates:
        if id == candidat["id"]:
            return candidat



def candidates_skills(skill):

    '''Загружает список кандидатов по навыкам'''

    skill = skill.lower()
    candidates = load_data()
    candidates_list = []

    for candidat in candidates:
        candidat_skill = candidat["skills"]
        candidat_skill = candidat_skill.split(", ")

        for _candidat_skill in candidat_skill:
            _candidat_skill = _candidat_skill.lower()
            if skill == _candidat_skill:
                candidates_list.append(candidat)

    return candidates_list



























