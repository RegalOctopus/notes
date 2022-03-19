from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/notes/",
            "Method": "GET",
            "body": None,
            "descripttion": "Returns an array of notes",
        },
        {
            "Endpoint": "/notes/id",
            "Method": "GET",
            "body": None,
            "descripttion": "Returns a single note object",
        },
        {
            "Endpoint": "/notes/create/",
            "Method": "POST",
            "body": {"body": ""},
            "descripttion": "Creates new note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/update/",
            "Method": "PUT",
            "body": {"body": ""},
            "descripttion": "Creates an existing note with data sent in put request",
        },
        {
            "Endpoint": "/notes/id/delete/",
            "Method": "DELETE",
            "body": None,
            "descripttion": "Deletes an existing note",
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response('Note Deleted')