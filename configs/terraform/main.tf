resource "aws_instance" "django_app" {
  ami           = "ami-0e04bcbe83a83792e"
  instance_type = "t2.micro"

  tags = {
    Name = "DjangoApp"
  }

  associate_public_ip_address = true
}

output "new_public_ip" {
  value = aws_instance.django_app.public_ip
  description = "The public IP address of the Django App instance"
}
output "instance_id" {
  value = aws_instance.django_app.id
  description = "The EC2 instance ID"
}