from google.appengine.ext import ndb


class Version(ndb.Model):
    version = ndb.IntegerProperty()
    bucket_path = ndb.StringProperty()

    @classmethod
    def latest(cls):
        latest = cls.query().order(-cls.version).get()
        if not latest:
            latest = Version(version=1, bucket_path='')
        return latest
