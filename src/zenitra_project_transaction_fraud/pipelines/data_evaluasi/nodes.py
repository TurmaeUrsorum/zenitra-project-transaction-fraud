"""
This is a boilerplate pipeline 'data_evaluasi'
generated using Kedro 1.0.0
"""

from sklearn_extra.cluster import KMedoids
from sklearn.metrics import silhouette_score, davies_bouldin_score
import gower
import pandas as pd
import numpy as np
import logging

log = logging.getLogger(__name__)


def dunn_index(distance_matrix, labels):
    clusters = np.unique(labels)
    inter = []
    intra = []

    # inter-cluster: min distance antar cluster
    for i in clusters:
        for j in clusters:
            if i != j:
                inter.append(np.min(distance_matrix[np.ix_(labels == i, labels == j)]))

    # intra-cluster: max distance dalam satu cluster
    for c in clusters:
        sub = distance_matrix[np.ix_(labels == c, labels == c)]
        intra.append(np.max(sub))

    return np.min(inter) / np.max(intra)


def evaluasi_model(df: pd.DataFrame, kmedoids: KMedoids):
    gower_dist = gower.gower_matrix(df)

    labels = kmedoids.predict(gower_dist)
    df["cluster"] = labels

    # Silhouette Score -> pakai jarak precomputed
    sil_score = silhouette_score(gower_dist, labels, metric="precomputed")

    # Davies-Bouldin Index -> butuh numeric encoded
    df_numeric = pd.get_dummies(df, drop_first=True)
    dbi_score = davies_bouldin_score(df_numeric, labels)

    dunn_score = dunn_index(gower_dist, labels)

    log.info("=== Cluster Evaluation (k=3) ===")
    log.info(f"Silhouette Score: {round(sil_score, 4)}")
    log.info(f"Davies-Bouldin Index: {round(dbi_score, 4)}")
    log.info(f"Dunn Index: {round(dunn_score, 4)}")
