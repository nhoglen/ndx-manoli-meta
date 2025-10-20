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
        colors = [[100.0, 100.0, 100.0],[0.0, 0.0, 0.0]]
        ppt = os.path.join('pretend','path')
        peartag = 'E0001'
        seartag = 'E0002'
        pGT = 'mut'
        sGT = 'WT'
        days = 0
        pChamb = 'right'
        PPT_lane = 2
        desc = 'Standard PPT.'
        f_ETside = 'ETL'
        p_ETside = 'ETR'
        p_fam = 'WT01'
        p_DOB = '20250101'
        s_ID = 'A0000'
        s_GT = 'WT'
        s_ETside = 'ETR'
        s_fam = 'WT01'
        s_DOB = '20250101'
        s_Sex = 'M'
        HomeCage_Box = '1'
        stimtype = 'stranger'

        lmdee_object = AssayMetadata(
                        assay_type=assay,
                        exclude_flag=exclude_flag,
                        duration=duration,
                        room=room,
                        timeline=timeline,
                        ethogram=ethogram,
                        scorer=experimenter, #edited
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
                        assay_type__annotations = ppt,
                        ### all below are new ###
                        assay_type__HomeCage_Box = HomeCage_Box,
                        assay_type__focal_ETside = f_ETside,
                        assay_type__partner_DOB = p_DOB,
                        assay_type__partner_ETside = p_ETside,
                        assay_type__partner_fam = p_fam,
                        assay_type__stranger_DOB = s_DOB,
                        assay_type__stranger_ETside = s_ETside,
                        assay_type__stranger_fam = s_fam,
                        assay_type__left_ETside = p_ETside,
                        assay_type__left_fam = p_fam,
                        assay_type__right_ETside = s_ETside,
                        assay_type__right_fam = s_fam,
                        assay_type__stim_ID = s_ID,
                        assay_type__stim_GT = s_GT,
                        assay_type__stim_sex = s_Sex,
                        assay_type__stim_DOB = s_DOB,
                        assay_type__stim_ETside = s_ETside,
                        assay_type__stim_fam = s_fam,
                        assay_type__stim_type = stimtype
                        )

        self.assertEqual(lmdee_object.assay_type, assay)
        self.assertEqual(lmdee_object.exclude_flag,exclude_flag)
        self.assertEqual(lmdee_object.duration,duration)
        self.assertEqual(lmdee_object.room,room)
        self.assertEqual(lmdee_object.timeline,timeline)
        self.assertEqual(lmdee_object.ethogram,ethogram)
        self.assertEqual(lmdee_object.scorer,experimenter)
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
        self.assertEqual(lmdee_object.assay_type__HomeCage_Box, HomeCage_Box)
        self.assertEqual(lmdee_object.assay_type__focal_ETside, f_ETside)
        self.assertEqual(lmdee_object.assay_type__partner_DOB, p_DOB)
        self.assertEqual(lmdee_object.assay_type__partner_ETside, p_ETside)
        self.assertEqual(lmdee_object.assay_type__partner_fam, p_fam)
        self.assertEqual(lmdee_object.assay_type__stranger_DOB, s_DOB)
        self.assertEqual(lmdee_object.assay_type__stranger_ETside, s_ETside)
        self.assertEqual(lmdee_object.assay_type__stranger_fam, s_fam)
        self.assertEqual(lmdee_object.assay_type__left_ETside, p_ETside)
        self.assertEqual(lmdee_object.assay_type__left_fam, p_fam)
        self.assertEqual(lmdee_object.assay_type__right_ETside, s_ETside)
        self.assertEqual(lmdee_object.assay_type__right_fam, s_fam)
        self.assertEqual(lmdee_object.assay_type__stim_ID, s_ID)
        self.assertEqual(lmdee_object.assay_type__stim_GT, s_GT)
        self.assertEqual(lmdee_object.assay_type__stim_sex, s_Sex)
        self.assertEqual(lmdee_object.assay_type__stim_DOB, s_DOB)
        self.assertEqual(lmdee_object.assay_type__stim_ETside, s_ETside)
        self.assertEqual(lmdee_object.assay_type__stim_fam, s_fam)
        self.assertEqual(lmdee_object.assay_type__stim_type, stimtype)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
