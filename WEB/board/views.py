from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BoardForm , CommentForm
from .models import Board, Hashtag, Comment

# Create your views here.

### 게시판관련
def boardlist(request):
        boards = Board.objects
        return render(request, 'board/boardlist.html', {'boards':boards})

def create(request):
    board = Board()
    board.title = request.GET['title']
    board.writer = request.GET['writer']
    board.content = request.GET['content']
    board.stat = request.GET['stat']
    board.hashtags = request.GET['hashtags']
    board.image = request.GET['image']
    board.date = timezone.datetime.now()
    board.save()
    return redirect('board:boardlist')

def boardform(request, board=None):
        user = request.user.nickname
        if request.method == 'POST':
                form = BoardForm(request.POST, request.FILES, instance=board)
                if form.is_valid():
                        board = form.save(commit=False)
                        board.title = form.cleaned_data['title']
                        board.writer = user
                        board.content = form.cleaned_data['content']
                        board.stat = form.cleaned_data['stat']
                        board.date = timezone.now()
                        board.save()
                        form.save_m2m()
                        return redirect('board:boardlist')
        else:
                form = BoardForm(instance=board)
                return render(request, 'board/new.html', {'form':form})

def edit(request, pk):
        board = get_object_or_404(Board, pk=pk)
        return boardform(request, board)

def remove(request, pk):
        board = get_object_or_404(Board, pk=pk)
        board.delete()
        return redirect('board:boardlist')


def detail(request, pk):
        board = get_object_or_404(Board, pk=pk)
        if request .method == "POST":
                form = CommentForm(request .POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.Board_pk= board
                        comment.comment_text = form.cleaned_data["comment_text"]
                        comment.c_date = timezone.now()
                        comment.save()
                        return redirect('board:detail', pk)
        else:
                form = CommentForm()
                return render(request, 'board/detail.html', {'form':form,'board':board})

def comment_delete(request, board_id, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        return redirect('board:detail',board_id)
##모바일 관련
def Mboard(request):
        return render(request, 'board/Mboardlist.html')