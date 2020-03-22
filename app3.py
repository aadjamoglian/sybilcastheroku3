import flask
from flask import Flask, render_template, request
import joblib
import pandas as pd
from predict import predict_person
app = Flask(__name__, template_folder='templates') #template_folder='templates'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return(flask.render_template('prediction.html'))
    if request.method == 'POST':
        vict_age = int(request.form['vict_age'])

        # Extract only the first letter from descent
        vict_sex = str(request.form['vict_sex'])[0]
        print(str(vict_sex))

        # Extract only the first letter from descent
        vict_desc = str(request.form['vict_desc'])[0]
		
        vict_premise = str(request.form['prem_desc'])
        vict_lat = float(request.form['vict_lat'])
        vict_lon = float(request.form['vict_lon'])
        vict_area = str(request.form['areaName'])
        
        # Day and Season MUST be lowercase
        vict_day = str(request.form['day']).lower()
        vict_season = str(request.form['season']).lower()
       

        input_variables = pd.DataFrame([[vict_age, vict_sex, vict_desc, vict_lat, vict_lon, vict_area, 
                                        vict_day, vict_season, vict_premise]],
                                       columns=['age','sex','descent','lat','lon','area','day','season','premise']) #dtype=float
        print(input_variables)
        prediction = predict_person(vict_age, vict_sex, vict_desc, vict_premise, vict_lat, vict_lon, vict_area, vict_season, vict_day)
        main_prediction = list(prediction.keys())[0]
        return flask.render_template('prediction.html',
                                     original_input={'Age':vict_age,
                                                     'Sex':vict_sex,
                                                     'Descent':vict_desc,
                                                     'Lat': vict_lat,
                                                     'Lon': vict_lon,
                                                     'Area': vict_area,
                                                     'Day/Night': vict_day, 
                                                     'Season' : vict_season, 
                                                     'Premise Desc': vict_premise
                                                     },
                                    result=prediction,
                                    main_predict = main_prediction
                                     )
if __name__ == '__main__':
    app.run(debug=True, port = 5502)