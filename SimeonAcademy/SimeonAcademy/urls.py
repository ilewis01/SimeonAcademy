from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'assessment.views.index'), 
    url(r'^login/$', 'assessment.views.login'),   
    url(r'^logout/$', 'assessment.views.logout'),
    url(r'^newProfile/$', 'assessment.views.newProfile'),
    url(r'^auth/$', 'assessment.views.auth_view'),
    url(r'^invalid_login/$', 'assessment.views.invalid_login'),
    url(r'^index/$', 'assessment.views.index'),
    url(r'^adminHome/$', 'assessment.views.adminHome'),

   	##Client Views
    url(r'^clientHome/$', 'assessment.views.clientHome'),
    url(r'^client_appointment/$', 'assessment.views.client_appointment'),
    url(r'^client_documents/$', 'assessment.views.client_documents'),

    ## Admin client option pages
    url(r'^newClient/$', 'assessment.views.newClient'),
    url(r'^confirmNewClient/$', 'assessment.views.confirmNewClient'),
    url(r'^clientCreated/$', 'assessment.views.clientCreated'),
    url(r'^searchClients/$', 'assessment.views.searchClients'),
    url(r'^clientSearchResults/$', 'assessment.views.clientSearchResults'),
    url(r'^clientOptions/$', 'assessment.views.clientOptions'),

    ## Mental Health Views
    url(r'^mh_preliminary/$', 'assessment.views.mh_preliminary'),
    url(r'^mh_activity/$', 'assessment.views.mh_activity'),
    url(r'^mh_demographic/$', 'assessment.views.mh_demographic'),
    url(r'^mh_education/$', 'assessment.views.mh_education'),
    url(r'^mh_familyBackground/$', 'assessment.views.mh_familyBackground'),
    url(r'^mh_familyHistory/$', 'assessment.views.mh_familyHistory'),
    url(r'^mh_legal/$', 'assessment.views.mh_legal'),
    url(r'^mh_relationships/$', 'assessment.views.mh_relationships'),
    url(r'^mh_stress/$', 'assessment.views.mh_stress'),
    url(r'^mh_useTable/$', 'assessment.views.mh_useTable'),
    url(r'^mh_viewForm/$', 'assessment.views.mh_viewForm'),

    ## SAP Views
    url(r'^sap_preliminary/$', 'assessment.views.sap_preliminary'),
    url(r'^sap_demographic/$', 'assessment.views.sap_demographic'),
    url(r'^sap_psychoactive/$', 'assessment.views.sap_psychoactive'),
    url(r'^sap_viewForm/$', 'assessment.views.sap_viewForm'),

    ## Anger Management Views
    url(r'^am_preliminary/$', 'assessment.views.am_preliminary'),
    url(r'^am_angerHistory/$', 'assessment.views.am_angerHistory'),
    url(r'^am_angerTarget/$', 'assessment.views.am_angerTarget'),
    url(r'^am_childhood/$', 'assessment.views.am_childhood'),
    url(r'^am_connections/$', 'assessment.views.am_connections'),
    url(r'^am_control/$', 'assessment.views.am_control'),
    url(r'^am_problems/$', 'assessment.views.am_problems'),
    url(r'^am_demographic/$', 'assessment.views.am_demographic'),
    url(r'^am_drugHistory/$', 'assessment.views.am_drugHistory'),
    url(r'^am_familyOrigin/$', 'assessment.views.am_familyOrigin'),
    url(r'^am_final/$', 'assessment.views.am_final'),
    url(r'^am_viewForm/$', 'assessment.views.am_viewForm'),
    url(r'^am_worst/$', 'assessment.views.am_worst'),

    ## Urine Test Views
    url(r'^ut_preliminary/$', 'assessment.views.ut_preliminary'),
    url(r'^ut_testResults/$', 'assessment.views.ut_testResults'),
    url(r'^ut_viewForm/$', 'assessment.views.ut_viewForm'),

    ## Discharge Views
    url(r'^discharge_preliminary/$', 'assessment.views.discharge_preliminary'),
    url(r'^discharge_client/$', 'assessment.views.discharge_client'),
    url(r'^discharge_viewForm/$', 'assessment.views.discharge_viewForm'),
    
)
