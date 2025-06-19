from flask import Blueprint, Response, jsonify
from api.adapters import database
from api.application import use_cases
from api.application.outputs.user_output import UserOutput
from api.infrastructure.repositories.user_repository import UserRepository


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/users")
def get_users() -> Response:
    user_repository = UserRepository(database.session())
    users = use_cases.get_users(user_repository)
    user_outputs = [UserOutput.from_user(user) for user in users]

    return jsonify([user_output.model_dump_json() for user_output in user_outputs])


@user_blueprint.route("/users/<string:user_id>")
def get_user_by_id(user_id: str) -> Response:
    user_repository = UserRepository(database.session())
    user = use_cases.get_user_by_id(user_repository, user_id)
    if user is None:
        return Response(status=404)
    user_output = UserOutput.from_user(user)

    return jsonify(user_output.model_dump_json())
