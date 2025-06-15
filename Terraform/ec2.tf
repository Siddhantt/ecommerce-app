resource "aws_security_group" "app_sg" {
  name   = "app-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  ami                    = "ami-03f4878755434977f" # Mumbai (ap-south-1) – Amazon Linux 2
  instance_type          = var.instance_type
  subnet_id = aws_subnet.public_subnet_a.id
  vpc_security_group_ids = [aws_security_group.app_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "EcommerceAppServer"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install docker -y
              systemctl start docker
              docker run -d -p 5000:5000 siddhanttayade/ecommerce-app:latest
              EOF
}
