## Introduction
A grpc sample code for learning.
* [10000 Messages in 2.18 seconds with Python and gRPC](https://www.youtube.com/watch?v=dQK0VLahrDk&list=PLyQnbMWK6HUXFM4csj3VPSdgRadRmyzNv&index=7&t=139s)
* [Gitrepo - Seans-gRPC](https://github.com/Sean-Bradley/Seans-gRPC)

## Initialization
We have a few package dependencies to install before all:
```console
$ pip install -r requirements.txt
```

## Initialize ProtocolBuffer Setting

### Create file `proto/pingpong.proto`
```
// my ping pong proto file
syntax = "proto3";

service PingPongService {
  rpc ping(Ping) returns (Pong) {}
}

message Ping {
  int32 count = 1;
}

message Pong {
  int32 count = 1;
}
```
### Execute command below:
```console
$ python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/pingpong.proto
```
After execution, below two files will be generated automatically:
* pingpong_pb2_grpc.py
* pingpong_pb2_grpc.py

## Build server.py
We build up a server [server.py](server.py) as below to service the request:
```python
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
    server.add_insecure_port("[::]:9999")
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
```
Then you can start the server by execute it:
```console
$ python server.py
Server on: threads 2 (2020-07-24 04:03:12.201500)
Server on: threads 2 (2020-07-24 04:03:22.202388)
```
## Build client.py
We build a client to test the server:
