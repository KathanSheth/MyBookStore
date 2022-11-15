import grpc
import logging
from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub
logging.getLogger().setLevel(logging.INFO)

request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)

logging.info(client.Recommend(request))
