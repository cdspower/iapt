#@IAPT: Here the controller is returning a dictionary that contains all of the rows from the query.
#@IAPT: Practical 3 - replaced the "books" with "results" to use the subview created.
def books():
    product_id = request.args(0)
    if product_id is not None:
        return dict(results = db((db.products.format == 'Book') & (db.products.id == product_id)).select())
    else:
        return dict(results = db(db.products.format == 'Book').select())

#@IAPT: Practical 3 - replaced the empty with "results" to use the subview created and removed the data request from the corresponding view file
#from Practical 2.
def videos():
    product_id = request.args(0)
    if product_id is not None:
        return dict(results = db((db.products.format == 'Blu-Ray') & (db.products.id == product_id)).select())
    else:
        return dict(results = db(db.products.format == 'Blu-Ray').select())
