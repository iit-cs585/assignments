# coding: utf-8
"""
@name=a2/a2.py
@possible_points=50

Unit tests for Assignment 2.
"""
import unittest
from a2 import *

#######################################################
# Here are four example sentences used in testing below

test_sentences = [
					['the', 'boy', 'jumped'],
					['the', 'dog', 'jumped'],
					['jump', 'dog'],
					['the', 'ball', 'boy', 'ran']
				  ]

test_tags = [
				['D', 'N', 'V'],
				['D', 'N', 'V'],
				['V', 'N'],
				['D', 'N', 'N', 'V']
			]
#######################################################



class TestA2(unittest.TestCase):


	def test_hmm_fit_emission(self):
		"""Test supervised HMM learning emission probabilities.
		"""
		model = HMM()
		model.fit(test_sentences, test_tags)
		self.assertEqual(0.2, round(model.emission_probas['N']['ball'], 1))
		self.assertEqual(0.4, round(model.emission_probas['N']['boy'], 1))
		self.assertEqual(0.4, round(model.emission_probas['N']['dog'], 1))
		self.assertEqual(0.0, round(model.emission_probas['N']['jump'], 1))
		self.assertEqual(0.0, round(model.emission_probas['N']['ran'], 1))

	def test_hmm_fit_emission_smoothed(self):
		"""Test supervised HMM learning emission probabilities.
		"""
		model = HMM(smoothing=1)
		model.fit(test_sentences, test_tags)
		self.assertEqual(0.4, round(model.emission_probas['D']['the'], 1))
		self.assertEqual(0.1, round(model.emission_probas['D']['ball'], 1))
		self.assertEqual(0.1, round(model.emission_probas['D']['boy'], 1))
		self.assertEqual(0.1, round(model.emission_probas['D']['jump'], 1))

	def test_hmm_fit_transition(self):
		"""Test supervised HMM learning.
		"""
		model = HMM()
		model.fit(test_sentences, test_tags)
		self.assertEqual(0.750, round(model.transition_probas['N']['V'], 3))
		self.assertEqual(0.0, round(model.transition_probas['N']['D'], 1))
		self.assertEqual(0.250, round(model.transition_probas['N']['N'], 3))

	def test_hmm_fit_transition_smoothed(self):
		"""Test supervised HMM learning.
		"""
		model = HMM(smoothing=1)
		model.fit(test_sentences, test_tags)
		self.assertEqual(0.571, round(model.transition_probas['N']['V'], 3))
		self.assertEqual(0.143, round(model.transition_probas['N']['D'], 3))
		self.assertEqual(0.286, round(model.transition_probas['N']['N'], 3))

	def test_hmm_fit_start(self):
		"""Test supervised HMM learning start_probas.
		"""
		model = HMM()
		model.fit(test_sentences, test_tags)
		self.assertEqual(0.75, round(model.start_probas['D'], 2))
		self.assertEqual(0.0, round(model.start_probas['N'], 1))
		self.assertEqual(0.25, round(model.start_probas['V'], 2))

	def test_hmm_fit_start_smoothed(self):
		"""Test supervised HMM learning start_probas.
		"""
		model = HMM(smoothing=1)
		model.fit(test_sentences, test_tags)
		self.assertEqual(0.57, round(model.start_probas['D'], 2))
		self.assertEqual(0.14, round(model.start_probas['N'], 2))
		self.assertEqual(0.29, round(model.start_probas['V'], 2))

	def test_hmm_viterbi(self):
		"""Test viterbi algorithm on 'time flies like an arrow'
		The given model should predict N,V,P,D,N tags.
		"""
		model = HMM()
		model.states = ['D', 'N', 'P', 'V']

		model.start_probas = {'D': .3,
							  'N': .4,
							  'P': .1,
							  'V': .2,
							  }

		model.emission_probas = {'D': {'time': 0.0, 'flies': 0.0, 'like': 0.0, 'an': 1.0, 'arrow': 0.0},
								 'V': {'time': 0.0, 'flies': 0.5, 'like': 0.5, 'an': 0.0, 'arrow': 0.0},
								 'P': {'time': 0.0, 'flies': 0.0, 'like': 1.0, 'an': 0.0, 'arrow': 0.0},
								 'N': {'time': 0.3, 'flies': 0.3, 'like': 0.0, 'an': 0.0, 'arrow': 0.4}
								 }
		model.transition_probas = {'D': {'D': 0.0, 'N': 1.0, 'P': 0.0, 'V': 0.0},
								   'N': {'D': 0.0, 'N': 0.3, 'P': 0.2, 'V': 0.5},
								   'P': {'D': 0.8, 'N': 0.2, 'P': 0.0, 'V': 0.0},
								   'V': {'D': 0.2, 'N': 0.5, 'P': 0.3, 'V': 0.0}
								   }

		path, proba = model.viterbi(['time', 'flies', 'like', 'an', 'arrow'])
		self.assertListEqual(list(path), ['N', 'V', 'P', 'D', 'N'])
		self.assertEqual(0.003, round(proba, 3))

	def test_hmm_viterbi2(self):
		"""Test viterbi algorithm on 'time flies like an arrow'
		Here, we've modified the model to make the most probable
		path be N,N,V,D,N .
		"""
		model = HMM()
		model.states = ['D', 'N', 'P', 'V']

		model.start_probas = {'D': .3,
							  'N': .4,
							  'P': .1,
							  'V': .2,
							  }

		model.emission_probas = {'D': {'time': 0.0, 'flies': 0.0, 'like': 0.0, 'an': 1.0, 'arrow': 0.0},
								 'V': {'time': 0.0, 'flies': 0.1, 'like': 0.9, 'an': 0.0, 'arrow': 0.0},
								 'P': {'time': 0.0, 'flies': 0.0, 'like': 1.0, 'an': 0.0, 'arrow': 0.0},
								 'N': {'time': 0.3, 'flies': 0.5, 'like': 0.0, 'an': 0.0, 'arrow': 0.2}
								 }
		model.transition_probas = {'D': {'D': 0.0, 'N': 1.0, 'P': 0.0, 'V': 0.0},
								   'N': {'D': 0.0, 'N': 0.5, 'P': 0.1, 'V': 0.4},
								   'P': {'D': 0.8, 'N': 0.2, 'P': 0.0, 'V': 0.0},
								   'V': {'D': 0.4, 'N': 0.3, 'P': 0.3, 'V': 0.0}
								   }

		path, proba = model.viterbi(['time', 'flies', 'like', 'an', 'arrow'])
		self.assertListEqual(list(path), ['N', 'N', 'V', 'D', 'N'])
		self.assertEqual(0.0009, round(proba, 4))


if __name__ == '__main__':
    unittest.main()