This project, called Movie_Review, is made one application called Review 
In this application there are two models namely 
i) Review model 
ii)  CustomUser model 

a) The review model defines the attributes that each review will have 
b) The CustomUser model extend AbstractUser class to include email as an attribute of the user. The CustomUser model is set as the User model that the project will utilise

This application handles user management, review submission, update, deletion, display and search 
a) User management:
This is implemented by;
1. Registration View 
To register a user:
- Use the link http://localhost:8000/api/v1/reviews/register/
- The JSON is as below;
{
    "email": "mich25@alx.com"
}


b) Submitting a review
To submit a review;
- Use the link link http://localhost:8000/api/v1/reviews/submit/
- The JSON is as below;
{
    "user": 5,
    "Rating": 4,
    "Movie_title": "Rango",
    "Review_Content": "Wonderful"
}

c) Deleting reveiw 
To delete a review;
- obtain the primary key of the review you want to delete 
- Then use the url link http://localhost:8000/api/v1/reviews/reviews/13/delete/

d) Updating reveiw 
To update a review 
- Obtain the primary key of the review you want to update
- Use the link http://localhost:8000/api/v1/reviews/reviews/13/update/
- The JSON is as below for the user of the pk=3
{
    "user": 5,
    "Rating": 4,
    "Movie_title": "Man Hunter",
    "Review_Content": "Wonder"
}

c) Listing reveiws
To list the reviews;  
- Use the url link http://localhost:8000/api/v1/reviews/reviews/


