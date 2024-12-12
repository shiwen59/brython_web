"""
Final
Author: Susan E. Liao
"""
# IMPORT STATEMENTS
import random


# CLASS DEFINITIONS 
class Person():
    def __init__(self, name, birthyear, father, mother, sex):
        self.name = name
        self.birthyear = birthyear
        self.father = father
        self.mother = mother
        self.sex = sex
        
def print_tree(person,generation=0):
    if generation<3:
        print(person.name,person.father.name,
              person.mother.name,person.birthyear,person.sex, generation)
        print_tree(person.mother,generation+1) 
        print_tree(person.father,generation+1) 
    else:
        print(person.name, person.birthyear,person.sex, generation)

def gen_person(name,generation,sex):
    birthyear=2004-30*generation+(len(name)%5)
    if generation==3:
        father=None
        mother=None
    else:
        father_name=male_names.pop()
        mother_name=female_names.pop()
        father=gen_person(father_name,generation+1,"male")
        mother=gen_person(mother_name,generation+1,"female")
    return Person(name,birthyear,father,mother,sex)

class Submarine:
    # attributes of each car
    def __init__(self):
        self.color = 'AliceBlue'
        self.current_speed = 0
        self.top_speed = 483 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate

    # report car color
    def get_color(self):
        return self.paint_color

    # report distance traveled
    def distance(self):
        return self.distance_traveled


class HotAirBalloon:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'AntiqueWhite'
        self.current_speed = 0
        self.top_speed = 455 # feet per second
        self.acceleration_rate = 110 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def get_color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class Scooter:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Aqua'
        self.current_speed = 0
        self.top_speed = 476 # feet per second
        self.acceleration_rate = 100 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate

    # report car color
    def get_color(self):
        return self.paint_color

    # report distance traveled
    def distance(self):
        return self.distance_traveled


class Jetpack:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Aquamarine'
        self.current_speed = 0
        self.top_speed = 463 # feet per second
        self.acceleration_rate = 102 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def get_color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class Bicycle:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Azure'
        self.current_speed = 0
        self.top_speed = 458 # feet per second
        self.acceleration_rate = 120 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def get_color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class Raft:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Brown'
        self.current_speed = 0
        self.top_speed = 414 # feet per second
        self.acceleration_rate = 109 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class Sled:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Orange'
        self.current_speed = 0
        self.top_speed = 475 # feet per second
        self.acceleration_rate = 125 # feet per second
        self.distance_traveled = 5

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


