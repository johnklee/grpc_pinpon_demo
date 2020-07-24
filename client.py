import os
import pingpong_pb2
import pingpong_pb2_grpc
import time
import grpc

def run():
    counter, pid = 0, os.getpid()
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = pingpong_pb2_grpc.PingPongServiceStub(channel)
        while True:
            try:
                start = time.time()
                response = stub.ping(pingpong_pb2.Ping(count=counter))
                counter = response.count
                if counter % 1000 == 0:
                    print("{}: resp={}: procid={}".format(time.time() - start, response.count, pid))
            except KeyboardInterrupt:
                print("Bye")
                channel.unsubscribe(close)
                exit()
            except:
                raise


def close(channel):
    channel.close()


if __name__ == '__main__':
    run()
