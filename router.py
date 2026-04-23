from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

bots = {
    "Bot_A": "AI, crypto, Elon Musk, space, technology optimism",
    "Bot_B": "anti-tech, privacy, capitalism critique, environment",
    "Bot_C": "finance, trading, ROI, markets, money"
}

bot_embeddings = {k: model.encode(v) for k, v in bots.items()}

def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def route_post_to_bots(post_content, threshold=0.3):
    post_embedding = model.encode(post_content)
    matched = []

    for bot, emb in bot_embeddings.items():
        sim = cosine_similarity(post_embedding, emb)
        if sim > threshold:
            matched.append((bot, float(round(sim, 2))))  # clean float output

    return matched