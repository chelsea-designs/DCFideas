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
    idea_teacher = db.Column(db.String(50), unique=True, nullable=False)
    idea_description = db.Column(db.Text, nullable=False)
    strand_id = db.Column(db.Integer, db.ForeignKey("strand.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Idea: {1}".format(
            self.id, self.idea_name
        )

class Users(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name