import json

from datasets import load_dataset

from genetic import nlp

ds = load_dataset("softcatala/ca_text_corpus")


datasets = [elem['text'] for elem in list(ds['train'])]
corpus = ' '.join(datasets)
corpus = nlp.calcular_bigrames_lletres(corpus)

# Desar el diccionari en un fitxer
with open("bigrama.json", "w", encoding="utf-8") as file:
    json.dump(corpus, file, indent=4, ensure_ascii=False)


