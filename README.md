API Endpoints
======

Running the API locally

1. All API calls are AJAX calls. 
2. Once you've installed Django and pulled the latest repo to run the Django Server and make API calls use, 
```
		$ python manage.py runserver  
```
3. Use whatever the base_URL the runserver gives you and then add the "/api/..." to the end of it to make the calls. 


User 
======
fields: Email, Password, Name, u_id

1. Create New User

```
	URL : api/user/ 
	Type : POST
	Parameters: first_name, last_name, email 
	Sample Response: 
		{"first_name": "Sasha", "last_name": "Azad", "user_id": 1, "email": "sasha172@gmail.com", "projects_worked_on": []}
```

2. Delete User

3. Update User

4. Login (IMPORTANT)

5. Logout

6. Get User

```
	URL : api/user/<user_id>/
	Type : GET
	Sample Response: 
		{"first_name": "Shweta", "last_name": "Raje", "user_id": 3, "email": "sraje@gatech.edu", "projects_worked_on": []}
```


Project 
======

fields: project_title, created_by_user, document_body

- Create New Project 
```
	URL : api/project/
	Type : POST
	Param : project_title, created_by_user, document_body 
	Sample Response: 
		{"project_id": 2, 
		"document_body": "This is old", 
		"project_title": "Yet Another Project", 
		"created_by_user": 1}
```

- Get Project
```
	URL : api/project/{project_id}/
	Type : GET
	Sample Response: 
		{"project_id": 2, "document_body": "This is old", "project_title": "Yet Another Project", "created_by_user": 1}
```

- Update Project
Note: Any field that shouldn't be changed should be sent in the params as an empty string
```
	URL : api/project/1/
	Type : POST
	Param : project_title, created_by_user, document_body 
	Sample Response: 
		{"project_id": 1, "document_body": "This is new", "project_title": "New Project Changed", "created_by_user": 1}
```

- Get Question History

```
	URL: api/project/<project_id>/history/
	Type: GET
	Sample Response: 
		[{"question_text": "How do pinecones work?", "from_project_id": 1, "question_id": 1}, 
		{"question_text": "What is osmosis?", "from_project_id": 1, "question_id": 2}]
```

- Delete Project 
```
	URL: api/project/delete/
	Type: POST
	Parameters: project_id
	Sample Response: {success:true}

```

Research Paper 
======
fields : r_id, title, main text, references, qid, uid, reference_style

- New Research Paper  (IMPORTANT)
```
Note : Check the "Create New Project" API call in Projects
```

- Update Research Paper with user typed content (Save) 
```
Note : Check the "Update Project" API call in Projects
```

- Delete Research Paper 
```
Note : Check the "Delete Project" API call in Projects
```

- Update Research Paper with References 


- Add Reference (IMPORTANT)
```
Note : Check the "Create new reference paper" API call in Reference Papers
```

- Delete Referecnce (IMPORTANT)
```
Note : Check the "Delete reference from project" API call in Reference Papers
```

5. Update Research Paper with content from studies


Reference Papers 
======
evidence_text, paper_title, paper_author, paper_link, referenced_by_project, question_id, paper_id


- Create new reference paper
```
	URL : api/reference/
	Parameters : evidence_text, paper_title, paper_author, paper_link, project_id, question_id
	Type : POST
	Sample Response: {success:true}
	
```

- Get References for Project
```
	URL : api/reference/<project_id>/
	Type : GET
	Sample Response: 
	[{"fields": {
		"evidence_text": "hello world", 
		"referenced_by_project": [1], 
		"paper_link": "Another Link", 	
		"paper_author": "Sasha Azad", 
		"paper_title": "Another Paper", 
		"question_id": 2}, 
		"model": "jill_server.ccreferencepapers", 
		"pk": 10}]
```

- Delete Reference from Project
```
	URL: api/reference/
	Type: POST
	Parameters: post_type="DELETE", reference_id
	Sample Response: {success:true}

```

Questions
======
fields : q_id, question text, keywords, context, date, uid 

- Create new question 

```
	URL : api/question/
	Parameters : question_text
	Type : POST
	Sample Response: 
		{
			"evidences": [
				{
					"evidence_text": "In the Mediterranean Basin, species suffer from unfavorable conditions such as recurrent forest fir", 
					"documentPath": "", 
					"trimmed_document": "https://watson-wdc01.ihost.com/instance/522/deepqa/v1/question/document/T_62088F95193880395F6AC70EBBB72B20/0/-1", 
					"paper_title": "Moya Pine Cone 2008 1286492597676 : Anatomic basis and insulation of serotinous cones in Pinus halep", 
					"originalFile": "Moya_Pine_Cone_2008_1286492597676.docx"
				},
		]}
```

- Find old question by qid 
```
Note : Check the "Get Question History" API call in Projects
```

- Find all questions from uid
```
Not needed???
```



OTHER (Ignore)
------ 
Format of API Calls: 
```
	URL: 
	Type: 
	Parameters: 
	Sample Response: 

```
