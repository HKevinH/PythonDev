
def get_common_context(request):
    logged_in = request.COOKIES.get('logged_in', 'False') == 'True'
    return {'logged_in': logged_in}

