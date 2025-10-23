from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_match_score(resume_text, job_description):
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_description, convert_to_tensor=True)
    similarity = util.cos_sim(emb1, emb2).item()
    return similarity * 100  # convert to percentage


def generate_suggestions(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    missing_keywords = [w for w in job_words if w not in resume_words and len(w) > 4]
    suggestions = [f"Consider adding '{kw}' to your resume." for kw in missing_keywords[:10]]

    return suggestions
