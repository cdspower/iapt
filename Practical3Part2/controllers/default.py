# -*- coding: utf-8 -*-

# @IAPT: This is a JOIN operation using contracted syntax of Web2Py.  See the Web2Py documentation for
#more complex JOIN notation that you might need for your own applications.
def index():
    #@IAPT: We return a dictionary that contains the results of the query - which is actually the two tables
    #matched up in the appropriate join - so we will need to be careful on the return to the view to specify
    #what tables we are looking for our data in.
    return dict(features=db(db.products.id==db.features.product_id).select())

def search():
    form=FORM('Search Products',
              INPUT(_name='search', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit'))
    if form.accepts(request,session):
        response.flash = 'Performing search for products containing the text: '+request.vars.search+'.'
    elif form.errors:
        response.flash = 'Your form is empty.  Please enter a name of a product to search the store.'
    else:
        response.flash = 'Please enter a name of a product to search the store.'

    if request.vars.search is not None:
        term="%"+request.vars.search+"%"
        results = db(db.products.name.like(term)).select()
    else:
        results = dict()
    return dict(form=form, results=results)