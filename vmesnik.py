import bottle
import stiri_v_vrsto

Igra=stiri_v_vrsto.Igra()
Naslov = stiri_v_vrsto.Igra()

@bottle.get("/")
def tece() :
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/<stolpec:int>/")
def vstavljanje(stolpec):
    Igra.potek(stolpec)
    bottle.redirect("/")


@bottle.post("/nova/")
def nova():
    Igra.nova_igra()
    bottle.redirect("/")

         
    
bottle.run(reloader=True , debug=True)
