from pynwb.testing.mock.file import mock_NWBFile
from pynwb.testing import TestCase
from pynwb.testing.testh5io import NWBH5IOMixin
from ndx_manoli_meta import IndividualMetadata
import os
import numpy as np

class TestLabMetaDataExtensionExampleRoundtrip(NWBH5IOMixin, TestCase):
    """
    Roundtrip test for LabMetaDataExtensionExample to test read/write

    This test class writes the LabMetaDataExtensionExample to an NWBFile, then
    reads the data back from the file, and compares that the data read from file
    is consistent with the original data. Using the pynwb.testing infrastructure
    simplifies this complex test greatly by allowing to simply define how to
    create the container, add to a file, and retrieve it form a file. The
    task of writing, reading, and comparing the data is then taken care of
    automatically by the NWBH5IOMixin.
    """
    

    def setUpContainer(self):
        """set up example LabMetaDataExtensionExample object"""
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
        
        self.lab_meta_data = IndividualMetadata(
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
        	
        return self.lab_meta_data

    def addContainer(self, nwbfile):
        """Add the test LabMetaDataExtensionExample to the given NWBFile."""
        nwbfile.add_lab_meta_data(lab_meta_data=self.lab_meta_data)

    def getContainer(self, nwbfile):
        """Get the LabMetaDataExtensionExample object from the given NWBFile."""
        return nwbfile.get_lab_meta_data(self.lab_meta_data.name)

