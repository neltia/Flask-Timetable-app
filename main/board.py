from main import *
from flask import Blueprint

blueprint = Blueprint("board", __name__, url_prefix='/board')

@blueprint.route("/main")
def board_main():
    return render_template("cover.html")
