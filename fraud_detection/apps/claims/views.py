from rest_framework import viewsets
from .models import InsuranceClaim
from .serializers import ClaimSerializer
from rest_framework.permissions import IsAuthenticated
from .services import FraudDetectionService

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = InsuranceClaim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        fraud_service = FraudDetectionService()
        fraud_service.detect_fraud(serializer.validated_data)
        super().perform_create(serializer)
