import json

CANDIDATES = "candidates.json"


def load_candidates(candidates: str) -> list:
    """
    Load from json file
    :param candidates: filename
    :return: list of dicts with candidate data
    """
    with open(candidates, encoding="utf-8") as file:
        return json.load(file)


def get_all() -> str:
    """
    Return candidates name, position, skills line by line
    :return: formatted string
    """
    candidate_list = []
    for candidate in load_candidates(CANDIDATES):
        candidate_output = "\n".join(
            [candidate["name"], candidate["position"], candidate["skills"]])
        candidate_list.append(candidate_output)
    return '\n\n'.join(candidate_list)


def get_by_pk(pk: int) -> str:
    """
    Return candidate`s name, position, skills by pk
    :param pk: pk in json
    :return: formatted string
    """
    for candidate in load_candidates(CANDIDATES):
        if candidate["pk"] == pk:
            url = f"<img src='{candidate['picture']}'>"
            return '\n'.join([url, candidate["name"], candidate["position"],
                              candidate["skills"]])


def get_by_skill(skill_name: str) -> str:
    """
    Return all candidate`s name, position, skills by skills
    :param skill_name: name of skill
    :return: formatted string
    """
    candidate_by_skills = []
    for candidate in load_candidates(CANDIDATES):
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidate_output = "\n".join(
                [candidate["name"], candidate["position"],
                 candidate["skills"]])
            candidate_by_skills.append(candidate_output)
    return "\n\n".join(candidate_by_skills)
