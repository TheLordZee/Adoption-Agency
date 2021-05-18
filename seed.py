from models import * 
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name='Bobby Fishers', species='fish', photo_url='https://www.peta.org/wp-content/uploads/2019/08/iStock-1160758684_NONTANUN-CHAIPRAKON-1-602x301.jpg', age=3, notes="The only fish I know tha can beat you at chess, and it doesn't even have hands", available=True)

p2 = Pet (name='Taxo', species='dog', photo_url='https://yt3.ggpht.com/ytc/AAUvwnhFY3d8qOpu-KNOALIzsq4ECnGwTPwWmVVpkdM9Fg=s900-c-k-c0x00ffffff-no-rj', age=3, notes='Iz a very good boi, like all doggies are.', available=True)

p3 = Pet (name='Tomatoe', species='hedgehog', photo_url='https://dcist.com/wp-content/uploads/sites/3/2018/11/hedgehogs2018-1500x1037.jpg', age=1, notes='', available=True)

p4 = Pet (name='Peanut Butter', species='dog', photo_url='https://dogtime.com/assets/uploads/2019/11/beaglier-mixed-dog-breed-pictures-cover-650x368.jpg', notes='', available=False)

p5 = Pet (name='Final Braincell', species='fish', age= 1, notes="iz a fishy", available=True)

db.session.add_all([p1,p2,p3,p4,p5])
db.session.commit()