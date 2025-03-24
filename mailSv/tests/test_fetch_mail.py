from CONTROLLER.fetchMailController import FetchMailController

def test_fetch_email_details_valid_id():
    controller = FetchMailController()
    result = controller.fetch_email_details(1)
    assert result is not None
    assert 'id' in result
    assert 'sender' in result

def test_fetch_email_details_invalid_id():
    controller = FetchMailController()
    result = controller.fetch_email_details(-1)
    assert result is None

def test_fetch_email_details_non_existent_id():
    controller = FetchMailController()
    result = controller.fetch_email_details(9999)
    assert result is None
