"""
Stario Chat - Request Handlers

Handlers are async functions that receive:
- Context (c): request info, signals parsing, tracing/logging
- Writer (w): response methods (html, patch, redirect, empty)

Dependencies (db, relay) are injected via closures where needed.
Functions like subscribe(db, relay) return a handler with deps captured.
"""

