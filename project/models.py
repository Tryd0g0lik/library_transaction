"""Models of db"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv_ import APP_POSTGRES_DBNAME, DSN
from project.models_some.model_init import Base
from project.postcresbase import create_database_if_not_exsists

# сreate DB
create_database_if_not_exsists(f"{APP_POSTGRES_DBNAME}")
def get_session():
    from project.logs import configure_logging
    log = logging.getLogger(__name__)
    configure_logging(logging.INFO)
    # Create on ENGINE
    log.info(f"[{get_session.__name__}]: START")
    log.info(f"[{get_session.__name__}]: DSN {DSN}")
    engine = create_engine(DSN)
    log.info("f[{get_session.__name__}]: received the engine of sqlalchemy")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    log.info(f"[{get_session.__name__}]: before run 'Session'")
    """Receive the session"""
    return Session()

