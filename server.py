from concurrent import futures
from datetime import datetime
import grpc
import pingpong_pb2
import pingpong_pb2_grpc
import time
import threading


class Listener(pingpong_pb2_grpc.PingPongServiceServicer):
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()

    def Ping(self, request, context):
        self.counter += 1
        if self.counter == 10000:
            print("10000 calls in {:.02f} seconds".format(time.time() - self.lastPrintTime))
            self.lastPrintTime = time.time()
            self.count = 0

        return pingpong_pb2.Pong(count=request.counter + 1)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pingpong_pb2_grpc.add_PingPongServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("localhost:9999")
    server.start()
    try:
        while True:
            print("Server on: threads {} ({})".format(threading.active_count(), datetime.now()))
            time.sleep(10)
    except:
        print("Bye")
        server.stop(0)
        raise


if __name__ == '__main__':
    server()
