def books():
    return dict(features = db(db.products.type == 'Book').select())

def videos():
#    return dict(features = db(db.products.type == 'Blu-Ray').select())
    return dict()