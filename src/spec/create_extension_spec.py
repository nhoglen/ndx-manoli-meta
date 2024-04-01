# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec

# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        name="""ndx-manoli-meta""",
        version="""0.1.0""",
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
                quantity=1
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
                name="experimenter",
                doc="Who actually ran the assay.",
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
            NWBDatasetSpec(
                name="introduction",
                doc="Information about introduction assays.",
                dtype='text',
                quantity='?',
                attributes=[
                    NWBAttributeSpec(
                            name="partner_ID",
                            required=True,
                            dtype="text",
                            doc="Eartag number of the partner vole.",
                            ),
                    NWBAttributeSpec(
                            name="partner_GT",
                            required=True,
                            dtype="text",
                            doc="Genotype of the partner vole.",
                            ),
                        ],
            ),
            NWBDatasetSpec(
                name="timed_mating",
                doc="Information about timed mating assays.",
                dtype='text',
                quantity='?',
                attributes=[
                    NWBAttributeSpec(
                            name="partner_ID",
                            required=True,
                            dtype="text",
                            doc="Eartag number of the partner vole.",
                    ),
                    NWBAttributeSpec(
                            name="partner_GT",
                            required=True,
                            dtype="text",
                            doc="Genotype of the partner vole.",
                    ),
                    NWBAttributeSpec(
                            name="days_post_pairing",
                            required=True,
                            dtype="int",
                            doc="How many days after the intro this assay was completed.",
                    ),
                ],
            ),
            NWBDatasetSpec(
                name="partner_preference_test",
                doc="Information about PPTs.",
                dtype='text',
                quantity='?',
                attributes=[
                    NWBAttributeSpec(
                            name="partner_ID",
                            required=True,
                            dtype="text",
                            doc="Eartag number of the partner vole.",
                        ),
                    NWBAttributeSpec(
                            name="partner_GT",
                            required=True,
                            dtype="text",
                            doc="Genotype of the partner vole.",
                        ),
                    NWBAttributeSpec(
                            name="days_post_pairing",
                            required=True,
                            dtype="int",
                            doc="How many days after the intro this assay was completed.",
                    ),
                    NWBAttributeSpec(
                            name="stranger_ID",
                            required=True,
                            dtype="text",
                            doc="Eartag number of the stranger vole used in the PPT.",
                    ),
                    NWBAttributeSpec(
                            name="stranger_GT",
                            required=True,
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
                            required=True,
                            dtype="text",
                            doc="Which chamber the partner is in.",
                    ),

                ],

                ),
                NWBDatasetSpec(
                    name="separation_reunion",
                    doc="Information about separation/reunion assays.",
                    dtype='text',
                    quantity='?',
                    attributes=[
                        NWBAttributeSpec(
                                name="partner_ID",
                                required=True,
                                dtype="text",
                                doc="Eartag number of the partner vole.",
                        ),
                        NWBAttributeSpec(
                                name="partner_GT",
                                required=True,
                                dtype="text",
                                doc="Genotype of the partner vole.",
                        ),
                        NWBAttributeSpec(
                                name="days_post_pairing",
                                required=True,
                                dtype="int",
                                doc="How many days after the intro this assay was completed.",
                        ),
                    ],
                ),
                NWBDatasetSpec(
                    name="stranger_aggression",
                    doc="Information about stranger aggression assays.",
                    dtype='text',
                    quantity='?',
                    attributes=[
                        NWBAttributeSpec(
                                name="stranger_ID",
                                required=True,
                                dtype="text",
                                doc="Eartag number of the stranger_GT vole.",
                        ),
                        NWBAttributeSpec(
                                name="stranger_GT",
                                required=True,
                                dtype="text",
                                doc="Genotype of the stranger vole.",
                        ),
                        NWBAttributeSpec(
                                name="days_post_pairing",
                                required=True,
                                dtype="int",
                                doc="How many days after the intro this assay was completed.",
                        ),

                    ],
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
