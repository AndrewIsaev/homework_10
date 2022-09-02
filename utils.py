import json

CANDIDATES = "candidates.json"


def load_candidates(candidates):
    with open(candidates, encoding="utf-8") as file:
        return json.load(file)


def get_all():
    candidate_list = []
    for candidate in load_candidates(CANDIDATES):
        candidate_output = "\n".join(
            [candidate["name"], candidate["position"], candidate["skills"]])
        candidate_list.append(candidate_output)
    return '\n\n'.join(candidate_list)


def get_by_pk(pk):
    for candidate in load_candidates(CANDIDATES):
        if candidate["pk"] == pk:
            url = candidate["picture"]
            return '\n'.join([url, candidate["name"], candidate["position"],
                              candidate["skills"]])


def get_by_skill(skill_name: str):
    candidate_by_skills = []
    for candidate in load_candidates(CANDIDATES):
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidate_output = "\n".join(
                [candidate["name"], candidate["position"],
                 candidate["skills"]])
            candidate_by_skills.append(candidate_output)
    return "\n\n".join(candidate_by_skills)

