import os

from fastapi.testclient import TestClient

from app import create_app


client = TestClient(create_app())


def test_registro_exitoso_reserva() -> None:
    response = client.post(
        "/api/v1/inventario/movimientos",
        json={"recurso": "PAR-01", "tipo_operacion": "RESERVA", "cantidad": 2, "usuario": "encargado-bodega"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["historia"] == "HU-002"


def test_tipo_operacion_invalido() -> None:
    response = client.post(
        "/api/v1/inventario/movimientos",
        json={"recurso": "PAR-01", "tipo_operacion": "BORRAR", "cantidad": 1, "usuario": "encargado-bodega"},
    )
    assert response.status_code == 400


def test_recurso_sin_datos() -> None:
    response = client.post(
        "/api/v1/inventario/movimientos",
        json={"recurso": "PAR-99", "tipo_operacion": "AJUSTE", "cantidad": 1, "usuario": "encargado-bodega"},
    )
    assert response.status_code == 404


def test_formato_invalido() -> None:
    response = client.post(
        "/api/v1/inventario/movimientos",
        json={"recurso": "PAR-01", "tipo_operacion": "RESERVA", "cantidad": 0},
    )
    assert response.status_code == 422


def test_dependencia_no_disponible() -> None:
    os.environ["SIMULAR_FALLA_SERVIDOR"] = "true"
    try:
        response = client.post(
            "/api/v1/inventario/movimientos",
            json={"recurso": "PAR-01", "tipo_operacion": "RESERVA", "cantidad": 1, "usuario": "encargado-bodega"},
        )
    finally:
        os.environ.pop("SIMULAR_FALLA_SERVIDOR", None)
    assert response.status_code == 503
