import grpc
import messaging_pb2
import messaging_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50052')
    stub = messaging_pb2_grpc.MessageServiceStub(channel)

    topic = input("Enter the topic to subscribe to: ")
    responses = stub.Subscribe(messaging_pb2.SubscribeRequest(topic=topic, subscriber_name="Subscriber1"))

    for response in responses:
        print(f"Received message on topic {response.topic} from {response.sender}: {response.message}")


if __name__ == '__main__':
    run()
