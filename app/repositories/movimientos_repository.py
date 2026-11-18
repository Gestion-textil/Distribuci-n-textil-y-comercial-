import os
from copy import deepcopy
from uuid import uuid4

from fastapi import HTTPException


class MovimientosRepository:
    _inventario = {
        "PAR-01": {"disponible": 12, "reservado": 0},
        "PAR-02": {"disponible": 4, "reservado": 0},
        "PAR-03": {"disponible": 0, "reservado": 0},
    }
    _bitacora: list[dict] = []

    def registrar(self, recurso: str, tipo_operacion: str, cantidad: int, usuario: str) -> dict:
        if os.getenv("SIMULAR_FALLA_SERVIDOR", "").strip().lower() in {"1", "true", "si", "sí"}:
            raise HTTPException(status_code=503, detail="Servicio temporalmente no disponible")

        if recurso not in self._inventario:
            raise HTTPException(status_code=404, detail="Recurso sin datos")

        inventario = deepcopy(self._inventario)
        estado = inventario[recurso]

        if tipo_operacion == "RESERVA":
            if cantidad > estado["disponible"]:
                raise HTTPException(status_code=400, detail="No hay disponibilidad suficiente")
            estado["disponible"] -= cantidad
            estado["reservado"] += cantidad
        elif tipo_operacion == "LIBERACION":
            if cantidad > estado["reservado"]:
                raise HTTPException(status_code=400, detail="No hay reservas suficientes")
            estado["reservado"] -= cantidad
            estado["disponible"] += cantidad
        elif tipo_operacion == "DEVOLUCION":
            estado["disponible"] += cantidad
        elif tipo_operacion == "AJUSTE":
            estado["disponible"] = cantidad

        movimiento_id = str(uuid4())
        registro = {
            "movimiento_id": movimiento_id,
            "recurso": recurso,
            "tipo_operacion": tipo_operacion,
            "cantidad": cantidad,
            "usuario": usuario,
        }
        self._inventario = inventario
        self._bitacora.append(registro.copy())
        return registro
