import boto3
import gzip
from io import BytesIO

region = 'us-east-1'
baseURL ='https://data.commoncrawl.org/'
key = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'
bucket = 'commoncrawl'

def download_data(key=key,  bucket=bucket):
    s3 = boto3.client('s3')

    result = s3.get_object(Bucket=bucket, Key=key)
    zipped_file = result['Body'].read()
    return zipped_file


def main():
    # your code here
    data = download_data()
    with gzip.GzipFile(fileobj=BytesIO(data), mode='rb') as file:
        first_line = file.readline().decode('utf-8').strip()
        uri = first_line.strip()
        response_uri = s3.get_object(Bucket=bucket, Key=s3_uri)

        for line in response_uri['Body'].iter_lines():
            print(line.decode('utf-8'))
    
    pass

 
if __name__ == "__main__":
    main()
