class ParseException(Exception):
    pass


def parse_args(args):
    start, offset = args.get("start"), args.get("offset")

    if start is None and offset is None:
        return []

    try:
        parsed_start = int(start)
        parsed_offset = int(offset)
    except (ValueError, TypeError):
        raise ParseException("Invalid parameters")

    if parsed_start < 0:
        raise ParseException("The parameter 'start' must be positive")

    if parsed_offset < 1:
        raise ParseException("The parameter 'offset' must greater than 1")

    return parsed_start, parsed_offset
