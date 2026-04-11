from stario import Context
from stario import Writer

from stariodemo.DataStructsPkg.WidgetModule import Widget


def WidgetListEndpoint(db):
    async def handler(c: Context, w: Writer) -> None:

        # Get all tasks
        print("==== All Tasks ====")
        all_tasks = await Widget.all()

        for task in all_tasks:
            print(f"{task.title} | Category: {task.category} | Due: {task.due_date}")

        w.empty(204)

    return handler
