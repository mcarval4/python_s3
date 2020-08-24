import boto3
import os

def DownloadS3(bucketName, remoteDirectoryName):
  s3_resource = boto3.resource('s3')
  bucket = s3_resource.Bucket(bucketName)
  for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
    if not os.path.exists(os.path.dirname(obj.key)):
      os.makedirs(os.path.dirname(obj.key))
    bucket.download_file(obj.key, obj.key)

if __name__ == "__main__":
  DownloadS3('psl-raw', 'iba/br/laminacao/year=2020/month=08/day=19')