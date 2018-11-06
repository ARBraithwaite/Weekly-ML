from PIL import Image
from io import BytesIO
import base64

from IPython.display import HTML
import pandas as pd


def pil_to_base64(img:Image)->str:
    with BytesIO() as buffer:
        img.save(buffer, 'jpeg')
        return base64.b64encode(buffer.getvalue()).decode()

def display_dataframe(df:pd.DataFrame, original_col_width:int=50)->str:
    '''Generates and displays and HTML version of the dataframe with inline images.'''
    pd.set_option('display.max_colwidth',-1)
    visaual_dataframe = HTML(df.to_html(formatters={
         'array':lambda x: f'A numpy array of shape {x.shape} and dtype {x.dtype}', 
        'image': lambda x: f"""<img src="data:image/jpeg; base64, {pil_to_base64(x)}" alt="Black box">"""},escape=False))
    pd.set_option('display.max_colwidth', original_col_width)
    return visaual_dataframe

