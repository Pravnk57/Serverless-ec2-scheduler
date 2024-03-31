# Serverless-ec2-scheduler
## Scheduling ec2 instances during company operating Hours.
# Scenario:
In some companies, there is no need to run their EC2 instances 24/7; they require instances to operate during specific time periods, such as company working hours, from 7:00 AM in the morning to 5:00 PM in the evening. To address this scenario, I will implement two Lambda functions responsible for starting and stopping instances. These Lambda functions will be triggered by two CloudWatch Events in the morning and evening. After implementing Lambda functions this will start and stop Instances at a specific cron period and sends the notification about the state change as well. This solution is fully serverless.

![scheduler](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/05560a6d-1e8f-4366-8ffa-2eacfba551ba)

## Steps :

### Step 1 :
### Creating the Instance :
1. Navigate to the EC2 Console.
2. Follow the Outlined steps below.
3. Create two Ec2 instances. In My case i already have some instances running, so create two Ec2 instances.
   
![image (30)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/7fbb4f97-0954-43a2-bdb8-9c1a0e286393)

### Step 2 :
### Creating the Policy :


1. Navigate to the IAM Console.
2. Click on "Policies" and then Click on "Create policy"
![image (31)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/a0bf1583-eac9-42c0-b511-a2ae65f96b37)

3. Select services as EC2.
4. And Actions are DescribeInstances , StartInstances.
![image (32)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/2acdac48-3d04-4045-a33a-eae1e98ed38d)

![image (33)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/55a747c8-d304-47b4-b869-404d900748bf)
![image (34)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/58705f12-4cfd-41c6-96a5-bf20664a9f4a)
![image (35)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/0e7b2636-3b40-4045-ab48-d019e25d87ab)
![image (36)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/812ff10c-7c31-4483-bad9-26015298dfa3)
![image (37)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/f1889cb9-1c92-4d22-90e5-cd148428c746)

5. Now we have created a policy for starting instances. We also need to create a policy for stopping the instances. This is because we are going to create two Lambda functions: one for starting and one for stopping the instances. Each function will have its own role, and we will attach these two policies to their respective roles.<br>
6. Now  we are going to repeat the same steps for Creating Stopping Policy also.<br>
7. Everything is same , Except Actions because we are going to stop the instance.<br>
8. The Actions are DescribeInstances , StopInstances .<br>
9. Keep your Plolicy name as "stop-ec2-policy".

## Step 3 :
## Creating the Lambda functions :

1. Navigate to the lambda Console.
2. Follow the Outlined steps below.

![image (38)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/b0af78fe-1872-4394-bd06-8e3008639a8c)
![image (39)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/24ba37f7-ac09-46b2-9459-7dbb798e59b4)

![image (43)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/88c09c9b-42d3-4b6c-b942-d10b208243c3)

![image (45)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/ad2ce33c-a9fe-4a51-a113-135d6c778d66)

![image (47)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/8cd2f8f6-88e0-434a-9e4e-e7c3fce6fcfd)

![image (48)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/ef13b854-ad59-471f-8771-02967c6ea401)

![image (49)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/1a4dc1ec-1c01-4639-917a-a8395f3a545b)

![image (50)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/98c52735-725b-4a16-ae76-f66dc37e248b)

Now again , go to the Lambda console and then test the code.But before testing the code we must stop our instances to test the start function code.

![image (52)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/26fec017-6811-4caf-8407-24fcd293ea76)

3. Now we Created a lambda function for Starting Instance.
4. We have to Repeat the same steps again to Create a Lambda function for Stopping Instance , Keep your lambda function name as "stop-function".
5. The only changes we have to make are to replace the default code with the 'stop-function-code.py' code and attach the policy we created for stopping instances to the role of this Lambda function.

![image (56)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/22c90ccc-5f00-4052-9550-7f84cb409d1e)

6. As demonstrated above, when I test my Python code, it runs successfully and stops the instance.
7. Now, we are ready to proceed and create schedules for this functions.

### Step 5 :
### Creating the Schedules Using Cloud Watch :

1. Navigate to the Cloud Watch Console.
2. Follow the Outlined Steps below.

![image (57)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/9480750a-5865-4dc3-aac8-406c4bb81557)

![image (58)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/a8550035-df5b-4347-b5d7-a59dd8332ac9)

![image (73)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/0c943c89-ab41-4574-a54f-9bb8350509d7)

![image (60)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/c0c48bf7-6249-48cd-a14b-4290d7065e34)

![image (61)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/a905991b-c399-4217-ba58-bfa2edf6c572)

![image (62)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/f6669acd-b0b2-4a11-87aa-d206670e425f)

![image (63)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/ad9ababe-cfaa-439e-aec5-39ba3b11e7da)

![image (64)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/bd40e4aa-ff13-4f9e-a578-2f83f1fe23f0)

![image (65)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/ecb7eb16-30a7-4c55-86f7-e4be65e52cf3)

![image (66)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/1d937b8b-ff73-4ef3-8e23-d3839a5e6529)

![image (67)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/83fcaf7d-6df7-4ca0-a7bb-513b34905484)

![image (68)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/a7dbbcd5-6ded-4d77-8150-d93fd5a01603)

3. We have now created a schedule for starting the instance every day at 7:00 AM.<br>
4. Next, we need to create a schedule for stopping instances.<br>
5. To create the schedule for stopping instances, follow the same steps as for starting instance scheduling with a few changes, Keep your rule name as "stop-rule".<br>
6. The changes include modifying the scheduled time and selecting the appropriate scheduling function.<br>
7. We need to change the schedule time to 17:00 because it will stop the Lambda function at 17:00 IST (5:00 PM).

![31 03 2024_12 23 23_REC](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/94cdba34-8667-495e-ae6c-04be4fadda6d)

8. We have to Change the Function as stop-function.
   
![31 03 2024_12 23 00_REC](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/10509648-be8d-4e3e-aeea-7e0170ddc44e)

9. Now, we have successfully created two schedules: one to start the instance every day at 7:00 AM and the other to stop the instance every day at 5:00 PM.

9. Now, we have successfully created two schedules: one to start the instance every day at 8:00 AM and the other to stop the instance every day at 5:00 PM.

![image (69)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/01d09200-1af4-47e9-80a6-f9e7b4263de7)

### Step 6 :
### Creating the SNS for Notification :

1. Navigate to the Amazon SNS Console.
2. Follow the Outlined Steps below.
 
![image (70)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/a5112dd5-e498-4df9-9524-6141e4eb3997)

![image (72)](https://github.com/Pravnk57/Serverless-ec2-scheduler/assets/117705143/cee57ece-dbaf-4ecd-8fed-4632c1cf0386)




























