from django.contrib import admin
from .models import (
    EntryConditionModel,
    EntryConditionLevel_1,
    EntryConditionLevel_2,
    EntryConditionField_2,
    EntryConditionField_3,
    TrailConditionModel,
    TrailConditionLevel_1,
    RiskManagementModel,
)

admin.site.register(EntryConditionModel)
admin.site.register(EntryConditionLevel_1)
admin.site.register(EntryConditionLevel_2)
admin.site.register(EntryConditionField_2)
admin.site.register(EntryConditionField_3)
admin.site.register(TrailConditionModel)
admin.site.register(TrailConditionLevel_1)
admin.site.register(RiskManagementModel)
