# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

schools_dict = [
                  {'name': 'Harvard Business School',
                   'url': 'http://www.hbs.edu/'},
                  {'name': 'Division of Continuing Education',
                   'url': 'http://www.extension.harvard.edu/'},
                  {'name': 'Faculty of Arts & Sciences',
                   'url': 'http://fas.harvard.edu/'},
                  {'name': 'Graduate School of Design',
                   'url': 'http://www.gsd.harvard.edu/'},
                  {'name': 'Harvard Graduate School of Education',
                   'url': 'http://www.gse.harvard.edu/'},
                  {'name': 'Harvard Kennedy School',
                   'url': 'http://www.hks.harvard.edu/'},
                  {'name': 'Harvard Law School',
                   'url': 'http://www.law.harvard.edu/index.html'},
                  {'name': 'Harvard School of Public Health',
                   'url': 'http://www.hsph.harvard.edu/'},
                  {'name': 'Harvard College',
                   'url': 'http://college.harvard.edu/'},
                  {'name': 'Harvard School of Dental Medicine',
                   'url': 'http://www.hsdm.harvard.edu/'},
                  {'name': 'Harvard Divinity School',
                   'url': 'http://www.hds.harvard.edu/'},
                  {'name': 'School of Engineering and Applied Sciences',
                   'url': 'http://seas.harvard.edu/'},
                  {'name': 'Graduate School of Arts & Sciences',
                   'url': 'http://gsas.harvard.edu/'},
                  {'name': 'Harvard Medical School',
                   'url': 'http://hms.harvard.edu/'},
                  {'name': 'Radcliffe Institute for Advanced Study',
                   'url': 'http://radcliffe.harvard.edu/'},
                  {'name': 'Harvard College Library',
                   'url': 'http://hcl.harvard.edu/'},
               ]

class Migration(DataMigration):

    def forwards(self, orm):
        for school in schools_dict:
            s = orm.School()
            s.name = school['name']
            s.url = school['url']
            s.save()

    def backwards(self, orm):
        for school in schools_dict:
            school_obj = orm.School.objects.get(name=school['name'])
            school_obj.delete()

    models = {
        'units.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'units.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subunits': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'schools'", 'symmetrical': 'False', 'to': "orm['units.Unit']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'units.unit': {
            'Meta': {'object_name': 'Unit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['units']
    symmetrical = True
