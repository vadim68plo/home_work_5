import functions
from flask import Flask


app = Flask(__name__)

@app.route("/")
def page_index():
    candidates = functions.all_candidates()
    candidates_list = ""

    for candidat in candidates:
        candidates_list += f"Имя кандидата - {candidat['name']} \n"
        candidates_list += f"Позиция кандидата {candidat['position']} \n"
        candidates_list += f"Навыки через запятую {candidat['skills']} \n"
        candidates_list += f"\n"

    return "<pre>" + candidates_list + "</pre>"


@app.route("/candidates/<int:id>")
def page_candidat(id):
    candidates_list = ""
    candidat = functions.candidates_id(id)
    _candidat_img = candidat['picture']
    candidates_list += f"Имя кандидата - {candidat['name']} \n"
    candidates_list += f"Позиция кандидата {candidat['position']} \n"
    candidates_list += f"Навыки через запятую {candidat['skills']} \n"
    candidates_list += f"\n"

    return "<img src=" + _candidat_img + ">" + "<pre>" + candidates_list + "</pre>"


@app.route("/skills/<skill>")
def page_skills(skill):
    _candidates_list = ""
    _candidats = functions.candidates_skills(skill)
    for _candidat in _candidats:
        _candidates_list += f"Имя кандидата - {_candidat['name']} \n"
        _candidates_list += f"Позиция кандидата {_candidat['position']} \n"
        _candidates_list += f"Навыки через запятую {_candidat['skills']} \n"
        _candidates_list += f"\n"

    return "<pre>" + _candidates_list + "</pre>"


app.run(host='0.0.0.0', port=8000)

