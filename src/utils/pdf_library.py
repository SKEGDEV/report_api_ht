import pdfkit
import base64
from os import getenv
from datetime import datetime as time
from flask import render_template

class objt_reportLibrary():

    def __init__(self, rpt_name:str, rpt_data:dict):
        self.name = rpt_name
        self.data = rpt_data

    def file2base64(self, file):
        with open(file, 'rb') as file64:
            return base64.b64encode(file64.read()).decode()       

    def make_template(self):
        today = time.now() 
        if(self.name == "qa"):
            return render_template("qualification.html", header=self.data.get("q_header"), qualifications=self.data.get("o_qualification"), date=today)
        if(self.name == "ap"):
            return render_template("apretitation.html")
        if(self.name == "ct"):
            return render_template("cotejo_list.html")


    def make_pdf(self):
        try:
            config = pdfkit.configuration(wkhtmltopdf=getenv('pdf_convert'))
            pdf = pdfkit.from_string(self.make_template(), False, css=[], configuration=config)
            pdfBase64 = self.file2base64(pdf)
            return{
                    "msm":"success",
                    "rpt":pdfBase64
                    }
        except Exception as e:
            return{
                    "msm":"Ocurrio un error durante la generacion del reporte",
                    "err":str(e)
                    }
