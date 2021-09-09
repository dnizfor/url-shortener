
from flask import render_template, request ,redirect
from .functions import is_url ,idMaker
from . import db ,models ,app
from .forms import shortLink


@app.route("/", methods = ["GET","POST"])
def home():
    form = shortLink()
    if request.method == "GET" : 
        return render_template("/base.html",form=form)
    else : 
        long_url = request.form.get("long_url")
        long_url = is_url(long_url)
        if  long_url == False :
            return render_template("/base.html",form=form,flash="False URL")
        
        
        

        short_url = idMaker()
        link = models.Link(long_url=long_url, short_url = short_url)
        db.session.add(link)
        db.session.commit()
        return render_template("/base.html",form=form,flash="<YOUR_DOMAİN>/" + short_url)
        

@app.route("/<id>", )
def redirc(id):
    rdrc = models.Link.query.filter_by(short_url=id).first()
    if(rdrc is None) :
        return redirect("/",code=301)
    else : 
        url = rdrc.long_url
        if(url[0:7] == "http://" or url[0:8] == "https://" ) :
            return redirect(url,code=301)

        return redirect("http://"+url,code=301)
   


  

@app.errorhandler(404)
def page_not_found(e):
    return "Page is not here .", 404