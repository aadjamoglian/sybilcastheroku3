import pymongo
import flask
import pprint
import pandas as pd
from sodapy import Socrata
from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import jsonify
import json
from flask_cors import CORS
import os.path
from flask import send_from_directory
from predict import predict_person
import joblib

# app = Flask(__name__, )
app = Flask(__name__)
# , static_url_path='/assets')
CORS(app)

assets_folder = os.path.join(app.root_path, 'assets')
@app.route('/assets/<path:filename>')
def assets(filename):
  # Add custom handling here.
  # Send a file download response.
  return send_from_directory(assets_folder, filename)


OutputData_folder = os.path.join(app.root_path, 'OutputData')
@app.route('/OutputData/<path:filename>')
def OutputData(filename):
  # Add custom handling here.
  # Send a file download response.
  return send_from_directory(OutputData_folder, filename)


@app.route("/", methods=['GET', 'POST'])
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

    # # Login info for lacity data access
    # client = Socrata("data.lacity.org",
    #              "GvIj0aUYYnBp2YRAZ2OHttpL6",
    #              username="jackantonyan@gmail.com",
    #              password="Ja142536$")

    # # Use limit variable to change number of records downloaded
    # results = client.get("63jg-8b9z", limit=2500000)

    # # 10 hottest, then 10 coldest days in the past 10 years
    # max_temps = ["2010-09-27", "2011-10-12", "2012-09-15", "2013-08-29", "2014-09-16", "2015-09-09", "2016-09-26", "2017-10-24", "2018-07-06", "2019-09-14"]
    # min_temps = ["2010-12-31", "2011-12-06", "2012-12-31", "2013-01-14", "2014-12-27", "2015-12-27", "2016-12-19", "2017-12-22", "2018-02-24", "2019-09-15"]
    # days = max_temps + min_temps

    # # Turn results into a dataframe
    # results_df = pd.DataFrame.from_records(results)
    # results_df['date_occ'] = pd.to_datetime(results_df['date_occ'])
    # results_df['date_occ'] = results_df['date_occ'].astype(str)

    # # Keep the relevant columns we need
    # new_results_df=results_df[['date_occ','time_occ','crm_cd','crm_cd_desc','area_name', 'lat', 'lon',]]

    # # filter records by days then put into seperate dataframe
    # df_date = new_results_df.set_index("date_occ")
    # df_final = df_date.loc[days]
    # df_final_fixed = df_final.reset_index()


    # # Turn dataframe into  dictionary
    # df_json_dict = df_final_fixed.to_dict(orient="records")

    # Mongo client using mLab
    # mongo_client = pymongo.MongoClient("mongodb+srv://dbUser:SybilCast@cluster0-vk9sm.mongodb.net/test?retryWrites=true&w=majority")

    # # initializing mongo
    # mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
    # db = mongo_client.crime_db
    # col = db["crime_data"]

    # # Drops "crime_data" database if one exists already
    # if col.count() > 0:
    #     col.drop()

    # # Creates mongo db from df_json_dict, 
    # # page returns data in json fomrat to "/" app route
    # db = mongo_client.crime_db
    # col = db["crime_data"]
    # col.insert(df_json_dict)
    # final = col.find()
    # finals = []
    # for j in final:
    #     j.pop('_id')
    #     finals.append(j)
    # return jsonify(finals)

@app.route("/data", methods=['GET', 'POST'])
def data():

    # app.config['MONGO_DBNAME'] = 'crime_db'
    # app.config['MONGO_URI'] = 'mongodb+srv://dbUser:SybilCast@cluster0-vk9sm.mongodb.net/test?retryWrites=true&w=majority'

    # uri = 'mongodb+srv://dbUser:SybilCast@cluster0-vk9sm.mongodb.net/test?retryWrites=true&w=majority'

    # client = MongoClient(uri,
    #                  connectTimeoutMS=30000,
    #                  socketTimeoutMS=None,
    #                  socketKeepAlive=True)

    # db = client.get_default_database()
    # print (db.collection_names())

    mongo_client = pymongo.MongoClient('mongodb+srv://dbUser:SybilCast@cluster0-vk9sm.mongodb.net/test?retryWrites=true&w=majority')
    db = mongo_client.crime_db
    col = db["crime_data"]
    final = col.find()
    finals = []
    for j in final:
        j.pop('_id')
        finals.append(j)
    return jsonify(finals)

# @app.route('/predictions', methods=['GET, POST'])
# def predictions():
#     render_template('predictions.html')

@app.route("/predictions", methods=['GET', 'POST'])
def render_predictions() -> "html":
    return render_template("predictions.html")

@app.route("/home", methods=['GET', 'POST'])
def render_home():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 