def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'id': user.id,
        'username': user.username,
        'phone': user.phone_num,
        'identity': user.get_identity_display(),
        'name': user.name,
        'token': token,
    }
