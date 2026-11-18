from app.domain.movimientos import Movimiento
from app.repositories.movimientos_repository import MovimientosRepository


class MovimientosService:
    def __init__(self) -> None:
        self.repository = MovimientosRepository()

    def procesar(self, recurso: str, tipo_operacion: str, cantidad: int, usuario: str) -> dict:
        movimiento = Movimiento(recurso, tipo_operacion, cantidad, usuario)
        movimiento.validar()
        registro = self.repository.registrar(recurso, tipo_operacion, cantidad, usuario)
        return movimiento.to_response(registro["movimiento_id"])
