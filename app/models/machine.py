class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    exercise = relationship("Exercise")
    
    name = db.Column(db.Integer, nullable=False)
    
    
