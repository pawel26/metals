from django.utils.http import urlencode


def add_query_params(url, *args, **kwargs):
    query_args = []
    for arg in args:
        if isinstance(arg, str):
            query_args.append(arg)
        elif isinstance(arg, dict):
            query_args.append(urlencode(arg))
        elif isinstance(arg, (list, tuple)):
            if not isinstance(arg[0], (list, tuple)):
                arg = [arg]
            query_args.append(urlencode(arg))

    query_args.append(urlencode([[k, kwargs[k]] for k in sorted(kwargs)]))

    parts = url.split('?', 1)
    base = parts[0]
    return '?'.join(
        [base, '&'.join(v for v in parts[1:] + query_args if v)]
    ).rstrip('?')
