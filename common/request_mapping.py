def request_mapping(root_url, branch_url):
    def wrapper(cls):
        def deco(*args, **kwargs):
            cls(root_url, branch_url, *args, **kwargs)

        return deco

    return wrapper
