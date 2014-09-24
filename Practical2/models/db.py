# @IAPT: Begin by connecting to the database - if you don't have one named store.db in the databases directory, then
# you will automatically have one created for you
db = DAL('sqlite://store.db')

# @IAPT: Now we need to define a simple set of tables.  There are two tables - 1 for the products, and 1 for the
# features.  The field 'id' will be automatically added to the table as a primary key.  If you want some other field
# to be primary key there are ways to overrride that.  See the Web2Py book for details on how to do that.
db.define_table('products', Field('name'), Field('price'), Field('type'), Field('description'), Field('publisher'), migrate = False)

# @IAPT: For the features we are going to set up a foreign key.  Now, remember that a foreign key equates to a 1-many
# relationship in our data model, so we will simply refer to the table that we want to match things to.  Web2Py will
# then automatically set up the foreign key for us.  Pretty simple.
db.define_table('features', Field('product_id', db.products), migrate = False)

# @IAPT: After running your website 1 time, you will automatically have created the above two tables that are empty
# of data.  Be aware - once you start modifying stuff - it can go very wrong.  Migrations will happen automatically,
# and there are several "gotchas" that are documented in the Data Abstraction Layer of Web2Py you should be aware
# of for working with SQLite.
