import grpc
import messaging_pb2
import messaging_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50052')
    stub = messaging_pb2_grpc.MessageServiceStub(channel)

    topic = input("Enter the topic to publish the message: ")
    message = input("Enter the message to send: ")
    response = stub.PublishMessage(messaging_pb2.MessageRequest(topic=topic, sender="Sender1", message=message))

    print("Publish response:", response.message)


if __name__ == '__main__':
    run()
