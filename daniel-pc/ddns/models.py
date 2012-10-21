from django.db import models


class IP(models.Model):
    IP = models.CharField(max_length=15)
    date = models.DateTimeField('date')

    def __unicode__(self):
        return u'%s @ %s' % (self.IP, self.date.ctime())

    class Meta:
        get_latest_by = "date"
