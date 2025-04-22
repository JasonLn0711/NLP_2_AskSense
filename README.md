# 🔍 AskSense: Semantic FAQ Matching Engine

Welcome to **AskSense** — a lightweight yet powerful semantic search tool designed to help users find the most relevant FAQ entries using state-of-the-art sentence embeddings and cosine similarity.

Unlike traditional keyword-based search, AskSense understands the **meaning** behind user queries and finds the most semantically similar responses, even if the wording is completely different.

---

## 🧠 What It Does

- ✅ Takes in a **user query**
- ✅ Compares it against a pre-built FAQ dataset
- ✅ Uses **Sentence-BERT** to generate embeddings
- ✅ Ranks and returns the most **semantically similar entries**

---

## 🚀 How It Works

1. Loads a custom FAQ dataset from `data/faq_corpus.txt` and `data/faq_dataset_10000.txt`
2. Encodes each FAQ entry into a vector using `paraphrase-multilingual-MiniLM-L12-v2` (rather than using `all-MiniLM-L6-v2` for only English text.)
3. Accepts a user input and encodes it as well
4. Calculates cosine similarity between the query and every FAQ entry
5. Displays the top matches in descending order of similarity

---

## 📁 Project Structure

```
AskSense/
├── data/
│   ├── faq_corpus.txt           # Clean FAQ dataset (1 question per line)
│   └── faq_dataset_10000.txt    # Clean FAQ dataset (1 question per line)
├── search_engine.py             # Core logic: loading model and matching
├── app.py                       # CLI interface (or GUI integration ready)
├── requirements.txt
└── README.md
```

---

## 🔧 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/JasonLn0711/NLP_2_AskSense.git
cd NLP_2_AskSense
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

---

## 📘 Sample Interaction
```
🔍 Enter your question: How do I change my password?

📌 Top Matches:
1. What should I do if I forget my login information? (score: 0.91)
2. How can I reset my password? (score: 0.89)
```

---

## 🔍 Powered By
- [sentence-transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
- `cosine similarity` from `pytorch_cos_sim`
- Clean, structured FAQ corpus you control

---

## 🧠 Use Case Ideas
- Customer support bots
- E-commerce FAQ search
- Internal knowledge base querying
- Legal or healthcare document lookup

---

## 📜 License
MIT License

Built with ❤️ as part of Jason Lin’s NLP learning journey.
