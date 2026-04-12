from datetime import date
from datetime import timedelta

from piccolo.engine.sqlite import TransactionType

from stariodemo.PiccoloPkg.WidgetDbModule import WidgetDb


async def SeedWidget() -> None:
    today = date.today()
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)

    async with WidgetDb._meta.db.transaction(transaction_type=TransactionType.immediate):
        # Create work tasks
        await WidgetDb.insert(
            WidgetDb(
                title="Complete quarterly report",
                description="Finalize Q1 financial report for management review",
                category="Work",
                priority=3,
                due_date=tomorrow,
            ),
        )
        await WidgetDb.insert(
            WidgetDb(
                title="Team meeting",
                description="Weekly team sync meeting",
                category="Work",
                priority=2,
                due_date=today,
            )
        )

        # Create personal tasks
        await WidgetDb.insert(
            WidgetDb(
                title="Grocery shopping",
                description="Buy ingredients for dinner",
                category="Personal",
                priority=2,
                due_date=today,
            )
        )

        # Create learning tasks
        await WidgetDb.insert(
            WidgetDb(
                title="Complete Python course",
                description="Finish the advanced Python programming course",
                category="Learning",
                priority=1,
                due_date=next_week,
            )
        )
        await WidgetDb.insert(
            WidgetDb(
                title="Read TortoiseORM documentation",
                description="Study the advanced features of TortoiseORM",
                category="Learning",
                priority=2,
                due_date=tomorrow,
            )
        )

    print("Data populated successfully!")
