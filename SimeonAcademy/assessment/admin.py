from django.contrib import admin
from assessment.models import State, RefReason, Client, \
AngerManagement, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, MHUseTable, \
MHFamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_AngerHistory2, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHBackground, MHEducation, \
MHStressor, MHLegalHistory, SType, Invoice, AM_AngerHistory3, TrackApp,\
A_Time, Appointment, ClientSession, AIS_Admin, AIS_General, AIS_Medical, \
AIS_Employment, AIS_Drug1, AIS_Legal, AIS_Family, AIS_Social1, \
AIS_Social2, AIS_Psych, ASI, UtPaid, SolidState, PrintableForms

admin.site.register(account)
admin.site.register(State)
admin.site.register(RefReason)
admin.site.register(Client)
admin.site.register(Drug)
admin.site.register(TermReason)
admin.site.register(Discharge)
admin.site.register(UrineResults)
admin.site.register(UtPaid)
admin.site.register(SolidState)
admin.site.register(TrackApp)
admin.site.register(PrintableForms)

##AIS REGISTERS
admin.site.register(AIS_Admin)
admin.site.register(AIS_General)
admin.site.register(AIS_Medical)
admin.site.register(AIS_Employment)
admin.site.register(AIS_Drug1)
admin.site.register(AIS_Legal)
admin.site.register(AIS_Family)
admin.site.register(AIS_Social1)
admin.site.register(AIS_Social2)
admin.site.register(AIS_Psych)
admin.site.register(ASI)

##SAP REGISTERS
admin.site.register(SapDemographics)
admin.site.register(SapPsychoactive)
admin.site.register(SAP)

##ANGER MANAGEMENT REGISTERS
admin.site.register(AM_Demographic)
admin.site.register(AM_DrugHistory)
admin.site.register(AM_ChildhoodHistory)
admin.site.register(AM_AngerHistory)
admin.site.register(AM_AngerHistory2)
admin.site.register(AM_AngerHistory3)
admin.site.register(AM_Connections)
admin.site.register(AM_WorstEpisode)
admin.site.register(AM_AngerTarget)
admin.site.register(AM_FamilyOrigin)
admin.site.register(AM_CurrentProblem)
admin.site.register(AM_Control)
admin.site.register(AM_Final)
admin.site.register(AngerManagement)

##MENTAL HEALTH REGISTERS
admin.site.register(MHDemographic)
admin.site.register(MHUseTable)
admin.site.register(MHFamilyHistory)
admin.site.register(MHBackground)
admin.site.register(MHEducation)
admin.site.register(MHStressor)
admin.site.register(MHLegalHistory)
admin.site.register(MentalHealth)

##SESSIONS AND APPOINTMENTS
admin.site.register(SType)
admin.site.register(A_Time)
admin.site.register(Appointment)
admin.site.register(ClientSession)
admin.site.register(Invoice)

