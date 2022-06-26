# Recipe Testing App

## Base URL:

All endpoints begin with `https://bake-it-till-you-make-it.herokuapp.com/api/`

NOTE: API Root is /api/

| Method | Endpoint                                                           | Description                                 |
| ------ | ------------------------------------------------------------------ | ------------------------------------------- |
| POST   | [/users/](#create-a-new-user)                                      | Create a new user                           |
| POST   | [/auth/token/login/](#login-user)                                  | Login user (remove /api from url)           |
| GET    | [/users/me/](#users-info)                                          | User's info                                 |
| POST   | [/auth/token/logout/](#logout-user)                                | Logout user (remove /api from url)          |
| GET    | [/recipes/](#list-of-recipes-logged-in-user)                       | List all logged in user created recipes     |
| GET    | [/all_recipes/](#list-of-all-recipes)                              | List all recipes for all users              |
| GET    | [/all_recipes?search=<search_term>](#search-recipes)               | Search recipes (limited to one search term) |
| POST   | [/recipes/](#create-a-new-recipe-for-user)                         | Create a new recipe                         |
| GET    | [/recipes/{id}/](#details-for-a-specific-recipe)                   | Details for a specific recipe               |
| PUT    | [/recipes/{id}/](#update-an-existing-recipe)                       | Update an existing recipe                   |
| PATCH  | [/recipes/{id}/](#update-part-of-an-existing-recipe)               | Update part of an existing recipe           |
| PATCH  | [/recipes/{id}/](#add-a-tag-to-an-existing-recipe)                 | Add a tag to an existing recipe             |
| DELETE | [/recipes/{id}/](#delete-recipe)                                   | Delete an existing recipe                   |
| POST   | [/recipes/{id}/notes/](#create-a-new-note-for-a-recipe)            | Create a note for a recipe                  |
| GET    | [/recipes/{id}/notes/](#list-of-notes-for-a-recipe)                | List of notes for a recipe                  |
| GET    | [/all_notes?search=<search_term>](#search-notes)                   | Search notes (limited to one search term)   |
| PUT    | [/recipes/{id}/notes/{id}/](#update-an-existing-note-for-a-recipe) | Update a specific note for a recipe         |
| PATCH  | [/recipes/{id}/notes/{id}/](#update-part-of-a-specific-note)       | Update an existing note                     |
| DELETE | [/recipes/{id}/notes/{id}/](#delete-a-specific-note-of-a-recipe)   | Delete part of an existing note             |
| POST   | [/recipes/{id}/feedback/](#give-feedback-for-a-new-recipe)         | Give feedback for a new recipe              |


## Create a new user

### Request

Required fields: username and password

Optional fields: email, first_name, last_name, date_joined, location and business name

```json
POST /users/

{
	"username": "Eric",
	"password": "Momentum1"
}
```

### Response

Response: If you receive the same info you provided, user creation was successful!

```json
201 Created

{
	"id": 2,
	"username": "Eric",
	"email": "",
	"first_name": "",
	"last_name": "",
	"date_joined": "06/22/2022 15:29",
	"location": null,
	"business_name": null
}

```


## Login user

### Request

Required fields: username, password

```json
POST auth/token/login/

{
	"username": "Eric",
	"password": "Momentum1"
}
```

### Response

```json
200 OK

{
    "auth_token": "51cad4728f8f16eb7c953f240fd90d53d11bb1af"
}
```

NOTE: auth_token must be passed for all requests with the logged in user. It remains active till user is [logged out](#logout-user).


## User's info

Requirement: user must be logged in.

### Request

```json
GET /users/me/
```

### Response

```json
200 OK

{
	"id": 2,
	"username": "Eric",
	"email": "",
	"first_name": "",
	"last_name": "",
	"date_joined": "06/22/2022 10:31",
	"location": null,
	"business_name": null
}
```


## Logout user

### Request

Required fields: None

```json
POST /auth/token/logout/
```

### Response

```json
204 No Content
```


## List of recipes (logged in user)

Returns list of all recipes for a logged in user.

Requirement: user must be logged in.

### Request

```json
GET /recipes/
```

### Response

```json
200 OK

{
	"id": 1,
	"title": "Title Test",
	"ingredients": "Ingredients Test",
	"recipe_steps": "Recipe Test",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"created_at": "06/17/22 22:10",
	"tags": [],
	"notes": []
},
{
	"id": 2,
	"title": "cheesesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Eric",
	"created_at": "06/22/2022 15:45",
	"tags": [],
	"notes": []
}
```


## List of all recipes

Returns list of all recipes for all users. 

Requirement: user must be logged in.

### Request

```json
GET /recipes/
```

### Response

```json
200 OK

{
	"id": 1,
	"title": "Title Test",
	"ingredients": "Ingredients Test",
	"recipe_steps": "Recipe Test",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"created_at": "06/17/22 22:10",
	"tags": [],
	"notes": []
},
{
	"id": 2,
	"title": "cheesesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Eric",
	"created_at": "06/22/2022 15:45",
	"tags": [],
	"notes": []
},
{
	"id": 3,
	"title": "5 Item Brownies",
	"version_number": "1",
	"ingredients": "Flour, sugar, eggs, butter, and cocoa powder",
	"recipe_steps": "Melt some butter, stir in the sugar, eggs, flour, and cocoa powder and bake 'em... saavvvy?!",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Jack",
	"created_at": "06/25/2022 23:42",
	"tags": [],
	"notes": []
},
{
	"id": 4,
	"title": "3 item Sugar Cookies",
	"version_number": "1",
	"ingredients": "Unsalted butter, granulated sugar, and flour",
	"recipe_steps": "Make the dough: beat together butter, sugar, and flour until blended. Form the cookies: form the dough into 1-inch balls. Roll the balls in sugar, then flatten them with a glass or measuring cup.Bake: bake until just barely golden around the edges and bottom. Rest: let rest and cool for at least 10-15 minutes before eating.",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Jack",
	"created_at": "06/25/2022 23:39",
	"tags": [],
	"notes": []
}
```


## Search recipes

Search through recipes.

Requirement: user must be logged in.

### Request

Note: can only use 1 search parameter. It queries the title and ingredients fields.

```json
GET /all_recipes?search=cheesesteak
```

### Response

```json
200 OK

[
	{
		"id": 2,
		"title": "cheesesteak",
		"version_number": "1",
		"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
		"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
		"image": null,
		"ready_for_feedback": false,
		"successful_variation": false,
		"chef": "Eric",
		"created_at": "06/22/2022 15:45",
		"tags": [],
		"notes": []
	}
]
```


## Create a new recipe for user

Requirement: user must be logged in.

### Request

Required fields: title, version_number, ingredients,  recipe_steps and tags

```json
POST /recipes/

{
	"title": "cheesesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"tags": ["Burger"]
}
```

### Response

```json
201 Created

{
	"id": 2,
	"title": "cheesesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Eric",
	"created_at": "06/22/2022 15:45",
	"tags": [
		"cheesesteak"
	],
	"notes": []
}
```

If missing a required field, ex. tags:

```json
400 Bad Request

{
	"tags": [
		"This field is required."
	]
}
```

If anonymous / guest user attempts to POST:

```json
401 Unauthorized

{
	"detail": "Authentication credentials were not provided."
}
```


## Details for a specific recipe

Requirement: user must be logged in.

### Request

```json
GET /recipes/id/
```

### Response

Response for GET: id, title, version_number, ingredients, recipe_steps, image, ready_for_feedback, successful_variation, chef, created_at and
notes (if any). In the below example, there are no notes for this recipe.

```json
200 OK

{
	"id": 2,
	"title": "cheesesteak",
	"version_number": "1",
	"ingredients": "1 Italian Roll, your choice of meat (as much as you want)",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"image": null,
	"ready_for_feedback": false,
	"successful_variation": false,
	"chef": "Eric",
	"created_at": "06/22/2022 15:45",
	"tags": [
		"cheesesteak"
	],
	"notes": []
}
```


## Update an existing recipe

Requirement: user must be logged in.

### Request

Required fields: title, version_number, ingredients, and recipe_steps 

```json
PUT /recipes/id/

{
	"title": "cheesesteak!!",
	"version_number": "2",
	"ingredients": "1 Italian Roll, and MEAT nomz!!",
	"recipe_steps": "Fry up the meat n pop it in the roll.",
	"tags": [
		"cheesesteak yumz"
	],
}
```

### Response

```json
200 OK

{
	"id": 2,
	"title": "cheesesteak!!",
	"version_number": "2",
	"ingredients": "1 Italian Roll, and MEAT nomz!!",
	"recipe_steps": "Fry up the meat n pop it in the roll.",
	"chef": "Eric",
	"created_at": "06/22/2022 15:45",
	"tags": [
		"cheesesteak yumz"
		],
	"notes": []
}
```

If missing a required field, ex. ingredients:

```json
400 Bad Request

{
	"ingredients": [
		"This field is required."
	]
}
```

If a chef tries to edit another chef's recipe:

```json
403 Forbidden

{
	"detail": "Editing posts is restricted to the author only."
}
```


## Update part of an existing recipe

Requirement: user must be logged in.

### Request

Required fields: title and/or version_number and/or ingredients and/or recipe_steps

```json
PATCH /recipes/id/

{
	"ingredients": "1 Italian Roll, and any meat (or tofu if you want)!?!?",
}
```

### Response

```json
200 OK

{
	"id": 2,
	"title": "cheesesteak",
	"version_number": "2",
	"ingredients": "1 Italian Roll, and any meat (or tofu if you want)!?!?",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"chef": "Eric",
	"created_at": "6/22/2022 15:45",
	"tags": [
		"cheesesteak yumz"
	],
	"notes": []
}
```

If a chef tries to edit anoter chef's recipe:

```json
403 Forbidden

{
	"detail": "Editing posts is restricted to the author only."
}
```


## Add a tag to an existing recipe

Requirement: user must be logged in.

### Request

Required fields: tags 
Note: if adding a new tag, you MUST include the other tag(s) in the string (if any), otherwise only the newest tag will be added. 

```json
PATCH /recipes/id/

{
	"tags": ["cheesesteak yumz", "ChefEric"]
}
```

### Response

```json
200 OK

{
	"id": 2,
	"title": "cheesesteak",
	"version_number": "2",
	"ingredients": "1 Italian Roll, and any meat (or tofu if you want)!?!?",
	"recipe_steps": "Fry up the meat n pop it in the bread.. YUM!",
	"chef": "Eric",
	"created_at": "6/22/2022 15:45",
	"tags": [
		"cheesesteak yumz",
		"ChefEric"
	],
	"notes": []
}
```

If another logged in user attempts to add a tag to an existing recipe that is not theirs:
```json
404 Not Found

{
	"detail": "Editing posts is restricted to the author only."
}
```


## Delete Recipe

Requirement: user must be logged in. 

### Request

Required in URL: recipe's id.

```json
DELETE /recipes/id/
```

### Response

A successful deletion returns:

```json
204 No Content
```

If another logged in user attempts to delete a recipe that is not theirs:
```json
404 Not Found

{
	"detail": "Editing posts is restricted to the author only."
}
```

If anonymous / guest attempts to delete a recipe:
```json
401 Unauthorized

{
	"detail": "Authentication credentials were not provided."
}
```


## Create a new note for a recipe

Requirement: user must be logged in.

### Request

Required fields: recipe_version -> This number MUST match the recipes/id or it will post to another recipe's id (possible bug?)

Optional fields: note 

```json
POST /recipes/id/notes/

{
	"recipe_version": 1,
	"note": "Chezsteak so nomz!"
}
```

### Response

```json
201 Created

{
	"id": "1",
	"note": "Chezsteak so nomz!",
	"note_by": "Eric",
	"recipe_version": "1",
	"created_at": "06/23/2022 17:32"
}

```

## List of notes for a recipe

### Request

```json
GET /recipes/id/notes/
```

### Response

```json
200 OK

[
	{
		"id": 6,
		"note": "Yummish!",
		"note_by": "Eric",
		"recipe_version": 1,
		"created_at": "06/23/2022 23:20"
	},
	{
		"id": 5,
		"note": "The best!",
		"note_by": "Eric",
		"recipe_version": 1,
		"created_at": "06/23/2022 23:20"
	},
	{
		"id": 4,
		"note": "Nom nomz",
		"note_by": "Eric",
		"recipe_version": 1,
		"created_at": "06/23/2022 23:19"
	},
	{
		"id": 2,
		"note": "Love this recipe.",
		"note_by": "Eric",
		"recipe_version": 1,
		"created_at": "06/23/2022 23:03"
	},
	{
		"id": 1,
		"note": "Chezsteak so nomz!",
		"note_by": "Eric",
		"recipe_version": 1,
		"created_at": "06/23/2022 23:01"
	}
]
```


## Search notes

Search through notes.

Requirement: user must be logged in.

### Request

Note: can only use 1 search parameter. It queries the notes field.

```json
GET /all_notes?search=nom
```

### Response

```json
200 OK

[
	{
		"id": 4,
		"note": "Nom nomz",
		"note_by": "Eric",
		"recipe_version": 1,
		"created_at": "06/23/2022 23:19"
	},
	{
		"id": 1,
		"note": "Chezsteak so nomz!!",
		"note_by": "Eric",
		"recipe_version": 1,
		"created_at": "06/23/2022 23:01"
	}
]
```


## Update an existing note for a recipe

Requirement: user must be logged in.

### Request

Required fields: recipe_version and note*

```json
PUT /recipes/id/notes/id/

{
	"recipe_version": 1,
	"note": "Love this recipe.. DELISH!!"
}
```

### Response

```json
200 OK

{
	"id": 2,
	"note": "Love this recipe.. DELISH!!",
	"note_by": "Eric",
	"recipe_version": 1,
	"created_at": "06/23/2022 23:03"
}
```

If another user attempts to edit the original user's note:
```json
403 Forbidden

{
	"detail": "Editing posts is restricted to the author only."
}
```


## Update part of a specific note

Requirement: user must be logged in.

### Request

Required fields: recipe_version and/or note*

```json
PATCH /recipes/id/notes/id/

{
	"recipe_version": 1,
	"note": "SOO GOOD!!"
}
```

### Response

```json
200 OK

{
	"id": 6,
	"note": "SOO GOOD!!",
	"note_by": "Eric",
	"recipe_version": 1,
	"created_at": "06/23/2022 23:20"
}
```


## Delete a specific note of a recipe

Requirement: user must be logged in. 

### Request

Required in URL: recipe and note ids.

```json
DELETE /recipes/id/notes/id/
```

### Response

A successful deletion returns:

```json
204 No Content
```

If another logged in user attempts to delete a note that is not theirs:
```json
404 Not Found

{
	"detail": "Editing posts is restricted to the author only."
}
```

If anonymous / guest attempts to delete a note:
```json
401 Unauthorized

{
	"detail": "Authentication credentials were not provided."
}
```


## Give feedback for a new recipe 

Requirement: user must be logged in. 

### Request

Required fields: rating (options are: #' 1 to 5), saltiness, sweetness and portion (options are: Too Little, Just Right, Too Much), and texture (options are: Yes or No) 

Required in URL: recipe id.

```json
POST /recipes/id/feedback/

[
	{
		"rating": "4",
		"saltiness": "Too Little",
		"sweetness": "Just Right",
		"portion": "Just Right",
		"texture": "No",
		"additional_comment": "It's delish!",
	}
]
```

### Response

```json
[
	{
		"id": 1,
		"test_recipe": 2,
		"rating": "4",
		"saltiness": "Too Little",
		"sweetness": "Just Right",
		"portion": "Just Right",
		"texture": "No",
		"additional_comment": "It's delish!",
		"tester": "Eric",
		"created_at": "06/25/2022 22:30"
	}
]
```