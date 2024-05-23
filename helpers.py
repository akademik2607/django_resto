import json


def done_worker(status, role, task_id, shift, comment=''):
    from config.settings import ROLES

    from checklist.models import TaskListShift, HoleItemTask, HOLE_TASKLILST_STATUSES

    if role != ROLES[2][0] and role != ROLES[3][0]:
        if comment:
            HoleItemTask.objects.filter(id=task_id).update(status=status, comment=comment)
        else:
            HoleItemTask.objects.filter(id=task_id).update(status=status)
        task_list = TaskListShift.objects.filter(
            role=role,
            shift=shift,
            is_active=True
        ).first()
        tasks = HoleItemTask.objects.filter(task_list=task_list, status=HOLE_TASKLILST_STATUSES[2][0]).all()

        items = []
        for task in tasks:
            items.append({
                'id': task.id,
                'name': task.text,
                'time': str(task.time),
                'is_notion': False,
                'is_dyn_task': task.is_dyn
            })

        return json.dumps({
            "id": {
                'id': task_list.id
            },
            'role': role,
            'items': items

        })
    return ''


def cook_info_bulk_worker(data):
    from checklist.models import KitchenItemProduct, TIMES_OF_DAY

    items = data.get('todoList').get('items')
    for item in items:
        short = 0
        if item.get('work_shift') == TIMES_OF_DAY[0][0]:
            short = item.get('standard') - item.get('morning')
        else:
            short = item.get('standard') - item.get('evening')
        KitchenItemProduct.objects.filter(
            id=item.get('id')
        ).update(
            standard=item.get('standard'),
            morning=item.get('morning'),
            evening=item.get('evening'),
            short=short
        )
    return json.dumps({'role': data.get('role'), 'items': []})
