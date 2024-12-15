"""
Here is a logic for work with the db transactions.
This is a management for control
"""
import logging
from typing import (Dict, Any)
from project.models import get_session

class Library_basis:
    """
    TODO:" This is basic class for a work with lybrary db.
    """
    
    def __init__(self):
        self.session = get_session()
        self._transaction = None

    def get_transaction(self) -> [Dict[str, Any], int]:
        """
        TODO: Receive the transaction object .
        :return: object
        """
        return self._transaction

    def close(self) -> None:
        """Close the session"""
        from project.logs import configure_logging
        log = logging.getLogger(__name__)
        configure_logging(logging.INFO)

        try:
            self.session.close()
        except Exception as e:
            log.info(f"[{__name__}]: Session was closed. Error => {e}")