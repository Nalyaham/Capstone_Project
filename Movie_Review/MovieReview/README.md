This project, called Movie_Review, is made one application called Review 
In this application there are two models namely 
i) Review model 
ii)  CustomUser model 

a) The review model defines the attributes that each review will have 
b) The CustomUser model extend AbstractUser class to include email as an attribute of the user. The CustomUser model is set as the User model that the project will utilise

This application handles user management, review submission, update, deletion, display and search 
a) User management:
This is implemented by;
1. Token Retrival 
2. Registration View 
To register a user:
- Use the link http://localhost:8000/api/v1/reviews/register/
- The JSON is as below;
{
    "email": "mich234@alx.com"
}


b) Submitting a review
To submit a review;
- Use the link link http://localhost:8000/api/v1/reviews/submit/
- The JSON is as below;
{
    "user": mih123,
    "Rating": 4,
    "Movie_title": "Rango",
    "Review_Content": "Wonderful"
}

c) Deleting reveiw 
This is implemented by;
1. delete_review which uses ReviewForm to handle form data from user. This view deletes information requested by the user
2. get_object_or_404 is used to permitt users to delete their own reviews
3. Login decorator is implemented for higher authentication

c) Updating reveiw 
To update a review 
- Use the link http://127.0.0.1:8000/api/v1/reviews/reviews/3/update/
- The JSON is as below for the user of the pk=3
{
    "user": mih123,
    "Rating": 4,
    "Movie_title": "Man Hunter",
    "Review_Content": "Wonder"
}

c) Listing reveiws
This is implemented by;
1. ReviewView which uses ReviewSerializer to handle API requests from user. This view lists paginated information requested by the user 
2. StandardResultsSetPagination pagination class is used to paginate the results of the list information 

d)Searching Views
This is implemented by;
1. Information retrieved from the Review table 
2. A search filter is utilised in order to filter the search by Rating and Movie_title 

