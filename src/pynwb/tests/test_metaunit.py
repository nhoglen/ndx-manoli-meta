from pynwb.testing.mock.file import mock_NWBFile
from pynwb.testing import TestCase
from ndx_manoli_meta import AssayMetadata
import numpy as np
import os

class TestLabMetaDataExtensionExample(TestCase):
    """Test basic functionality of LabMetaDataExtensionExample without read/write"""

    def setUp(self):
        """Set up an NWB file."""
        self.nwbfile = mock_NWBFile()

    def test_constructor(self):
        """Test that the constructor sets values as expected."""
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

        lmdee_object = AssayMetadata(
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
                        assay_type__description = desc,
                        assay_type__annotations = ppt
                        )

        self.assertEqual(lmdee_object.assay_type, assay)
        self.assertEqual(lmdee_object.exclude_flag,exclude_flag)
        self.assertEqual(lmdee_object.duration,duration)
        self.assertEqual(lmdee_object.room,room)
        self.assertEqual(lmdee_object.timeline,timeline)
        self.assertEqual(lmdee_object.ethogram,ethogram)
        self.assertEqual(lmdee_object.experimenter,experimenter)
        self.assertEqual(lmdee_object.timeline_complete,timeline_complete)
        self.assertEqual(list(lmdee_object.colors),list(colors))
        self.assertEqual(lmdee_object.assay_type__partner_ID,peartag)
        self.assertEqual(lmdee_object.assay_type__partner_GT, pGT)
        self.assertEqual(lmdee_object.assay_type__stranger_ID, seartag)
        self.assertEqual(lmdee_object.assay_type__stranger_GT, sGT)
        self.assertEqual(lmdee_object.assay_type__partner_chamber, pChamb)
        self.assertEqual(lmdee_object.assay_type__PPT_lane, PPT_lane)
        self.assertEqual(lmdee_object.assay_type__days_post_pairing, days)
        self.assertEqual(lmdee_object.assay_type__description, desc)
        self.assertEqual(lmdee_object.assay_type__annotations, ppt)
