from django.shortcuts import render
from .models import schedule, task, assessment_sheet


def get_schedule(request):
    event_list = schedule.objects.all()
    context = {
        'object_list': event_list,
    }
    return render(request, 'education/schedule.html', context)


def get_tasks(request):
    task_list = task.objects.all()
    context = {
        'object_list': task_list,
    }
    return render(request, 'education/task.html', context)

def get_assessment_sheet(request):
    assessment_sheet_list = assessment_sheet.objects.all()
    context = {
        'object_list': assessment_sheet_list,
    }
    return render(request, 'education/assessment_sheet_list.html', context)
