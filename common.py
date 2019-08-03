from google.appengine.ext import ndb

class Common(ndb.Model):
	name = ndb.StringProperty()
	path = ndb.StringProperty()
	blob_key = ndb.BlobKeyProperty()
	host = ndb.StringProperty()
	client = ndb.StringProperty()
	size = ndb.StringProperty()
	time = ndb.StringProperty()
