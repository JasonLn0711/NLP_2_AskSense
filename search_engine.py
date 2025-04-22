# %%
from sentence_transformers import SentenceTransformer, util
import os

# %%
class SemanticSearchEngine:
    def __init__(self, corpus_path):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        base_dir = os.path.dirname(__file__)
        full_path = os.path.join(base_dir, corpus_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            self.corpus = [line.strip() for line in f.readlines()]
        self.embeddings = self.model.encode(self.corpus, convert_to_tensor=True)

    def search(self, query, top_k=3):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]
        top_results = scores.topk(top_k)
        return [(self.corpus[idx], float(scores[idx])) for idx in top_results.indices]