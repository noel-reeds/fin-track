from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from models.user import User


db = SQLAlchemy()


def fintrack_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fintrack_db.sqlite'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view ='auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    from .app import main as main_blueprint
    from models.user import expenditure as expenditure

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(expenditure)

    return app


if __name__ == "__main__":
    app.run(debug=True)
