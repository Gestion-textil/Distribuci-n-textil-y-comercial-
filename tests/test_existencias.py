import os

from fastapi.testclient import TestClient

from app import create_app


client = TestClient(create_app())


def test_consultar_existencias_retorna_contrato_estandar() -> None:
    response = client.get("/api/v1/inventario/existencias")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["mensaje"] == "Consulta procesada con éxito"
    assert body["data"]["historia"] == "HU-001"
    assert body["data"]["funciones_cubiertas"] == [f"FUN-{number:03d}" for number in range(1, 8)]


def test_consultar_existencias_por_referencia() -> None:
    response = client.get(
        "/api/v1/inventario/existencias",
        params={"referencia": "PAR-01"},
    )

    assert response.status_code == 200
    existencias = response.json()["data"]["existencias"]
    assert len(existencias) == 1
    assert existencias[0]["rollos"] == 12


def test_simular_indisponibilidad_retorna_503() -> None:
    os.environ["SIMULAR_FALLA_SERVIDOR"] = "true"
    try:
        response = client.get("/api/v1/inventario/existencias")
    finally:
        os.environ.pop("SIMULAR_FALLA_SERVIDOR", None)

    assert response.status_code == 503
