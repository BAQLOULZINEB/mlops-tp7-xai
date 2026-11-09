"""TP7 - src/xai_commun.py

ROLE      : Module partage : charge le modele PAR SON ALIAS fraude@production, refait le decoupage du TP2 et definit le cas de Mme Benali.
ENTREE    : registre MLflow du TP2 + data/transactions.csv
SORTIE    : m, X, Xtr, Xte, ytr, yte, VERSION, CAS (importes par tous les scripts)
A RETENIR : Expliquer le modele SERVI, sur le MEME jeu de test que celui ou il a ete evalue.
"""

import mlflow
import mlflow.sklearn
import pandas as pd
from mlflow import MlflowClient
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri('http://127.0.0.1:5000')
NOM, ALIAS = 'fraude', 'production'
VERSION = MlflowClient().get_model_version_by_alias(NOM, ALIAS)   # numero et run d'origine
m = mlflow.sklearn.load_model(f'models:/{NOM}@{ALIAS}')          # la foret du TP2

df = pd.read_csv('data/transactions.csv')
X, y = df.drop(columns='fraude'), df['fraude']
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,      # decoupage du TP2
                                      random_state=42)
CAS = pd.DataFrame([{'montant': 1800.0, 'anciennete': 30,         # Mme Benali
                     'freq_24h': 4, 'nuit': 1}])
