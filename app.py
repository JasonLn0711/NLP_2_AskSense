# %%
from search_engine import SemanticSearchEngine

searcher = SemanticSearchEngine('./data/faq_dataset_10000.txt')

while True:
    query = input("\n🔍 Enter your question (or 'eixt'):")
    if query.lower() == 'exit':
        break
    results = searcher.search(query)
    print(f"\n🔍 Question: {query}")
    print('📌 Top Matches:')
    for i, (text, score) in enumerate(results, 1):
        print(f"{i}. {text} (score: {score: .4f})")
    print("")

# %%



