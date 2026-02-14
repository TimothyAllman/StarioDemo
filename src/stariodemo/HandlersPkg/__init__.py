"""
Stario Chat - Request Handlers

Handlers are async functions that receive:
- Context (c): request info, signals parsing, tracing/logging
- Writer (w): response methods (html, patch, redirect, empty)

Dependencies (db, relay) are injected via closures where needed.
Functions like subscribe(db, relay) return a handler with deps captured.
"""

from dataclasses import dataclass


@dataclass
class ChatSignals:
    """
    Schema for signals sent from client.

    Datastar automatically sends signals with every request (@get, @post).
    Using a dataclass lets us parse and validate them with c.signals(ChatSignals).
    """

    user_id: str = ""
    username: str = ""
    color: str = ""
    message: str = ""
