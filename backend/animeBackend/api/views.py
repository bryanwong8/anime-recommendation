from flask import Blueprint
from animeBackend.recommend import get_recommendation

blueprint = Blueprint('api', __name__)


@blueprint.route('/', methods=('GET',))
def home():
    return "hi"
