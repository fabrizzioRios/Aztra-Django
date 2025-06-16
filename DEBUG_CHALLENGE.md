# 🐞 Debug Challenge: Django REST Serializer

## Código con Error

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short")
        return value
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('title', instance.title)
        instance.save()
        return instance
```
## 🔍 Problemas Identificados
- Uso de `instance.titulo` (en español) cuando el modelo probablemente usa `title` (en inglés). Esto causará un `AttributeError` ya que el campo titulo no existe en el modelo.
- Solo se valida la longitud del título pero no otros campos importantes como el contenido
- El método update solo modifica el título, ignorando otros campos que podrían estar en `validated_data`
