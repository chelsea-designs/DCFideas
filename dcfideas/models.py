from dcfideas import db


class Strand(db.Model):
    # schema for the Strand model
    id = db.Column(db.Integer, primary_key=True)
    strand_name = db.Column(db.String(25), unique=True, nullable=False)
    ideas = db.relationship("Idea", backref="strand", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.strand_name

class Element(db.Model):
    # schema for the Element model
    id = db.Column(db.Integer, primary_key=True)
    element_name = db.Column(db.String(25), unique=True, nullable=False)
    ideas = db.relationship("Idea", backref="element", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.element_name

class Aole(db.Model):
    # schema for the Element model
    id = db.Column(db.Integer, primary_key=True)
    aole_name = db.Column(db.String(25), unique=True, nullable=False)
    ideas = db.relationship("Idea", backref="aole", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.aole_name

class Camcynnydd(db.Model):
    # schema for the Element model
    id = db.Column(db.Integer, primary_key=True)
    camcynnydd_name = db.Column(db.String(25), unique=True, nullable=False)
    year_name = db.Column(db.Integer, nullable=False)
    ideas = db.relationship("Idea", backref="camcynnydd", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "Cam Cynydd:{0} - Year: {1}".format(
            self.camcynnydd_name, self.year_name
        )

class Idea(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    idea_name = db.Column(db.String(50), unique=True, nullable=False)
    idea_teacher = db.Column(db.String(50), unique=True, nullable=False)
    idea_description = db.Column(db.Text, nullable=False)
    element_id = db.Column(db.Integer, db.ForeignKey("element.id", ondelete="CASCADE"), nullable=False)
    strand_id = db.Column(db.Integer, db.ForeignKey("strand.id", ondelete="CASCADE"), nullable=False)
    aole_id = db.Column(db.Integer, db.ForeignKey("aole.id", ondelete="CASCADE"), nullable=False)
    camcynnydd_id = db.Column(db.Integer, db.ForeignKey("camcynnydd.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Idea: {1} | Urgent: {2}".format(
            self.id, self.idea_name, self.is_urgent
        )