import os
import grpc
from flask import Flask, render_template
from recommendations.recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations.recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")

recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    rec_request = RecommendationRequest(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    rec_response = recommendations_client.Recommend(rec_request)
    return render_template("homepage.html", recommendations=rec_response.recommendations,)
