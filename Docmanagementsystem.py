'''You are the operation manager at a training institute,Each trainer submits a .txt file daily with session summaries
>collect these reports
>Read and verify content
>Organise files into data-wise folders
>Backup the day's reports'''
#step1: create a directory structure for report submission
import os
from datetime import datetime
import shutil
#create directories
os.makedirs('training_reports/daily_reports',exist_ok=True)
os.makedirs('training_reports/backup',exist_ok=True)
print("Directory structure created succesfully")

#step2: Simulate trainer report submission(write multiple file)
trainers=['SB','Sai','Anjali','Somu']
for trainer in trainers:
    with open(f'training_reports/daily_reports/{trainer}_report.txt','w')as f:
        f.write(f"Trainer:{trainer}\nDate:2025-06-16\nTopic:File handling using python")
print("Sample trainer report created")
#step3:Read and verify trainer repoerts
report_dir='training_reports/daily_reports'
for filename in os.listdir(report_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(report_dir,filename),'r') as file:
            print(f"\nReading {filename}:")
            print(file.read())
#rename reports to include date(SB_20250616)
#datetime is used to change the date and automatically
date_str=datetime.now().strftime('%y-%m-%d')
for filename in os.listdir(report_dir):
    if filename.endswith('.txt'):
        name_part=filename.split('_')[0]
        new_name=f'{name_part}_{date_str}.txt'
        os.rename(
            os.path.join(report_dir,filename),
            os.path.join(report_dir, new_name)
        )
print("reports renamed with date")
#step5:move reports to date-wise folder
dated_folder=f'training_reports/daily_reports/{date_str}'
os.makedirs(dated_folder,exist_ok=True)
for filename in os.listdir(report_dir):
    if filename.endswith('.txt'):
        shutil.move(
            os.path.join(report_dir,filename),
            os.path.join(dated_folder,filename)
        )
print(f"reports moved sucessfully:{dated_folder}")
#step 6:automate daily backup of report
backup_folder=f'training_reports/backup/backup_{date_str}'
os.makedirs(backup_folder,exist_ok=True)
#copy all files from date folder to backup
for filename in os.listdir(dated_folder):
    shutil.copy(
        os.path.join(dated_folder,filename),
        os.path.join(backup_folder,filename)
    )
print("Backup successfull")