# Grpc python example

### This is an example of how to use grpc whit python.
### Steps to make it work:

* You must separate the directories *grpc-server* and *grpc-consumer*.
* Install the dependencies `pip3 install -f requirements.txt` (on each directory).
* Run the main.py files, first **grpc-server/main.py** and then **grpc-consumer/main.py**.
* You should see a print of the item names in the grpc-consumer terminal.
* There is a Dockerfile, but I didn't test it.
* If you want to recreate the protobuf py files you should use this command `python3 -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs/items_records.proto`
inside one of the two directories (*grpc-consumer* or *grpc=server*) and then copy/replace the files: *item_records_pb2.py* and *item_records_pb2_grpc.py* into the other directory.

This is a very basic example, but it might help you to understand how grpc works.