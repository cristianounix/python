from typing import Dict, Optional, Union

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import config

db = SQLAlchemy()


def create_app(cfg: Optional[config.Config] = None) -> Flask:
    if cfg is None:
        cfg = config.Config()
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(cfg)

    # Init_apps
    db.init_app(app)

    @app.route("/square")
    def square() -> str:
        number = int(request.args.get("number", 0))
        return str(number ** 2)

    @app.route("/")
    def templated_square() -> str:
        number = int(request.args.get("number", 0))
        return render_template("base.html", number=number, square=number ** 2)

    @app.route("/author/<int:author_id>")
    def get_author(author_id: int) -> Dict[str, Union[int, str]]:
        from app.models import Author

        return Author.query.get(author_id).dict()

    @app.route("/login", methods=["POST"])
    def login(author_id: int) -> Dict[str, Union[int, str]]:
        redirect_url = request.args.get("next", "/")
        return {"redirect_url": redirect_url}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
