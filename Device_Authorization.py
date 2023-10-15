import requests
import time


def deviceAuthorize():
    HOST = 'cilogon.org'
    CLIENT_ID = '<Your client id>'
    CLIENT_SECRET = '<your client secret if you have one>'
    SCOPE = 'openid profile'
    #need to find the valid host
    #endpoints urls vary from provider to provider and they can be found at HOST/.well-known/openid-configuration
    DEVICE_ENDPOINT = 'https://{}/oauth2/device_authorization'.format(HOST)
    TOKEN_ENDPOINT = 'https://{}/oauth2/token'.format(HOST)

    device_code_payload = {
        'client_id': CLIENT_ID,
        'client_secret':CLIENT_SECRET,
        'scope':SCOPE
    }
    device_code_response = requests.post(DEVICE_ENDPOINT,data=device_code_payload)
    # print("The response ",device_code_response)
    device_code_data = device_code_response.json()
    if 'error' in device_code_data:
        ERROR = device_code_data['error']
        ERROR_DESCRIPTION = device_code_data['error_description']
        if len(ERROR) != 0:
            print('Error : ',ERROR_DESCRIPTION)
            return
    
    #No error
    DEVICE_CODE = device_code_data['device_code']
    USER_CODE = device_code_data['user_code']
    # EXPIRES_IN = device_code_data['expires_in']
    VERIFICATION_URI_COMPLETE = device_code_data['verification_uri_complete']
    # Interval field is optional
    INTERVAL = 5
    if 'interval' in device_code_data:
        INTERVAL = device_code_data['interval']

    CHECK_FAILED = 0
    if len(DEVICE_CODE)==0:
        print("Error:No device_code found in response.")
        CHECK_FAILED = 1
    if len(USER_CODE)==0:
        print("Error:No user_code found in response.")
        CHECK_FAILED = 1
    # if len(EXPIRES_IN)==0:
    #     print("Error:No expires_in found in response.")
    #     CHECK_FAILED = 1
    if CHECK_FAILED ==1 :
        print("Exitting")
        return
    

    
    print('Device code successful')
    print('1. On your computer or mobile device navigate to: ', VERIFICATION_URI_COMPLETE)
    print('2. Enter the following code: ', USER_CODE)

    token_payload = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:device_code',
        'device_code': DEVICE_CODE,
        'client_id': CLIENT_ID,
        'client_secret':CLIENT_SECRET
    }

    authenticated = False
    while not authenticated:
        print('Checking if the user completed the flow...')
        token_response = requests.post(TOKEN_ENDPOINT, data=token_payload)

        token_data = token_response.json()
        # ERROR = token_data['error']
        # ERROR_DESCRIPTION = token_data['error_description']

        if 'error' in token_data:
            ERROR = token_data['error']
            ERROR_DESCRIPTION = token_data['error_description']
            print('Error',ERROR_DESCRIPTION+'\n')
            if ERROR =='authorization_pending' or ERROR=='slow_down':
                if ERROR == 'slow_down':
                    INTERVAL = INTERVAL+5
                time.sleep(INTERVAL)
            else:
                if ERROR_DESCRIPTION == 'no pending request':
                    print('\nERROR: User denied the user_code.\n')
                    print('Please begin a new device code request.\n')
                else:
                    print('Error',ERROR_DESCRIPTION+'\n')
                    if ERROR_DESCRIPTION == 'device_code expired':
                        print('Please begin a new device code request.\n')
                return
        else:
            print('Authenticated!')
            print('tokens are:',token_data)
            authenticated = True
    return

if __name__ == '__main__':
    deviceAuthorize()