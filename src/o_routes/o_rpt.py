from src.utils.pdf_library import objt_reportLibrary

class o_rpt():

    def __init__(self, o_request):
        self.oRequest = o_request

    def generateRpt(self):  
        try:
            rpt_name = self.oRequest['oRpt']['rpt_type'] 
            if(not self.is_availableRpt(rpt_name)):
                return{
                    "msm":"Ocurrio un error inesperado",
                    "err":"El reporte que desea generar no existe o no esta disponible, por favor contacte con nuestro soporte de IT"
                    }
            o_data = self.oRequest['oData'] 
            return objt_reportLibrary(rpt_name, o_data).make_pdf()
        except Exception as e:
            return{
                    "msm":"Un error inesperado ha ocurrido",
                    "err":str(e)
                    }

    def is_availableRpt(self, rpt:str):
        if(rpt == "qa"):
            return True
        if(rpt == "ap"):
            return True
        if(rpt == "ct"):
            return True
        return False
