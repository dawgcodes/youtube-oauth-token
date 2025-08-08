
import google.oauth2.credentials
import google_auth_oauthlib.flow
import json
import sys

from flask import Flask
import flask


# secret file path
client_secret_file = sys.argv[1]

# Use the client_secret.json file to identify the application requesting
# authorization. The client ID (from that file) and access scopes are required.
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    client_secret_file,
    ['https://www.googleapis.com/auth/youtube.readonly'])

# Indicate where the API server will redirect the user after the user completes
# the authorization flow. The redirect URI is required. The value must exactly
# match one of the authorized redirect URIs for the OAuth 2.0 client, which you
# configured in the API Console. If this value doesn't match an authorized URI,
# you will get a 'redirect_uri_mismatch' error.
flow.redirect_uri = 'http://localhost:5000/'

# Generate URL for request to Google's OAuth 2.0 server.
# Use kwargs to set optional request parameters.
authorization_url, _ = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type='offline',
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes='true')

print('Please go to this URL:')
print(authorization_url)

print()


app = Flask(__name__)

@app.route("/")
def auth_route_callback():
    auth_code = flask.request.args.get("code")
    
    flow.fetch_token(code=auth_code)
    
    credentials = flow.credentials
    
    credential_obj = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    
    with open('credentials.json', 'w') as f:
        json.dump(credential_obj, f, indent=2)
    
    success_string = "Credentials file successfully written. Server can be shutdown"
    print(success_string)
    return success_string

app.run()
