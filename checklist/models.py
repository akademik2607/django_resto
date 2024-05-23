from django.db import models

from config.settings import ROLES

NULLABLE = {
    'null': True,
    'blank': True
}


HOLE_TASKLILST_STATUSES = (
    ('done', 'בוצע'),
    ('not_done', 'לא בוצע'),
    ('choose', 'נא לבחור')
)

WORK_DAY_STATUSES = (
    ('working_day', 'יום עבודה'),
    ('day_off', 'יום חופש'),
)

TIMES_OF_DAY = (
    ('morning', 'בוקר'),
    ('evening', 'עֶרֶב')
)


class WorkingShift(models.Model):
    pass


class CheckList(models.Model):
    name = models.CharField(verbose_name='name', max_length=100, **NULLABLE)
    role = models.CharField(verbose_name='role', choices=ROLES, max_length=50)
    workday = models.CharField(verbose_name='is_work_day', choices=WORK_DAY_STATUSES, max_length=30, **NULLABLE)
    shift = models.CharField(verbose_name='shift', choices=TIMES_OF_DAY, max_length=30)
    is_active = models.BooleanField(verbose_name='is_active', default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name if self.name else str(self.id)


# Tasks START
class TaskList(CheckList):
    class Meta:
        abstract = True


class TemplateTaskListShift(TaskList):
    working_shift = models.ForeignKey(WorkingShift, on_delete=models.CASCADE, related_name='template_task_list')

    class Meta:
        verbose_name = 'Task template'
        verbose_name_plural = 'Task templates'



class TaskListShift(TaskList):
    working_shift = models.ForeignKey(WorkingShift, on_delete=models.CASCADE, related_name='task_list')

    class Meta:
        verbose_name = 'Task list'
        verbose_name_plural = 'Task list'


class HoleItem(models.Model):
    text = models.TextField(verbose_name='משימה', **NULLABLE)
    time = models.TimeField(verbose_name='שעה', **NULLABLE)
    status = models.CharField(verbose_name='סטטוס', choices=HOLE_TASKLILST_STATUSES, max_length=40)
    comment = models.TextField(verbose_name='למה לא בוצע', default='', **NULLABLE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.text


class HoleItemTemplate(HoleItem):
    template_list = models.ForeignKey(TemplateTaskListShift, related_name='template_item', on_delete=models.CASCADE)


class HoleItemTask(HoleItem):
    is_dyn = models.BooleanField('is_dyn_task', default=False)
    author_name = models.CharField('author_name', max_length=125, **NULLABLE)
    task_list = models.ForeignKey(TaskListShift, related_name='task_list', on_delete=models.CASCADE)

# Tasks END


# Products START
class ProductList(CheckList):
    class Meta:
        abstract = True



class TemplateProductListShift(ProductList):
    working_shift = models.ForeignKey(WorkingShift, on_delete=models.CASCADE, related_name='template_product_list')

    class Meta:
        verbose_name = 'Product template'
        verbose_name_plural = 'Product templates'


class ProductListShift(TaskList):
    working_shift = models.ForeignKey(WorkingShift, on_delete=models.CASCADE, related_name='product_list')

    class Meta:
        verbose_name = 'Product list'
        verbose_name_plural = 'Product list'


class KitchenItem(models.Model):
    task = models.TextField(verbose_name='משימה', **NULLABLE)
    arabic_name = models.TextField(verbose_name='שם בערבית', **NULLABLE)
    short = models.IntegerField(verbose_name='חסר', default=0)
    standard = models.IntegerField(verbose_name='תקן', default=0)
    morning = models.IntegerField(verbose_name='בוקר', default=0)
    evening = models.IntegerField(verbose_name='ערב', default=0)
    cause = models.TextField(verbose_name='סיבה', **NULLABLE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.task


class KitchenItemTemplate(KitchenItem):
    template_list = models.ForeignKey(TemplateProductListShift, related_name='template_item', on_delete=models.CASCADE)


class KitchenItemProduct(KitchenItem):
    status = models.CharField(verbose_name='סטטוס', choices=HOLE_TASKLILST_STATUSES, max_length=40, default=HOLE_TASKLILST_STATUSES[2][0])
    task_list = models.ForeignKey(ProductListShift, related_name='task_list', on_delete=models.CASCADE)


#Products END





