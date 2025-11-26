from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Issuer, Credential, Subject
from .serializers import IssuerSerializer, CredentialSerializer, SubjectSerializer
from .utils.blockchain import generate_credential_hash


class SubjectView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssuerView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        issuers = Issuer.objects.all()
        serializer = IssuerSerializer(issuers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = IssuerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CredentialView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        credentials = Credential.objects.all()
        serializer = CredentialSerializer(credentials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
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
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


