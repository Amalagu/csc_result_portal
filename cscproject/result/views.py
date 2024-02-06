from django.shortcuts import render
from django.http import HttpResponse
import os
from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd

from .forms import UploadFileForm
from decorators.account_decorators import advisor_required, student_required
from accounts.models import Student, User, Advisor
from result.models import RegisteredCourse, Result
from course.models import Course
from portal.models import Semester, Session
from result.api.serializers import ResultSerializer


























@student_required
def student_view_result(request):
    semesters = Semester.objects.all()
    sessions = Session.objects.all()
    current_session = Session.objects.filter(iscurrentsession=True).first()
    all_results = RegisteredCourse.objects.filter(result__student=request.user.student, result__session=current_session)

    context={
        'semesters' : semesters,
        'sessions' : sessions,
        'all_results' : all_results
    }
    
    if request.method == 'GET':
        session = request.GET.get('session', None)
        semester_name = request.GET.get('semester', None)
        requested_courses = RegisteredCourse.objects.filter(result__student=request.user.student, result__session=session)
        context['all_results'] = requested_courses
    return render(request, 'result/student-result-page.html', context)

@advisor_required
def advisor_view_result(request):
    semesters = Semester.objects.all()
    sessions = Session.objects.all()
    courses=Course.objects.filter( iselective=False)
    context={
        'courses' : courses,
        'semesters' : semesters,
        'sessions' : sessions
    }
    return render(request, "result/advisor-result-page.html", context)



@advisor_required
def view_all_courses_semester_result(request):
    return render(request, "result/advisor-semester-result-sheet.html")


@advisor_required
def view_cgpa_summary(request):
    return render(request, "result/advisor-cgpa-summary.html")

@advisor_required
def view_generated_transcript(request, pk=0):
    return render(request, "result/advisor-generated-transcript.html")


@advisor_required
def view_generated_transcript_list(request):
    return render(request, "result/advisor-list-generated-transcript.html")


@advisor_required
def view_single_course_result(request):
    semesters = Semester.objects.all()
    sessions = Session.objects.all()
    advisor = Advisor.objects.get(advisor=request.user)
    courses=Course.objects.filter()
    context={
        'courses' : courses,
        'semesters' : semesters,
        'sessions' : sessions
    }
    if request.method == 'GET':
        session_id = request.GET.get('session', None)
        semester_name = request.GET.get('semester', None)
        course_id = request.GET.get('course', None)
        if session_id is not None and semester_name is not None and course_id=='all':
            all_unique_registered_course=RegisteredCourse.objects.filter(
                semester__name=semester_name, 
                session__name=session_id, 
                student__student_class=advisor.advisor_class
                ).values(
                    'course__code', 
                    'course__unit',
                    'course__id').distinct()
            results = Result.objects.filter(semester__name=semester_name, session__name= session_id, student_class=advisor.advisor_class)
            serializer = ResultSerializer(results, many=True)
            context = {
                'data' : serializer.data,
                'all_unique_registered_course': all_unique_registered_course        
                       }
            #return JsonResponse(serializer.data, safe=False)
            return render(request, "result/advisor-semester-result-sheet.html", context)
        elif session_id is not None and semester_name is not None and course_id is not None:
            selected_course_result = RegisteredCourse.objects.filter(semester__name=semester_name, session__name= session_id, course__id=course_id, student__student_class=advisor.advisor_class)
            context["selected_course_result"] = selected_course_result
    return render(request, "result/advisor-single-course-result.html", context)




class pd():
    def read_excel(self):
        pass
    def read_csv(self):
        pass
    class df():
        def to_json(self):
            pass
        def iter_row(self):
            pass
def parsetoresultmodel(request):
    excel_file_path = 'Books.xlsx'
    df = pd.read_excel(excel_file_path, engine='openpyxl')

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Now you can use the JSON data as needed
    print(json_data)
    return  HttpResponse("Successful")



@advisor_required
def view_upload_result_page(request):
    return render(request, 'result/advisor-upload-result.html')



import traceback
import pandas as pd
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            file = request.FILES['excel_file']
            if file.name.endswith('.csv') or file.name.endswith('.xlsx'):
                # Read data using pandas
                if file.name.endswith('.csv'):
                    print('in CSV')
                    df = pd.read_csv(file)
                else:
                    df = pd.read_excel(file)
                if request.POST['type'] == 'Class list':
                    # Transform and save data
                    user_list = []
                    student_list = []

                    for index, row in df.iterrows():
                        #iterating through the rows in the file and saving the details
                        user = User(email=row['email'], first_name=row['first_name'], last_name=row['last_name'])
                        user.set_password('workings2020?')
                        user_list.append(user)

                        student = Student(student=user, registeration_number=row['registeration_number'])
                        student_list.append(student)

                    User.objects.bulk_create(user_list)
                    Student.objects.bulk_create(student_list)
                else: 
                    #if file type is Result sheet
                    course_registeration_list = []
                    course_id = int(request.POST['course_code'])     #HARDCODED COURSECODE TO BE MODIFIED LATER
                    updated_fields = ['testscore', 'examscore', 'labscore', 'examscore', 'grade', 'totalscore', 'remark']
                    for index, row in df.iterrows(): 
                        #iterating through the lines in the file and saving the details
                        try:
                            course_item= RegisteredCourse.objects.get(student_id=row['registeration_number'], course_id=course_id, session=request.POST['session'])
                            if row['testscore']:
                                course_item.testscore = row['testscore']
                            if row['labscore']:
                                course_item.labscore = row['labscore']
                            course_item.examscore = row['examscore']
                            course_item.totalscore = row['totalscore']
                            course_item.grade = row['grade']
                            course_item.remark = row['remark']
                            course_registeration_list.append(course_item)
                        except Exception:
                            traceback.print_exc()
                            print(Exception)
                            #print( f"Invalid file content at {index}")
                    RegisteredCourse.objects.bulk_update(course_registeration_list, updated_fields)
                    """{'csrfmiddlewaretoken': ['kUfLzQTCHuBxSUiK3g5j8ardoo8pUsqLiNtmHLdXXpMhdbalU6fUVUYh3VDirZpH'],
                      'file_title': ['Test File1'], 'type': ['Class list'], 'course_code': ['1'], 
                      'session': ['2022/2023'], 'semester': ['RAIN'], 'class_set': ['2022/2023']}"""


                return HttpResponse('success_page')  # Redirect to a success page
            else:
                form.add_error('file', 'Invalid file format. Please upload a CSV or Excel file.')
    else:
        form = UploadFileForm()

    return render(request, 'upload_file.html', {'form': form})




# Read Excel file into a Pandas DataFrame

