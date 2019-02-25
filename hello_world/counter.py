from sanic.response import text
from sanic import Blueprint
import redis

counter_bp = Blueprint("counter_bp")
r = redis.Redis(host='localhost', port=6379, db=0)

@counter_bp.route("/counter_get", methods=["GET"])
def get_counter(request):
    return text(r.get("counter"))

@counter_bp.route("/counter_inc", methods=["POST"])
def inc_counter(request):
    r.setnx("counter", 0)
    r.incr("counter")
    return text(r.get("counter"))