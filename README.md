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


















