from project.models_some.model_autors import Author


class Client(Author):
    """
    TODO: This guys take books from a library
    :param firstname: str. Author's name.
    :param secondname: str. Authors's secondname.
    :param birthday: datetime.
    """
    __tablename__ = "clients"
    

    def __str__(self):
        return f"Person ID: {self.id}, Person firstname: {self.firstname} \
        Person birthday: {self.birthday}"