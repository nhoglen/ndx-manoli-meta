# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec

# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        name="""ndx-manoli-meta""",
        version="""0.2.2""",
        doc="""Metadata specific to Manoli lab experiments.""",
        author=[
            "Nerissa Hoglen",
        ],
        contact=[
            "nerissa.hoglen@ucsf.edu",
        ],
    )
    ns_builder.include_namespace("core")
    ns_builder.include_type('LabMetaData', namespace='core')

    labmetadata_ext = NWBGroupSpec(
        name='vole_metadata',
        doc='Extension for storing metadata for Manoli lab behavioral assays.',
        neurodata_type_def='AssayMetadata',
        neurodata_type_inc='LabMetaData',

        datasets=[
            NWBDatasetSpec(
                name="assay_type",
                doc="What assay type is recorded in the file.",
                dtype='text',
                quantity=1,
                attributes=[
                    NWBAttributeSpec(
                            name="description",
                            required=True,
                            dtype="text",
                            doc="Description of the assay (especially if non standard).",
                            ),
                    NWBAttributeSpec(
                            name="annotations",
                            required=False,
                            dtype="text",
                            doc="Filename corresponding to annotation file.",
                            ),
                    NWBAttributeSpec(
                            name="partner_ID",
                            required=False,
                            dtype="text",
                            doc="Eartag number of the partner vole.",
                            ),
                    NWBAttributeSpec(
                            name="partner_GT",
                            required=False,
                            dtype="text",
                            doc="Genotype of the partner vole.",
                            ),
                    NWBAttributeSpec(
                            name="days_post_pairing",
                            required=False,
                            dtype="int",
                            doc="How many days after the intro this assay was completed.",
                            ),
                    NWBAttributeSpec(
                            name="stranger_ID",
                            required=False,
                            dtype="text",
                            doc="Eartag number of the stranger vole used in the PPT.",
                            ),
                    NWBAttributeSpec(
                            name="stranger_GT",
                            required=False,
                            dtype="text",
                            doc="Genotype of the stranger vole used in the PPT.",
                            ),
                    NWBAttributeSpec(
                            name="PPT_lane",
                            required=False,
                            dtype="int",
                            doc="Which lane of the PPT apparatus or video.",
                            ),
                    NWBAttributeSpec(
                            name="partner_chamber",
                            required=False,
                            dtype="text",
                            doc="Which chamber the partner is in.",
                            ),
                    NWBAttributeSpec(
                            name="divided",
                            required=False,
                            dtype="bool",
                            doc="Whether the assay took place with a divider.",
                            ),
                    NWBAttributeSpec(
                            name="isolation_length",
                            required=False,
                            dtype="int",
                            doc="Amount of time (in s) the focal animal was isolated before assay start.",
                            ),
                    NWBAttributeSpec(
                            name="left_ID",
                            required=False,
                            dtype="text",
                            doc="Eartag for animal in left chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="left_GT",
                            required=False,
                            dtype="text",
                            doc="Genotype for animal in left chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="left_sex",
                            required=False,
                            dtype="text",
                            doc="Sex for animal in left chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="left_DOB",
                            required=False,
                            dtype="text",
                            doc="Birthdate for animal in left chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="left_type",
                            required=False,
                            dtype="text",
                            doc="Experimental description for animal in left chamber of a three-chamber assay (ie partner vs stranger, novel vs familiar, etc).",
                            ),
                    NWBAttributeSpec(
                            name="right_ID",
                            required=False,
                            dtype="text",
                            doc="Eartag for animal in right chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="right_GT",
                            required=False,
                            dtype="text",
                            doc="Genotype for animal in right chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="right_sex",
                            required=False,
                            dtype="text",
                            doc="Sex for animal in right chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="right_DOB",
                            required=False,
                            dtype="text",
                            doc="Birthdate for animal in right chamber of a three-chamber assay.",
                            ),
                    NWBAttributeSpec(
                            name="right_type",
                            required=False,
                            dtype="text",
                            doc="Experimental description for animal in right chamber of a three-chamber assay (ie partner vs stranger, novel vs familiar, etc).",
                            ),
                        ],
            ),
            NWBDatasetSpec(
                name="exclude_flag",
                doc="Should the assay be excluded.",
                dtype='bool',
                quantity=1
            ),
            NWBDatasetSpec(
                name="duration",
                doc="Length of a complete assay, in seconds.",
                dtype='float',
                quantity=1
            ),
            NWBDatasetSpec(
                name="room",
                doc="The lab room in which the assay was conducted.",
                dtype='text',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="camera_type",
                doc="The camera type with which the assay was recorded.",
                dtype='text',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="timeline",
                doc="Which social behavior timeline system was followed for sequencing and timing the assays.",
                dtype='text',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="ethogram",
                doc="Which ethogram standard was used for scoring the assay.",
                dtype='text',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="scorer",
                doc="Who scored the assay.",
                dtype='text',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="timeline_complete",
                doc="Whether the whole social timeline was run to completion.",
                dtype='bool',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="genotype_confirmed",
                doc="Whether the genotype of the focal animal was confirmed after the experiment.",
                dtype='bool',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="pregnancy",
                doc="Whether the focal animal or partner was confirmed to be pregnant.",
                dtype='text',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="path_to_histology_files",
                doc="The path to any corresponding histology files.",
                dtype='text',
                quantity='?'
            ),
            NWBDatasetSpec(
                name="colors",
                doc="The color(s) to use for plotting this assay.",
                dtype='float',
                quantity='?',
                shape=(3,)
            ),


        ]

    )

    # TODO: add all of your new data types to this list
    new_data_types = [labmetadata_ext]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "spec"))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
