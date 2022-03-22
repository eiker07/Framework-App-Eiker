from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.page import Page

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model2 = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/autor', methods=['GET'])
def autor():
    return render_template('autor.html')


@app.route('/autor_detail', methods=['POST'])
def person_detail():
    id_page = request.form['id_page']
    titulo = request.form['titulo']
    n_pagina = request.form['n_pagina']
    autor=request.form['autor']
    p = Page(id_page=id_page, titulo=titulo, n_pagina=n_pagina, autor=autor)
    model2.append(p)
    return render_template('autor_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/file')
def file():
    data = [(i.id_page, i.titulo, i.n_pagina, i.autor) for i in model2]
    print(data)
    return render_template('file.html', value=data)


if __name__ == '__main__':
    app.run()