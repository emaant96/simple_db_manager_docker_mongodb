from bottle import Bottle, template, request
import pymongo

app = Bottle()
client = pymongo.MongoClient("mongodb:27017")
db = client["database"]
tabella = db["cibo"]

def main():
	init(tabella)
	app.run(host='0.0.0.0')

def init(tabella):
	if tabella.find().count() == 0:
		listaDoc = [
			{"tipo": "frutta", "nome": "mele"},
			{"tipo": "frutta", "nome": "pere"},
			{"tipo": "frutta", "nome": "arance"},
			{"tipo": "frutta", "nome": "limoni"},
			{"tipo": "verdura", "nome": "insalata"},
			{"tipo": "verdura", "nome": "carote"},
			{"tipo": "verdura", "nome": "broccoli"},
			{"tipo": "verdura", "nome": "cavoli"}
		]
		tabella.insert_many(listaDoc)

def show_food(tabella,tipo):
	query = {"tipo": tipo}
	risultato = tabella.find(query)
	return risultato

def delete_food(tabella,tipo,nome):
	query = {"tipo": tipo, "nome": nome}
	tabella.delete_one(query)

def add_food(tabella,tipo,nome):
	doc = {"tipo":tipo,"nome":nome}
	tabella.insert_one(doc)

@app.route('/')
def index():
    return template("form.tpl", message="Seleziona l'azione e compila i campi")

@app.route('/', method="POST")
def formhandler():
	action = request.forms.get('azione')
	tipo = request.forms.get('tipo')
	nome = request.forms.get('nome')

	if action == "delete":
		delete_food(tabella,tipo,nome)
		print("cancellato")
		return template("form.tpl", message="elemento {" + tipo + ": " + nome + "} cancellato correttamente")

	elif action == "add":
		add_food(tabella,tipo,nome)
		print("inserito")
		return template("form.tpl", message="elemento {" + tipo + ": " + nome + "} inserito correttamente")	

	elif action == "show":
		risultato = show_food(tabella,tipo)
		messaggio = "elementi di tipo " + tipo + " presenti nel database: "
		for x in risultato:
			messaggio = messaggio + "{" + x["tipo"] + ": " + x["nome"] + "}"
		return template("form.tpl", message=messaggio)


if __name__ == "__main__":
    main()