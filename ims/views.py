from decimal import Decimal
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ams.logic import DATAHANDLER
from basic.models import UserDatabase
from ims.models import (
    BagInventory,
    Material,
    MaterialCategory,
    MaterialGroup,
    MaterialMovement,
    MaterialReport,
    MaterialType,
    PO_Status,
    Plant,
    PlantType,
    PurchaseOrder,
    PurchaseOrderItem,
    Stock,
    StorageLocation,
    StorageLocationType,
    Transaction,
    TransactionStatus,
    UnitOfMeasure,
    Units,
    Warehouse,
    WarehouseType,
)

# Create your views here.


class ImsView(APIView):
    def get(self, request):
        return Response({"status": "success"}, status=status.HTTP_200_OK)


class UnitsView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Units, data_copy=data_copy)
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
        pipe = DATAHANDLER(request=request, class_name=PlantType, data_copy=data_copy)
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
        pipe = DATAHANDLER(
            request=request, class_name=WarehouseType, data_copy=data_copy
        )
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
        pipe = DATAHANDLER(
            request=request, class_name=StorageLocationType, data_copy=data_copy
        )
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
        pipe = DATAHANDLER(
            request=request, class_name=StorageLocation, data_copy=data_copy
        )
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
        pipe = DATAHANDLER(
            request=request, class_name=MaterialMovement, data_copy=data_copy
        )
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
        pipe = DATAHANDLER(
            request=request, class_name=TransactionStatus, data_copy=data_copy
        )
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

        instance = pipe_out.order_by("-created_at")
        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        data_copy["created_by"] = str(request.user.pk)
        data_copy["transaction_status"] = str(
            TransactionStatus.objects.filter(status_code="PENG").first().pk
        )
        data_copy["movement"] = str(
            MaterialMovement.objects.filter(movement_code=data_copy["movement_code"])
            .first()
            .pk
        )
        movement = MaterialMovement.objects.filter(pk=data_copy["movement"]).first()

        if movement is None:
            return Response(
                {"message": "Invalid movement"}, status=status.HTTP_400_BAD_REQUEST
            )

        if movement.movement_code == "SL2TECH":
            pipe = DATAHANDLER(
                request, Transaction, data_copy, bloc="material_movement_sl_tech"
            )
            valid = self.validate_SL2TECH(data_copy)

            if isinstance(valid, Response):
                return valid

            pipe_out = pipe.process(pk=pk)
            return pipe_out
        elif movement.movement_code == "TECH2TECH":
            pipe = DATAHANDLER(
                request, Transaction, data_copy, bloc="material_movement_tech_tech"
            )
            valid = self.validate_TECH2TECH(data_copy)

            if isinstance(valid, Response):
                return valid

            pipe_out = pipe.process(pk=pk)
            return pipe_out
        elif movement.movement_code == "TECH2SL":
            pipe = DATAHANDLER(
                request, Transaction, data_copy, bloc="material_movement_tech_sl"
            )
            valid = self.validate_TECH2SL(data_copy)

            if isinstance(valid, Response):
                return valid

            pipe_out = pipe.process(pk=pk)
            return pipe_out
        else:
            pipe = DATAHANDLER(
                request, Transaction, data_copy, bloc="material_movement"
            )

            valid = self.validate(data_copy)

            if isinstance(valid, Response):
                return valid

            pipe_out = pipe.process(pk=pk)
            return pipe_out

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        if "transaction_status" in data_copy:
            print("update transaction status")
            data_copy["transaction_status"] = str(
                TransactionStatus.objects.filter(
                    status_code=data_copy["transaction_status"]
                )
                .first()
                .pk
            )
            print(data_copy)
            pipe = DATAHANDLER(
                request, Transaction, data_copy, bloc="update_transaction_status"
            )
            print(pipe)
            pipe_out = pipe.process(pk=pk)

            return pipe_out



        pipe = DATAHANDLER(request, Transaction, data_copy)
        pipe_out = pipe.process(pk=pk)
        
        return pipe_out

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Transaction, data_copy).process(pk=pk)
        return pipe

    def validate(self, data_copy):
        if (
            "source_code" not in data_copy
            or "destination_code" not in data_copy
            or "movement" not in data_copy
        ):
            return Response(
                {"message": "Missing source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        source = StorageLocation.objects.filter(
            location_code=data_copy["source_code"]
        ).first()
        destination = StorageLocation.objects.filter(
            location_code=data_copy["destination_code"]
        ).first()
        if source is None or destination is None:
            return Response(
                {"message": "Invalid source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        material = Material.objects.filter(pk=data_copy["material"]).first()
        volume = Decimal(str(data_copy["volume"]))

        if material is None:
            return Response(
                {"message": "Invalid material_code"}, status=status.HTTP_400_BAD_REQUEST
            )

        stock = Stock.objects.filter(material=material, storage_location=source).first()

        if volume > stock.quantity:
            return Response(
                {"message": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST
            )

        return True

    def validate_SL2TECH(self, data_copy):
        if (
            "source_code" not in data_copy
            or "destination_code" not in data_copy
            or "movement" not in data_copy
        ):
            return Response(
                {"message": "Missing source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        source = StorageLocation.objects.filter(
            location_code=data_copy["source_code"]
        ).first()
        destination = UserDatabase.objects.filter(
            user_code=data_copy["destination_code"]
        ).first()
        if source is None or destination is None:
            return Response(
                {"message": "Invalid source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        material = Material.objects.filter(pk=data_copy["material"]).first()
        volume = Decimal(str(data_copy["volume"]))

        if material is None:
            return Response(
                {"message": "Invalid material_code"}, status=status.HTTP_400_BAD_REQUEST
            )

        stock = Stock.objects.filter(material=material, storage_location=source).first()

        if volume > stock.quantity:
            return Response(
                {"message": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST
            )

        return True

    def validate_TECH2SL(self, data_copy):
        if (
            "source_code" not in data_copy
            or "destination_code" not in data_copy
            or "movement" not in data_copy
        ):
            return Response(
                {"message": "Missing source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        destination = StorageLocation.objects.filter(
            location_code=data_copy["destination_code"]
        ).first()
        source = UserDatabase.objects.filter(user_code=data_copy["source_code"]).first()

        if source is None or destination is None:
            return Response(
                {"message": "Invalid source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        material = Material.objects.filter(pk=data_copy["material"]).first()
        volume = Decimal(str(data_copy["volume"]))

        if material is None:
            return Response(
                {"message": "Invalid material_code"}, status=status.HTTP_400_BAD_REQUEST
            )

        stock = BagInventory.objects.filter(material=material, user=source).first()

        if stock and volume > stock.volume:
            return Response(
                {"message": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST
            )

        return True

    def validate_TECH2TECH(self, data_copy):
        if (
            "source_code" not in data_copy
            or "destination_code" not in data_copy
            or "movement" not in data_copy
        ):
            return Response(
                {"message": "Missing source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        source = UserDatabase.objects.filter(user_code=data_copy["source_code"]).first()
        destination = UserDatabase.objects.filter(
            user_code=data_copy["destination_code"]
        ).first()
        print("Source:", source)
        print("Destination:", destination)
        if source is None or destination is None:
            return Response(
                {"message": "Invalid source_code or destination_code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        material = Material.objects.filter(pk=data_copy["material"]).first()
        volume = Decimal(str(data_copy["volume"]))

        if material is None:
            return Response(
                {"message": "Invalid material_code"}, status=status.HTTP_400_BAD_REQUEST
            )

        stock = BagInventory.objects.filter(material=material, user=source).first()

        if stock and volume > stock.volume:
            return Response(
                {"message": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST
            )

        return True


class MaterialReportView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=MaterialReport, data_copy=data_copy
        )
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
        pipe = DATAHANDLER(
            request=request, class_name=PurchaseOrder, data_copy=data_copy
        )
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
        if "status" in data_copy.keys() and data_copy["status"] == "DELIVERED":
            data_copy["status"] = (
                PO_Status.objects.filter(status_code="DELIVERED").first().pk
            )
            pipe = DATAHANDLER(request, PurchaseOrder, data_copy, bloc="po_delivered")
        else:
            pipe = DATAHANDLER(request, PurchaseOrder, data_copy)
        pipe_out = pipe.process(pk=pk)
        return pipe_out

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PurchaseOrder, data_copy).process(pk=pk)
        return pipe


class PurchaseOrderItemView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=PurchaseOrderItem, data_copy=data_copy
        )
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


class BagInventoryView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=BagInventory, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out.filter(user=request.user)
        # instance = pipe_out

        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BagInventory, data_copy).process(pk=pk)
        return pipe

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BagInventory, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BagInventory, data_copy).process(pk=pk)
        return pipe


