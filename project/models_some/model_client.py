from project.models_some.model_autors import Authors


class Clients(Authors):
    """
    TODO: This guys take books from a library
    :param firstname: str. Author's name.
    :param secondname: str. Authors's secondname.
    :param birthday: datetime.
    """
    __tablename__ = "clients"
    pass

    