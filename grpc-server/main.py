import grpc
from concurrent import futures
import item_records_pb2
import item_records_pb2_grpc

items = [
    {
        'name': 'Test 1',
        'foo': 'bar'
    },
    {
        'name': 'Test 2',
        'foo': 'bar'
    },
    {
        'name': 'Test 3',
        'foo': 'bar'
    },
    {
        'name': 'Test 4',
        'foo': 'bar'
    }
]


class ItemsRecords(item_records_pb2_grpc.ItemsRecordsServicer):
    def PingItemsRecords(self, request, context):
        response = item_records_pb2.PingItemsRecordsResponse(msg='Ok')
        return response

    def GetItemsRecords(self, request, context):
        data = []
        for item in items:
            data.append(item_records_pb2.Item(name=item['name'], foo=item['foo'], source='test'))
        response = item_records_pb2.GetItemsResponse(data=data)
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    item_records_pb2_grpc.add_ItemsRecordsServicer_to_server(
        ItemsRecords(),
        server
    )

    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started on port 50051')
    server.wait_for_termination()


if __name__ == "__main__":
    main()
