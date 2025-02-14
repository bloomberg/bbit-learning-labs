"""Flask app instance creation for Tech Lab 2025."""

import os

from flask import Flask, Response, jsonify

from app import newsfeed
from app.utils.file_loader import load_json_files
from app.utils.redis import REDIS_CLIENT


def create_app():
    """Create a Flask app instance."""
    app = Flask("app")

    # Load JSON files into Redis
    dataset_directory = os.path.join(os.path.dirname(__file__), "../resources/dataset/news")
    REDIS_CLIENT.save_entry("all_articles", load_json_files(dataset_directory))

    @app.route("/ping", methods=["GET"])
    def ping() -> Response:
        """Flask route to check if the server is up and running."""
        return jsonify("Pong!", 200)

    @app.route("/get-newsfeed", methods=["GET"])
    def get_newsfeed() -> Response:
        """Flask route to get the latest newsfeed from datastore."""
        # PART 1
        return jsonify({}, 200)

    @app.route("/get-featured-article", methods=["GET"])
    def get_featured_article() -> Response:
        """Flask route to get the featured article from datastore."""
        # PART 2
        return jsonify({}, 200)

    return app
