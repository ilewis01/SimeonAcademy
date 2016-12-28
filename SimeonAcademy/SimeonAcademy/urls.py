from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^roommate_page/$', 'assessment.views.roommate_page'),
    url(r'^roommate_new/$', 'assessment.views.roommate_new'),
    url(r'^roommate_ref/$', 'assessment.views.roommate_ref'),
    url(r'^roommate_eval/$', 'assessment.views.roommate_eval'),
    url(r'^roommate_all/$', 'assessment.views.roommate_all'),
    url(r'^roommate_win/$', 'assessment.views.roommate_win'),
    url(r'^roommate_profile/$', 'assessment.views.roommate_profile'),
    url(r'^roommate_view_application/$', 'assessment.views.roommate_view_application'),
    url(r'^verify_rm_delete/$', 'assessment.views.verify_rm_delete'),
    url(r'^complete_rm_removal/$', 'assessment.views.complete_rm_removal'),
    url(r'^rm_edit_app/$', 'assessment.views.rm_edit_app'),
    url(r'^rm_delete_app/$', 'assessment.views.rm_delete_app'),
    url(r'^rm_top_apps/$', 'assessment.views.rm_top_apps'),
    url(r'^rm_new_lease/$', 'assessment.views.rm_new_lease'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'assessment.views.index'), 
    url(r'^login/$', 'assessment.views.login'),   
    url(r'^logout/$', 'assessment.views.logout'),
    url(r'^newProfile/$', 'assessment.views.newProfile'),
    url(r'^auth/$', 'assessment.views.auth_view'),
    url(r'^invalid_login/$', 'assessment.views.invalid_login'),
    url(r'^index/$', 'assessment.views.index'),
    url(r'^adminHome/$', 'assessment.views.adminHome'),    
    url(r'^searchFormMain/$', 'assessment.views.searchFormMain'),
    url(r'^appointmentMain/$', 'assessment.views.appointmentMain'),
    url(r'^billingMain/$', 'assessment.views.billingMain'),
    url(r'^AdministrativeMain/$', 'assessment.views.AdministrativeMain'),    
    url(r'^uniFormSearch/$', 'assessment.views.uniFormSearch'),
    url(r'^emailMain/$', 'assessment.views.emailMain'),

    ##Counselor Schedule
    url(r'^setSchedule/$', 'assessment.views.setSchedule'),
    url(r'^viewAppointments/$', 'assessment.views.viewAppointments'),
    url(r'^avaiableAppointments/$', 'assessment.views.avaiableAppointments'),
    url(r'^apptHistory/$', 'assessment.views.apptHistory'),
    url(r'^workDateSelector/$', 'assessment.views.workDateSelector'),
    url(r'^calendarSaved/$', 'assessment.views.calendarSaved'),

   	##Client Views
    url(r'^clientHome/$', 'assessment.views.clientHome'),
    url(r'^clientHistory/$', 'assessment.views.clientHistory'),
    url(r'^client_appointment/$', 'assessment.views.client_appointment'),
    url(r'^client_documents/$', 'assessment.views.client_documents'),
    url(r'^all_active_clients/$', 'assessment.views.all_active_clients'),
    url(r'^all_discharged_clients/$', 'assessment.views.all_discharged_clients'),
    url(r'^updateStatus/$', 'assessment.views.updateStatus'),
    url(r'^updateSuccess/$', 'assessment.views.updateSuccess'),
    url(r'^uniClientSearch/$', 'assessment.views.uniClientSearch'),
    url(r'^searchClientMain/$', 'assessment.views.searchClientMain'),
    url(r'^editClientInfo/$', 'assessment.views.editClientInfo'),
    url(r'^confirmDeleteClient/$', 'assessment.views.confirmDeleteClient'),
    url(r'^clientDeleteSucess/$', 'assessment.views.clientDeleteSucess'),
    url(r'^clientInvoiceMain/$', 'assessment.views.clientInvoiceMain'),
    url(r'^clientFiles/$', 'assessment.views.clientFiles'),
    url(r'^clientAppointments/$', 'assessment.views.clientAppointments'),
    url(r'^submitClientUpdate/$', 'assessment.views.submitClientUpdate'),
    url(r'^clientAccountUpdated/$', 'assessment.views.clientAccountUpdated'),
    url(r'^updateClientPage/$', 'assessment.views.updateClientPage'),
    url(r'^clientProfile/$', 'assessment.views.clientProfile'),

    ## Admin client option pages
    url(r'^newClient/$', 'assessment.views.newClient'),
    url(r'^confirmNewClient/$', 'assessment.views.confirmNewClient'),
    url(r'^clientCreated/$', 'assessment.views.clientCreated'),
    url(r'^searchClients/$', 'assessment.views.searchClients'),
    url(r'^clientSearchResults/$', 'assessment.views.clientSearchResults'),
    url(r'^clientOptions/$', 'assessment.views.clientOptions'),
    url(r'^new_note_pad/$', 'assessment.views.new_note_pad'),
    url(r'^notePadAdded/$', 'assessment.views.notePadAdded'),
    url(r'^notePadDeleted/$', 'assessment.views.notePadDeleted'),

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
    url(r'^mh_viewForm/$', 'assessment.views.mh_viewForm'),
    url(r'^mh_to_op_errors/$', 'assessment.views.mh_to_op_errors'),
    url(r'^printMH/$', 'assessment.views.printMH'),
    url(r'^op_type_error/$', 'assessment.views.op_type_error'),
    url(r'^op_input_error/$', 'assessment.views.op_input_error'),
    url(r'^op_item_exist/$', 'assessment.views.op_item_exist'),
    url(r'^dynamic_useTable/$', 'assessment.views.dynamic_useTable'),

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
    url(r'^print_sap/$', 'assessment.views.print_sap'),

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
    url(r'^finishChildhood/$', 'assessment.views.finishChildhood'),
    url(r'^am_angerHistory2_suicide/$', 'assessment.views.am_angerHistory2_suicide'),
    url(r'^generateErrors/$', 'assessment.views.generateErrors'),

    ## Urine Test Views
    url(r'^ut_preliminary/$', 'assessment.views.ut_preliminary'),
    url(r'^ut_pay/$', 'assessment.views.ut_pay'),
    url(r'^ut_paid/$', 'assessment.views.ut_paid'),
    url(r'^ut_testResults/$', 'assessment.views.ut_testResults'),
    url(r'^ut_viewForm/$', 'assessment.views.ut_viewForm'),
    url(r'^printUT/$', 'assessment.views.printUT'),
    url(r'^UT_complete/$', 'assessment.views.UT_complete'),
    url(r'^existingUT/$', 'assessment.views.existingUT'),

    ## Discharge Views
    url(r'^discharge_success/$', 'assessment.views.discharge_success'),
    url(r'^discharge_client/$', 'assessment.views.discharge_client'),
    url(r'^discharge_viewForm/$', 'assessment.views.discharge_viewForm'),
    url(r'^process_discharge/$', 'assessment.views.process_discharge'),

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
    url(r'^new_comment/$', 'assessment.views.new_comment'),
    url(r'^printASI/$', 'assessment.views.printASI'),

    ##Global Views
    url(r'^generic_exit/$', 'assessment.views.generic_exit'),
    url(r'^uni_generic_exit/$', 'assessment.views.uni_generic_exit'),
    url(r'^genericDelete/$', 'assessment.views.genericDelete'),
    url(r'^genericFormDeleted/$', 'assessment.views.genericFormDeleted'),
    url(r'^genericRefreshForm/$', 'assessment.views.genericRefreshForm'),
    url(r'^genericFormRefreshed/$', 'assessment.views.genericFormRefreshed'),
    url(r'^closeSession/$', 'assessment.views.closeSession'),
    url(r'^refreshSession/$', 'assessment.views.refreshSession'),
    url(r'^sessionClosed/$', 'assessment.views.sessionClosed'),
    url(r'^sessionClosedAlt/$', 'assessment.views.sessionClosedAlt'),
    url(r'^deleteSession/$', 'assessment.views.deleteSession'),
    url(r'^uni_exit_session/$', 'assessment.views.uni_exit_session'),
    url(r'^hasExistingSession/$', 'assessment.views.hasExistingSession'),
    url(r'^existingResolve/$', 'assessment.views.existingResolve'),
    url(r'^sessionResolveSuccess/$', 'assessment.views.sessionResolveSuccess'),
    url(r'^session_open_error/$', 'assessment.views.session_open_error'),
    url(r'^invoice/$', 'assessment.views.invoice'),
    url(r'^form_complete/$', 'assessment.views.form_complete'),
    url(r'^form_saved/$', 'assessment.views.form_saved'),
    url(r'^form_existing/$', 'assessment.views.form_existing'),
    url(r'^printForm/$', 'assessment.views.printForm'),
    url(r'^printLoaded/$', 'assessment.views.printLoaded'),
    url(r'^underConstruction/$', 'assessment.views.underConstruction'),
    url(r'^error_zero/$', 'assessment.views.error_zero'),
    url(r'^dataTemplate/$', 'assessment.views.dataTemplate'),
)
