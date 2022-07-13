from dcfideas import db

class Strand(db.Model):
    # schema for the Strand model
    id = db.Column(db.Integer, primary_key=True)
    strand_name = db.Column(db.String(50), unique=False, nullable=False)
    strand_element = db.Column(db.String(50), unique=True, nullable=False)
    ideas = db.relationship("Idea", backref="strand", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.strand_name

class Subject(db.Model):
    # schema for the Subject model
    id = db.Column(db.Integer, primary_key=True)
    aole = db.Column(db.String(50), unique=False, nullable=False)
    subject = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Area of Learning: {1} - Subject: {2}".format(
            self.id, self.aole, self.subject
        )

class Idea(db.Model):
    # schema for the Task model
    idea_name = db.Column(db.String(50), unique=True, nullable=False)
    cam_cynnydd = db.Column(db.Integer, unique=False, nullable=False)
    idea_description = db.Column(db.Text, nullable=False)
    subject = db.Column(db.String(50), unique=False, nullable=False)
    strand_id = db.Column(db.Integer, db.ForeignKey("strand.id", ondelete="CASCADE"), nullable=False)
    created_by = db.Column(db.String(50), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)
    idea_resource = db.Column(db.VARCHAR(500), unique=False, nullable=False)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Idea: {1}".format(
            db.Column(db.Integer, primary_key=True), self.idea_name
        )

class Users(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username