from pynwb.testing.mock.file import mock_NWBFile
from pynwb.testing import TestCase
from pynwb.testing.testh5io import NWBH5IOMixin
from ndx_manoli_meta import AssayMetadata
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
        assay = "partner_preference_test"
        exclude_flag = False
        duration = 10800.0
        room = 'Platyzilla'
        timeline = 'sensitized'
        ethogram = 'mark1'
        experimenter = 'Gina Williams'
        timeline_complete = True
        colors = np.array([100.0, 100.0, 100.0])
        ppt = os.path.join('pretend','path')
        peartag = 'E0001'
        seartag = 'E0002'
        pGT = 'mut'
        sGT = 'WT'
        days = 0
        pChamb = 'right'
        PPT_lane = 2
        desc = 'Standard PPT.'
        self.lab_meta_data = AssayMetadata(
                        assay_type=assay,
                        exclude_flag=exclude_flag,
                        duration=duration,
                        room=room,
                        timeline=timeline,
                        ethogram=ethogram,
                        experimenter=experimenter,
                        timeline_complete=timeline_complete,
                        colors=colors,
                        assay_type__partner_ID=peartag,
                        assay_type__partner_GT=pGT,
                        assay_type__days_post_pairing=days,
                        assay_type__stranger_ID=seartag,
                        assay_type__stranger_GT=sGT,
                        assay_type__PPT_lane = PPT_lane,
                        assay_type__partner_chamber = pChamb,
                        assay_type__description = desc
                        )
        return self.lab_meta_data

    def addContainer(self, nwbfile):
        """Add the test LabMetaDataExtensionExample to the given NWBFile."""
        nwbfile.add_lab_meta_data(lab_meta_data=self.lab_meta_data)

    def getContainer(self, nwbfile):
        """Get the LabMetaDataExtensionExample object from the given NWBFile."""
        return nwbfile.get_lab_meta_data(self.lab_meta_data.name)
