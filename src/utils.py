from src.model import encoder
from scipy import spatial


def get_similarity_score(sentence1 : str, sentence2 : str):
    """
    Get the similarity score between two sentences
    """
    sentence1_embedding = encoder.encode(sentence1)
    sentence2_embedding = encoder.encode(sentence2)
    result = 1 - spatial.distance.cosine(sentence1_embedding, sentence2_embedding)
    return result