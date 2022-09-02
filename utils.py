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
    pass


def get_by_skill(skill_name):
    pass

print(get_all())