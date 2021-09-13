# from django.shortcuts import render
# from rest_framework import generics
# from .models import Post
# from .serializers import PostSerializer


# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer




from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # کاربر بدون لاگین امکان مشاهده ای پی آی ندارد
    # permission_classes = [permissions.IsAuthenticated]
    # کاربر بدون لاگین فقط می تواند محتوای ای پی ای را ببیند اما امکان ارسال ندارد
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # این متد باعث میشه اطلاعات کاربر درخواست دهنده، بعنوان poster در serializer ذخیره بشه
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)