import grpc
import item_records_pb2
import item_records_pb2_grpc

def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = item_records_pb2_grpc.ItemsRecordsStub(channel)
        request = item_records_pb2.EmptyRequest()
        result = stub.PingItemsRecords(request)
        print(f'recived: {result.msg}')

        request = item_records_pb2.EmptyRequest()
        result = stub.GetItemsRecords(request)
        for item in result.data:
            print(item.name)

if __name__ == "__main__":
    main()
