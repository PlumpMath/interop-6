# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        pt = orm.ProjectType()
        pt.name = "Collections"
        pt.save()

        pt = orm.ProjectType()
        pt.name = "Ontologies & Schemas"
        pt.save()

        pt = orm.ProjectType()
        pt.name = "Apps"
        pt.save()

        pt = orm.ProjectType()
        pt.name = "Tools & Services"
        pt.save()
                
    def backwards(self, orm):
        for project_type in orm.ProjectType.objects.all():
            project_type.delete()

    models = {
        'project_types.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['project_types']
    symmetrical = True
