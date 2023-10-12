def session_data(request):
    # Define the data you want to make available in the context
    session_data = {
        'id': request.session.get('user_id', 0),
        # Add more session data as needed
    }
    return {'session_data': session_data}
