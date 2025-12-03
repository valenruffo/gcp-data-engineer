python wordcount.py \
    --runner DataflowRunner \
    --project gcp-data-engineer-05 \
    --region us-central1 \
    --temp_location gs://gcs-bucket-06/temp/ \
    --staging_location gs://gcs-bucket-06/staging/ \
    --template_location gs://gcs-bucket-06/templates/wordcount_template