# GLOBAL VARIABLES
male_names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi', 'Sebastian', 'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew', 'Luke', 'Asher', 'Carter', 'Julian', 'Grayson', 'Leo', 'Jayden', 'Gabriel', 'Isaac', 'Lincoln', 'Anthony', 'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles', 'Christopher', 'Jaxon', 'Maverick', 'Josiah', 'Isaiah', 'Andrew', 'Elias', 'Joshua', 'Nathan', 'Caleb', 'Ryan', 'Adrian', 'Miles', 'Eli', 'Nolan', 'Christian', 'Aaron', 'Cameron', 'Ezekiel', 'Colton', 'Luca', 'Landon', 'Hunter', 'Jonathan', 'Santiago', 'Axel', 'Easton', 'Cooper', 'Jeremiah', 'Angel', 'Roman', 'Connor', 'Jameson', 'Robert', 'Greyson', 'Jordan', 'Ian', 'Carson', 'Jaxson', 'Leonardo', 'Nicholas', 'Dominic', 'Austin', 'Everett', 'Brooks', 'Xavier', 'Kai', 'Jose', 'Parker', 'Adam', 'Jace', 'Wesley', 'Kayden', 'Silas', 'Bennett', 'Declan', 'Waylon', 'Weston', 'Evan', 'Emmett', 'Micah', 'Ryder', 'Beau', 'Damian', 'Brayden', 'Gael', 'Rowan', 'Harrison', 'Bryson', 'Sawyer', 'Amir', 'Kingston', 'Jason', 'Giovanni', 'Vincent', 'Ayden', 'Chase', 'Myles', 'Diego', 'Nathaniel', 'Legend', 'Jonah', 'River', 'Tyler', 'Cole', 'Braxton', 'George', 'Milo', 'Zachary', 'Ashton', 'Luis', 'Jasper', 'Kaiden', 'Adriel', 'Gavin', 'Bentley', 'Calvin', 'Zion', 'Juan', 'Maxwell', 'Max', 'Ryker', 'Carlos', 'Emmanuel', 'Jayce', 'Lorenzo', 'Ivan', 'Jude', 'August', 'Kevin', 'Malachi', 'Elliott', 'Rhett', 'Archer', 'Karter', 'Arthur', 'Luka', 'Elliot', 'Thiago', 'Brandon', 'Camden', 'Justin', 'Jesus', 'Maddox', 'King', 'Theo', 'Enzo', 'Matteo', 'Emiliano', 'Dean', 'Hayden', 'Finn', 'Brody', 'Antonio', 'Abel', 'Alex', 'Tristan', 'Graham', 'Zayden', 'Judah', 'Xander', 'Miguel', 'Atlas', 'Messiah', 'Barrett', 'Tucker', 'Timothy', 'Alan', 'Edward', 'Leon', 'Dawson', 'Eric', 'Ace', 'Victor', 'Abraham', 'Nicolas', 'Jesse', 'Charlie', 'Patrick', 'Walker', 'Joel', 'Richard', 'Beckett', 'Blake', 'Alejandro', 'Avery', 'Grant', 'Peter', 'Oscar', 'Matias', 'Amari', 'Lukas', 'Andres', 'Arlo', 'Colt', 'Adonis', 'Kyrie', 'Steven', 'Felix', 'Preston', 'Marcus', 'Holden', 'Emilio', 'Remington', 'Jeremy', 'Kaleb', 'Brantley', 'Bryce', 'Mark', 'Knox', 'Israel', 'Phoenix', 'Kobe', 'Nash', 'Griffin', 'Caden', 'Kenneth', 'Kyler', 'Hayes', 'Jax', 'Rafael', 'Beckham', 'Javier', 'Maximus', 'Simon', 'Paul', 'Omar', 'Kaden', 'Kash', 'Lane', 'Bryan', 'Riley', 'Zane', 'Louis', 'Aidan', 'Paxton', 'Maximiliano', 'Karson', 'Cash', 'Cayden', 'Emerson', 'Tobias', 'Ronan', 'Brian', 'Dallas', 'Bradley', 'Jorge', 'Walter', 'Josue', 'Khalil', 'Damien', 'Jett', 'Kairo', 'Zander', 'Andre', 'Cohen', 'Crew', 'Hendrix', 'Colin', 'Chance', 'Malakai', 'Clayton', 'Daxton', 'Malcolm', 'Lennox', 'Martin', 'Jaden', 'Kayson', 'Bodhi', 'Francisco', 'Cody', 'Erick', 'Kameron', 'Atticus', 'Dante', 'Jensen', 'Cruz', 'Finley', 'Brady', 'Joaquin', 'Anderson', 'Gunner', 'Muhammad', 'Zayn', 'Derek', 'Raymond', 'Kyle', 'Angelo', 'Reid', 'Spencer', 'Nico', 'Jaylen', 'Jake', 'Prince', 'Manuel', 'Ali', 'Gideon', 'Stephen', 'Ellis', 'Orion', 'Rylan', 'Eduardo', 'Mario', 'Rory', 'Cristian', 'Odin', 'Tanner', 'Julius', 'Callum', 'Sean', 'Kane', 'Ricardo', 'Travis', 'Wade', 'Warren', 'Fernando', 'Titus', 'Leonel', 'Edwin', 'Cairo', 'Corbin', 'Dakota', 'Ismael', 'Colson', 'Killian', 'Major', 'Tate', 'Gianni', 'Elian', 'Remy', 'Lawson', 'Niko', 'Nasir', 'Kade', 'Armani', 'Ezequiel', 'Marshall', 'Hector', 'Desmond', 'Kason', 'Garrett', 'Jared', 'Cyrus', 'Russell', 'Cesar', 'Tyson', 'Malik', 'Donovan', 'Jaxton', 'Cade', 'Romeo', 'Nehemiah', 'Sergio', 'Iker', 'Caiden', 'Jay', 'Pablo', 'Devin', 'Jeffrey', 'Otto', 'Kamari', 'Ronin', 'Johnny', 'Clark', 'Ari', 'Marco', 'Edgar', 'Bowen', 'Jaiden', 'Grady', 'Zayne', 'Sullivan', 'Jayceon', 'Sterling', 'Andy', 'Conor', 'Raiden', 'Royal', 'Royce', 'Solomon', 'Trevor', 'Winston', 'Emanuel', 'Finnegan', 'Pedro', 'Luciano', 'Harvey', 'Franklin', 'Noel', 'Troy', 'Princeton', 'Johnathan', 'Erik', 'Fabian', 'Oakley', 'Rhys', 'Porter', 'Hugo', 'Frank', 'Damon', 'Kendrick', 'Mathias', 'Milan', 'Peyton', 'Wilder', 'Callan', 'Gregory', 'Seth', 'Matthias', 'Briggs', 'Ibrahim', 'Roberto', 'Conner', 'Quinn', 'Kashton', 'Sage', 'Santino', 'Kolton', 'Alijah', 'Dominick', 'Zyaire', 'Apollo', 'Kylo', 'Reed', 'Philip', 'Kian', 'Shawn', 'Kaison', 'Leonidas', 'Ayaan', 'Lucca', 'Memphis', 'Ford', 'Baylor', 'Kyson', 'Uriel', 'Allen', 'Collin', 'Ruben', 'Archie', 'Dalton', 'Esteban', 'Adan', 'Forrest', 'Alonzo', 'Isaias', 'Leland', 'Jase', 'Dax', 'Kasen', 'Gage', 'Kamden', 'Marcos', 'Jamison', 'Francis', 'Hank', 'Alexis', 'Tripp', 'Frederick', 'Jonas', 'Stetson', 'Cassius', 'Izaiah', 'Eden', 'Maximilian', 'Rocco', 'Tatum', 'Keegan', 'Aziel', 'Moses', 'Bruce', 'Lewis', 'Braylen', 'Omari', 'Mack', 'Augustus', 'Enrique', 'Armando', 'Pierce', 'Moises', 'Asa', 'Shane', 'Emmitt', 'Soren', 'Dorian', 'Keanu', 'Zaiden', 'Raphael', 'Deacon', 'Abdiel', 'Kieran', 'Phillip', 'Ryland', 'Zachariah', 'Casey', 'Zaire', 'Albert', 'Baker', 'Corey', 'Kylan', 'Denver', 'Gunnar', 'Jayson', 'Drew', 'Callen', 'Jasiah', 'Drake', 'Kannon', 'Braylon', 'Sonny', 'Bo', 'Moshe', 'Huxley', 'Quentin', 'Rowen', 'Santana', 'Cannon', 'Kenzo', 'Wells', 'Julio', 'Nikolai', 'Conrad', 'Jalen', 'Makai', 'Benson', 'Derrick', 'Gerardo', 'Davis', 'Abram', 'Mohamed', 'Ronald', 'Raul', 'Arjun', 'Dexter', 'Kaysen', 'Jaime', 'Scott', 'Lawrence', 'Ariel', 'Skyler', 'Danny', 'Roland', 'Chandler', 'Yusuf', 'Samson', 'Case', 'Zain', 'Roy', 'Rodrigo', 'Sutton', 'Boone', 'Saint', 'Saul', 'Jaziel', 'Hezekiah', 'Alec', 'Arturo', 'Jamari', 'Jaxtyn', 'Julien', 'Koa', 'Reece', 'Landen', 'Koda', 'Darius', 'Sylas', 'Ares', 'Kyree', 'Boston', 'Keith', 'Taylor', 'Johan', 'Edison', 'Sincere', 'Watson', 'Jerry', 'Nikolas', 'Quincy', 'Shepherd', 'Brycen', 'Marvin', 'Dariel', 'Axton', 'Donald', 'Bodie', 'Finnley', 'Onyx', 'Rayan', 'Raylan', 'Brixton', 'Colby', 'Shiloh', 'Valentino', 'Layton', 'Trenton', 'Landyn', 'Alessandro', 'Ahmad', 'Gustavo', 'Ledger', 'Ridge', 'Ander', 'Ahmed', 'Kingsley', 'Issac', 'Mauricio', 'Tony', 'Leonard', 'Mohammed', 'Uriah', 'Duke', 'Kareem', 'Lucian', 'Marcelo', 'Aarav', 'Leandro', 'Reign', 'Clay', 'Kohen', 'Dennis', 'Samir', 'Ermias', 'Otis', 'Emir', 'Nixon', 'Ty', 'Sam', 'Fletcher', 'Wilson', 'Dustin', 'Hamza', 'Bryant', 'Flynn', 'Lionel', 'Mohammad', 'Cason', 'Jamir', 'Aden', 'Dakari', 'Justice', 'Dillon', 'Layne', 'Zaid', 'Alden', 'Nelson', 'Devon', 'Titan', 'Chris', 'Khari', 'Zeke', 'Noe', 'Alberto', 'Roger', 'Brock', 'Rex', 'Quinton', 'Alvin', 'Cullen', 'Azariah', 'Harlan', 'Kellan', 'Lennon', 'Marcel', 'Keaton', 'Morgan', 'Ricky', 'Trey', 'Karsyn', 'Langston', 'Miller', 'Chaim', 'Salvador', 'Amias', 'Tadeo', 'Curtis', 'Lachlan', 'Amos', 'Anakin', 'Krew', 'Tomas', 'Jefferson', 'Yosef', 'Bruno', 'Korbin', 'Augustine', 'Cayson', 'Mathew', 'Vihaan', 'Jamie', 'Clyde', 'Brendan', 'Jagger', 'Carmelo', 'Harry', 'Nathanael', 'Mitchell', 'Darren', 'Ray', 'Jedidiah', 'Jimmy', 'Lochlan', 'Bellamy', 'Eddie', 'Rayden', 'Reese', 'Stanley', 'Joe', 'Houston', 'Douglas', 'Vincenzo', 'Casen', 'Emery', 'Joziah', 'Leighton', 'Marcellus', 'Atreus', 'Aron', 'Hugh', 'Musa', 'Tommy', 'Alfredo', 'Junior', 'Neil', 'Westley', 'Banks', 'Eliel', 'Melvin', 'Maximo', 'Briar', 'Colten', 'Lance', 'Nova', 'Trace', 'Axl', 'Ramon', 'Vicente', 'Brennan', 'Caspian', 'Remi', 'Deandre', 'Legacy', 'Lee', 'Valentin', 'Ben', 'Louie', 'Westin', 'Wayne', 'Benicio', 'Grey', 'Zayd', 'Gatlin', 'Mekhi', 'Orlando', 'Bjorn', 'Harley', 'Alonso', 'Rio', 'Aldo', 'Byron', 'Eliseo', 'Ernesto', 'Talon', 'Thaddeus', 'Brecken', 'Kace', 'Kellen', 'Enoch', 'Kiaan', 'Lian', 'Creed', 'Rohan', 'Callahan', 'Jaxxon', 'Ocean', 'Crosby', 'Dash', 'Gary', 'Mylo', 'Ira', 'Magnus', 'Salem', 'Abdullah', 'Kye', 'Tru', 'Forest', 'Jon', 'Misael', 'Madden', 'Braden', 'Carl', 'Hassan', 'Emory', 'Kristian', 'Alaric', 'Ambrose', 'Dario', 'Allan', 'Bode', 'Boden', 'Juelz', 'Kristopher', 'Genesis', 'Idris', 'Ameer', 'Anders', 'Darian', 'Kase', 'Aryan', 'Dane', 'Guillermo', 'Elisha', 'Jakobe', 'Thatcher', 'Eugene', 'Ishaan', 'Larry', 'Wesson', 'Yehuda', 'Alvaro', 'Bobby', 'Bronson', 'Dilan', 'Kole', 'Kyro', 'Tristen', 'Blaze', 'Brayan', 'Jadiel', 'Kamryn', 'Demetrius', 'Maurice', 'Arian', 'Kabir', 'Rocky', 'Rudy', 'Randy', 'Rodney', 'Yousef', 'Felipe', 'Robin', 'Aydin', 'Dior', 'Kaiser', 'Van', 'Brodie', 'London', 'Eithan', 'Stefan', 'Ulises', 'Camilo', 'Branson', 'Jakari', 'Judson', 'Yahir', 'Zavier', 'Damari', 'Jakob', 'Jaxx', 'Bentlee', 'Cain', 'Niklaus', 'Rey', 'Zahir', 'Aries', 'Blaine', 'Kyng', 'Castiel', 'Henrik', 'Joey', 'Khalid', 'Bear', 'Graysen', 'Jair', 'Kylen', 'Darwin', 'Alfred', 'Ayan', 'Kenji', 'Zakai', 'Avi', 'Cory', 'Fisher', 'Jacoby', 'Osiris', 'Harlem', 'Jamal', 'Santos', 'Wallace', 'Brett', 'Fox', 'Leif', 'Maison', 'Reuben', 'Adler', 'Zev', 'Calum', 'Kelvin', 'Zechariah', 'Bridger', 'Mccoy', 'Seven', 'Shepard', 'Azrael', 'Leroy', 'Terry', 'Harold', 'Mac', 'Mordechai', 'Ahmir', 'Cal', 'Franco', 'Trent', 'Blaise', 'Coen', 'Dominik', 'Marley', 'Davion', 'Jeremias', 'Riggs', 'Jones', 'Will', 'Damir', 'Dangelo', 'Canaan', 'Dion', 'Jabari', 'Landry', 'Salvatore', 'Kody', 'Hakeem', 'Truett', 'Gerald', 'Lyric', 'Gordon', 'Jovanni', 'Kamdyn', 'Alistair', 'Cillian', 'Foster', 'Terrance', 'Murphy', 'Zyair', 'Cedric', 'Rome', 'Abner', 'Colter', 'Dayton', 'Jad', 'Xzavier', 'Rene', 'Vance', 'Duncan', 'Frankie', 'Bishop', 'Davian', 'Everest', 'Heath', 'Jaxen', 'Marlon', 'Maxton', 'Reginald', 'Harris', 'Jericho', 'Keenan', 'Korbyn', 'Wes', 'Eliezer', 'Jeffery', 'Kalel', 'Kylian', 'Turner', 'Willie', 'Rogeli', 'Ephraim']
female_names = ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Camila', 'Gianna', 'Abigail', 'Luna', 'Ella', 'Elizabeth', 'Sofia', 'Emily', 'Avery', 'Mila', 'Scarlett', 'Eleanor', 'Madison', 'Layla', 'Penelope', 'Aria', 'Chloe', 'Grace', 'Ellie', 'Nora', 'Hazel', 'Zoey', 'Riley', 'Victoria', 'Lily', 'Aurora', 'Violet', 'Nova', 'Hannah', 'Emilia', 'Zoe', 'Stella', 'Everly', 'Isla', 'Leah', 'Lillian', 'Addison', 'Willow', 'Lucy', 'Paisley', 'Natalie', 'Naomi', 'Eliana', 'Brooklyn', 'Elena', 'Aubrey', 'Claire', 'Ivy', 'Kinsley', 'Audrey', 'Maya', 'Genesis', 'Skylar', 'Bella', 'Aaliyah', 'Madelyn', 'Savannah', 'Anna', 'Delilah', 'Serenity', 'Caroline', 'Kennedy', 'Valentina', 'Ruby', 'Sophie', 'Alice', 'Gabriella', 'Sadie', 'Ariana', 'Allison', 'Hailey', 'Autumn', 'Nevaeh', 'Natalia', 'Quinn', 'Josephine', 'Sarah', 'Cora', 'Emery', 'Samantha', 'Piper', 'Leilani', 'Eva', 'Everleigh', 'Madeline', 'Lydia', 'Jade', 'Peyton', 'Brielle', 'Adeline', 'Vivian', 'Rylee', 'Clara', 'Raelynn', 'Melanie', 'Melody', 'Julia', 'Athena', 'Maria', 'Liliana', 'Hadley', 'Arya', 'Rose', 'Reagan', 'Eliza', 'Adalynn', 'Kaylee', 'Lyla', 'Mackenzie', 'Alaia', 'Isabelle', 'Charlie', 'Arianna', 'Mary', 'Remi', 'Margaret', 'Iris', 'Parker', 'Ximena', 'Eden', 'Ayla', 'Kylie', 'Elliana', 'Josie', 'Katherine', 'Faith', 'Alexandra', 'Eloise', 'Adalyn', 'Amaya', 'Jasmine', 'Amara', 'Daisy', 'Reese', 'Valerie', 'Brianna', 'Cecilia', 'Andrea', 'Summer', 'Valeria', 'Norah', 'Ariella', 'Esther', 'Ashley', 'Emerson', 'Aubree', 'Isabel', 'Anastasia', 'Ryleigh', 'Khloe', 'Taylor', 'Londyn', 'Lucia', 'Emersyn', 'Callie', 'Sienna', 'Blakely', 'Kehlani', 'Genevieve', 'Alina', 'Bailey', 'Juniper', 'Maeve', 'Molly', 'Harmony', 'Georgia', 'Magnolia', 'Catalina', 'Freya', 'Juliette', 'Sloane', 'June', 'Sara', 'Ada', 'Kimberly', 'River', 'Ember', 'Juliana', 'Aliyah', 'Millie', 'Brynlee', 'Teagan', 'Morgan', 'Jordyn', 'London', 'Alaina', 'Olive', 'Rosalie', 'Alyssa', 'Ariel', 'Finley', 'Arabella', 'Journee', 'Hope', 'Leila', 'Alana', 'Gemma', 'Vanessa', 'Gracie', 'Noelle', 'Marley', 'Elise', 'Presley', 'Kamila', 'Zara', 'Amy', 'Kayla', 'Payton', 'Blake', 'Ruth', 'Alani', 'Annabelle', 'Sage', 'Aspen', 'Laila', 'Lila', 'Rachel', 'Trinity', 'Daniela', 'Alexa', 'Lilly', 'Lauren', 'Elsie', 'Margot', 'Adelyn', 'Zuri', 'Brooke', 'Sawyer', 'Lilah', 'Lola', 'Selena', 'Mya', 'Sydney', 'Diana', 'Ana', 'Vera', 'Alayna', 'Nyla', 'Elaina', 'Rebecca', 'Angela', 'Kali', 'Alivia', 'Raegan', 'Rowan', 'Phoebe', 'Camilla', 'Joanna', 'Malia', 'Vivienne', 'Dakota', 'Brooklynn', 'Evangeline', 'Camille', 'Jane', 'Nicole', 'Catherine', 'Jocelyn', 'Julianna', 'Lena', 'Lucille', 'Mckenna', 'Paige', 'Adelaide', 'Charlee', 'Mariana', 'Myla', 'Mckenzie', 'Tessa', 'Miriam', 'Oakley', 'Kailani', 'Alayah', 'Amira', 'Adaline', 'Phoenix', 'Milani', 'Annie', 'Lia', 'Angelina', 'Harley', 'Cali', 'Maggie', 'Hayden', 'Leia', 'Fiona', 'Briella', 'Journey', 'Lennon', 'Saylor', 'Jayla', 'Kaia', 'Thea', 'Adriana', 'Mariah', 'Juliet', 'Oaklynn', 'Kiara', 'Alexis', 'Haven', 'Aniyah', 'Delaney', 'Gracelynn', 'Kendall', 'Winter', 'Lilith', 'Logan', 'Amiyah', 'Evie', 'Alexandria', 'Gracelyn', 'Gabriela', 'Sutton', 'Harlow', 'Madilyn', 'Makayla', 'Evelynn', 'Gia', 'Nina', 'Amina', 'Giselle', 'Brynn', 'Blair', 'Amari', 'Octavia', 'Michelle', 'Talia', 'Demi', 'Alaya', 'Kaylani', 'Izabella', 'Fatima', 'Tatum', 'Makenzie', 'Lilliana', 'Arielle', 'Palmer', 'Melissa', 'Willa', 'Samara', 'Destiny', 'Dahlia', 'Celeste', 'Ainsley', 'Rylie', 'Reign', 'Laura', 'Adelynn', 'Gabrielle', 'Remington', 'Wren', 'Brinley', 'Amora', 'Lainey', 'Collins', 'Lexi', 'Aitana', 'Alessandra', 'Kenzie', 'Raelyn', 'Elle', 'Everlee', 'Haisley', 'Hallie', 'Wynter', 'Daleyza', 'Gwendolyn', 'Paislee', 'Ariyah', 'Veronica', 'Heidi', 'Anaya', 'Cataleya', 'Kira', 'Avianna', 'Felicity', 'Aylin', 'Miracle', 'Sabrina', 'Lana', 'Ophelia', 'Elianna', 'Royalty', 'Madeleine', 'Esmeralda', 'Joy', 'Kalani', 'Esme', 'Jessica', 'Leighton', 'Ariah', 'Makenna', 'Nylah', 'Viviana', 'Camryn', 'Cassidy', 'Dream', 'Luciana', 'Maisie', 'Stevie', 'Kate', 'Lyric', 'Daniella', 'Alicia', 'Daphne', 'Frances', 'Charli', 'Raven', 'Paris', 'Nayeli', 'Serena', 'Heaven', 'Bianca', 'Helen', 'Hattie', 'Averie', 'Mabel', 'Selah', 'Allie', 'Marlee', 'Kinley', 'Regina', 'Carmen', 'Jennifer', 'Jordan', 'Alison', 'Stephanie', 'Maren', 'Kayleigh', 'Angel', 'Annalise', 'Jacqueline', 'Braelynn', 'Emory', 'Rosemary', 'Scarlet', 'Amanda', 'Danielle', 'Emelia', 'Ryan', 'Carolina', 'Astrid', 'Kensley', 'Shiloh', 'Maci', 'Francesca', 'Rory', 'Celine', 'Kamryn', 'Zariah', 'Liana', 'Poppy', 'Maliyah', 'Keira', 'Skyler', 'Noa', 'Skye', 'Nadia', 'Addilyn', 'Rosie', 'Eve', 'Sarai', 'Edith', 'Jolene', 'Maddison', 'Meadow', 'Charleigh', 'Matilda', 'Elliott', 'Madelynn', 'Holly', 'Leona', 'Azalea', 'Katie', 'Mira', 'Ari', 'Kaitlyn', 'Danna', 'Cameron', 'Kyla', 'Bristol', 'Kora', 'Armani', 'Nia', 'Malani', 'Dylan', 'Remy', 'Maia', 'Dior', 'Legacy', 'Alessia', 'Shelby', 'Maryam', 'Sylvia', 'Yaretzi', 'Lorelei', 'Madilynn', 'Abby', 'Helena', 'Jimena', 'Elisa', 'Renata', 'Amber', 'Aviana', 'Carter', 'Emmy', 'Haley', 'Alondra', 'Elaine', 'Erin', 'April', 'Emely', 'Imani', 'Kennedi', 'Lorelai', 'Hanna', 'Kelsey', 'Aurelia', 'Colette', 'Jaliyah', 'Kylee', 'Macie', 'Aisha', 'Dorothy', 'Charley', 'Kathryn', 'Adelina', 'Adley', 'Monroe', 'Sierra', 'Ailani', 'Miranda', 'Mikayla', 'Alejandra', 'Amirah', 'Jada', 'Jazlyn', 'Jenna', 'Jayleen', 'Beatrice', 'Kendra', 'Lyra', 'Nola', 'Emberly', 'Mckinley', 'Myra', 'Katalina', 'Antonella', 'Zelda', 'Alanna', 'Amaia', 'Priscilla', 'Briar', 'Kaliyah', 'Itzel', 'Oaklyn', 'Alma', 'Mallory', 'Novah', 'Amalia', 'Fernanda', 'Alia', 'Angelica', 'Elliot', 'Justice', 'Mae', 'Cecelia', 'Gloria', 'Ariya', 'Virginia', 'Cheyenne', 'Aleah', 'Jemma', 'Henley', 'Meredith', 'Leyla', 'Lennox', 'Ensley', 'Zahra', 'Reina', 'Frankie', 'Lylah', 'Nalani', 'Reyna', 'Saige', 'Ivanna', 'Aleena', 'Emerie', 'Ivory', 'Leslie', 'Alora', 'Ashlyn', 'Bethany', 'Bonnie', 'Sasha', 'Xiomara', 'Salem', 'Adrianna', 'Dayana', 'Clementine', 'Karina', 'Karsyn', 'Emmie', 'Julie', 'Julieta', 'Briana', 'Carly', 'Macy', 'Marie', 'Oaklee', 'Christina', 'Malaysia', 'Ellis', 'Irene', 'Anne', 'Anahi', 'Mara', 'Rhea', 'Davina', 'Dallas', 'Jayda', 'Mariam', 'Skyla', 'Siena', 'Elora', 'Marilyn', 'Jazmin', 'Megan', 'Rosa', 'Savanna', 'Allyson', 'Milan', 'Coraline', 'Johanna', 'Melany', 'Chelsea', 'Michaela', 'Melina', 'Angie', 'Cassandra', 'Yara', 'Kassidy', 'Liberty', 'Lilian', 'Avah', 'Anya', 'Laney', 'Navy', 'Opal', 'Amani', 'Zaylee', 'Mina', 'Sloan', 'Romina', 'Ashlynn', 'Aliza', 'Liv', 'Malaya', 'Blaire', 'Janelle', 'Kara', 'Analia', 'Hadassah', 'Hayley', 'Karla', 'Chaya', 'Cadence', 'Kyra', 'Alena', 'Ellianna', 'Katelyn', 'Kimber', 'Laurel', 'Lina', 'Capri', 'Braelyn', 'Faye', 'Kamiyah', 'Kenna', 'Louise', 'Calliope', 'Kaydence', 'Nala', 'Tiana', 'Aileen', 'Sunny', 'Zariyah', 'Milana', 'Giuliana', 'Eileen', 'Elodie', 'Rayna', 'Monica', 'Galilea', 'Journi', 'Lara', 'Marina', 'Aliana', 'Harmoni', 'Jamie', 'Holland', 'Emmalyn', 'Lauryn', 'Chanel', 'Tinsley', 'Jessie', 'Lacey', 'Elyse', 'Janiyah', 'Jolie', 'Ezra', 'Marleigh', 'Roselyn', 'Lillie', 'Louisa', 'Madisyn', 'Penny', 'Kinslee', 'Treasure', 'Zaniyah', 'Estella', 'Jaylah', 'Khaleesi', 'Alexia', 'Dulce', 'Indie', 'Maxine', 'Waverly', 'Giovanna', 'Miley', 'Saoirse', 'Estrella', 'Greta', 'Rosalia', 'Mylah', 'Teresa', 'Bridget', 'Kelly', 'Adalee', 'Aubrie', 'Lea', 'Harlee', 'Anika', 'Itzayana', 'Hana', 'Kaisley', 'Mikaela', 'Naya', 'Avalynn', 'Margo', 'Sevyn', 'Florence', 'Keilani', 'Lyanna', 'Joelle', 'Kataleya', 'Royal', 'Averi', 'Kallie', 'Winnie', 'Baylee', 'Martha', 'Pearl', 'Alaiya', 'Rayne', 'Sylvie', 'Brylee', 'Jazmine', 'Ryann', 'Kori', 'Noemi', 'Haylee', 'Julissa', 'Celia', 'Laylah', 'Rebekah', 'Rosalee', 'Aya', 'Bria', 'Adele', 'Aubrielle', 'Tiffany', 'Addyson', 'Kai', 'Bellamy', 'Leilany', 'Princess', 'Chana', 'Estelle', 'Selene', 'Sky', 'Dani', 'Thalia', 'Ellen', 'Rivka', 'Amelie', 'Andi', 'Kynlee', 'Raina', 'Vienna', 'Alianna', 'Livia', 'Madalyn', 'Mercy', 'Novalee', 'Ramona', 'Vada', 'Berkley', 'Gwen', 'Persephone', 'Milena', 'Paula', 'Clare', 'Kairi', 'Linda', 'Paulina', 'Kamilah', 'Amoura', 'Hunter', 'Isabela', 'Karen', 'Marianna', 'Sariyah', 'Theodora', 'Annika', 'Kyleigh', 'Nellie', 'Scarlette', 'Keyla', 'Kailey', 'Mavis', 'Lilianna', 'Rosalyn', 'Sariah', 'Tori', 'Yareli', 'Aubriella', 'Bexley', 'Bailee', 'Jianna', 'Keily', 'Annabella', 'Azariah', 'Denisse', 'Promise', 'August', 'Hadlee', 'Halle', 'Fallon', 'Oakleigh', 'Zaria', 'Jaylin', 'Paisleigh', 'Crystal', 'Ila', 'Aliya', 'Cynthia', 'Giana', 'Maleah', 'Rylan', 'Aniya', 'Denise', 'Emmeline', 'Scout', 'Simone', 'Noah', 'Zora', 'Meghan', 'Landry', 'Ainhoa', 'Lilyana', 'Noor', 'Belen', 'Brynleigh', 'Cleo', 'Meilani', 'Karter', 'Amaris', 'Frida', 'Iliana', 'Violeta', 'Addisyn', 'Nancy', 'Denver', 'Leanna', 'Braylee', 'Kiana', 'Wrenley', 'Barbara', 'Khalani', 'Aspyn', 'Ellison', 'Judith', 'Robin', 'Valery', 'Aila', 'Deborah', 'Cara', 'Clarissa', 'Iyla', 'Lexie', 'Anais', 'Kaylie', 'Nathalie', 'Alisson', 'Della', 'Addilynn', 'Elsa', 'Zoya', 'Layne', 'Marlowe', 'Jovie', 'Kenia', 'Samira', 'Jaylee', 'Jenesis', 'Etta', 'Shay', 'Amayah', 'Avayah', 'Egypt', 'Flora', 'Raquel', 'Whitney', 'Zola', 'Giavanna', 'Raya', 'Veda', 'Halo', 'Paloma', 'Nataly', 'Whitley', 'Dalary', 'Drew', 'Guadalupe', 'Kamari', 'Esperanza', 'Loretta', 'Malayah', 'Natasha', 'Stormi', 'Ansley', 'Carolyn', 'Corinne', 'Paola', 'Brittany', 'Emerald', 'Freyja', 'Zainab', 'Artemis', 'Jillian', 'Kimora', 'Zoie', 'Aislinn', 'Emmaline', 'Ayleen', 'Queen', 'Jaycee', 'Murphy', 'Nyomi', 'Elina', 'Hadleigh', 'Marceline', 'Marisol', 'Yasmin', 'Zendaya', 'Chandler', 'Emani', 'Jaelynn', 'Kaiya', 'Nathalia', 'Violette', 'Joyce', 'Paityn', 'Elisabeth', 'Emmalynn', 'Luella', 'Yamileth', 'Aarya', 'Luisa', 'Zhuri', 'Araceli', 'Harleigh', 'Madalynn', 'Melani', 'Laylani', 'Magdalena', 'Mazikeen', 'Belle', 'Kadence']
sex="Female"
n=0

