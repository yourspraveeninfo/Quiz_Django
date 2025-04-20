from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Question, UserScore
from .forms import RegisterForm
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz')
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def quiz(request):
    if not request.user.is_authenticated:
        return redirect('login')

    questions = Question.objects.all()
    score = 0

    if request.method == "POST":
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option and int(selected_option) == question.correct_option:
                score += 1

        UserScore.objects.update_or_create(user=request.user, defaults={"score": score})
        return redirect('leaderboard')

    return render(request, "quiz.html", {"questions": questions})

def leaderboard(request):
    scores = UserScore.objects.all().order_by('-score')  # ✅ Correct field name
    return render(request, "leaderboard.html", {"scores": scores})

def logout_viewl(request):
    logout(request)
    return redirect('login')