import rec_db
import random
import grpc
from concurrent import futures
from recommendations_pb2 import (
     BookCategory,
     BookRecommendation,
     RecommendationResponse,
)
import recommendations_pb2_grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound


class RecommendService(recommendations_pb2_grpc.RecommendationsServicer):

    def Recommend(self, request, context):
        if request.category not in rec_db.books_by_category.keys():
            # context.abort(grpc.StatusCode.NOT_FOUND, "Category not found.")
            raise NotFound("Category not found.")
        books_for_cat = rec_db.books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_cat))
        books_to_recommend = random.sample(books_for_cat, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors)
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(RecommendService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

