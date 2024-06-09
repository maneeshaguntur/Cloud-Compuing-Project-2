### Project 2: PaaS Application Development in Cloud Computing [CSE 546, Spring 2024]

#### **Summary:**
This project involved developing a cloud-based video analysis application using AWS Lambda and other AWS services. The application provides face recognition as a service on videos streamed from clients. The project consists of two main parts: implementing a video-splitting function and integrating face recognition to create a complete multi-stage pipeline.

### **Complete Project Overview**

#### **Setup and Configuration:**

1. **Input Bucket Creation:**
   - **Bucket Name:** `input`
   - **Function:** Stores uploaded videos in .mp4 format. Each upload triggers the video-splitting Lambda function.
   - **Data:** 100-video dataset for testing.

2. **Stage-1 Bucket Creation:**
   - **Bucket Name:** `stage-1`
   - **Function:** Stores output images from the video-splitting function, organized in folders named after the input videos.

3. **Output Bucket Creation:**
   - **Bucket Name:** `output`
   - **Function:** Stores results of the face-recognition function as text files with identified names.

#### **Lambda Function Implementations:**

1. **Video-Splitting Function:**
   - **Name:** "video-splitting"
   - **Trigger:** Activated by new video uploads to the input bucket.
   - **Processing:** 
     - Uses ffmpeg to split videos into frames.
     - Stores one frame with the same name as the input video in the stage-1 bucket.
     - Invocation command: `ffmpeg -i ' +video_filename+ ' -vframes 1 ' + '/tmp/' +outfile`
   - **Next Step:** Invokes the face-recognition function asynchronously after processing.

2. **Face-Recognition Function:**
   - **Name:** "face-recognition"
   - **Trigger:** Activated by addding files to Stage-1 bucket.
   - **Processing:**
     - Extracts faces from frames using OpenCV APIs.
     - Uses a pre-trained ResNet-34 model to recognize faces.
     - Stores results as text files in the output bucket.
   - **Invocation Parameters:** 
     - `bucket_name`: stage-1
     - `image_file_name`: Name of the frame file (e.g., `test_00.jpg`)

#### **Testing & Validation:**

1. **IAM User Creation:**
   - Created an IAM user with necessary permissions for automated grading (s3:Get*, s3:PutObject, s3:List*, lambda:GetFunction, cloudwatch:GetMetricData, s3:Delete*).

2. **Workload Testing:**
   - Used a workload generator with 100 video uploads to test the complete application pipeline.
   - Monitored execution duration, concurrency of Lambda functions, and total end-to-end latency.

3. **Validation Criteria:**
   - **Lambda Function Validation:** Confirmed existence and correct operation of both "video-splitting" and "face-recognition" Lambda functions.
   - **S3 Bucket Validation:** Ensured correct initial state and content of input, stage-1, and output buckets.
   - **Output Validation:** Verified correct number, naming, and content of images in stage-1 and text files in the output bucket.

#### **Grading Criteria Met:**


 **Performance Metrics:** 
   - Total end-to-end latency of the 100 video workload met the required limits.
   - Deduction: Points based on latency performance.

 **Folder and Image Validation:** 
   - Correct number and naming of folders and images in stage-1 bucket.
   - Deduction: 1 point for each incorrect/missing image.

 **Output Accuracy:** 
   - Correctness of identified names in text files in the output bucket.
   - Deduction: 1 point for each wrong name.

 **Pipeline Performance:** 
   - Total end-to-end latency met required limits.
   - Deduction: Points based on incomplete requests if latency exceeded.


#### **Skills and Techniques Acquired:**
This project enhanced my ability to use AWS PaaS resources to build sophisticated, scalable cloud applications, providing a solid foundation for future serverless computing projects.
