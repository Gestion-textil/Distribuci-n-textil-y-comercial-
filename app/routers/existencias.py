from fastapi import APIRouter, HTTPException, Query

from app.domain.existencias import ExistenciasOut
from app.services.existencias_service import ExistenciasService


router = APIRouter(prefix="/api/v1/inventario", tags=["HU-001"])
service = ExistenciasService()


@router.get("/existencias", response_model=ExistenciasOut)
def consultar_existencias(
    referencia: str | None = Query(default=None, min_length=1),
) -> dict:
    try:
        data = service.consultar(referencia)
    except HTTPException:
        raise
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error

    return {
        "success": True,
        "mensaje": "Consulta procesada con éxito",
        "data": data,
    }
