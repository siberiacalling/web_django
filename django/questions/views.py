import random

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response


def paginate(objects_list, request, amount_objects_on_page):
    paginator = Paginator(objects_list, amount_objects_on_page)

    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)
    return objects_page


def home_page(request):
    question_list = generate_question_list(30)
    questions = paginate(question_list, request, 5)
    return render_to_response('questions/hot_list.html', {"questions": questions})


def hot(request):
    question_list = generate_question_list(30)
    questions = paginate(question_list, request, 5)
    return render_to_response('questions/hot_list.html', {"questions": questions})


def ask(request):
    return render(request, 'questions/ask.html', {})


def signup(request):
    return render(request, 'questions/signup.html', {})


def login(request):
    return render(request, 'questions/login.html', {})


def one_question(request):
    question = generate_question()

    answers_list = generate_answers_list(15)
    answers = paginate(answers_list, request, 5)

    return render_to_response('questions/question.html', {"question": question, "answers": answers})
   # return render(request, 'questions/question.html', context=data)


def tag(request):
    data = generate_question_list(3)
    question_list = {"question_list": data}
    return render(request, 'questions/tag.html', context=question_list)


def settings(request):
    return render(request, 'questions/settings.html', {})


def generate_question_list(questions_amount):
    questions = []
    for i in range(1, questions_amount):
        tags = ['tag' + str(random.randint(1, 20)), 'tag' + str(random.randint(1, 20))]

        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'tags': tags,
            'text': 'text' + str(i),
            'rating': random.randint(1, 50),
            'answers_amount': random.randint(1, 15)

        })
    return questions


def generate_questions(questions_amount):
    questions = []
    for i in range(1, questions_amount):
        questions.append('title' + str(i))
    return questions


def generate_question():
    tags = ['tag' + str(random.randint(1, 20)), 'tag' + str(random.randint(1, 20))]
    i = random.randint(1, 50)
    question = {
        'title': 'title' + str(i),
        'id': i,
        'tags': tags,
        'text': 'text' + str(i),
        'rating': random.randint(1, 50),
        'answers_amount': random.randint(1, 15)
    }
    return question


def generate_answers_list(answers_amount):
    questions = []
    for i in range(answers_amount):
        questions.append({
            'title': 'answer' + str(i),
            'id': i,
            'text': 'text answer' + str(i),
            'rating': random.randint(1, 50),
        })
    return questions
