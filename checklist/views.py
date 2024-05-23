from datetime import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from checklist.models import CheckList, WORK_DAY_STATUSES, TaskList, HoleItemTemplate, HoleItemTask, TaskListShift, \
    TemplateTaskListShift, KitchenItemTemplate, TIMES_OF_DAY, ProductListShift, TemplateProductListShift, \
    KitchenItemProduct, WorkingShift

from .models import HOLE_TASKLILST_STATUSES


def index(request):
    return render(request, 'index.html')



@api_view(['POST'])
@permission_classes([AllowAny])
def take_board(request):
    print(request.data)
    working_shift = WorkingShift.objects.get(pk=1)
    if request.data['role'] != 'hot_streak' and request.data['role'] != 'cold_streak':
        task_list = TaskListShift.objects.filter(
            role=request.data['role'],
            shift=request.data['shift'],
            is_active=True
        ).first()
        if not task_list:
            template_list = TemplateTaskListShift.objects.filter(
                role=request.data['role'],
                shift=request.data['shift'],

            ).first()
            template_tasks = HoleItemTemplate.objects.filter(template_list=template_list).all()
            print('TEMPLATE TASKS!!!!!', template_tasks)
            TaskListShift(
                role=request.data['role'],
                workday=(
                    WORK_DAY_STATUSES[1][0]
                    if (datetime.today().weekday() == 4 or datetime.today().weekday() == 5) else WORK_DAY_STATUSES[0][0]
                ),
                shift=request.data['shift'],
                is_active=True,
                working_shift=working_shift
            ).save()
            task_list = TaskListShift.objects.latest('id')
            for template_task in template_tasks:
                HoleItemTask(
                    text=template_task.text,
                    time=template_task.time,
                    status=template_task.status,
                    # working_shift_type=template_task.working_shift_type,
                    task_list=task_list,
                ).save()

            tasks = HoleItemTask.objects.filter(task_list=task_list, status=HOLE_TASKLILST_STATUSES[2][0]).all()
            print('tasks', tasks)
            items = []
            for task in tasks:
                items.append({
                    'id': task.id,
                    'name': task.text,
                    'time': task.time,
                    'is_notion': False,
                    'is_dyn_task': task.is_dyn
                })
            return Response({
                "id": {
                    'id': task_list.id
                },
                'items': items
            })

        else:
            tasks = HoleItemTask.objects.filter(task_list=task_list, status=HOLE_TASKLILST_STATUSES[2][0]).all()
            print('tasks', tasks)
            items = []
            for task in tasks:
                items.append({
                    'id': task.id,
                    'name': task.text,
                    'time': task.time,
                    'is_notion': False,
                    'is_dyn_task': task.is_dyn
                })
            return Response({
                "id": {
                    'id': task_list.id
                },
                'items': items
            })
    else:
        task_list = ProductListShift.objects.filter(
            role=request.data['role'],
            shift=request.data['shift'],
            is_active=True
        ).first()
        print('task liiist', task_list)
        if not task_list:
            template_list = TemplateProductListShift.objects.filter(
                role=request.data['role'],
                shift=request.data['shift'],

            ).first()
            template_tasks = KitchenItemTemplate.objects.filter(template_list=template_list).all()

            # TIMES_OF_DAY = (
            #     ('morning', 'בוקר'),
            #     ('evening', 'עֶרֶב')
            # )
            prev_list = ProductListShift.objects.filter(
                role=request.data['role'],
                shift=(
                    TIMES_OF_DAY[0][0]
                    if (request.data['shift'] == TIMES_OF_DAY[1][0]) else  TIMES_OF_DAY[1][0]
                )

            ).first()
            prev_tasks = KitchenItemProduct.objects.filter(task_list=prev_list).all()

            print('TEMPLATE TASKS!!!!!', template_tasks)
            ProductListShift(
                role=request.data['role'],
                workday=(
                    WORK_DAY_STATUSES[1][0]
                    if (datetime.today().weekday() == 4 or datetime.today().weekday() == 5) else WORK_DAY_STATUSES[0][0]
                ),
                shift=request.data['shift'],
                is_active=True,
                working_shift=working_shift
            ).save()
            task_list = ProductListShift.objects.latest('id')
            for template_task in template_tasks:
                morning = template_task.morning
                evening = template_task.evening
                short = 0
                for prev_product in prev_tasks:
                    if prev_product.task == template_task.task:
                       if request.data['shift'] == TIMES_OF_DAY[0][0]:
                           evening = prev_product.evening
                           short = template_task.standard - evening
                       else:
                           morning = prev_product.morning
                           short = template_task.standard - morning
                KitchenItemProduct(
                    task=template_task.task,
                    arabic_name=template_task.arabic_name,
                    short=short,
                    standard=template_task.standard,
                    morning=morning,
                    evening=evening,
                    cause=template_task.cause,
                    task_list=task_list,
                ).save()
            tasks = KitchenItemProduct.objects.filter(task_list=task_list, status=HOLE_TASKLILST_STATUSES[2][0]).all()
            print('tasks', tasks)
            items = []
            for task in tasks:
                items.append({
                    'id': task.id,
                    'name': task.task,
                    'arabic_name': task.arabic_name,
                    'short': task.short,
                    'standard': task.standard,
                    'morning': task.morning,
                    'evening': task.evening,
                    'cause': task.cause,
                    'work_shift': request.data['shift']
                })

            return Response({
                "id": {
                    'id': task_list.id
                },
                'items': items
            })
        else:
            tasks = KitchenItemProduct.objects.filter(task_list=task_list, status=HOLE_TASKLILST_STATUSES[2][0]).all()
            print('tasks', tasks)
            items = []
            for task in tasks:
                items.append({
                    'id': task.id,
                    'name': task.task,
                    'arabic_name': task.arabic_name,
                    'short': task.short,
                    'standard': task.standard,
                    'morning': task.morning,
                    'evening': task.evening,
                    'cause': task.cause,
                    'work_shift': request.data['shift']

                })

            return Response({
                "id": {
                    'id': task_list.id
                },
                'items': items
            })




@api_view(['POST'])
@permission_classes([AllowAny])
def update_task(request):
    pass
