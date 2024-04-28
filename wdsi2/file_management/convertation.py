import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def xlsxToDataFrame(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print("An error occurred while converting xsltToDataFrame:", e)
        return None
    

def dataframeToPdf(df, pdfName):
    fig, ax =plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values,colLabels=df.columns,loc='center')

    pp = PdfPages(pdfName)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    
