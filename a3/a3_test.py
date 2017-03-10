# coding: utf-8
"""
@name=a3/a3.py
@possible_points=50

Unit tests for Assignment 3.
"""
import unittest
from a3 import *

#######################################################
# Here are two example sentences used in testing below


data = [
			[('EU', 'NNP', 'I-NP', 'I-ORG'),
			 ('reject', 'VBZ', 'I-VP', 'O'),
			 ('German', 'JJ', 'I-NP', 'I-MISC'),
			 ('call', 'NN', 'I-NP', 'O')
			],
			[('The', 'DT', 'I-NP', 'O'),
			 ('European', 'NNP', 'I-NP', 'I-ORG'),
			 ('Commission', 'NNP', 'I-NP', 'I-ORG'),
			 ('said', 'VBD', 'I-VP', 'O'),
			 ('on', 'IN', 'I-PP', 'O'),
			 ('Thursday', 'NNP', 'I-NP', 'O')
			]
		]
#######################################################



class TestA3(unittest.TestCase):


	def test_labels(self):
		"""Test that NER labels are returned.
		"""
		dicts, labels = make_feature_dicts(data, token=True, caps=False, pos=False, chunk=False, context=False)
		self.assertEqual('I-ORG', labels[0])
		self.assertEqual('O', labels[1])
		self.assertEqual(10, len(labels))

	def test_token_features(self):
		"""Test token features.
		"""
		dicts, labels = make_feature_dicts(data, token=True, caps=False, pos=False, chunk=False, context=False)
		self.assertEqual(1, dicts[0]['tok=eu'])
		self.assertEqual(1, dicts[1]['tok=reject'])
		self.assertEqual(10, len(dicts))
		# make sure no other features are there.
		self.assertEqual(1, len(dicts[0]))

	def test_caps_features(self):
		"""Test caps features.
		"""
		dicts, labels = make_feature_dicts(data, token=False, caps=True, pos=False, chunk=False, context=False)
		self.assertEqual(1, dicts[0]['is_caps'])
		self.assertTrue('is_caps' not in dicts[1])


	def test_pos_features(self):
		"""Test pos features.
		"""
		dicts, labels = make_feature_dicts(data, token=False, caps=False, pos=True, chunk=False, context=False)
		self.assertEqual(1, dicts[0]['pos=NNP'])
		self.assertTrue(1, dicts[1]['pos=VBZ'])

	def test_chunk_features(self):
		"""Test chunk features.
		"""
		dicts, labels = make_feature_dicts(data, token=False, caps=False, pos=False, chunk=True, context=False)
		self.assertEqual(1, dicts[0]['chunk=I-NP'])
		self.assertTrue(1, dicts[1]['chunk=I-VP'])

	def test_context_features(self):
		"""Test context features.
		"""
		dicts, labels = make_feature_dicts(data, token=True, caps=False, pos=False, chunk=False, context=True)
		self.assertEqual(1, dicts[0]['next_tok=reject'])
		self.assertTrue(1, dicts[1]['prev_tok=eu'])
		self.assertTrue(1, dicts[1]['next_tok=german'])
				

if __name__ == '__main__':
    unittest.main()