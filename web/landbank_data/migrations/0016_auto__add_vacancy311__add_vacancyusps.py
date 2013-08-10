# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vacancy311'
        db.create_table(u'landbank_data_vacancy311', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_no', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('request_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('bldg_loc', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hazardous', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('boarded', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('entry_point', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('occupied', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('fire', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('in_use', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('houseno', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')()),
            ('loc', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=3435, null=True)),
            ('ward', self.gf('django.db.models.fields.IntegerField')()),
            ('policedistrict', self.gf('django.db.models.fields.IntegerField')()),
            ('ca_num', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('landbank_data', ['Vacancy311'])

        # Adding model 'VacancyUSPS'
        db.create_table(u'landbank_data_vacancyusps', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('quarter', self.gf('django.db.models.fields.IntegerField')()),
            ('fips', self.gf('django.db.models.fields.BigIntegerField')()),
            ('naddr_res', self.gf('django.db.models.fields.IntegerField')()),
            ('naddr_bus', self.gf('django.db.models.fields.IntegerField')()),
            ('naddr_oth', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vacant', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vacant', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_vacant', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vac_avg', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vac_avg', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vac_3', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vac_3', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_vac_3', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vac_3_6', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vac_3_6', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_vac_3_6', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vac_6_12', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vac_6_12', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_vac_6_12', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vac_12_24', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vac_12_24', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_vac_12_24', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vac_24_36', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vac_24_36', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_vac_24_36', self.gf('django.db.models.fields.IntegerField')()),
            ('res_vac_36', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_vac_36', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_vac_36', self.gf('django.db.models.fields.IntegerField')()),
            ('pqv_is_res', self.gf('django.db.models.fields.IntegerField')()),
            ('pqv_is_bus', self.gf('django.db.models.fields.IntegerField')()),
            ('pqv_is_oth', self.gf('django.db.models.fields.IntegerField')()),
            ('pqv_ns_res', self.gf('django.db.models.fields.IntegerField')()),
            ('pqv_ns_bus', self.gf('django.db.models.fields.IntegerField')()),
            ('pqv_ns_oth', self.gf('django.db.models.fields.IntegerField')()),
            ('res_nostat', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_nostat', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_nostat', self.gf('django.db.models.fields.IntegerField')()),
            ('res_ns_3', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ns_3', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_ns_3', self.gf('django.db.models.fields.IntegerField')()),
            ('res_ns_3_6', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ns_3_6', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_ns_3_6', self.gf('django.db.models.fields.IntegerField')()),
            ('res_ns_6_12', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ns_6_12', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_ns_6_12', self.gf('django.db.models.fields.IntegerField')()),
            ('res_ns_12_24', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ns_12_24', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_ns_12_24', self.gf('django.db.models.fields.IntegerField')()),
            ('res_ns_24_36', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ns_24_36', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_ns_24_36', self.gf('django.db.models.fields.IntegerField')()),
            ('res_ns_36', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ns_36', self.gf('django.db.models.fields.IntegerField')()),
            ('oth_ns_36', self.gf('django.db.models.fields.IntegerField')()),
            ('pqns_is_res', self.gf('django.db.models.fields.IntegerField')()),
            ('pqns_is_bus', self.gf('django.db.models.fields.IntegerField')()),
            ('pqns_is_oth', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('landbank_data', ['VacancyUSPS'])


    def backwards(self, orm):
        # Deleting model 'Vacancy311'
        db.delete_table(u'landbank_data_vacancy311')

        # Deleting model 'VacancyUSPS'
        db.delete_table(u'landbank_data_vacancyusps')


    models = {
        'landbank_data.assessor': {
            'Meta': {'object_name': 'Assessor'},
            'attic_desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'basement_desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'ca_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_num': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'chicago_flag': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'class_desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'current_building_assmt': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'current_land_assmt': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'current_total_assmt': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'estim_hunit': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ext_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'garage_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'gisdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'houseno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_y': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'loc': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3435', 'null': 'True'}),
            'long_x': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'no_tract_info': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['landbank_data.PropertyTypes']"}),
            'ptype_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'sqft_bldg': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'sqft_land': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'tract_fix': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'type_pt_2_4': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type_pt_5': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type_pt_condo': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type_pt_nonres': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type_pt_sf': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type_pt_unknown': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ward': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year_built': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'landbank_data.auction': {
            'Meta': {'object_name': 'Auction'},
            'addr_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'adj_yd': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'adj_yq': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'apt': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'buyer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'buyer_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_num': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'city_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date_doc': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_rec': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'doc': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'gisdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'houseno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_y': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'loc': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3435', 'null': 'True'}),
            'long_x': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'no_tract_info': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['landbank_data.PropertyTypes']"}),
            'reo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'residential': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seller': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'seller_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'tract_fix': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'yeard': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'yq_doc': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'landbank_data.cashfin': {
            'Meta': {'object_name': 'CashFin'},
            'addr_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'amount_prime': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'apt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'buyer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'buyer_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_num': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'city_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date_doc': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_rec': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'doc': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'gisdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'houseno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_y': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'likely_cash': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'likely_distressed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'loc': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3435', 'null': 'True'}),
            'long_x': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'no_tract_info': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['landbank_data.PropertyTypes']"}),
            'residential': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seller': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'seller_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'tract_fix': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'landbank_data.censustract': {
            'Meta': {'object_name': 'CensusTract'},
            'commarea': ('django.db.models.fields.IntegerField', [], {}),
            'fips': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3435'})
        },
        'landbank_data.communityarea': {
            'Meta': {'object_name': 'CommunityArea'},
            'area_name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'area_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3435'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'shape_len': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        'landbank_data.foreclosure': {
            'Meta': {'object_name': 'Foreclosure'},
            'addr_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'adj_yd': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'adj_yq': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'apt': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'ca_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_num': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'case_num1': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'case_num2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'case_num3': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'city_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date_doc': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_rec': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'defendant_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'defendant_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'filing_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'gisdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'houseno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_y': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'loc': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3435', 'null': 'True'}),
            'long_x': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'no_tract_info': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'plaintiff': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['landbank_data.PropertyTypes']"}),
            'residential': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'tract_fix': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'yeard': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'yq_doc': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'landbank_data.mortgage': {
            'Meta': {'object_name': 'Mortgage'},
            'addr_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'adj_yd': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'adj_yq': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'apt': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'borrower1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'borrower1_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'ca_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_num': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'city_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date_doc': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_rec': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'doc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'gisdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'houseno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_y': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lender1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'lender1_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'lender2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'lender2_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'loc': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3435', 'null': 'True'}),
            'long_x': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'mort_amt': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'no_tract_info': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['landbank_data.PropertyTypes']"}),
            'residential': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'tract_fix': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'yeard': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'yq_doc': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'landbank_data.pinarealookup': {
            'Meta': {'object_name': 'PinAreaLookup'},
            'census_tract_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'community_area_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'ward_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'})
        },
        'landbank_data.propertytypes': {
            'Meta': {'object_name': 'PropertyTypes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_desc': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        'landbank_data.scavenger': {
            'Meta': {'object_name': 'Scavenger'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'db_index': 'True'}),
            'tax_amount': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'tax_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'total_amount': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'township': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'})
        },
        'landbank_data.summarystats': {
            'Meta': {'object_name': 'SummaryStats'},
            'area_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'area_number': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'bldg_assmt_avg': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'bldg_sqft_avg': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land_assmt_avg': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'land_sqft_avg': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'ppsf_avg': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['landbank_data.PropertyTypes']"}),
            'total_assmt_avg': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        'landbank_data.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'addr_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'adj_yd': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'adj_yq': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'amount_prime': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'apt': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'business_buyer': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'buyer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'buyer_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'ca_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ca_num': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'city_final': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date_doc': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_rec': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'doc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'gisdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'houseno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_y': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'loc': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3435', 'null': 'True'}),
            'long_x': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'no_tract_info': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'non_condo': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '14', 'db_index': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ptype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['landbank_data.PropertyTypes']"}),
            'purchase_less_20k': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'residential': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seller': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'seller_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'tract_fix': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'yeard': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'yq_doc': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'landbank_data.vacancy311': {
            'Meta': {'object_name': 'Vacancy311'},
            'bldg_loc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'boarded': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ca_num': ('django.db.models.fields.IntegerField', [], {}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'entry_point': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'fire': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'hazardous': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'houseno': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_use': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'loc': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3435', 'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'occupied': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'policedistrict': ('django.db.models.fields.IntegerField', [], {}),
            'request_date': ('django.db.models.fields.DateTimeField', [], {}),
            'request_no': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ward': ('django.db.models.fields.IntegerField', [], {}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {})
        },
        'landbank_data.vacancyusps': {
            'Meta': {'object_name': 'VacancyUSPS'},
            'bus_nostat': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ns_12_24': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ns_24_36': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ns_3': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ns_36': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ns_3_6': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ns_6_12': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vac_12_24': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vac_24_36': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vac_3': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vac_36': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vac_3_6': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vac_6_12': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vac_avg': ('django.db.models.fields.IntegerField', [], {}),
            'bus_vacant': ('django.db.models.fields.IntegerField', [], {}),
            'fips': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naddr_bus': ('django.db.models.fields.IntegerField', [], {}),
            'naddr_oth': ('django.db.models.fields.IntegerField', [], {}),
            'naddr_res': ('django.db.models.fields.IntegerField', [], {}),
            'oth_nostat': ('django.db.models.fields.IntegerField', [], {}),
            'oth_ns_12_24': ('django.db.models.fields.IntegerField', [], {}),
            'oth_ns_24_36': ('django.db.models.fields.IntegerField', [], {}),
            'oth_ns_3': ('django.db.models.fields.IntegerField', [], {}),
            'oth_ns_36': ('django.db.models.fields.IntegerField', [], {}),
            'oth_ns_3_6': ('django.db.models.fields.IntegerField', [], {}),
            'oth_ns_6_12': ('django.db.models.fields.IntegerField', [], {}),
            'oth_vac_12_24': ('django.db.models.fields.IntegerField', [], {}),
            'oth_vac_24_36': ('django.db.models.fields.IntegerField', [], {}),
            'oth_vac_3': ('django.db.models.fields.IntegerField', [], {}),
            'oth_vac_36': ('django.db.models.fields.IntegerField', [], {}),
            'oth_vac_3_6': ('django.db.models.fields.IntegerField', [], {}),
            'oth_vac_6_12': ('django.db.models.fields.IntegerField', [], {}),
            'oth_vacant': ('django.db.models.fields.IntegerField', [], {}),
            'pqns_is_bus': ('django.db.models.fields.IntegerField', [], {}),
            'pqns_is_oth': ('django.db.models.fields.IntegerField', [], {}),
            'pqns_is_res': ('django.db.models.fields.IntegerField', [], {}),
            'pqv_is_bus': ('django.db.models.fields.IntegerField', [], {}),
            'pqv_is_oth': ('django.db.models.fields.IntegerField', [], {}),
            'pqv_is_res': ('django.db.models.fields.IntegerField', [], {}),
            'pqv_ns_bus': ('django.db.models.fields.IntegerField', [], {}),
            'pqv_ns_oth': ('django.db.models.fields.IntegerField', [], {}),
            'pqv_ns_res': ('django.db.models.fields.IntegerField', [], {}),
            'quarter': ('django.db.models.fields.IntegerField', [], {}),
            'res_nostat': ('django.db.models.fields.IntegerField', [], {}),
            'res_ns_12_24': ('django.db.models.fields.IntegerField', [], {}),
            'res_ns_24_36': ('django.db.models.fields.IntegerField', [], {}),
            'res_ns_3': ('django.db.models.fields.IntegerField', [], {}),
            'res_ns_36': ('django.db.models.fields.IntegerField', [], {}),
            'res_ns_3_6': ('django.db.models.fields.IntegerField', [], {}),
            'res_ns_6_12': ('django.db.models.fields.IntegerField', [], {}),
            'res_vac_12_24': ('django.db.models.fields.IntegerField', [], {}),
            'res_vac_24_36': ('django.db.models.fields.IntegerField', [], {}),
            'res_vac_3': ('django.db.models.fields.IntegerField', [], {}),
            'res_vac_36': ('django.db.models.fields.IntegerField', [], {}),
            'res_vac_3_6': ('django.db.models.fields.IntegerField', [], {}),
            'res_vac_6_12': ('django.db.models.fields.IntegerField', [], {}),
            'res_vac_avg': ('django.db.models.fields.IntegerField', [], {}),
            'res_vacant': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'landbank_data.ward': {
            'Meta': {'object_name': 'Ward'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '39', 'null': 'True'}),
            'alderman': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'data_admin': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'edit_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3435'}),
            'hall_office': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True'}),
            'hall_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perimeter': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'shape_len': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'ward': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ward_class': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ward_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'})
        }
    }

    complete_apps = ['landbank_data']