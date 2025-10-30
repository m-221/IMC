from flask import Flask,render_template,request,redirect
app = Flask(__name__)
@app.route('/')
def cal():
    return render_template('imc.html')

@app.route('/result',methods=['POST'])
def result():
    if request.method=='POST':
        peso=int(request.form['num1'])
        altura=int(request.form['num2'])
        operation=request.form['operacion']
        if operation=='imc':
            pya=altura/100
            result = peso / (pya ** 2)
        
            return render_template('result.html',result=result,pya=pya)
        return render_template('calculo.html')
