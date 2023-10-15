#!/usr/bin/env bash

sleep 1
export VAULT_TOKEN=devroot
export VAULT_ADDR=http://127.0.0.1:8200

cat - > /tmp/minpolicy.hcl <<EOF
path "/identity/*" {
	capabilities = ["read", "list"]
}
EOF
vault policy write min /tmp/minpolicy.hcl

vault auth enable oidc
vault auth enable jwt

vault write auth/jwt/config \
    oidc_discovery_url="https://$AUTH0_DOMAIN" \
    oidc_client_id="" \
    oidc_client_secret="" \
    default_role="demo"

vault write auth/jwt/role/demo \
    role_type="jwt" \
    bound_audiences="$AUTH0_CLIENT_ID" \
    allowed_redirect_uris="http://localhost:8250/oidc/callback" \
    user_claim="sub" \
    groups_claim="iss" \
    policies=webapps \
    ttl=1h


#you can use your ID token as well if it is in JWT format
vault write auth/jwt/login role=demo jwt=<JWT_TOKEN>

# curl \
#     --request POST \
#     --data '{"jwt": "<JWT_TOKEN>", "role": "demo"}' \
#     http://127.0.0.1:8200/v1/auth/jwt/login

    
