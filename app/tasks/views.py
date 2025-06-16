from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tasks.models import Tarea
from tasks.serializers import TareaSerializer, CambiarEstadoSerializer


class TaskListView(generics.ListAPIView):
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tarea.objects.all()

        # Filtro obligatorio por proyecto
        proyecto_id = self.request.query_params.get('proyecto')
        if not proyecto_id:
            return Tarea.objects.none()

        queryset = queryset.filter(proyecto_id=proyecto_id)

        # Filtro opcional por estado
        estado = self.request.query_params.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)

        # Ordenamiento por fecha de vencimiento
        return queryset.order_by('fecha_vencimiento')


class ChangeStateView(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = CambiarEstadoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        tarea = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tarea.estado = serializer.validated_data['estado']
        tarea.save()

        return Response({
            'status': 'success',
            'message': 'Estado actualizado correctamente',
            'data': TareaSerializer(tarea).data
        }, status=status.HTTP_200_OK)
