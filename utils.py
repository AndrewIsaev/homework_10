import json

CANDIDATES = "candidates.json"


def load_candidates(candidates):
    with open(candidates, encoding="utf-8") as file:
        return json.load(file)

def get_all():
    pass

def get_by_pk(pk):
    pass

def get_by_skill(skill_name):
    pass

