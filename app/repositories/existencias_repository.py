import os

from fastapi import HTTPException


class ExistenciasRepository:
    _seed = [
        {"referencia": "PAR-01", "rollos": 12, "metros": 480.5, "estado": "DISPONIBLE"},
        {"referencia": "PAR-02", "rollos": 4, "metros": 160.0, "estado": "DISPONIBLE"},
        {"referencia": "PAR-03", "rollos": 0, "metros": 0.0, "estado": "AGOTADO"},
    ]

    def consultar(self, referencia: str | None = None) -> list[dict]:
        if os.getenv("SIMULAR_FALLA_SERVIDOR", "").strip().lower() in {"1", "true", "si", "sí"}:
            raise HTTPException(
                status_code=503,
                detail="Servicio temporalmente no disponible",
            )

        if referencia:
            return [
                item.copy()
                for item in self._seed
                if item["referencia"] == referencia
            ]

        return [item.copy() for item in self._seed]
