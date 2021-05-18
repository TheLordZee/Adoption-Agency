from flask import *
from flask_debugtoolbar import *
from models import *
from forms import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "DUIEHE8effEWjfde8HPu7"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home():
    """Shows home page"""

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/pets/new', methods=["GET","POST"])
def add_pet():
    """Allows a user to add a pet to the site"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)


@app.route('/pets/<int:p_id>')
def show_pet(p_id):
    """Shows Pet Info Page"""
    pet = Pet.query.get_or_404(p_id)
    return render_template('pet.html', pet=pet)

@app.route('/pets/<int:p_id>/edit', methods=["GET", "POST"])
def edit_pet(p_id):
    """Allows user to edit a pet"""
    pet = Pet.query.get_or_404(p_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/pets/{p_id}')
    else:
        return render_template('edit-pet.html', form=form, pet=pet)