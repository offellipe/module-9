from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.balance_editor_composer import balance_editor_composer

bank_routes_bp = Blueprint("bank_routes", __name__)

@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        return jsonify(http_response.body), http_response.status_code

@bank_routes_bp.route("/bank/login", methods=["POST"])
def create_login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        return jsonify(http_response.body), http_response.status_code

@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def edit_balance(user_id):
    try:
        http_request = HttpRequest(
            body=request.json,
            params={ "user_id": user_id },
            headers=request.headers
            )
        http_response = balance_editor_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        return jsonify(http_response.body), http_response.status_code
