from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ams.logic import DATAHANDLER
from ims.models import Material, MaterialCategory, MaterialGroup, MaterialMovement, MaterialReport, MaterialType, PO_Status, Plant, PlantType, PurchaseOrder, PurchaseOrderItem, StorageLocation, StorageLocationType, Transaction, TransactionStatus, UnitOfMeasure, Units, Warehouse, WarehouseType
# Create your views here.


class ImsView(APIView):
    def get(self, request):
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    
    


class UnitsView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=Units, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Units, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Units, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Units, data_copy).process(pk=pk)
        return pipe
    
    
class UnitOfMeasureView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UnitOfMeasure, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UnitOfMeasure, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UnitOfMeasure, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UnitOfMeasure, data_copy).process(pk=pk)
        return pipe
    


class MaterialGroupView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=MaterialGroup, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialGroup, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialGroup, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialGroup, data_copy).process(pk=pk)
        return pipe
    
class MaterialCategoryView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=MaterialCategory, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialCategory, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialCategory, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialCategory, data_copy).process(pk=pk)
        return pipe
    
class MaterialTypeView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=MaterialType, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialType, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialType, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialType, data_copy).process(pk=pk)
        return pipe
    

class MaterialView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Material, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Material, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Material, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Material, data_copy).process(pk=pk)
        return pipe
    
    
class PlantTypeView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=PlantType, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PlantType, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PlantType, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PlantType, data_copy).process(pk=pk)
        return pipe
    
    
class PlantView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Plant, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Plant, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Plant, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Plant, data_copy).process(pk=pk)
        return pipe
    
class WarehouseTypeView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=WarehouseType, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, WarehouseType, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, WarehouseType, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, WarehouseType, data_copy).process(pk=pk)
        return pipe


class WarehouseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Warehouse, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Warehouse, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Warehouse, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Warehouse, data_copy).process(pk=pk)
        return pipe
    
    
class StorageLocationTypeView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=StorageLocationType, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StorageLocationType, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StorageLocationType, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StorageLocationType, data_copy).process(pk=pk)
        return pipe
    
class StorageLocationView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=StorageLocation, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StorageLocation, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):    
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StorageLocation, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StorageLocation, data_copy).process(pk=pk)
        return pipe
    
    
class MaterialMovementView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=MaterialMovement, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialMovement, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialMovement, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialMovement, data_copy).process(pk=pk)
        return pipe
    
class TransactionStatusView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=TransactionStatus, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, TransactionStatus, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, TransactionStatus, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, TransactionStatus, data_copy).process(pk=pk)
        return pipe
    
class TransactionView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Transaction, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Transaction, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Transaction, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Transaction, data_copy).process(pk=pk)
        return pipe
    
    
class MaterialReportView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=MaterialReport, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialReport, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialReport, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, MaterialReport, data_copy).process(pk=pk)
        return pipe
    


class PO_StatusView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=PO_Status, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PO_Status, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PO_Status, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PO_Status, data_copy).process(pk=pk)
        return pipe
    
    
class PurchaseOrderView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=PurchaseOrder, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PurchaseOrder, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PurchaseOrder, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PurchaseOrder, data_copy).process(pk=pk)
        return pipe
    
class PurchaseOrderItemView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=PurchaseOrderItem, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PurchaseOrderItem, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PurchaseOrderItem, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PurchaseOrderItem, data_copy).process(pk=pk)
        return pipe
    
    
    