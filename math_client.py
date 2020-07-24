"""The Python implememntation of math grpc client"""
import os
import time
import grpc
import random
import pingpong_pb2
import pingpong_pb2_grpc


def run(port=9999, min_num=0, max_num=100):
    "The run method, that sends gRPC conformant messsages to the server"
    counter = 0
    pid = os.getpid()
    with grpc.insecure_channel("localhost:{}".format(port)) as channel:
        stub = pingpong_pb2_grpc.MathServiceStub(channel)
        while True:
            try:
                start = time.time()
                n1, n2 = random.randint(min_num, max_num), random.randint(min_num, max_num)
                response = stub.sum(pingpong_pb2.Numbers(num1=n1, num2=n2))
                sum_result = response.result
                counter += 1
                if counter % 1000 == 0:
                    print("{:.02f}/procid={}/counter={}: n1={},n2={} with sum={}".format(time.time() - start, pid, counter, n1, n2, sum_result))
                    # counter = 0

                # time.sleep(0.001)
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                exit()


def close(channel):
    "Close the channel"
    channel.close()


if __name__ == "__main__":
    run()
