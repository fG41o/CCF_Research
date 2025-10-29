from typing import Optional
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

def make_preprocess(kind: str, feature_names: list) -> Optional[ColumnTransformer]:
    """
    kind:
      - 'none' — без препроцессинга
      - 'scale_amount_time' — стандартизировать столбцы 'Amount' и 'Time' (если есть)
    """
    if kind == "none":
        return None

    if kind == "scale_amount_time":
        cols = [c for c in ["Amount", "Time"] if c in feature_names]
        if not cols:
            return None
        return ColumnTransformer(
            transformers=[("scaler", StandardScaler(), cols)],
            remainder="passthrough",
            verbose_feature_names_out=False,
        )

    raise ValueError(f"Unknown preprocess kind: {kind}")