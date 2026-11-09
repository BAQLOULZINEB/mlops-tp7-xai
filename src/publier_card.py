"""TP7 - src/publier_card.py

ROLE      : Attache MODEL_CARD.md au run des explications et a la version du modele (description + tag).
ENTREE    : MODEL_CARD.md + reports/run_xai.txt
SORTIE    : description et tag model_card sur fraude v1
A RETENIR : La documentation vit avec le modele, dans le registre.
"""

from pathlib import Path
import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri('http://127.0.0.1:5000')
c = MlflowClient()
v = c.get_model_version_by_alias('fraude', 'production')
run_id = Path('reports/run_xai.txt').read_text().strip()   # le run de l'activite 6
with mlflow.start_run(run_id=run_id):                      # on rouvre ce run
    mlflow.log_artifact('MODEL_CARD.md')
card = Path('MODEL_CARD.md').read_text(encoding='utf-8')
c.update_model_version('fraude', v.version, description=card)  # visible dans le registre
c.set_model_version_tag('fraude', v.version, 'model_card', 'MODEL_CARD.md, run ' + run_id[:8])
print('Model Card attachee a fraude v' + v.version, 'et au run', run_id[:8])
