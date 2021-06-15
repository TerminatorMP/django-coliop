from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import xmlrpc.client

cmplClient = xmlrpc.client.ServerProxy("http://localhost:8008/")

class GetJobId(APIView):
  renderer_classes = [JSONRenderer]
  parser_classes = [JSONParser]

  def post(self, request, format=None):
    jobId = request.data['name']
    data = cmplClient.getJobId(jobId, 'cbc', 3)
    return Response({
      'jobId': data[2]
    })

class GetMessages(APIView):
  renderer_classes = [JSONRenderer]
  parser_classes = [JSONParser]

  def get(self, request, format=None):
    jobId = request.query_params['jobId']
    data = cmplClient.getCmplMessages(jobId)
    return Response({
      'message': data
    })

class CheckForSolution(APIView):
  renderer_classes = [JSONRenderer]
  parser_classes = [JSONParser]

  def get(self, request, format=None):
    jobId = request.query_params['jobId']
    data = cmplClient.knock(jobId)
    return Response({
      'solutionStatus': data
    })

class GetSolution(APIView):
  renderer_classes = [JSONRenderer]
  parser_classes = [JSONParser]

  def get(self, request, format=None):
    jobId = request.query_params['jobId']
    data = cmplClient.getSolutions(jobId)
    return Response({
      'solution': data
    })


class SendXML(APIView):
  renderer_classes = [JSONRenderer]
  parser_classes = [JSONParser]

  def post(self, request, format=None):
    problemXml = request.data['xml']
    data = cmplClient.send(problemXml)
    return Response(
      status=status.HTTP_200_OK
    )