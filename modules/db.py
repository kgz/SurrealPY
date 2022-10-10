"""."""
import uuid

from surrealdb.clients.http import HTTPClient


class db(HTTPClient):
    """."""

    def __init__(self) -> None:
        super().__init__("http://localhost:8000", namespace="test", database="testdb", username="root", password="root")

    def idv4(self):
        """."""
        return str(uuid.uuid4()).replace("-", "")