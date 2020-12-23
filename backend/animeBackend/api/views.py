from flask import Blueprint


blueprint = Blueprint('api', __name__)


@blueprint.route('/', methods=('GET',))
def home():
    return "hi"
