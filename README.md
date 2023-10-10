# VaultWithCILogon
Configuring CILogon as an identity provider for users to authenticate themselves to Vault and get vault tokens.

# step 1:
Register to CILogon at https://cilogon.org/oauth2/register.
Use Client Registration image as reference for vault server running in dev environment.(see callbacks)

# step 2: 
Once registered, we get the client id and client secret which we put them in .env file in this repo

# step 3:
In a terminal run terminal1.sh 

# step 4: 
In other terminal run terminal2.sh. Now, you will be taken to CILogon login page, where you enter your institutional login credentials. Once you do that you will see the vault token in terminal. Now, you can use the vault token to access vault. 

# step 5. 
If you want to access through vault UI, go to http://localhost:8200/ui
Select method as token and enter the vault token that you have received in the terminal output.
Now, you can access the vault through its ui.