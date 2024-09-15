resource "aws_instance" "django_app" {
  ami           = "ami-0e04bcbe83a83792e" # Use the correct AMI ID for your region
  instance_type = "t2.micro"     # Specify the EC2 instance type here

  tags = {
    Name = "DjangoApp"
  }

  # Ensure that the instance gets a public IP if it's in a VPC with an Internet Gateway
  associate_public_ip_address = true
}

# Output the public IP of the EC2 instance
output "new_public_ip" {
  value = aws_instance.django_app.public_ip
  description = "The public IP address of the Django App instance"
}
output "instance_id" {
  value = aws_instance.django_app.id
  description = "The EC2 instance ID"
}