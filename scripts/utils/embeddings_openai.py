from typing import List

import matplotlib.pyplot as plt
import numpy as np
from openai import OpenAI
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

OPENAI_API_KEY = ""

client = OpenAI(api_key=OPENAI_API_KEY)


def process_embeddings(embeddings: List) -> List:
    embeddings_post = []
    for embed in embeddings:
        embeddings_post.append(embed.embedding)
    return embeddings_post


def get_embeddings_openai(texts_list: List[str]) -> List:
    embeddings = client.embeddings.create(
        input=texts_list,
        model="text-embedding-ada-002",
    ).data
    embeddings_post = process_embeddings(embeddings=embeddings)
    return embeddings_post


def visualize_embeddings_tsne(embeddings):
    tsne = TSNE(n_components=2, perplexity=7, random_state=0)
    embeddings_array = np.array(embeddings)
    embeddings_2d = tsne.fit_transform(embeddings_array)

    plt.figure(figsize=(6, 5))
    plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])
    plt.legend()
    plt.show()


def visualize_embeddings_tsne_with_labels(embeddings, labels):
    tsne = TSNE(n_components=2, perplexity=7, random_state=0)
    embeddings_array = np.array(embeddings)
    embeddings_2d = tsne.fit_transform(embeddings_array)

    plt.figure(figsize=(6, 5))
    for i, label in enumerate(set(labels)):
        indices = [j for j, x in enumerate(labels) if x == label]
        plt.scatter(embeddings_2d[indices, 0], embeddings_2d[indices, 1], label=label)
    plt.legend()
    plt.show()


def visualize_embeddings_pca(embeddings):
    # Crea un oggetto PCA con 2 componenti principali
    pca = PCA(n_components=2)

    # Esegui PCA sui tuoi dati
    embeddings_pca = pca.fit_transform(embeddings)

    # Crea un grafico scatter
    plt.figure(figsize=(6, 5))
    plt.scatter(embeddings_pca[:, 0], embeddings_pca[:, 1])
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.show()


def visualize_embeddings_pca_with_labels(embeddings, labels):
    # Crea un oggetto PCA con 2 componenti principali
    pca = PCA(n_components=2)

    # Esegui PCA sui tuoi dati
    embeddings_pca = pca.fit_transform(embeddings)

    # Crea un grafico scatter
    plt.figure(figsize=(6, 5))
    for i, label in enumerate(set(labels)):
        plt.scatter(embeddings_pca[labels == label, 0], embeddings_pca[labels == label, 1], label=label)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    texts = [
        "Ciao sono Antonio e mi piace giocare a tennis.",
        "Ciao sono Alessio e mi piace giocare a tennis.",
        "Ciao sono Alessio e mi piace giocare a calcio.",
        "Ciao sono Alessandro e mi piace giocare a calcio-tennis.",
        "Ciao luca come stai? so che sei andato allo stadio ieri.",
        "Ieri sera ha fatto molto freddo perciò mi sono coperto bene.",
        "Domani se sarà una bella giornata uscirò a prendermi un bel gelato.",
        "Sto andando a Napoli a mangiarmi una bella pizza margherita.",
        "A Milano ho saputo che sta piovendo ininterrottamente da 5 ore.",
        "New York è la città più bella al mondo, anche se è piuttosto cara.",
        "ChatGPT è uno strumento molto utile per gli sviluppatori di software.",
    ]
    embeddings = get_embeddings_openai(texts_list=texts)

    # visualize_embeddings_tsne(embeddings=embeddings)
    # visualize_embeddings_tsne_with_labels(embeddings=embeddings, labels=["Lavoratore", "Datore di lavoro"])
    visualize_embeddings_pca(embeddings=embeddings)
    # visualize_embeddings_pca_with_labels(embeddings=embeddings, labels=["Lavoratore", "Datore di lavoro"])
