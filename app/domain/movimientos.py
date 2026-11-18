from pydantic import BaseModel, Field


TIPOS_MOVIMIENTO_VALIDOS = ("AJUSTE", "RESERVA", "LIBERACION", "DEVOLUCION")


class MovimientoIn(BaseModel):
    recurso: str = Field(min_length=1)
    tipo_operacion: str = Field(min_length=1)
    cantidad: int = Field(gt=0)
    usuario: str = Field(min_length=1)


class MovimientoOut(BaseModel):
    success: bool
    mensaje: str
    data: dict


class Movimiento:
    def __init__(self, recurso: str, tipo_operacion: str, cantidad: int, usuario: str) -> None:
        self.recurso = recurso
        self.tipo_operacion = tipo_operacion
        self.cantidad = cantidad
        self.usuario = usuario

    def validar(self) -> None:
        if self.tipo_operacion not in TIPOS_MOVIMIENTO_VALIDOS:
            raise ValueError("tipo_operacion no permitido")

    def to_response(self, movimiento_id: str) -> dict:
        self.validar()
        return {
            "movimiento_id": movimiento_id,
            "recurso": self.recurso,
            "tipo_operacion": self.tipo_operacion,
            "cantidad": self.cantidad,
            "usuario": self.usuario,
        }
