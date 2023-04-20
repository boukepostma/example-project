from kedro.framework.hooks import hook_impl
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class AzureSecretsHook:
    @hook_impl
    def after_context_created(self, context) -> None:
        params = context.config_loader["parameters"]

        my_credential = DefaultAzureCredential()
        
        secrets = {}
        for cred_name, secret_configs in params["secrets"].items():
            KVUri = f"https://{secret_configs['key_vault_name']}.vault.azure.net"
            client = SecretClient(vault_url=KVUri, credential=my_credential)

            secrets = {
                **secrets,
                cred_name: {
                    "account_name": secret_configs["account_name"],
                    "account_key": client.get_secret(secret_configs["storage_key_id"]).value,
                }
            }
        
        context.config_loader["credentials"] = {
            **context.config_loader["credentials"],
            **secrets,
        }
        print(context.config_loader["credentials"])