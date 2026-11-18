from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="Distribucion textil y comercial", version="1.0.0")

    from app.routers.movimientos import router

    app.include_router(router)
    return app
