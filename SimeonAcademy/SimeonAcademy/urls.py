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
    url(r'^clientHistory/$', 'assessment.views.clientHistory'),
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
    url(r'^mh_demographic/$', 'assessment.views.mh_demographic'),
    url(r'^mh_education/$', 'assessment.views.mh_education'),
    url(r'^mhDemoOpPage/$', 'assessment.views.mhDemoOpPage'),
    url(r'^verify_mhOp/$', 'assessment.views.verify_mhOp'),
    url(r'^mh_background/$', 'assessment.views.mh_background'),
    url(r'^mh_stress/$', 'assessment.views.mh_stress'),
    url(r'^mh_familyHistory/$', 'assessment.views.mh_familyHistory'),
    url(r'^mh_legal/$', 'assessment.views.mh_legal'),
    url(r'^mh_psych/$', 'assessment.views.mh_psych'),
    url(r'^mh_useTable/$', 'assessment.views.mh_useTable'),
    url(r'^mh_viewForm/$', 'assessment.views.mh_viewForm'),   

    ## SAP Views
    url(r'^sap_preliminary/$', 'assessment.views.sap_preliminary'),
    url(r'^sap_demographic/$', 'assessment.views.sap_demographic'),
    url(r'^sap_psychoactive/$', 'assessment.views.sap_psychoactive'),
    url(r'^sap_psychoactive2/$', 'assessment.views.sap_psychoactive2'),
    url(r'^sap_special/$', 'assessment.views.sap_special'),
    url(r'^sap_social/$', 'assessment.views.sap_social'),
    url(r'^sap_other/$', 'assessment.views.sap_other'),
    url(r'^sap_sources/$', 'assessment.views.sap_sources'),
    url(r'^sap_viewForm/$', 'assessment.views.sap_viewForm'),

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
    url(r'^printAM/$', 'assessment.views.printAM'),

    ## Urine Test Views
    url(r'^ut_preliminary/$', 'assessment.views.ut_preliminary'),
    url(r'^ut_pay/$', 'assessment.views.ut_pay'),
    url(r'^ut_paid/$', 'assessment.views.ut_paid'),
    url(r'^ut_testResults/$', 'assessment.views.ut_testResults'),
    url(r'^ut_viewForm/$', 'assessment.views.ut_viewForm'),

    ## Discharge Views
    url(r'^discharge_preliminary/$', 'assessment.views.discharge_preliminary'),
    url(r'^discharge_client/$', 'assessment.views.discharge_client'),
    url(r'^discharge_viewForm/$', 'assessment.views.discharge_viewForm'),

    ##Addiction Severity Views
    url(r'^asi_preliminary/$', 'assessment.views.asi_preliminary'),
    url(r'^asi_admin/$', 'assessment.views.asi_admin'),
    url(r'^asi_general/$', 'assessment.views.asi_general'),
    url(r'^asi_medical/$', 'assessment.views.asi_medical'),
    url(r'^asi_employment/$', 'assessment.views.asi_employment'),
    url(r'^asi_drug1/$', 'assessment.views.asi_drug1'),
    url(r'^asi_legal/$', 'assessment.views.asi_legal'),
    url(r'^asi_family/$', 'assessment.views.asi_family'),
    url(r'^asi_social1/$', 'assessment.views.asi_social1'),
    url(r'^asi_social2/$', 'assessment.views.asi_social2'),
    url(r'^asi_psych/$', 'assessment.views.asi_psych'),
    url(r'^asi_viewForm/$', 'assessment.views.asi_viewForm'),

    ##Global Views
    url(r'^generic_exit/$', 'assessment.views.generic_exit'),
    url(r'^uni_generic_exit/$', 'assessment.views.uni_generic_exit'),
    url(r'^genericDelete/$', 'assessment.views.genericDelete'),
    url(r'^genericFormDeleted/$', 'assessment.views.genericFormDeleted'),
    url(r'^genericRefreshForm/$', 'assessment.views.genericRefreshForm'),
    url(r'^genericFormRefreshed/$', 'assessment.views.genericFormRefreshed'),
    url(r'^closeSession/$', 'assessment.views.closeSession'),
    url(r'^sessionClosed/$', 'assessment.views.sessionClosed'),
    url(r'^deleteSession/$', 'assessment.views.deleteSession'),
    url(r'^uni_exit_session/$', 'assessment.views.uni_exit_session'),
    
)
