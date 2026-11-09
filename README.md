# TP07 - Explicabilite et auditabilite (XAI)

Fiche explicative : `EXPLICATION_TP7.html` | Rapport : `rapport_tp7.md` | Model Card : `MODEL_CARD.md`

```powershell
# terminal 1 : serveur MLflow du TP2
cd ..	p2-mlflow ; .venv\Scripts\Activate.ps1
mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlartifacts
# terminal 2 : ici
.venv\Scripts\Activate.ps1
python src/verifier_modele.py
python src/xai_importance.py ; python src/xai_global.py ; python src/xai_local.py
python src/xai_lime.py ; python src/interpretables.py
python src/journaliser.py ; python src/publier_card.py
```
