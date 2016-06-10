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
    url(r'^all_active_clients/$', 'assessment.views.all_active_clients'),
    url(r'^all_discharged_clients/$', 'assessment.views.all_discharged_clients'),

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
    url(r'^mh_location/$', 'assessment.views.mh_location'),

    ## SAP Views
    url(r'^sap_preliminary/$', 'assessment.views.sap_preliminary'),
    url(r'^sap_demographic/$', 'assessment.views.sap_demographic'),
    url(r'^sap_psychoactive/$', 'assessment.views.sap_psychoactive'),
    url(r'^sap_psychoactive2/$', 'assessment.views.sap_psychoactive2'),
    url(r'^sap_special/$', 'assessment.views.sap_special'),
    url(r'^sap_preFinal/$', 'assessment.views.sap_preFinal'),
    url(r'^sap_final/$', 'assessment.views.sap_final'),
    url(r'^sap_viewForm/$', 'assessment.views.sap_viewForm'),
    url(r'^sap_location/$', 'assessment.views.sap_location'),

    ## Anger Management Views
    url(r'^am_preliminary/$', 'assessment.views.am_preliminary'),
    url(r'^am_angerHistory/$', 'assessment.views.am_angerHistory'),
    url(r'^am_angerHistory2/$', 'assessment.views.am_angerHistory2'),
    url(r'^am_angerHistory3/$', 'assessment.views.am_angerHistory3'),
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
    url(r'^am_location/$', 'assessment.views.am_location'),
    url(r'^printAM/$', 'assessment.views.printAM'),
    url(r'^exit_am/$', 'assessment.views.exit_am'),
    url(r'^am_deleted/$', 'assessment.views.am_deleted'),

    ## Urine Test Views
    url(r'^ut_preliminary/$', 'assessment.views.ut_preliminary'),
    url(r'^ut_testResults/$', 'assessment.views.ut_testResults'),
    url(r'^ut_viewForm/$', 'assessment.views.ut_viewForm'),
    url(r'^ut_form_saved/$', 'assessment.views.ut_form_saved'),
    url(r'^ut_form_saved2/$', 'assessment.views.ut_form_saved2'),

    ## Discharge Views
    url(r'^discharge_preliminary/$', 'assessment.views.discharge_preliminary'),
    url(r'^discharge_client/$', 'assessment.views.discharge_client'),
    url(r'^discharge_viewForm/$', 'assessment.views.discharge_viewForm'),

    ##Addiction Severity Views
    url(r'^asi_demographic/$', 'assessment.views.asi_demographic'),
    
)
