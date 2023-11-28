from typing import List

import matplotlib.pyplot as plt
from openai import OpenAI
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

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


def clustering_embeddings(n_clusters, embeddings):
    # Esegui il clustering K-means
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(embeddings)
    labels = kmeans.labels_

    # Esegui la PCA per ridurre la dimensionalità a 2
    pca = PCA(n_components=2)
    reduced_embeddings = pca.fit_transform(embeddings)

    # Assegna le etichette "A" e "B" ai cluster
    label_map = {0: "Lavoratore", 1: "Datore di lavoro"}
    mapped_labels = [label_map[label] for label in labels]

    # Visualizza i cluster in uno spazio bidimensionale
    fig, ax = plt.subplots()
    for i, (coords, label) in enumerate(zip(reduced_embeddings, mapped_labels)):
        ax.scatter(coords[0], coords[1], label=label)
        ax.text(coords[0], coords[1], f"Testo {i + 1}")

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("Visualizzazione dei cluster")
    plt.show()

    # Unisci le coordinate ridotte e le etichette
    # result = list(zip(reduced_embeddings, mapped_labels))
    #
    # return result


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
    clustering_embeddings(n_clusters=2, embeddings=embeddings)
