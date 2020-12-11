from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
#%%
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = False)
conn = engine.connect()

#%%
app = Flask(__name__)

#%%
@app.route('/')
def home():
    return(
        f"Welcome to the Hawaii Climate App API!<br/>"
        f"Available Rountes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/apit/v1.0/<start>/<end><br/>"
    )

#%%
@app.route('/api/v1.0/precipitation')
def precipitation():
    engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = False)
    conn = engine.connect()

    query = '''
    select date, prcp 
    from measurement 
    where date >= (select date(max(date), '-1 year') from measurement)

    '''

    measurement = pd.read_sql(query, conn)
   # measurement_df = measurement.set_index('date')

   # Sort the dataframe by date
   # prcp_data = measurement_df.sort_index()

    data_measurement = measurement.to_json(orient='records')
    return(data_measurement)

#%%
@app.route('/api/v1.0/stations')
def stations():
    engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = False)
    conn = engine.connect()
    
    station_df = pd.read_sql('select station from station', conn)
    
    data_station_json = station_df.to_json(orient='records')
    return(data_station_json)

#%%
@app.route('/api/v1.0/tobs')
def tobs():
    
    engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = False)
    conn = engine.connect()
    
    query = '''
       select 
          name, 
          count(station) as active_count 
       from measurement 
       join station 
       using (station) 
       group by name
       order by count(station) desc
    '''

    active_station = pd.read_sql(query, conn)

    station_names = active_station['name']
    most_active_station = station_names.iloc[0]
    
    query = f'''
      select 
          tobs
      from measurement
      join station
      using (station)
      where 
          date >= (select date(max(date), '-1 year') from measurement)
          and name = '{most_active_station}'
     '''
 
    tobs_df = pd.read_sql(query, conn)
    
    data_tobs_json = tobs_df.to_json(orient='records')
    return(data_tobs_json)

#%%
@app.route('/api/v1.0/<start>')
def calc_temps_start(start_date):
    engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = False)
    conn = engine.connect()
   
    query = f'''
    select 
        min(tobs) as min_temp,
        avg(tobs) as avg_temp,
        max(tobs)as max_temp
    from measurement
    join station
    using (station)
    where date >= '{start_date}'
    '''
    temp_stats_start_df = pd.read_sql(query, conn)
    
    return temp_stats_start_df
#%%
@app.route('/api/v1.0/<start>/<end>')
def calc_temps(start_date, end_date):
    
    engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo = False)
    conn = engine.connect()
   
    query = f'''
    select 
        min(tobs) as min_temp,
        avg(tobs) as avg_temp,
        max(tobs)as max_temp
    from measurement
    join station
    using (station)
    where date between '{start_date}' and '{end_date}'
    '''
    temp_stats_df = pd.read_sql(query, conn)
    
    return temp_stats_df
#%%
#if __name__ == '__main__':
#    app.run(debug=True)



