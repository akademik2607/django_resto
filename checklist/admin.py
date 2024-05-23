from django.contrib import admin

# Register your models here.
from checklist.models import \
    WorkingShift, TaskListShift, \
    TemplateTaskListShift, HoleItemTemplate, \
    HoleItemTask, KitchenItemTemplate, KitchenItemProduct, TemplateProductListShift, ProductListShift


class HoleItemTemplateInline(admin.TabularInline):
    model = HoleItemTemplate


class HoleItemTaskInline(admin.TabularInline):
    model = HoleItemTask


class TemplateTaskListShiftAdmin(admin.ModelAdmin):
    inlines = [HoleItemTemplateInline]


class TaskListShiftAdmin(admin.ModelAdmin):
    inlines = [HoleItemTaskInline]





class KitchenItemTemplateInline(admin.TabularInline):
    model = KitchenItemTemplate


class KitchenItemProductInline(admin.TabularInline):
    model = KitchenItemProduct


class TemplateProductListShiftAdmin(admin.ModelAdmin):
    inlines = [KitchenItemTemplateInline]


class ProductListShiftAdmin(admin.ModelAdmin):
    inlines = [KitchenItemProductInline]


class WorkingShiftAdmin(admin.ModelAdmin):
    pass


admin.site.register(TemplateTaskListShift, TemplateTaskListShiftAdmin)
admin.site.register(TaskListShift, TaskListShiftAdmin)


admin.site.register(ProductListShift, ProductListShiftAdmin)
admin.site.register(TemplateProductListShift, TemplateProductListShiftAdmin)

admin.site.register(WorkingShift, WorkingShiftAdmin)
