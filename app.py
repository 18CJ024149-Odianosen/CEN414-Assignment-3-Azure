from flask import Flask, redirect, render_template
from pymongo import MongoClient

import pandas as pd
import numpy as np
from plots import *

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/refresh_plots', methods=['GET'])
def refresh_plots():


    
    #get and mutate dataframe 
    for i in range(1,10):
        df = pd.read_csv(f'Homicide{i}_Database.csv')

        df.pivot_table(index='Country', columns = 'Sex', values = f'{2009+i}').plot(kind = 'bar', figsize=(15,5))

        plt.xlabel('Country')
        plt.ylabel(f'{2009+i}')
        plt.title('Homicides Male and Female Count per 100,000')
        plt.legend(loc='upper right')
        plt.savefig(f'./static/images/Azure{i}.png')
        # plt.show()
        
    #generate plots

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)