# class Widget(models.Model):
#     id = fields.IntField(pk=True)
#     title = fields.CharField(max_length=200, nullable=False)
#     description = fields.TextField(null=True)
#     is_completed = fields.BooleanField(default=False)
#     due_date = fields.DateField(null=True)
#     priority = fields.IntField(default=1)
#     category = fields.CharField(max_length=100, default="General")
#     created_at = fields.DatetimeField(auto_now_add=True)
#     modified_at = fields.DatetimeField(auto_now=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         table = "Widget"


# # Generate Pydantic model for Task
# Task_Pydantic = pydantic_model_creator(Widget, name="Task")
# TaskIn_Pydantic = pydantic_model_creator(Widget, name="TaskIn", exclude_readonly=True)
