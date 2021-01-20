from main import *
from flask import Blueprint

blueprint = Blueprint("member", __name__, url_prefix='/member')

@blueprint.route("join", methods=["GET", "POST"])
def memeber_join():
    return "가입"
