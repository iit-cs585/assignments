# coding: utf-8
"""
@name=a1/a1.py
@possible_points=50

Unit tests for Assignment 1.
"""
import unittest
from a1 import *


class TestA1(unittest.TestCase):

    
    def test_baa_fsa(self):
        """
        @points=6
        Test the sheep speak FSA.
        """
        states = [0, 1, 2, 3, 4]
        initial_state = 0
        accept_states = [4]
        transition = {
            0: {'b': 1},
            1: {'a': 2},
            2: {'a': 3},
            3: {'a': 3, '!': 4},
        }
        self.assertTrue(run_fsa(states, initial_state, accept_states, transition, list('baa!')))
        self.assertTrue(run_fsa(states, initial_state, accept_states, transition, list('baaaa!')))
        self.assertFalse(run_fsa(states, initial_state, accept_states, transition, list('')))
        self.assertFalse(run_fsa(states, initial_state, accept_states, transition, list('baa')))
        self.assertFalse(run_fsa(states, initial_state, accept_states, transition, list('bac')))
        self.assertFalse(run_fsa(states, initial_state, accept_states, transition, list('baaa!a')))

    def test_name_fsa(self):
        """
        @points=6
        Test the name FSA.
        """
        states, initial_state, accept_states, transition = get_name_fsa()
        self.assertTrue(run_fsa(states, initial_state, accept_states, transition, ['Mr.', 'Frank', 'Michael', 'Lewis']))
        self.assertTrue(run_fsa(states, initial_state, accept_states, transition, ['Ms.', 'Frank', 'Lewis']))
        self.assertTrue(run_fsa(states, initial_state, accept_states, transition, ['Flo', 'Michael', 'Lutz']))
        self.assertTrue(run_fsa(states, initial_state, accept_states, transition, ['Flo', 'Lutz']))
        self.assertFalse(run_fsa(states, initial_state, accept_states, transition, ['Flo', 'Michael']))
        self.assertFalse(run_fsa(states, initial_state, accept_states, transition, ['Michael']))

    def test_read_grammar(self):
        """
        @points=6
        Test that a grammar can be read from a list of strings.
        """
        grammar_rules = ['S :- NP VP',
                 'NP :- Det Noun',
                 'NP :- ProperNoun',
                 'VP :- Verb',
                 'VP :- Verb NP',
                 'Det :- a the',
                 'Noun :- book flight',
                 'Verb :- book books include',
                 'ProperNoun :- Houston TWA John'] 
        rules = read_grammar(grammar_rules)
        rules = sorted(rules)
        self.assertEqual(rules[0][0], 'Det')
        self.assertEqual(rules[0][1][0], 'a')
        self.assertEqual(rules[0][1][1], 'the')

        self.assertEqual(rules[1][0], 'NP')
        self.assertEqual(rules[1][1][0], 'Det')
        self.assertEqual(rules[1][1][1], 'Noun')
        
    def test_get_leaves(self):
        """
        @points=6
        Test that we can get the leaves of a parse tree.
        """
        tree = Tree('S', [Tree('NP',
                               [Tree('N', [Tree('John')])]),
                          Tree('VP',
                               [Tree('V', [Tree('books')]),
                                Tree('N', [Tree('flight')])])])
        leaves = tree.get_leaves()
        self.assertListEqual(['John', 'books', 'flight'], leaves)

    def test_get_productions(self):
        """
        @points=6
        Test that we can get the productions from a parse tree.
        """
        tree = Tree('S', [Tree('NP',
                               [Tree('N', [Tree('John')])]),
                          Tree('VP',
                               [Tree('V', [Tree('books')]),
                                Tree('N', [Tree('flight')])])])
        
        productions = tree.get_productions()
        self.assertEqual(productions[0], ('S', ['NP', 'VP']))
        self.assertEqual(productions[1], ('NP', ['N']))
        self.assertEqual(productions[2], ('N', ['John']))
        self.assertEqual(productions[3], ('VP', ['V', 'N']))
        self.assertEqual(productions[4], ('V', ['books']))
        self.assertEqual(productions[5], ('N', ['flight']))

    def test_is_pos(self):
        """
        @points=6
        Test that we can check if a rule is a part-of-speech rule.
        """
        
        rules = [('S', ['NP', 'VP']),
                 ('NP', ['ProperNoun']),
                 ('ProperNoun', ['John', 'Mary']),
                 ('VP', ['V', 'ProperNoun']),
                 ('V', ['likes', 'hates'])]
        self.assertFalse(is_pos(('S', ['NP', 'VP']), rules))
        self.assertFalse(is_pos(('NP', ['ProperNoun']), rules))
        self.assertTrue(is_pos(('ProperNoun', ['John', 'Mary']), rules))
        self.assertTrue(is_pos(('V', ['likes', 'hates']), rules))

    def test_is_valid_production(self):
        """
        @points=6
        Test that we can check if a production is valid.
        """
        rules = [('S', ['NP', 'VP']),
                 ('NP', ['ProperNoun']),
                 ('ProperNoun', ['John', 'Mary']),
                 ('VP', ['V', 'ProperNoun']),
                 ('V', ['likes', 'hates'])]
        self.assertTrue(is_valid_production(('S', ['NP', 'VP']), rules))
        self.assertTrue(is_valid_production(('NP', ['ProperNoun']), rules))
        self.assertTrue(is_valid_production(('ProperNoun', ['John']), rules))
        self.assertTrue(is_valid_production(('ProperNoun', ['Mary']), rules))
        self.assertTrue(is_valid_production(('V', ['likes']), rules))

        self.assertFalse(is_valid_production(('S', ['VP', 'NP']), rules))
        self.assertFalse(is_valid_production(('V', ['John']), rules))
        self.assertFalse(is_valid_production(('NP', ['NP', 'VP']), rules))
                 

    def test_is_valid_tree(self):
        """
        @points=8
        Test that we can check if a parse tree is valid.
        """
        rules = [('S', ['NP', 'VP']),
                 ('NP', ['N']),
                 ('NP', ['D', 'N']),
                 ('N', ['John', 'flight', 'book']),
                 ('D', ['the', 'a']),
                 ('VP', ['V', 'NP']),
                 ('V', ['books', 'book', 'likes', 'hates']),
                ]
        # Valid tree for "John books flight"
        tree = Tree('S', [Tree('NP', [Tree('N', [Tree('John')])]),
                          Tree('VP', [Tree('V', [Tree('books')]),
                                      Tree('NP', [Tree('N', [Tree('flight')])])])])
        self.assertTrue(is_valid_tree(tree, rules, ['John', 'books', 'flight']))
        self.assertFalse(is_valid_tree(tree, rules, ['John', 'books', 'likes']))

        # Valid tree for "John books the flight"
        tree2 = Tree('S', [Tree('NP', [Tree('N', [Tree('John')])]),
                          Tree('VP', [Tree('V', [Tree('books')]),
                                      Tree('NP', [Tree('D', [Tree('the')]),
                                                  Tree('N', [Tree('flight')])])])])

        self.assertTrue(is_valid_tree(tree2, rules, ['John', 'books', 'the', 'flight']))
        self.assertFalse(is_valid_tree(tree2, rules, ['John', 'books', 'flight']))

        # Tree with an invalid rule: D :- flight
        tree3 = Tree('S', [Tree('NP', [Tree('N', [Tree('John')])]),
                           Tree('VP', [Tree('V', [Tree('books')]),
                                       Tree('NP', [Tree('D', [Tree('flight')])])])])        
        self.assertFalse(is_valid_tree(tree3, rules, ['John', 'books', 'flight']))
        

if __name__ == '__main__':
    unittest.main()
