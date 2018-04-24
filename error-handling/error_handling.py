def handle_error_by_throwing_exception():
    raise Exception('Opps')


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except Exception:
        return None


def handle_error_by_returning_tuple(input_data):
    result = handle_error_by_returning_none(input_data)
    return (result is not None, result)


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object as f:
        f.do_something()
