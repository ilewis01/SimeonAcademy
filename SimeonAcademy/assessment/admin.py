from django.contrib import admin
from assessment.models import State, RefReason, Client, MaritalStatus, \
LivingSituation, AngerManagement, EducationLevel, Drug, TermReason, \
Discharge, UrineResults, SAP, account, MentalHealth, UseTable, \
FamilyHistory

admin.site.register(account)
admin.site.register(State)
admin.site.register(RefReason)
admin.site.register(Client)
admin.site.register(MaritalStatus)
admin.site.register(LivingSituation)
admin.site.register(AngerManagement)
admin.site.register(EducationLevel)
admin.site.register(Drug)
admin.site.register(TermReason)
admin.site.register(Discharge)
admin.site.register(UrineResults)
admin.site.register(SAP)
admin.site.register(MentalHealth)
admin.site.register(UseTable)
admin.site.register(FamilyHistory)

