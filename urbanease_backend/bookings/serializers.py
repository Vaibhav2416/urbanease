# from rest_framework import serializers
# from .models import Booking

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = [
#             "id",
#             "service",
#             "scheduled_at",
#             "address",
#             "status",
#             "created_at",
#         ]
#         depth = 1   # expands service and its category
#         read_only_fields = ["id", "status", "created_at"]

#     def create(self, validated_data):
#         validated_data["customer"] = self.context["request"].user
#         return super().create(validated_data)

# bookings/serializers.py
# from rest_framework import serializers
# from .models import Booking
# from services.models import Service
# from services.serializers import ServiceSerializer

# class BookingSerializer(serializers.ModelSerializer):
#     # Accept service as ID on input and validate against Service queryset
#     service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

#     class Meta:
#         model = Booking
#         fields = [
#             "id",
#             "service",
#             "scheduled_at",
#             "address",
#             "status",
#             "created_at",
#         ]
#         read_only_fields = ["id", "status", "created_at"]
#         depth = 1  # will expand service to nested object in output

#     def create(self, validated_data):
#         # set customer from request.user (passed via context in view)
#         validated_data["customer"] = self.context["request"].user
#         return super().create(validated_data)

# bookings/serializers.py
from rest_framework import serializers
from .models import Booking
from services.serializers import ServiceSerializer
from users.serializers import SimpleUserSerializer
from services.models import Service
class BookingSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())  # will set queryset in __init__
    provider = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "service", "provider", "scheduled_at", "address", "status", "created_at"]
        read_only_fields = ["id","service", "status", "created_at", "provider"]
        depth = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # lazy import to avoid circular import at module load
        from services.models import Service
        self.fields['service'].queryset = Service.objects.all()

    def create(self, validated_data):
        # set customer from request.user (passed via context in view)
        validated_data["customer"] = self.context["request"].user
        return super().create(validated_data)


# from rest_framework import serializers
# from .models import Booking
# from services.models import Service
# from services.serializers import ServiceSerializer
# from users.serializers import SimpleUserSerializer

# class BookingSerializer(serializers.ModelSerializer):
#     # ✅ For READ: return full service object
#     service = ServiceSerializer(read_only=True)

#     # ✅ For WRITE: accept service ID
#     service_id = serializers.PrimaryKeyRelatedField(
#         source="service",
#         queryset=Service.objects.all(),
#         write_only=True
#     )

#     provider = SimpleUserSerializer(read_only=True)

#     class Meta:
#         model = Booking
#         fields = [
#             "id",
#             "service",        # nested object (output)
#             "service_id",     # ID only (input)
#             "provider",
#             "scheduled_at",
#             "address",
#             "status",
#             "created_at",
#         ]
#         read_only_fields = ["id", "status", "created_at", "provider"]

#     def create(self, validated_data):
#         validated_data["customer"] = self.context["request"].user
#         return super().create(validated_data)