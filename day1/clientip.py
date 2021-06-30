@app.route('/hello')
def hello():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
    return ['Your IP is: {}\n'.format(client_ip)]