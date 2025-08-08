# `dawgcodes-youtube-oauth-token`

This is a script for fetching the oauth2 token 
from the command line.

## Usage 

0. Getting the oauth client secret file from Google Cloud console, which should contain the following fields:
   ```json
   {
        "installed": {
            "client_id": "some-random-id.apps.googleusercontent.com",
            "project_id": "my-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "SomeClientSecret123-Ab_C",
            "redirect_uris": [
                "urn:ietf:wg:oauth:2.0:oob",
                "http://localhost"
            ]
        }
    }
   ```
1. Clone the script
2. Install the dependency
   ```bash
   pip install -r requirements.txt
   ```
3. Execute the script by passing the file in
   ```bash
   python youtube-token.py client-secret.json
   ```
4. Follow the outputted link and paste the token in
5. A file named `credential.json` will be created, it would have
   the following key
   ```json
   {
      "token": "ya29.somereallylong-client-token",
      "refresh_token": "1//a0Ab-Afasdfonfi-adfawf-M",
      "token_uri": "https://oauth2.googleapis.com/token",
      "client_id": "some-client-id.apps.googleusercontent.com",
      "client_secret": "SomeClientSecret123-Ab_C"
   }
   ```


The default scope would only includes
`https://www.googleapis.com/auth/youtube.readonly`.

You can also simply change the scope in for any other permissions that you
would like to obtain.
