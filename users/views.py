from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def register_view(request):
    form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)
