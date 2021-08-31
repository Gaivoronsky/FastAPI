import uvicorn

from .setting import settings


uvicorn.run(
    'workshop.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
