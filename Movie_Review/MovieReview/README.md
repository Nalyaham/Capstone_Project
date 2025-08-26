This project, called Movie_Review, is made one application called Review 
In this application there are two models namely 
i) Review model 
ii)  CustomUser model 

a) The review model defines the attributes that each review will have 
b) The CustomUser model extend AbstractUser class to include email as an attribute of the user. The CustomUser model is set as the User model that the project will utilise

This application handles user management, review submission, update, deletion, display and search 
a) User management:
This is implemented by;
1. Register form to handle form data from a user 
2. RegisterView to save a user's information into the system 

b) Review Submitting 
This is implemented by;
1. Submit_review which uses ReviewForm to handle form data to create a review 
2. Login decorator is implemented for higher authentication

c) Deleting reveiw 
This is implemented by;
1. delete_review which uses ReviewForm to handle form data from user. This view deletes information requested by the user
2. get_object_or_404 is used to permitt users to delete their own reviews
3. Login decorator is implemented for higher authentication

c) Updating reveiw 
This is implemented by;
1. update_review which uses ReviewForm to handle form data from user. This view updates information requested by the user
2. get_object_or_404 is used to permitt users to delete their own reviews
3. Login decorator is implemented for higher authentication

c) Listing reveiws
This is implemented by;
1. ReviewView which uses ReviewSerializer to handle API requests from user. This view lists paginated information requested by the user 
2. StandardResultsSetPagination pagination class is used to paginate the results of the list information 

d)Searching Views
This is implemented by;
1. Information retrieved from the Review table 
2. A search filter is utilised in order to filter the search by Rating and Movie_title 

