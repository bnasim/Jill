
# Common Imports for all Manager Files 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

# Other Imports
from ..models import CCUser, CCQuestion, CCAnswer, CCReferencePapers, CCProjects

@csrf_exempt
def projectRequest(request, project_id=None):
	if request.method == "POST":
		if project_id is None:
			return createProject(request)
		else:
			return updateProject(request,project_id)
	else:
		return getProject(request, project_id)


@csrf_exempt
def deleteProject(request):
	project_id =  request.POST.get('project_id','')
	instance = CCProjects.objects.filter(id=project_id)
	
	if len(instance) == 0:
		# Ref. Paper exists! Edit the evidence text showing to point to the new evidence text?
		errorMessage = "Error! No such project exists."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")	

	instance.delete()	
	return HttpResponse(json.dumps({'success': True}), content_type="application/json")	


def createProject(request):
	project_title = request.POST.get('project_title','')
	created_by_user = request.POST.get('created_by_user','')
	document_body = request.POST.get('document_body','')

	project = None

	user = CCUser.objects.filter(id=created_by_user)
	if len(user)==0:
		errorMessage = "Error! This user doesn't exist. Your session has expired. Login again"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	existing_projects = CCProjects.objects.filter(project_title=project_title).filter(created_by_user = user[0])

	if len(existing_projects) > 0:
		# Project Exists!
		project = existing_projects[0]
		errorMessage = "Error! You have already created this project."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if project is None:
		project = CCProjects()

	project.created_by_user = user[0]
	project.project_title = project_title
	project.document_body = document_body
	
	project.save()

	response_data = project.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


def updateProject(request, project_id=None):
	
	project_title = request.POST.get('project_title','')
	created_by_user = request.POST.get('created_by_user','')
	document_body = request.POST.get('document_body','')

	project = None

	user = CCUser.objects.filter(id=created_by_user)
	if len(user) == 0:
		errorMessage = "Error! This user doesn't exist. Your session has expired. Login again"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	existing_projects = CCProjects.objects.filter(id=project_id).filter(created_by_user = user[0])

	project = None
	if len(existing_projects) > 0:
		#Project Exists!
		project = existing_projects[0]
		if project_title != "":
			project.project_title = project_title
		if document_body != "":
			project.document_body = document_body
		project.save()

	if project == None:
		errorMessage = "Error! This project doesn't exist!"
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")


	response_data = project.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


def getProject(request, project_id=None):
	response_data = {}
	if project_id:
		projects = CCProjects.objects.filter(id=project_id)
		#Ideally there shouldn't be duplicate users.


		if len(projects)>0:
			project = projects[0]
			response_data = project.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


def getProjectHistory(request, project_id=None):
	response_data = []
	# project_id = request.POST.get('project_id','')

	if project_id != '':
		questions = CCQuestion.objects.filter(from_project_id=project_id)

		if len(questions) == 0:
			errorMessage = "Error! No questions have been asked in this project yet."
			return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")
		
		for eachQuestion in questions: 
			response_data.append(eachQuestion.getResponseData())
			
	return HttpResponse(json.dumps(response_data), content_type="application/json")








