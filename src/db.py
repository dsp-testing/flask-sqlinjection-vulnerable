import logging
import os
import sqlite3
from typing import Any, List
from rich import print

logger = logging.getLogger(__name__)

DB_FILENAME = os.path.realpath("data/test.db")

def _get_connection() -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(DB_FILENAME)
    except sqlite3.Error:
        logger.exception("Unable to get database")
        raise
    else:
        return conn

def get_challenges_for_candidate(cpf: str) -> List[Any]:
    query = f"""
        SELECT title, score FROM challenges c
        JOIN users u
        ON u.id = c.user_id
        WHERE u.cpf='{cpf}';
    """
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")

    conn = _get_connection()
    cur = conn.cursor()

    cur.execute(query)
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
