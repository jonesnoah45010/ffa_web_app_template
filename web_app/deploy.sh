#!/bin/bash

SERVICE_NAME="YOUR-APP-NAME" # Define your service name here. Example "test-portal"
PROJECT_NAME="YOUR-GCLOUD-PROJECT" # Reference to an existing Google Cloud Console Project
REGION="us-central1" # Should match the region you want to host your app from

# Step 1: Build and push the container image
gcloud builds submit --tag gcr.io/${PROJECT_NAME}/${SERVICE_NAME} .

# Step 2: Deploy the Cloud Run service 
gcloud run deploy ${SERVICE_NAME} \
    --image=gcr.io/${PROJECT_NAME}/${SERVICE_NAME} \
    --region=${REGION} \
    --allow-unauthenticated \
    --platform managed \
    --project ${PROJECT_NAME}  \
    --quiet