import asyncio
from project.models_some.model_book import Book
from project.models_some.model_borrow import Borrow
from project.models_some.model_client import Client
from project.models_some.model_person import Person
from project.veiws_some.views_author import author_api_path
from project.veiws_some.views_book import book_api_path
from project.veiws_some.views_client import сlient_api_path


async def api_path():
    await asyncio.gather(
        author_api_path(),
        book_api_path(),
        сlient_api_path()
    )