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