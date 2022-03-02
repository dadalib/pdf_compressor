# import the ilovepdf api
from pylovepdf.ilovepdf import ILovePdf

PDF_NAME_FILE = 'my_pdf.pdf'
OUTPUT_NAME_FOLDER = 'output_folder'

# public key from https://developer.ilovepdf.com/login
# key provide in the following link https://developer.ilovepdf.com/user/projects
public_key = 'my_public_key'

# creating a IlovePdf object
ilovepdf = ILovePdf(public_key, verify_ssl=True)

# assigning a new compress task
task = ilovepdf.new_task('compress')

# adding the pdf file to the task
task.add_file(PDF_NAME_FILE)

# setting the output folder directory
# if no folder exist it will create one
task.set_output_folder(OUTPUT_NAME_FOLDER)

# execute the task
task.execute()

# donwload the task compress_date
task.download()

# delete the task
task.delete_current_task()
