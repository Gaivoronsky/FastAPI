from workshop.database import engine
from workshop.tables import Base

Base.metadata.create_all(engine)