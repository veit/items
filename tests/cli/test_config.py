def test_config(items_cli, db_path):
    assert items_cli("config") == str(db_path)


def test_config_normal_path(db_path, items_cli_no_redirect):
    items_cli = items_cli_no_redirect
    assert items_cli("config") != str(db_path)
