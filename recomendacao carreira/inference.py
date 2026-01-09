from knowledge_base import RULES

def forward_chaining(facts):
    scores = {}

    for rule in RULES:
        score = 0
        career = rule["career"]

        for interest, weight in rule["interests"].items():
            if facts.has_fact(interest):
                score += weight

        matched_skills = 0
        for skill, weight in rule["skills"].items():
            if facts.has_fact(skill):
                score += weight
                matched_skills += 1

        if matched_skills > 0:
            score += 1

        score += rule["popularity"]

        if score > 0:
            scores[career] = score

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
