from rest_framework.permissions import DjangoModelPermissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Issuer, Credential, Subject
from .serializers import IssuerSerializer, CredentialSerializer, SubjectSerializer
from .utils.blockchain import generate_credential_hash


# -------- SUBJECT --------
class SubjectListCreateView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [DjangoModelPermissions]


class SubjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [DjangoModelPermissions]


# -------- ISSUER --------
class IssuerListCreateView(ListCreateAPIView):
    queryset = Issuer.objects.all()
    serializer_class = IssuerSerializer
    permission_classes = [DjangoModelPermissions]


class IssuerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Issuer.objects.all()
    serializer_class = IssuerSerializer
    permission_classes = [DjangoModelPermissions]


# -------- CREDENTIAL --------
class CredentialListCreateView(ListCreateAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [DjangoModelPermissions]

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            hash_value = generate_credential_hash(data.get('data'))
            credential = Credential.objects.create(
                issuer_id=data.get('issuer'),
                subject_did=data.get('subject_did'),
                credential_type=data.get('credential_type'),
                data=data.get('data'),
                hash=hash_value
            )
            serializer = CredentialSerializer(credential)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CredentialDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [DjangoModelPermissions]