people = []
while (len(female_names)>=8) and (len(male_names)>=8):
    n+=1
    if sex=="Female":
        exec(f"id_{str(n)}=gen_person(female_names.pop(),0,\"female\")")
        sex="Male"
        exec(f"people.append(id_{str(n)})")
    else:
        exec(f"id_{str(n)}=gen_person(male_names.pop(),0,\"male\")")
        sex="Female"
        exec(f"people.append(id_{str(n)})")


friend = id_7
neighbor = id_50



study_group = []

for i in range(1, 8):
    exec(f"person{i} = id_{i+65}")
    exec(f"study_group.append(person{i})")

nums = [430, True, 33, True, 570, None, 944, 201.8193280206529, 'Tuesday', 682, 98.94720670304808, 219, 164, 184.2687611259553, 914, 727, 469, 658, 446.88990787411996, None, 205, 931, 'Happy', 695.1520426719662, 200, 647, 987, 169, None, 423, 502.9061488446327, 865, 28.053809609905823, 845.5902700343556, True, 516, 237, 281.9156136620423, None, 589, 28.226242513961022, 73.67679508117088, None, 938.406400954232, 48.035259719087605, 621, 883.2285171108035, 801, 297.9853564291469, 642.2869004641448, 636.0991725673584, 977, 705, 954, 733, 493, 418.73162992971356, 470, 'Seven', 145.62003144004217, 873.3730550457321, 86, 887, 893, 104, 922.193232183253, True, 534.6075293845828, 560, 767.1550968615129, True, 786, 777.8388717938185, 971, 34.25839163171435, 361.760886838892, 510.6490299888919, 100, 617.809907312167, 39, 108.87268404185484, 233.16325245038988, 886.1379475144615, 942.4036162790741, 769, 419.972371695768, 154, 736, 598.040950486763, 620, 388, 229, 917, 360.611667290697, 66, 705, 392.300806723162, 247, 747.516399152557, 827.4015837998611, 662, 421.44384195730754, 120.93992837978773]

