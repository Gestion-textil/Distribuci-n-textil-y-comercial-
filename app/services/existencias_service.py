from app.domain.existencias import Existencia
from app.repositories.existencias_repository import ExistenciasRepository


class ExistenciasService:
    def __init__(self) -> None:
        self.repository = ExistenciasRepository()

    def consultar(self, referencia: str | None = None) -> dict:
        registros = self.repository.consultar(referencia)
        existencias = [
            Existencia(
                referencia=item["referencia"],
                rollos=item["rollos"],
                metros=item["metros"],
                estado=item["estado"],
            ).to_response()
            for item in registros
        ]

        return {
            "historia": "HU-001",
            "estado": "PROCESADA",
            "funciones_cubiertas": [f"FUN-{numero:03d}" for numero in range(1, 8)],
            "existencias": existencias,
        }
