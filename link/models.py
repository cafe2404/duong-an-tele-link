from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=255,verbose_name='Tên (viết liền không dấu)')
    title = models.CharField(max_length=255,default='Nhắn cho em để set kèo',verbose_name='Tiêu đề')
    url = models.URLField(verbose_name='Link telegram')
    button_text = models.CharField(max_length=255,default='Bấm vào đây để gặp lễ tân',verbose_name='Nội dung nút bấm')
    image = models.ImageField(upload_to='images/', blank=True, null=True,verbose_name='Hình ảnh')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    