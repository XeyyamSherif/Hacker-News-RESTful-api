from django.http.response import HttpResponse
from .models import Post, comments
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CommentSerializer, PostSerializer
from django.http import JsonResponse
from .tasks import add


""" post class crud starts from here"""


@api_view(["GET", "POST", "DELETE"])
def postlist(request):
    if request.method == 'GET':
        post_all = Post.objects.all()
        ser_post = PostSerializer(post_all, many=True)
        return Response(ser_post.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def postDetail(request, pk):
    try:
        tutorial = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'})

    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        ser_post = PostSerializer(post)
        return Response(ser_post.data)

    if request.method == 'DELETE':
        post = Post.objects.get(id=pk)
        post.delete()
        return HttpResponse("deleted")

    if request.method == 'PUT':
        post_upd = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post_upd, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


""" comments class crud starts from here """


@api_view(["GET"])
def comments_of_post(request, pk):
    comments_post = comments.objects.filter(post=pk)
    ser_post = CommentSerializer(comments_post, many=True)
    return Response(ser_post.data)


@api_view(["POST"])
def addComment(request, pk):
    commented_post = Post.objects.get(id=pk)
    comment_data = request.data
    new_comment = comments.objects.create(
        content=comment_data["content"],
        author_name=comment_data["author_name"],
        post=commented_post,
    )
    new_comment.save()
    serializer = CommentSerializer(new_comment)

    return Response(serializer.data)


@api_view(["PUT", "DELETE"])
def edit_comments(request, pk):
    try:
        tutorial = comments.objects.get(pk=pk)
    except comments.DoesNotExist:
        return JsonResponse({'message': 'such comment does not exist'})

    if request.method == "DELETE":
        comment_for_delete = comments.objects.get(id=pk)
        comment_for_delete.delete()
        return HttpResponse("deleted")

    if request.method == "PUT":
        post_upd = comments.objects.get(id=pk)
        serializer = CommentSerializer(instance=post_upd, data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)


"""other methods starts from here"""


def increase_upvote(request, pk):
    """This method increases upvote 1 unit"""
    try:
        tutorial = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'})
    upvoted_post = Post.objects.get(id=pk)
    upvoted_post.upvote += 1
    upvoted_post.save()
    return HttpResponse("increased")
