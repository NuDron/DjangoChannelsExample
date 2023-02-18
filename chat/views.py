from django.shortcuts import render


def lobby(request):
    return render(request=request, template_name='chat/lobby.html', context={})
