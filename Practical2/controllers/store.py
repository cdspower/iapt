#@IAPT: Here the controller is returning a dictionary that contains all of the rows from the query.
def books():
    return dict(books = db(db.products.format == 'Book').select())

#@IAPT: So here is a version which is MVC based where we are just returning control to the view
#This could be more advanced functionality, like committing changes from the user, doing intermediary
#calculations that the user needs or any number of things in the business logic of the application.
#It just happens that in this case, the controller doesn't have any business logic to execute.
def videos():
    return dict()
