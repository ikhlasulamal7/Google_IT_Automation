#!/usr/bin/env python3

import datetime
import os

from run import catalog_data
from reports import generate_report
from emails import generate as generate_email
from emails import send as send_email

def pdf_body(input_for,desc_dir):
    res = []
    wt = []
    for item in os.listdir(desc_dir):
        filename = os.path.join(desc_dir,item)
        with open(filename) as f:
            line = f.readlines()
            weight = line[1].strip('\n')
            name = line[0].strip('\n')
            print(name,weight)
            res.append('name: ' +name)
            wt.append('weight: ' +weight)
            print(res)
            print(wt)
    new_obj = ""
    for i in range(len(res)):
        if res[1] and input_for == 'pdf':
            new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_obj

if __name__ == "__main__":
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    current_date = datetime.date.today().strftime("%B %d, $Y")
    title = 'Processed Update on ' + str(current_date)
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf',description_directory))
    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email'
    msg = generate_email("automation@example.com", "student-00-a386de18887c@example.com", email_subject, email_body, "/tmp/processed.pdf")
    send_email(msg)