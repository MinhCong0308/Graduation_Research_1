#   Graduation Research 1  
## A Conversational Laptop‑Shopping Assistant  
**Nguyen Cong Minh · 20226056 · HUST**


## ✨  Overview
This project delivers an end‑to‑end dialogue system that helps Vietnamese & English customers find the right **laptop** through natural‑language conversation.

| Stage | Module | Core Model / Technique |
|-------|--------|------------------------|
| 1 | Named‑Entity Recognition | **VElectra‑base** fine‑tuned on 45 tags |
| 2 | Intent Classification | **mT5‑small encoder** (EN pre‑train → VI fine‑tune) + TF‑IDF fusion |
| 3 | Dialogue State Tracking | JSON state + pointer to product array |
| 4 | Text‑to‑SQL | Rule templates → safe PostgreSQL |
| 5 | Ranking | Spec normalisation & weighted scoring |
| 6 | Response | Streamlit / CLI demo |


##   Repository Layout
```
Graduation_Research_1/
├─ crawler/                  # SKU scraper
├─ dataset/                  # ner/, intent/, postgres_dump.sql
├─ fine_tune_velectra/       # NER training scripts & ckpt
├─ two_phrase_train_for_laptop_intent/
│  ├─ fine_tune_laptop_intent.ipynb/             # English pre‑train
│  └─ mt5_encoder_based_for_intent.ipynb/             # Vietnamese fine‑tune
├─ tfidf_vectorizer.pkl # pkl file for tfidf vectorizer parameters
├─ dialogue_state_traking.ipynb # notebook for running a demo
##   Datasets

| Task | Lang | Size | Source |
|------|------|------|--------|
| NER | vi | 120 sents / 45 tags | Hand‑annotated + ChatGPT |
| Intent (pre‑train) | en | 22 500 | Kaggle general‑intent |
| Intent (laptop) | vi + en | 961 | Synthetic dialogues |
| Product DB | — | ≈400 SKUs | crawled from thegioididong.com |

```
## 🏋️‍♀️  Training Results

| Model | P | R | F1 / Acc |
|-------|---|---|----------|
| VElectra NER | 0.991 | 0.990 | **0.990** |
| Intent EN | 0.916 | 0.911 | 0.910 |
| Intent EN + VI (+ TF‑IDF) | **0.927** | **0.922** | **0.922** |

---

