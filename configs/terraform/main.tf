resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # WARNING: Open to all IPs. You can restrict this to your specific IP.
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"  # Allow all outbound traffic
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
  ami                    = "ami-0e04bcbe83a83792e"
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

# Output EC2 instance ID
output "instance_id" {
  value = aws_instance.django_app.id
  description = "The ID of the EC2 instance"
}

# Output security group ID
output "security_group_id" {
  value = aws_security_group.allow_ssh.id
  description = "The ID of the security group"
}

# Output key pair name
output "key_pair_name" {
  value = aws_key_pair.django_key_pair.key_name
  description = "The name of the key pair"
}