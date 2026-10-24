
resource "aws_vpc" "cloudops" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name        = "cloudops-monitoring-vpc"
    Environment = "learning"
    Project     = "CloudOps-Monitoring"
  }
}
