import re
import sqlite3
from typing import Any, Dict, List, Tuple

DB_PATH = "demo.db"
QUERY_FILE = "queries.sql"


class Database:
    def __init__(self, db_path: str = DB_PATH, query_file: str = QUERY_FILE) -> None:
        self.db_path = db_path
        self.query_file = query_file
        self.queries = self._load_queries()
        self._init_db()

    def _load_queries(self) -> Dict[str, str]:
        queries: Dict[str, str] = {}
        with open(self.query_file, "r", encoding="utf-8") as f:
            content: str = f.read()
            blocks: list[Any] = re.findall(
                r"-- name: (.+?)\n(.*?)(?=\n-- name:|\Z)",
                content,
                re.DOTALL,
            )
            for name, sql in blocks:
                queries[name.strip()] = sql.strip()
        return queries

    def _init_db(self) -> None:
        with self.get_connection() as conn:
            conn.execute(self.queries["create_table"])
            conn.commit()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def insert_person(self, name: str, age: int, profession: str) -> None:
        with self.get_connection() as conn:
            conn.execute(
                self.queries["insert_person"],
                {
                    "name": name,
                    "age": age,
                    "profession": profession,
                },
            )
            conn.commit()

    def get_all_people(self) -> List[Tuple[Any]]:
        with self.get_connection() as conn:
            cursor = conn.execute(self.queries["get_all_people"])
            return cursor.fetchall()
