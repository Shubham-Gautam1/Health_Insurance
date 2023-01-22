from flask import Flask,render_template,request
import pickle,json
import numpy as np

with open('files/Linear_model.pkl','rb') as file:
    model = pickle.load(file)

with open('files/project_data.json') as file:
    data = json.load(file)



app = Flask(__name__)

@app.route('/')


@app.route('/Homepage')
def Homepage():
    return render_template('home.html')

@app.route('/submit',methods=['GET'])
def submit():

    age = request.args.get('age')
    sex = request.args.get('sex')
    bmi = request.args.get('bmi')
    children = request.args.get('children')
    smoker = request.args.get('smoker')
    region = request.args.get('region')

    my_region = 'region_' + region
    region_index = data['columns'].index(my_region)

    array = np.zeros(len(data['columns']))
    array[0]=age
    array[1]=data['sex'][sex]
    array[2]=bmi
    array[3]=children
    array[4]=data['smoker'][smoker]
    array[region_index]=1

    pred = model.predict([array])[0].round(0)

    return "<center><h1>Medical Health Insurance</h1></center> Age: {}, Sex: {}, BMI: {}, Children: {}, Smoker: {}, Region: {}<br><br>Premium: {}".format(age,sex,bmi,children,smoker,region,pred)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)