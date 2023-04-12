variable "environment" {
  type        = string
  description = "Name of the environment"
  default     = "dev"
}

variable "location" {
  type        = string
  description = "Location of the resources"
  default     = "West Europe"
}

variable "prefix" {
  type        = string
  description = "Prefix of the resource name"
  default     = "ml"
}

variable arm_subscription_id {
  type        = string
  description = "ID of Azure subscription"
}

variable  arm_tenant_id {
  type        = string
  description = "ID of tenant in Azure"
}

variable  arm_client_id {
  type        = string
  description = "ID of service principal in Azure"
}

variable  arm_client_secret {
  type        = string
  description = "Secret of service principal in Azure"
}
