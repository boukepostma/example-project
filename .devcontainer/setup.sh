apt-get update
apt-get upgrade -y
pre-commit install
apt-get install htop -y
az login --use-device-code
az account set --subscription b3427a92-a6bb-4354-9822-98b9a61bbe58
az configure --defaults workspace=ml-elegant-sloth-mlw group=ml-elegant-sloth-rg location=westeurope