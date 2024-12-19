"""Models of db"""

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv_ import APP_POSTGRES_DBNAME, DSN
from project.logs import configure_logging
from project.models_some.model_init import Base
from project.postcresbase import create_database_if_not_exsists

log = logging.getLogger(__name__)
configure_logging(logging.INFO)

# сreate DB
create_database_if_not_exsists(f"{APP_POSTGRES_DBNAME}")
engine = create_engine(DSN, pool_pre_ping=True)
log.info(f"[{__name__}]: received the engine of sqlalchemy")
Base.metadata.create_all(bind=engine)
log.info(f"[{__name__}]: Tabular db was created.  ")


def get_session():

    # Create on ENGINE
    log.info(f"[{get_session.__name__}]: START")
    Session = sessionmaker(bind=engine)
    log.info(f"[{get_session.__name__}]: before run 'Session'")
    """Receive the session"""
    return Session()
