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

class Idea(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
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
            self.id, self.idea_name
        )