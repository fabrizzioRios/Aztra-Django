from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    autor = serializers.ReadOnlyField(source='autor.username')

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('autor', 'fecha_creacion')

    def validate_titulo(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El título debe tener al menos 5 caracteres")
        return value
