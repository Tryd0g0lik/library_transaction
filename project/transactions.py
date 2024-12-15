"""
Here is a logic for work with the db transactions.
This is a management for control
"""
from typing import (Dict, Any)
from project.models import get_session
from project.models_some.model_autors import Authors
from project.models_some.model_client import Clients
from project.models_some.model_book import Books
from project.models_some.model_borrow import Borrows

# class Library_basis:
#     """
#     TODO:" This is basic class for a work with lybrary db.
#     """
#
#     def __init__(self):
#         self.session = get_session()
#         self._transaction = None
#
#
    
    