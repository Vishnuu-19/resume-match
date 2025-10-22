def calculate_score(resume_content):
    score = 0
    total_criteria = 5  # Example criteria count

    if 'keywords' in resume_content:
        score += 20
    if 'experience' in resume_content:
        score += 20
    if 'education' in resume_content:
        score += 20
    if 'skills' in resume_content:
        score += 20
    if 'format' in resume_content:
        score += 20

    return (score / total_criteria) * 100  # Return score as a percentage