groceries = {
    "Milk": 1.90,
    "Bread": 4.62,
    "Eggs": 6.37,
    "Cheese": 8.65,
    "Butter": 9.47,
    "Apples": 0.59,
    "Bananas": 0.29,
    "Chicken": 16.29,
    "Beef": 12.75,
    "Rice": 3.18,
    "Pasta": 1.52,
    "Tomatoes": 2.31,
    "Potatoes": 5.83,
    "Onions": 1.32,
    "Carrots": 2.13,
    "Broccoli": 4.79,
    "Yogurt": 4.08,
    "Orange Juice": 3.62,
    "Cereal": 3.87,
    "Coffee": 4.42,
    "Tea": 4.15,
    "Sugar": 5.65,
    "Salt": 7.36,
    "Pepper": 7.17,
    "Olive Oil": 7.81
}

preamble = "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."


words_start_end_same = [
    "Area", "agenda", "arena", "bub", "civic", "deed", "dad", "eve", "fluff", "gag",
    "gig", "level", "Madam", "Minim", "mum", "Nun", "otto", "pap", "peep", "pip",
    "pop", "radar", "redder", "Refer", "reviver", "Rotator", "sagas", "sees",
    "solos", "stats", "tenet", "tit", "tot", "wow", "kayak", "noon", "deified", "racecar", "redivider", "repaper", "rotor", "peep", "wow", "fluff",
    "success", "aura", "solos", "tart", "trout", "scenes", "tart", "text", "tint"
]

