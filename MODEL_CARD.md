# Model Card - fraude (version servie par l'alias production)

## Modele
Nom et version dans le registre MLflow : `fraude`, version 1 (alias `production`).
Famille et reglages : RandomForestClassifier, 500 arbres, profondeur max 16, random_state 42 (scikit-learn 1.7.2, format skops).
Run d'origine (MLflow) : 53a72956 (experience tp2-registre).

## Objectif et usage prevu
Attribuer un score de risque de fraude (probabilite) a une transaction par carte, a partir de montant, anciennete du client, nombre de transactions en 24 h et paiement de nuit.
Usage : mettre une transaction en attente et declencher une verification (appel, SMS) par un conseiller.

## Usages exclus
Bloquer definitivement un compte ou refuser un client sans revue humaine.
Noter la solvabilite ou le profil d'un client ; usage sur d'autres pays ou canaux (virements, e-commerce) que ceux des donnees.

## Donnees
Fichier `data/transactions.csv` : 5 000 lignes, 568 fraudes (11,4 %), empreinte md5 `cf9f6f86c141e7df32c61715c493483f` (identique au ticket DVC v1 du TP3).
Origine : donnees **synthetiques** generees par `donnees.py` (graine 7) ; decoupage 75/25, random_state 42.

## Performances (jeu de test, 1 250 transactions)
F1 : 0.8669   precision : 0.8837   rappel : 0.8507   AUC : 0.9872
Matrice : 1 101 vrais normaux, 15 fausses alertes, 20 fraudes ratees, 114 fraudes detectees (sur 134).

## Methodes d'explicabilite
Globale : importance par permutation (F1, 10 repetitions) et SHAP TreeExplainer (400 transactions) ; MDI de la foret a titre indicatif.
Locale : SHAP waterfall (exact, base 0.1157 + contributions = prediction) ; LIME (2 000 voisins, graine 0) en controle.
Variables les plus influentes : montant (permutation 0.593, SHAP 0.116), puis anciennete, freq_24h et nuit (proches, 0.20 a 0.27). Montant eleve, faible anciennete, nuit et nombreuses transactions poussent vers la fraude.

## Comparaison avec un modele interpretable
Regression logistique avec log10(montant) : F1 0.8593, 113 fraudes detectees sur 134 (1 de moins que la foret), coefficients lisibles (cote x0.928 par mois d'anciennete, x4.76 par transaction en 24 h).
Arbre de profondeur 3 : F1 0.5737 seulement ; la lisibilite d'un arbre court coute trop cher ici.

## Limites et risques connus
Donnees synthetiques : performances a revalider sur donnees reelles ; 134 fraudes de test, un ecart de 0.01 de F1 (environ 1 fraude) n'est pas significatif.
SHAP mesure la contribution au score du modele, pas une cause reelle ; LIME est instable sur les petites contributions (anciennete, freq_24h changent de signe selon la graine).
Variable `nuit` : effet fort et interaction avec le montant ; surveiller un biais envers les clients qui paient la nuit (travail de nuit).

## Recommandations d'utilisation et de surveillance
Toujours une revue humaine avant blocage ; expliquer au client avec SHAP (pas LIME seul).
Surveiller chaque mois : F1/rappel sur fraudes confirmees, distribution du montant et part de paiements de nuit (derive, cf. donnees v2 du TP3) ; reentrainer via le workflow `reentrainement-fraude` (TP6) avec la regle F1 >= 0.82.

## Tracabilite
Run des explications (experience tp7-explicabilite) : b0b69a93 (tag `explications_run` sur fraude v1).
Auteurs : Zineb (nom complet a completer)   Date : 9 novembre 2026   Prochaine revue : 9 fevrier 2027 (trimestrielle) ou a chaque changement d'alias.
