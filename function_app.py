import azure.functions as func
import logging

from io import BytesIO
import barcode
from barcode.writer import ImageWriter

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

BARCODE_TYPE = 'Code128'
    
@app.route(route="generatebarcode/{barcodenumber}")
def generatebarcode(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    barcode_number = req.route_params.get('barcodenumber')
    '''if len(barcode_number) != 14:
        raise func.HTTPException(status_code=400, detail="EAN-13 barcode number must be 12 digits long.")'''

    #try:
    if(1):
        # Create the barcode with an ImageWriter to generate an image
        ean = barcode.get(BARCODE_TYPE, barcode_number, writer=ImageWriter)

        # Use BytesIO to store the barcode image in memory
        barcode_io = BytesIO()

        options = {
            'module_width': .28,  # Adjust the width of each barcode module
            'module_height': 12.0,  # Adjust the height of the barcode
            'quiet_zone': 0,       # Minimal quiet zone around the barcode
            'font_size': 8,       # Font size for the text below the barcode
            'text_distance': 4,    # Space between the barcode and the text
            'dpi': 200             # DPI to control the resolution
            #,'format' : 'PNG'
        }

        ean.write(barcode_io, options=options)

        # Reset the pointer to the start of the BytesIO object
        barcode_io.seek(0)


        # Return the barcode as a PNG image
        return func.HttpResponse(
            barcode_io.getvalue()
            ,mimetype='image/svg'
            )
    
    #except Exception as e:
    #    return func.HttpResponse(str(e) + " " + str(barcode_number) + " " + str(type(barcode_number)))
        