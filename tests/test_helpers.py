from aio2ch import clean_html_tags, get_board_and_thread_from_url


def test_clean_html_tags(raw_text, clean_text):
    clean = clean_html_tags(raw_text)

    assert clean == clean_text


def test_get_board_and_thread_from_url(thread_url, thread_as_number):
    board, thread = get_board_and_thread_from_url(thread_url)

    assert board == "test"
    assert thread == f"{thread_as_number}"
