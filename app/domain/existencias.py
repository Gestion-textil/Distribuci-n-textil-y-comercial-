from pydantic import BaseModel, Field


PAR_CATALOGOS_VALIDOS = ("PAR-01", "PAR-02", "PAR-03")


class ExistenciasIn(BaseModel):
    referencia: str | None = Field(default=None, min_length=1)
    incluir_invalidas: bool = False


class ExistenciasOut(BaseModel):
    success: bool
    mensaje: str
    data: dict


class Existencia:
    def __init__(
        self,
        referencia: str,
        rollos: int,
        metros: float,
        estado: str,
    ) -> None:
        self.referencia = referencia
        self.rollos = rollos
        self.metros = metros
        self.estado = estado

    def es_valida(self) -> bool:
        return self.referencia in PAR_CATALOGOS_VALIDOS and self.rollos >= 0 and self.metros >= 0

    def to_response(self) -> dict:
        if not self.es_valida():
            raise ValueError("Existencia invalida")

        return {
            "referencia": self.referencia,
            "rollos": self.rollos,
            "metros": self.metros,
            "estado": self.estado,
        }
