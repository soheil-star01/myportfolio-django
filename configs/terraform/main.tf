resource "aws_instance" "django_app" {
  ami           = "ami-0e04bcbe83a83792e" # Use the correct AMI ID for your region
  instance_type = "t2.micro"     # Specify the EC2 instance type here

  tags = {
    Name = "DjangoApp"
  }
}