import unittest
import sys
import os


# Add the parent directory to the path to import the Character class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.classes.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        """Set up a character for testing"""
        self.character = Character(
            firstname="Jean",
            lastname="Dupont",
            lineage="Dupont",
            generation=1,
            age=30,
            job="Farmer",
            titles=["Sir", "Knight"],
            picture="path/to/picture.jpg"
        )
    
    def test_init(self):
        """Test character initialization"""
        self.assertEqual(self.character.firstname, "Jean")
        self.assertEqual(self.character.lastname, "Dupont")
        self.assertEqual(self.character.lineage, "Dupont")
        self.assertEqual(self.character.generation, 1)
        self.assertEqual(self.character.age, 30)
        self.assertEqual(self.character.job, "Farmer")
        self.assertEqual(self.character.titles, ["Sir", "Knight"])
        self.assertEqual(self.character.picture, "path/to/picture.jpg")
        self.assertEqual(self.character.full_name, "Jean Dupont")
    
    def test_str(self):
        """Test string representation"""
        self.assertEqual(str(self.character), "Jean Dupont")
    
    def test_setter_valid_values(self):
        """Test setting valid values"""
        self.character.firstname = "Pierre"
        self.assertEqual(self.character.firstname, "Pierre")
        
        self.character.lastname = "Martin"
        self.assertEqual(self.character.lastname, "Martin")
        
        self.character.lineage = "Martin"
        self.assertEqual(self.character.lineage, "Martin")
        
        self.character.generation = 2
        self.assertEqual(self.character.generation, 2)
        
        self.character.age = 40
        self.assertEqual(self.character.age, 40)
        
        self.character.job = "Blacksmith"
        self.assertEqual(self.character.job, "Blacksmith")
        
        self.character.titles = ["Duke", "Lord"]
        self.assertEqual(self.character.titles, ["Duke", "Lord"])
        
        self.character.picture = "new/path/to/picture.jpg"
        self.assertEqual(self.character.picture, "new/path/to/picture.jpg")
    
    def test_setter_invalid_types(self):
        """Test setting invalid types"""
        with self.assertRaises(TypeError):
            self.character.firstname = 123
        
        with self.assertRaises(TypeError):
            self.character.lastname = 123
            
        with self.assertRaises(TypeError):
            self.character.lineage = 123
            
        with self.assertRaises(TypeError):
            self.character.generation = "not an int"
            
        with self.assertRaises(TypeError):
            self.character.age = "not an int"
            
        with self.assertRaises(TypeError):
            self.character.job = 123
            
        with self.assertRaises(TypeError):
            self.character.titles = "not a list"
            
        with self.assertRaises(TypeError):
            self.character.titles = [1, 2, 3]
            
        with self.assertRaises(TypeError):
            self.character.picture = 123
    
    def test_setter_invalid_values(self):
        """Test setting invalid values"""
        with self.assertRaises(ValueError):
            self.character.firstname = ""
            
        with self.assertRaises(ValueError):
            self.character.lastname = ""
            
        with self.assertRaises(ValueError):
            self.character.lineage = ""
            
        with self.assertRaises(ValueError):
            self.character.generation = 0
            
        with self.assertRaises(ValueError):
            self.character.age = -1
            
        with self.assertRaises(ValueError):
            self.character.job = ""
            
        with self.assertRaises(ValueError):
            self.character.picture = ""
    
    def test_equality(self):
        """Test equality comparison"""
        same_character = Character(
            firstname="Jean",
            lastname="Dupont",
            lineage="Different",  # Different lineage, but should still be equal
            generation=2,         # Different generation, but should still be equal
            age=40,               # Different age, but should still be equal
            job="Baker",          # Different job, but should still be equal
            titles=["Duke"],      # Different titles, but should still be equal
            picture="other.jpg"   # Different picture, but should still be equal
        )
        self.assertEqual(self.character, same_character)
        
        different_character = Character(
            firstname="Pierre",   # Different firstname, should not be equal
            lastname="Dupont",
            lineage="Dupont",
            generation=1,
            age=30,
            job="Farmer",
            titles=["Sir", "Knight"],
            picture="path/to/picture.jpg"
        )
        self.assertNotEqual(self.character, different_character)
        
        self.assertNotEqual(self.character, "Not a character")
    
    def test_hash(self):
        """Test hashing"""
        character_dict = {self.character: "value"}
        same_character = Character(
            firstname="Jean",
            lastname="Dupont",
            lineage="Different",
            generation=2,
            age=40,
            job="Baker",
            titles=["Duke"],
            picture="other.jpg"
        )
        self.assertIn(same_character, character_dict)

    def test_family_relations(self):
        """Test family relations (parents, children, spouse)"""
        # Create family members
        father = Character("Pierre", "Dupont", "Dupont", 1, 50, "Farmer", [], "father.jpg")
        mother = Character("Marie", "Dupont", "Martin", 1, 48, "Teacher", [], "mother.jpg")
        sibling = Character("Paul", "Dupont", "Dupont", 2, 25, "Baker", [], "sibling.jpg")
        spouse = Character("Sophie", "Martin", "Martin", 2, 28, "Doctor", [], "spouse.jpg")
        child = Character("Lucas", "Dupont", "Dupont", 3, 5, "Child", [], "child.jpg")

        # Test parent-child relationships
        self.character.add_parent(father)
        self.character.add_parent(mother)
        sibling.add_parent(father)
        sibling.add_parent(mother)

        # Test parents
        self.assertEqual(len(self.character.parents), 2)
        self.assertIn(father, self.character.parents)
        self.assertIn(mother, self.character.parents)

        # Test siblings
        siblings = self.character.get_siblings()
        self.assertEqual(len(siblings), 1)
        self.assertIn(sibling, siblings)

        # Test spouse
        self.character.set_spouse(spouse)
        self.assertEqual(self.character.spouse, spouse)
        self.assertEqual(spouse.spouse, self.character)

        # Test children
        self.character.add_child(child)
        self.assertIn(child, self.character.children)
        self.assertIn(self.character, child.parents)

    def test_family_validation(self):
        """Test family relation validations"""
        parent1 = Character("Parent1", "Test", "Test", 1, 50, "Job", [], "test.jpg")
        parent2 = Character("Parent2", "Test", "Test", 1, 50, "Job", [], "test.jpg")
        parent3 = Character("Parent3", "Test", "Test", 1, 50, "Job", [], "test.jpg")
        spouse1 = Character("Spouse1", "Test", "Test", 2, 30, "Job", [], "test.jpg")
        spouse2 = Character("Spouse2", "Test", "Test", 2, 30, "Job", [], "test.jpg")

        # Test maximum parents
        self.character.add_parent(parent1)
        self.character.add_parent(parent2)
        with self.assertRaises(ValueError):
            self.character.add_parent(parent3)

        # Test single spouse
        self.character.set_spouse(spouse1)
        with self.assertRaises(ValueError):
            self.character.set_spouse(spouse2)

    def test_family_tree(self):
        """Test family tree generation"""
        # Create a simple family
        grandfather = Character("Grand", "Pere", "Pere", 1, 70, "Retired", [], "grand.jpg")
        grandmother = Character("Grand", "Mere", "Mere", 1, 68, "Retired", [], "grand.jpg")
        father = Character("Pere", "Test", "Test", 2, 45, "Job", [], "pere.jpg")
        
        # Build relationships
        grandfather.set_spouse(grandmother)
        father.add_parent(grandfather)
        father.add_parent(grandmother)
        self.character.add_parent(father)

        # Test tree structure
        tree = grandfather.get_family_tree(depth=2)
        
        self.assertEqual(tree['character'], "Grand Pere")
        self.assertEqual(tree['spouse'], "Grand Mere")
        self.assertTrue(any(child['character'] == "Pere Test" for child in tree['children']))
        
        # Test depth limit
        limited_tree = grandfather.get_family_tree(depth=1)
        self.assertIn('children', limited_tree)
        self.assertEqual(len(limited_tree['children']), 1)

if __name__ == "__main__":
    unittest.main()