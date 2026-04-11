# from datetime import date
# from datetime import timedelta

# from stario import Context
# from stario import Writer

# from stariodemo.DataStructsPkg.WidgetModule import Widget


# def WidgetAddEndpoint(db):
#     async def handler(c: Context, w: Writer) -> None:
#         # Create some tasks
#         today = date.today()
#         tomorrow = today + timedelta(days=1)
#         next_week = today + timedelta(days=7)

#         # Create work tasks
#         await Widget.create(title="Complete quarterly report", description="Finalize Q1 financial report for management review", category="Work", priority=3, due_date=tomorrow)
#         await Widget.create(title="Team meeting", description="Weekly team sync meeting", category="Work", priority=2, due_date=today)

#         # Create personal tasks
#         await Widget.create(title="Grocery shopping", description="Buy ingredients for dinner", category="Personal", priority=2, due_date=today)

#         # Create learning tasks
#         await Widget.create(title="Complete Python course", description="Finish the advanced Python programming course", category="Learning", priority=1, due_date=next_week)
#         await Widget.create(title="Read TortoiseORM documentation", description="Study the advanced features of TortoiseORM", category="Learning", priority=2, due_date=tomorrow)

#         print("Data populated successfully!")
#         w.empty(204)

#     return handler
