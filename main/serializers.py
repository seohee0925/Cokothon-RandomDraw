from rest_framework import serializers
from .models import Capsule

import base64
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 부분을 분리
            header, data = data.split(';base64,')
            # base64 데이터 디코드
            decoded_img = base64.b64decode(data)
            # ContentFile을 사용하여 Django ImageField에 저장 가능한 형태로 변환
            data = ContentFile(decoded_img, name='temp.png')  # 파일 확장자에 주의하세요.
        return super().to_internal_value(data)

class CapsuleSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)  # 이미지 필드를 Base64ImageField로 교체
    
    class Meta:
        model = Capsule
        fields = ('content', 'destination', 'image', 'open_date')

    def create(self, validated_data):
        user_email = self.context.get('user_email')
        
        capsule = Capsule.objects.create(email=user_email, **validated_data)
        return capsule

