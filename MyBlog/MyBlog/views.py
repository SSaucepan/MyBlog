from django.shortcuts import render


def index(request):
    '''首页'''
    return render(request, 'index.html')

def index11(request):
    '''首页'''
    return render(request, 'index_1.html')


def blog_list(request):
    '''博客列表'''
    return render(request, 'list.html')


def about_me(request):
    '''关于我'''
    return render(request, 'about.html')


if __name__ == '__main__':
    pass