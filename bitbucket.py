#!/usr/bin/python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth2Session

class ClientSecrets:
    '''
    The structure of this class follows Google convention for `client_secrets.json`:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    Bitbucket does not emit this structure so it must be manually constructed.
    '''
    client_id = ""
    client_secret = ""
    redirect_uris = [
      "https://localhost"  # Used for testing.
    ]
    auth_uri = "https://bitbucket.org/site/oauth2/authorize"
    token_uri = "https://bitbucket.org/site/oauth2/access_token"
    server_base_uri = "https://api.bitbucket.org/"

def main():
    c = ClientSecrets()
    # Fetch a request token
    bitbucket = OAuth2Session(c.client_id)
    # Redirect user to Bitbucket for authorization
    authorization_url = bitbucket.authorization_url(c.auth_uri)
    print('Please go here and authorize: {}'.format(authorization_url[0]))
    # Get the authorization verifier code from the callback url
    redirect_response = raw_input('Paste the full redirect URL here:')
    # Fetch the access token
    bitbucket.fetch_token(
      c.token_uri,
      authorization_response=redirect_response,
      username=c.client_id,
      password=c.client_secret)
    # Fetch a protected resource, i.e. user profile
    r = bitbucket.get(c.server_base_uri + '1.0/user')
    print(r.content)

if __name__ == '__main__':
    main()
