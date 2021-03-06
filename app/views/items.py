from flask import Blueprint
from app.models import Item

bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/<int:item_id>', methods=['PUT', 'GET'])
@bp.route('/', methods=['POST', 'GET'])
def items(item_id=None):
    return Item.get_delete_put_post(item_id)

