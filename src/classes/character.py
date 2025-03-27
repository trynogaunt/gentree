from src.database.database import Database

class Character():
    def __init__(self, firstname: str, lastname: str, lineage: str, generation: int, age: int, job: str, titles: list, picture: str):

        self.__firstname = firstname
        self.__lastname = lastname
        self.__lineage = lineage
        self.__generation = generation
        self.__age = age
        self.__job = job
        self.__titles = titles
        self.__picture = picture
        self.__parents = []
        self.__children = []
        self.__spouse = []
        self.__id = None

 


#region class getter
    @property
    def firstname(self):
        return self.__firstname
    
    @property
    def lastname(self):
        return self.__lastname

    @property
    def lineage(self):
        return self.__lineage
    
    @property
    def generation(self):
        return self.__generation
    
    @property
    def age(self):
        return self.__age
    
    @property
    def job(self):
        return self.__job
    
    @property
    def titles(self):
        return self.__titles
    
    @property
    def picture(self):
        return self.__picture
    
    @property
    def full_name(self):
        return f"{self.__firstname} {self.__lastname}"
    
    @property
    def parents(self):
        return self.__parents

    @property
    def children(self):
        return self.__children

    @property
    def spouse(self):
        return self.__spouse

#endregion class getter
#region class setter   
    @firstname.setter
    def firstname(self, firstname):
        if not isinstance(firstname, str):
            raise TypeError("Le prénom doit être une chaîne de caractères")
        if not firstname.strip():
            raise ValueError("Le prénom ne peut pas être vide")
        self.__firstname = firstname.strip()
    
    @lastname.setter
    def lastname(self, lastname):
        if not isinstance(lastname, str):
            raise TypeError("Le nom doit être une chaîne de caractères")
        if not lastname.strip():
            raise ValueError("Le nom ne peut pas être vide")
        self.__lastname = lastname.strip()

    @lineage.setter
    def lineage(self, lineage):
        if not isinstance(lineage, str):
            raise TypeError("La lignée doit être une chaîne de caractères")
        if not lineage.strip():
            raise ValueError("La lignée ne peut pas être vide")
        self.__lineage = lineage.strip()

    @generation.setter
    def generation(self, generation):
        if not isinstance(generation, int):
            raise TypeError("La génération doit être un nombre entier")
        if generation < 1:
            raise ValueError("La génération doit être supérieure à 0")
        self.__generation = generation

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError("L'âge doit être un nombre entier")
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        self.__age = age

    @job.setter
    def job(self, job):
        if not isinstance(job, str):
            raise TypeError("Le métier doit être une chaîne de caractères")
        if not job.strip():
            raise ValueError("Le métier ne peut pas être vide")
        self.__job = job.strip()

    @titles.setter
    def titles(self, titles):
        if not isinstance(titles, list):
            raise TypeError("Les titres doivent être une liste")
        if not all(isinstance(title, str) for title in titles):
            raise TypeError("Tous les titres doivent être des chaînes de caractères")
        self.__titles = [title.strip() for title in titles if title.strip()]

    @picture.setter
    def picture(self, picture):
        if not isinstance(picture, str):
            raise TypeError("Le chemin de l'image doit être une chaîne de caractères")
        if not picture.strip():
            raise ValueError("Le chemin de l'image ne peut pas être vide")
        self.__picture = picture.strip()
#endregion class setter
    def __str__(self):
               return f"{self.__firstname} {self.__lastname}"
           
    def __eq__(self, other):
        if isinstance(other, Character):
            return self.__firstname == other.firstname and self.__lastname == other.lastname
        return False

    def __hash__(self):
        return hash((self.__firstname, self.__lastname))

    def add_parent(self, parent: 'Character') -> None:
        if len(self.__parents) >= 2:
            raise ValueError("Un personnage ne peut pas avoir plus de deux parents")
        if parent not in self.__parents:
            self.__parents.append(parent)
            if self not in parent.children:
                parent.add_child(self)

    def add_child(self, child: 'Character') -> None:
        if child not in self.__children:
            self.__children.append(child)
            if self not in child.parents:
                child.add_parent(self)

    def set_spouse(self, spouse: 'Character') -> None:
        if self.__spouse is not None:
            raise ValueError(f"{self.full_name} est déjà marié(e)")
        if spouse.__spouse is not None:
            raise ValueError(f"{spouse.full_name} est déjà marié(e)")
        
        self.__spouse = spouse
        spouse.__spouse = self

    def get_siblings(self) -> list['Character']:
        siblings = []
        for parent in self.__parents:
            for child in parent.children:
                if child != self and child not in siblings:
                    siblings.append(child)
        return siblings

    def get_family_tree(self, depth: int = 2) -> dict:
        if depth < 0:
            return None
        
        tree = {
            'character': self.full_name,
            'parents': [],
            'siblings': [],
            'spouse': None,
            'children': []
        }

        if self.__spouse:
            tree['spouse'] = self.__spouse.full_name

        for parent in self.__parents:
            parent_tree = parent.get_family_tree(depth - 1)
            if parent_tree:
                tree['parents'].append(parent_tree)

        for sibling in self.get_siblings():
            tree['siblings'].append(sibling.full_name)

        for child in self.__children:
            child_tree = child.get_family_tree(depth - 1)
            if child_tree:
                tree['children'].append(child_tree)

        return tree

    @classmethod
    def get_characters(cls) -> list['Character']:
        with Database() as db:
            db.connect()
            query = "SELECT * FROM characters"
            characters = db.execute_query(query)
            return [cls._create_from_db(char_data) for char_data in characters]
        
    @classmethod
    def _create_from_db(cls, char_data: tuple) -> 'Character':
        character = cls(
            firstname=char_data[1],
            lastname=char_data[2],
            lineage=char_data[3],
            generation=char_data[4],
            age=char_data[5],
            job=char_data[6],
            titles=[],
            picture=char_data[7]
        )
        
        character.__id = char_data[0]
        with Database() as db:
            db.connect()
            query = "SELECT title FROM titles WHERE character_id = ?"
            titles = db.execute_query(query, (character.__id,))
            character.titles = [title[0] for title in titles]
        
        with Database() as db:
            # Load parents
            query = """
                SELECT c.* FROM characters c
                JOIN relationships r ON c.id = r.character1_id
                WHERE r.character2_id = ? AND r.relationship_type = 'parent'
            """
            parents = db.execute_query(query, (character.__id,))
            character.__parents = [cls._create_from_db(parent) for parent in parents]

            # Load spouse
            query = """
                SELECT c.* FROM characters c
                JOIN relationships r ON c.id = r.character2_id
                WHERE r.character1_id = ? AND r.relationship_type = 'spouse'
            """
            spouse = db.execute_query(query, (character.__id,))
            if spouse:
                character.__spouse = cls._create_from_db(spouse[0])

        return character
    