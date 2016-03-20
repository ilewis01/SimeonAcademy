from django.contrib import admin
from assessment.models import State, RefReason, Client, MaritalStatus, \
LivingSituation, AngerManagement, EducationLevel, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, UseTable, \
FamilyHistory, AM_Demographic, AM_DrugHistory,AM_ChildhoodHistory, \
AM_AngerHistory, AM_Connections, AM_WorstEpisode, AM_AngerTarget, \
AM_FamilyOrigin, AM_CurrentProblem, AM_Control, AM_Final, \
SapDemographics, SapPsychoactive, MHDemographic, MHFamily, MHEducation, \
MHRelationship, MHActivity, MHStressor, MHLegalHistory

admin.site.register(account)
admin.site.register(State)
admin.site.register(RefReason)
admin.site.register(Client)
admin.site.register(MaritalStatus)
admin.site.register(LivingSituation)
admin.site.register(EducationLevel)
admin.site.register(Drug)
admin.site.register(TermReason)
admin.site.register(Discharge)
admin.site.register(UrineResults)
##SAP REGISTERS
admin.site.register(SapDemographics)
admin.site.register(SapPsychoactive)
admin.site.register(SAP)
##ANGER MANAGEMENT REGISTERS
admin.site.register(AM_Demographic)
admin.site.register(AM_DrugHistory)
admin.site.register(AM_ChildhoodHistory)
admin.site.register(AM_AngerHistory)
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
admin.site.register(UseTable)
admin.site.register(FamilyHistory)
admin.site.register(MHFamily)
admin.site.register(MHEducation)
admin.site.register(MHRelationship)
admin.site.register(MHActivity)
admin.site.register(MHStressor)
admin.site.register(MHLegalHistory)
admin.site.register(MentalHealth)

