resource "aws_db_subnet_group" "default" {
  name       = "ecommerce-db-subnet-group"
  subnet_ids = [
    aws_subnet.public_subnet_a.id,
    aws_subnet.public_subnet_b.id
  ]

  tags = {
    Name = "Ecommerce DB Subnet Group"
  }
}

resource "aws_db_instance" "postgres" {
  allocated_storage       = 20
  engine                  = "postgres"
  engine_version          = "15"
  instance_class          = "db.t3.micro"
  db_name                 = "ecommercedb"
  username                = var.db_username
  password                = var.db_password
  skip_final_snapshot     = true
  publicly_accessible     = true
  db_subnet_group_name    = aws_db_subnet_group.default.name
  vpc_security_group_ids  = [aws_security_group.app_sg.id]

  tags = {
    Name = "ecommerce-postgres"
  }
}
