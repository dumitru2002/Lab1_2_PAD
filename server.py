import grpc
from concurrent import futures
import messaging_pb2
import messaging_pb2_grpc
from queue import Queue
from threading import Lock

class MessageServiceServicer(messaging_pb2_grpc.MessageServiceServicer):
    def __init__(self):
        # Dicționar pentru a stoca subscriberi pe topicuri
        self.topic_subscribers = {}
        self.lock = Lock()

    def PublishMessage(self, request, context):
        with self.lock:
            print(f"Received message from {request.sender} on topic {request.topic}: {request.message}")
            if request.topic in self.topic_subscribers:
                # Trimite mesajul tuturor subscriberilor abonați la acest topic
                for subscriber in self.topic_subscribers[request.topic]:
                    subscriber["queue"].put(messaging_pb2.MessageResponse(topic=request.topic, sender=request.sender, message=request.message))
        return messaging_pb2.MessageResponse(sender="Broker", topic=request.topic, message="Message delivered")

    def Subscribe(self, request, context):
        subscriber_queue = Queue()
        subscriber = {"name": request.subscriber_name, "queue": subscriber_queue}

        with self.lock:
            # Adauga subscriberul la topicul specificat
            if request.topic not in self.topic_subscribers:
                self.topic_subscribers[request.topic] = []
            self.topic_subscribers[request.topic].append(subscriber)

        try:
            while True:
                message = subscriber_queue.get()
                yield message
        except grpc.RpcError:
            print(f"{request.subscriber_name} disconnected from topic {request.topic}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messaging_pb2_grpc.add_MessageServiceServicer_to_server(MessageServiceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
