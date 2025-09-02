from django.shortcuts import render , redirect


def chatPage(request , *args , **kwags):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context = {}
    return render(request , 'chat/chatPage.html' , context)


