from boto3.session import Session
 
ACCESS_KEY='xxxx'
SECRET_KEY='yyyy'

session = Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
 
for bucket in s3.buckets.all():
    print ('--------------------')
    print (bucket.name)
    print ('--------------------')
    your_bucket = s3.Bucket(bucket.name)
    for s3_file in your_bucket.objects.all():
        print(s3_file.key," ultima Modificacao: ",s3_file.last_modified)
