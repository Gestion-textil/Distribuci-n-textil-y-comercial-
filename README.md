# Distribución textil y comercial

Estructura funcional y arquitectónica inicial de un Web Service a partir del modelo de negocio seleccionado, mediante la identificación de módulos, submódulos, funcionalidades y procesos.

## HU-001

### Instalación

```bash
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Endpoint

`GET /api/v1/inventario/existencias`

Parámetro opcional: `referencia=PAR-01`

Para simular indisponibilidad del servicio:

```bash
SIMULAR_FALLA_SERVIDOR=true uvicorn app.main:app --reload
```
