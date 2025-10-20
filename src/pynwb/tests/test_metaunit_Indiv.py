from pynwb.testing.mock.file import mock_NWBFile
from pynwb.testing import TestCase
from ndx_manoli_meta import IndividualMetadata
import numpy as np
import os

class TestLabMetaDataExtensionExample(TestCase):
    """Test basic functionality of LabMetaDataExtensionExample without read/write"""

    def setUp(self):
        """Set up an NWB file."""
        self.nwbfile = mock_NWBFile()

    def test_constructor(self):
        """Test that the constructor sets values as expected."""
        age = 'P7W'
        age_ref = 'birth'
        desc = 'test vole'
        geno = 'WT'
        species = 'vole'
        sex = 'M'
        eartag = 'A0000'
        weight = "4500 kg"
        DOB = '20251010'
        strain = 'WT'

        lmdee_object = IndividualMetadata(
        	age__reference = age_ref,
        	age = age,
        	description = desc,
        	genotype = geno,
        	species = species,
        	sex = sex,
        	individual_id = eartag,
        	weight = weight,
        	date_of_birth = DOB,
        	strain = strain
        	)

        
        self.assertEqual(lmdee_object.age, age)
        self.assertEqual(lmdee_object.age__reference, age_ref)
        self.assertEqual(lmdee_object.description, desc)
        self.assertEqual(lmdee_object.genotype, geno)
        self.assertEqual(lmdee_object.species, species)
        self.assertEqual(lmdee_object.sex, sex)
        self.assertEqual(lmdee_object.individual_id, eartag)
        self.assertEqual(lmdee_object.weight, weight)
        self.assertEqual(lmdee_object.date_of_birth, DOB)
        self.assertEqual(lmdee_object.strain, strain)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
