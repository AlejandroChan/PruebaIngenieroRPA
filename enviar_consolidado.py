# install the following libraries using pip
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import smtplib

# change this path to the proper datapath where files are located
data_path = "/Users/alejandrochanduvi/Downloads/Boletas"
pdf_path = "/Users/alejandrochanduvi/Documents/consolidado.pdf"

def send_email_pdf_figs(path_to_pdf, subject, message, destination, sender, password=None):
    ## credits: http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script
    from socket import gethostname
    #import email
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import json

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, password)
    # Craft message (obj)
    msg = MIMEMultipart()

    message = f'{message}\nSend from Hostname: {gethostname()}'
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = destination
    # Insert the text to the msg going by e-mail
    msg.attach(MIMEText(message, "plain"))
    # Attach the pdf to the msg going by e-mail
    with open(path_to_pdf, "rb") as f:
        #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
    msg.attach(attach)
    # send msg
    server.send_message(msg)

    
def main():
    # reading files
    list_df = []
    for name in glob.glob(os.path.join(data_path, "*.txt")):
        print(name)
        df_tmp = pd.read_csv(name, sep=":", header=None, index_col=0).T
        list_df.append(df_tmp)
    df = pd.concat(list_df).reset_index(drop=True)
    df = df.fillna(0)
    
    # generating PDF
    fig, ax =plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')

    pp = PdfPages(pdf_path)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    
    # sending email 
    # TO-DO uncomment for sending email
    # send_email_pdf_figs(pdf_path, "Boletas de Pago", "Adjunto consolidado de boletas de pago", "destinatario@gmail.com", "enviador@gmail.com", password="dummy")
   
# for running the script: `python enviar_consolidado.py`

if __name__ == "__main__":
    main()