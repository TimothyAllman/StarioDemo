from datetime import date
from datetime import timedelta

from stariodemo.PiccoloPkg.WidgetDbModule import WidgetDb


async def SeedWidget() -> None:
    today = date.today()
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)

    # async with WidgetDb._meta.db.transaction(transaction_type=TransactionType.immediate):
    #     # Create work tasks
    qry = WidgetDb.insert(
        WidgetDb(
            title="Complete quarterly report",
            description="Finalize Q1 financial report for management review",
            category="Work",
            priority=3,
            due_date=tomorrow,
        ),
        WidgetDb(
            title="Team meeting",
            description="Weekly team sync meeting",
            category="Work",
            priority=2,
            due_date=today,
        ),
        WidgetDb(
            title="Grocery shopping",
            description="Buy ingredients for dinner",
            category="Personal",
            priority=2,
            due_date=today,
        ),
        WidgetDb(
            title="Complete Python course",
            description="Finish the advanced Python programming course",
            category="Learning",
            priority=1,
            due_date=next_week,
        ),
        WidgetDb(
            title="Read PiccoloOrm documentation",
            description="Study the advanced features of PiccoloOrm",
            category="Learning",
            priority=2,
            due_date=tomorrow,
        ),
    )

    result = await qry.run()

    print("Data populated successfully!")
