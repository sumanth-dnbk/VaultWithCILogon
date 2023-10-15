# VaultWithCILogon

Configuring CILogon as an identity provider for users to authenticate themselves to Vault and get vault tokens.

## Step 1:
1. Register to CILogon at [https://cilogon.org/oauth2/register].
2. Use the Client Registration image present in repo as a reference for the Vault server running in a development environment (see callbacks).

## Step 2:
Once registered, we get the client id and client secret, which we put into the `.env` file in this repository.

__OIDC LOGIN__
## Step 3:
In a terminal, run `Start_Server.sh`. This starts the vault server with debug logs.

## Step 4:
In another terminal, run `OIDC_Login.sh`. You will be taken to the CILogon login page, where you enter your institutional login credentials. Once you do that, you will see the Vault token in the terminal(eg. hvs.332490328). Now, you can use the Vault token to access Vault.

## Step 5:
If you want to access Vault through the Vault UI, follow these steps:
1. Go to [http://localhost:8200/ui].
2. Select the method as "token" and enter the Vault token that you received in the terminal output.
3. Now, you can access Vault through its UI.

**References:** [https://github.com/ncabatoff/vault-1.1-webinar/blob/master/README-oidc.md](https://github.com/ncabatoff/vault-1.1-webinar/blob/master/README-oidc.md)

__JWT LOGIN__

## Step 3:
In a terminal, run `Start_Server.sh`. This starts the vault server with debug logs.

## Step 4:
In other terminal run `python Device_Authorization.py` after providing host, clientid and client secret in the file(6,7,8) lines. You will get the tokens as output after you finish the flow.
## Step 5:
After putting the id token at line 34,nn another terminal, run `JWT_Login.sh`. Once you do that, you will see the Vault token in the terminal(eg. hvs.332490328). Now, you can use the Vault token to access Vault.

## Step 6:
If you want to access Vault through the Vault UI, follow these steps:
1. Go to [http://localhost:8200/ui].
2. Select the method as "token" and enter the Vault token that you received in the terminal output.
3. Now, you can access Vault through its UI.

**References:** [https://developer.hashicorp.com/vault/docs/auth/jwt]
