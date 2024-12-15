""" Decorater. This is a decorative function for an admin panel. """

from flask_admin import Admin
from flask_login import LoginManager


# Decorator

def admin_pannel():
    """
    TODO: This is a decorative function for an admin panel.\n
        The function for decorate is 'create_admin' from the 'app.py'\n
        Old 'create_admin'.\n
        The old 'create_admin' function returns \n
        ```text \n
        flask_dict = create_flask() \n
        app_ = flask_dict["app"]\n
        csrf = flask_dict["csrf"]\n
        bcrypt = flask_dict["bcrypt"]\n
        ``` \n
        New 'create_admin'\n
        The new 'create_admin' function receives an administration panel and \n
        ```text \n
        flask_dict = create_flask\n
        app_ = flask_dict["app"]\n
        csrf = flask_dict["csrf"]\n
        bcrypt = flask_dict["bcrypt"]\n
        ```\n
        The admin panel is access to path '/admin/'.
    """
    
    def wrapper(app_) -> dict:
        
        # FORM INTEGRATIONS to the ADMIN PANEL
        # class MyTransactionDate(ModelView):
        #     column_exclude_list = ["amount"]
        #     form = FormEditTransactionData
        #
        # class MyUser_TransactionAdmin(ModelView):
        #     form = FormEditUser_TransactionData
        #
        # class MyUserAdmin(ModelView):
        #     form = FormEditorUserData
        
        # ADMIN PANEL
        app_dict = app_()
        admin = Admin(app_dict["app"])
        bank = Bank()
        session = bank.session
        # admin.add_views(
        #     MyUserAdmin(Users, session, name="User", url="/admin/users/"),
        #     MyTransactionDate(
        #         Transaction, session,
        #         url="/admin/transaction/"
        #     ),
        #     MyUser_TransactionAdmin(
        #         User_Transaction, session,
        #         name="User transaction",
        #         url="/admin/user_transaction/"
        #         )
        # )
        # https://flask-admin.readthedocs.io/en/latest/advanced/#managing-files-folders
        # admin.add_view(
        #     FileAdmin("project/static", '/static/', name='Static Files')
        #     )
        
        # LOGIN command
        login_manager = LoginManager()
        login_manager.init_app(app_dict["app"])
        
        # Loder of user
        @login_manager.user_loader
        def user_loader(user_id):
            bank = Bank()
            session = bank.session
            return session(Users).query.get(user_id)
        
        return app_dict
    
    return wrapper