random_words = [
    "Elderberry", "thyme", "tangerine", "quail", "tomato", "zebra", "mint", "sage", 
    "xylophone", "zucchini", "hazelnut", "honeydew", "date", "quinoa", "radish", 
    "iceberg", "orange", "walnut", "papaya", "fennel", "cherry", "udon", "parsley", 
    "xigua", "vinegar", "okra", "melon", "yam", "jackfruit", "dill", "guava", 
    "blueberry", "oregano", "basil", "indigo", "cucumber", "lychee", "quince", 
    "banana", "raspberry", "fennel", "spinach", "kale", "jicama", "dragonfruit", 
    "apple", "grape", "nutmeg", "vanilla", "nectar", "honey", "watermelon", 
    "mango", "strawberry", "kiwi", "cashew", "garlic", "umbra", "endive", 
    "ugly", "fig", "rhubarb", "avocado", "kumquat", "nectarine", "plum", 
    "yeast", "lemon", "almond", "eggplant"
]

word_list = words_start_end_same + random_words

random.shuffle(word_list)

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

braille = {
    'A': '⠁', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑', 'F': '⠋',
    'G': '⠛', 'H': '⠓', 'I': '⠊', 'J': '⠚', 'K': '⠅', 'L': '⠇',
    'M': '⠍', 'N': '⠝', 'O': '⠕', 'P': '⠏', 'Q': '⠟', 'R': '⠗',
    'S': '⠎', 'T': '⠞', 'U': '⠥', 'V': '⠧', 'W': '⠺', 'X': '⠭',
    'Y': '⠽', 'Z': '⠵',
    '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
    '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',
    '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒', '!': '⠖', '?': '⠦',
    '-': '⠤', '(': '⠶', ')': '⠶', '\'': '⠄', '/': '⠌'
}

address = "251MERCER"

phrase = "NYC10012"
