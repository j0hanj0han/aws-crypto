import sys
import boto3
from botocore.config import Config

from awscrypto.utils import utils



my_config = Config(
    region_name = 'us-west-3',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

client = boto3.client('kinesis', config=my_config)


def main():
    print("hello world!")
    ec2 = boto3.client('ec2', config=my_config)
    response = ec2.describe_instances()
    print(response)

    utils.coucou()

if __name__ == "__main__":
    sys.exit(main())





