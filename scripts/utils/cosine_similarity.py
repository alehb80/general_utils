from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == '__main__':
    # Definisci le due stringhe
    string1 = "Via Mario Rossi 13"
    string2 = "V. M. Rossi 13"

    # Crea un oggetto TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Addestra il vettore TF-IDF sulle due stringhe
    tfidf_matrix = tfidf_vectorizer.fit_transform([string1, string2])

    # Calcola la similarità coseno tra i vettori TF-IDF
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    print("Similarità coseno tra le due stringhe:", cosine_sim[0][0])
