import os
from pathlib import Path
from tempfile import TemporaryDirectory

import faker
import pytest

import items
from items.api import Item


@pytest.fixture(scope="session")
def db_path(tmp_path_factory):
    """Path to temporary database"""
    return tmp_path_factory.mktemp("items_db")


@pytest.fixture(scope="session")
def session_items_db(db_path):
    """ItemsDB"""
    db_ = items.ItemsDB(db_path)
    yield db_
    db_.close()


@pytest.fixture(autouse=True, scope="session")
def setup_test_env():
    found = os.environ.get("APP_ENV", "")
    os.environ["APP_ENV"] = "TESTING"
    yield
    os.environ["APP_ENV"] = found


def pytest_addoption(parser):
    parser.addoption(
        "--fdb",
        action="store_true",
        default=False,
        help="Create new db for each test",
    )


def db_scope(fixture_name, config):
    if config.getoption("--fdb", None):
        return "function"
    return "session"


@pytest.fixture(scope=db_scope)
def db():
    """ItemsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = items.ItemsDB(db_path)
        yield db_
        db_.close()


@pytest.fixture(scope="function")
def items_db(session_items_db, request, faker):
    db = session_items_db
    db.delete_all()
    # Support for random selection "@pytest.mark.num_items({NUMBER})`.
    faker.seed_instance(99)
    m = request.node.get_closest_marker("num_items")
    if m and len(m.args) > 0:
        num_items = m.args[0]
        for _ in range(num_items):
            db.add_item(Item(summary=faker.sentence(), owner=faker.first_name()))
    return db
