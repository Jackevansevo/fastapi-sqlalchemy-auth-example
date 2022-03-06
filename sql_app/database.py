import inflect
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declared_attr, registry, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

mapper_registry = registry()
_pluralizer = inflect.engine()


@mapper_registry.as_declarative_base()
class Base(object):

    @declared_attr
    def __tablename__(cls):
        return _pluralizer.plural(cls.__name__.lower())

    id = Column(Integer, primary_key=True)
