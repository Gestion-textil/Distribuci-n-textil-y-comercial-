from fastapi import APIRouter, HTTPException

from app.domain.movimientos import MovimientoIn, MovimientoOut
from app.services.movimientos_service import MovimientosService


router = APIRouter(prefix="/api/v1/inventario", tags=["HU-002"])
service = MovimientosService()


@router.post("/movimientos", response_model=MovimientoOut)
def registrar_movimiento(payload: MovimientoIn) -> dict:
    try:
        data = service.procesar(
            payload.recurso,
            payload.tipo_operacion.upper(),
            payload.cantidad,
            payload.usuario,
        )
    except HTTPException:
        raise
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail={
                "codigo": "VALIDACION_NEGOCIO",
                "mensaje": "No fue posible completar la operación",
                "detalle": {"campo": str(error)},
            },
        ) from error

    return {
        "success": True,
        "mensaje": "Operación procesada con éxito",
        "data": {
            "historia": "HU-002",
            "estado": "PROCESADA",
            "funciones_cubiertas": [f"FUN-{numero:03d}" for numero in range(8, 15)],
            "movimiento": data,
        },
    }
