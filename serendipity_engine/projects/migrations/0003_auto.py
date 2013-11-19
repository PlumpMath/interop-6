# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field projects_interoperated_with on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_projects_interoperated_with')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_project', models.ForeignKey(orm['projects.project'], null=False)),
            ('to_project', models.ForeignKey(orm['projects.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_project_id', 'to_project_id'])


    def backwards(self, orm):
        # Removing M2M table for field projects_interoperated_with on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_projects_interoperated_with'))


    models = {
        'elements.element': {
            'Meta': {'object_name': 'Element'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'project_types.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'api': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'api_doc_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'classlist': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': "orm['units.Contributor']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'elements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': "orm['elements.Element']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'to': "orm['project_types.ProjectType']"}),
            'projects_interoperated_with': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects_interoperated_with_rel_+'", 'null': 'True', 'to': "orm['projects.Project']"}),
            'school': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['units.School']", 'symmetrical': 'False', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'units': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': "orm['units.Unit']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
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

    complete_apps = ['projects']