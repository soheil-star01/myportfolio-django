resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_ssh"
  }
}

resource "tls_private_key" "django_key_pair" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "aws_key_pair" "django_key_pair" {
  key_name   = "django-key"
  public_key = tls_private_key.django_key_pair.public_key_openssh
}

resource "aws_instance" "django_app" {
  ami                    = "ami-04f76ebf53292ef4d"
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.django_key_pair.key_name
  associate_public_ip_address = true
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  tags = {
    Name = "DjangoApp"
  }
}

output "new_public_ip" {
  value       = aws_instance.django_app.public_ip
  description = "The public IP address of the Django App instance"
}

output "private_key" {
  value       = tls_private_key.django_key_pair.private_key_pem
  description = "The private key to access the EC2 instance"
  sensitive   = true
}

output "instance_id" {
  value = aws_instance.django_app.id
  description = "The ID of the EC2 instance"
}

output "security_group_id" {
  value = aws_security_group.allow_ssh.id
  description = "The ID of the security group"
}

output "key_pair_name" {
  value = aws_key_pair.django_key_pair.key_name
  description = "The name of the key pair"
}