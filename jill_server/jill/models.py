from django.db import models

# Create your models here.

# Table for Users
class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)

	def __unicode__(self):
		return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["first_name"] = self.first_name
		response_data["last_name"] = self.last_name
		response_data["email"] = self.email
		response_data["user_id"] = self.id
        
		# questions_asked = Question.objects.filter(asked_by_user=self.id)
		# response_questions = []

		# if questions_asked and len(questions_asked) > 0:
		#     for ques in questions_asked:
		#         response_questions.append(ques.getResponseData())

		# response_data["questions_asked"] = response_questions

		projects_worked_on = []

		projects = Projects.objects.filter(created_by_user=self.id)
		if projects and len(projects) > 0:
			for proj in projects:
				projects_worked_on.append(proj.getResponseData())

		response_data["projects_worked_on"] = projects_worked_on

		return response_data


# Table for Questions asked to Watson
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	evidence_list = models.ForeignKey('ReferencePapers')
	answers = models.ForeignKey('Answer')
	asked_by_user = models.ForeignKey('User', related_name="asked_by_user")
	from_project_id = models.ForeignKey('Projects', related_name="from_project_id")

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["question_text"] = self.question_text
		response_data["asked_by_user"] = self.asked_by_user.id
		response_data["from_project_id"] = self.from_project_id.id
		response_data['question_id'] = self.id

		# response_data["answers"] = self.answers.id

		response_answers = []
		answers = Answer.objects.filter(question_id=self.id)

		if answers and len(answers)>0:
			for ans in answers: 
				response_answers.append(ans.getResponseData())

		response_data["answers"] = response_answers

		return response_data


# Table for Answers Obtained
class Answer(models.Model):
	answer_text =  models.CharField(max_length=200)
	confidence =  models.CharField(max_length=200)
	evidence_list = models.ForeignKey('ReferencePapers')
	question_id = models.ForeignKey('Question')

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["answer_text"] = self.answer_text
		response_data["confidence"] = self.confidence
		response_data["question_id"] = self.question_id.id
		response_data['answer_id'] = self.id

		response_evidence = []
		evidenceList = ReferencePapers.objects.filter(answer_id=self.id)

		if evidenceList and len(evidenceList)>0:
			for eachRef in evidenceList:
				response_evidence.append(eachRef.getResponseData())

		response_data["reference_papers"] = response_evidence

		return response_data


class ReferencePapers(models.Model):
	evidence_text =  models.CharField(max_length=200)
	paper_title =  models.CharField(max_length=200)
	paper_link =  models.CharField(max_length=200)
	answer_id = models.ForeignKey('Answer', related_name="answer_id")

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["evidence_text"] = self.evidence_text
		response_data["paper_title"] = self.paper_title
		response_data["paper_link"] = self.paper_link
		response_data["answer_id"] = self.answer_id.id
		response_data['paper_id'] = self.id

		return response_data

class Projects(models.Model):
	project_title = models.CharField(max_length=200)
	created_by_user = models.ForeignKey('User', related_name="created_by_user")

	def __unicode__(self):
	    return self.name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["project_title"] = self.project_title
		response_data["created_by_user"] = self.created_by_user
		response_data['project_id'] = self.id

		return response_data





