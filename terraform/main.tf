terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">=3.17.0"
    }
  }  
}

provider "azurerm" {
  features{}
  subscription_id   = var.arm_subscription_id
  tenant_id         = var.arm_tenant_id
  client_id         = var.arm_client_id
  client_secret     = var.arm_client_secret
}

data "azurerm_client_config" "current" {}

resource "azurerm_resource_group" "default" {
  name     = "${random_pet.prefix.id}-rg"
  location = var.location
}

resource "random_pet" "prefix" {
  prefix = var.prefix
  length = 2
}

resource "random_integer" "suffix" {
  min = 10000000
  max = 99999999
}

# terraform apply --var-file="secret.tfvars"