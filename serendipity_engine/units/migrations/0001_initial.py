# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unit'
        db.create_table(u'units_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'units', ['Unit'])

        # Adding model 'School'
        db.create_table(u'units_school', (
            (u'unit_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['units.Unit'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'units', ['School'])

        # Adding M2M table for field subunits on 'School'
        m2m_table_name = db.shorten_name(u'units_school_subunits')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('school', models.ForeignKey(orm[u'units.school'], null=False)),
            ('unit', models.ForeignKey(orm[u'units.unit'], null=False))
        ))
        db.create_unique(m2m_table_name, ['school_id', 'unit_id'])

        # Adding model 'Contributor'
        db.create_table(u'units_contributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'units', ['Contributor'])


    def backwards(self, orm):
        # Deleting model 'Unit'
        db.delete_table(u'units_unit')

        # Deleting model 'School'
        db.delete_table(u'units_school')

        # Removing M2M table for field subunits on 'School'
        db.delete_table(db.shorten_name(u'units_school_subunits'))

        # Deleting model 'Contributor'
        db.delete_table(u'units_contributor')


    models = {
        u'units.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'units.school': {
            'Meta': {'object_name': 'School', '_ormbases': [u'units.Unit']},
            'subunits': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'schools'", 'symmetrical': 'False', 'to': u"orm['units.Unit']"}),
            u'unit_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['units.Unit']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'units.unit': {
            'Meta': {'object_name': 'Unit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['units']