"""
Stario Chat - HTML Views

Views are pure functions: data in, HTML out.
They receive messages and users as parameters - no global state access.
This makes them easy to test and enables the closure-based dependency injection.

Stario's HTML helpers work like function calls:
  Div({"class": "foo"}, "child1", child2)  →  <div class="foo">child1...</div>

Datastar attributes (data.*) add reactivity:
  data.signals({...})  - client-side reactive state
  data.bind("field")   - two-way binding to signal
  data.on("event", "code")  - event handler
  at.get/at.post       - trigger server requests
"""

