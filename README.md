# Distribución textil y comercial

Estructura funcional y arquitectónica inicial de un Web Service a partir del modelo de negocio seleccionado, mediante la identificación de módulos, submódulos, funcionalidades y procesos.

## HU-002

### Endpoint

`POST /api/v1/inventario/movimientos`

Tipos admitidos: `AJUSTE`, `RESERVA`, `LIBERACION` y `DEVOLUCION`.

Ejemplo:

```json
{
  "recurso": "PAR-01",
  "tipo_operacion": "RESERVA",
  "cantidad": 2,
  "usuario": "encargado-bodega"
}
```
