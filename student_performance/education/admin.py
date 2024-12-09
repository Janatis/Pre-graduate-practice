from django.contrib import admin
from education.models import position, academic_degree, teacher, event_type, student, schedule, code_programm, subject_classification, task_type, task, subject, education_programm, status_check, result_file, assessment_sheet


admin.site.register(position)
admin.site.register(academic_degree)
admin.site.register(event_type)
admin.site.register(student)
admin.site.register(schedule)
admin.site.register(code_programm)
admin.site.register(subject_classification)
admin.site.register(task_type)
admin.site.register(task)
admin.site.register(subject)
admin.site.register(education_programm)
admin.site.register(status_check)
admin.site.register(result_file)
admin.site.register(assessment_sheet)
admin.site.register(teacher)
