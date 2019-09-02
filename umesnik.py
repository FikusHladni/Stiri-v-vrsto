import bottle
import stiri_v_vrsto

Igra=stiri_v_vrsto.Igra()
Naslov = stiri_v_vrsto.Igra()

@bottle.get("/")
def tece() :
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/0/")
def vstavljanje1():
    Igra.potek(0)
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/1/")
def vstavljanje2():
    Igra.potek(1)
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/2/")
def vstavljanje3():
    Igra.potek(2)
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/3/")
def vstavljanje4():
    Igra.potek(3)
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/4/")
def vstavljanje5():
    Igra.potek(4)
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/5/")
def vstavljanje6():
    Igra.potek(5)
    return bottle.template("template.tpl", Igra = Igra)

@bottle.post("/6/")
def vstavljanje7():
    Igra.potek(6)
    return bottle.template("template.tpl", Igra = Igra)


@bottle.post("/7/")
def nova():
    Igra.nova_igra()
    return bottle.template("template.tpl" , Igra = Igra)
    
    
    

# @bottle.get("/igra/")
# def test_index():
#     return bottle.template('igra.html',id_igra = id, ,stanje = stanje)





    
    

# @bottle.post("/nova_igra/")
# def ugibaj_2 ():
#     id_igre = int(bottle.request.get_cookie("id_igre"))
#     crka = bottle.request.forms.getunicode("crka")
#     vislice.ugibaj(id_igre,crka)
#     bottle.redirect("/igra/")

# @bottle.post("/igra/<id_igre:int>/")
# def ugibaj (id_igre):
#     crka = bottle.request.forms.getunicode("crka")
#     vislice.ugibaj(id_igre,crka)
#     bottle.redirect("/igra/{0}/".format(id_igre))
    

    

bottle.run(reloader=True , debug=True)
