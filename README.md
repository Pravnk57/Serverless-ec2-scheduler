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

