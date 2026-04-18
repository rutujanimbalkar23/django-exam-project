from django.shortcuts import render, redirect
from .models import Question, Choice, Submission


# -----------------------------
# Submit Exam View
# -----------------------------
def submit_exam(request):
    if request.method == "POST":
        score = 0

        for question in Question.objects.all():
            selected_choice = request.POST.get(str(question.id))

            if selected_choice:
                try:
                    choice = Choice.objects.get(id=selected_choice)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

        Submission.objects.create(score=score)

        return redirect('show_exam_result', score=score)

    questions = Question.objects.all()
    return render(request, 'exam.html', {'questions': questions})


# -----------------------------
# Show Exam Result View
# -----------------------------
def show_exam_result(request, score):
    total = Question.objects.count()

    return render(request, 'result.html', {
        'score': score,
        'total': total
    })