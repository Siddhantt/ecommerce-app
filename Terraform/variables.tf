variable "aws_region" {
  default = "ap-south-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "db_username" {
  default = "ecomuser"   # ✅ Not a reserved word
}

variable "db_password" {
  default = "yourStrongPassword123"
}