class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    #get name
    def get_name(self):
        return self.name

        # get tracks
    def get_tracks(self):
        return self.tracks
        
        # get score
    def get_score(self):
        return self.score
    #change name
    def change_name(self, new_name):
        if type(new_name) == str: #type checking for name property
            self.name = new_name
        else:
            raise Exception("Invalid value for name")
    
    # change age
    def change_age(self, new_age):
        if type(new_age) == int: #type checking for name property
            self.age = new_age
        else:
            raise Exception("Only integer value accepted")

      # Add track
    def add_track(self, new_track):
        if type(new_track) == str: #type checking for name property
            self.tracks.append(new_track)
        else:
            raise Exception("Only string value accepted")
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())

print(Bob.get_tracks())