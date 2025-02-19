"""
Code for importing registration list data into DIRBS Core.

Copyright (c) 2018 Qualcomm Technologies, Inc.

 All rights reserved.



 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the
 limitations in the disclaimer below) provided that the following conditions are met:


 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following
 disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
 disclaimer in the documentation and/or other materials provided with the distribution.

 * Neither the name of Qualcomm Technologies, Inc. nor the names of its contributors may be used to endorse or promote
 products derived from this software without specific prior written permission.

 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY
 THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

"""

from dirbs.importer.base_delta_importer import BaseDeltaImporter


class RegistrationListImporter(BaseDeltaImporter):
    """Registration list data importer."""

    @property
    def _import_type(self):
        """Overrides AbstractImporter._import_type."""
        return 'registration_list'

    @property
    def _import_relation_name(self):
        """Overrides AbstractImporter._import_relation_name."""
        return 'registration_list'

    @property
    def _schema_file(self):
        """Overrides AbstractImporter._schema_file."""
        if self._delta:
            return 'RegistrationListDeltaSchema.csvs'
        return 'RegistrationListSchema.csvs'

    @property
    def _owner_role_name(self):
        """Overrides AbstractImporter._owner_role_name."""
        return 'dirbs_core_import_registration_list'

    @property
    def _staging_tbl_ddl(self):
        """Overrides BaseImporter._staging_tbl_ddl."""
        return """CREATE UNLOGGED TABLE {0} (
                                             row_id       BIGSERIAL NOT NULL,
                                             imei         TEXT,
                                             imei_norm    TEXT NOT NULL,
                                             make         TEXT,
                                             model        TEXT,
                                             status       TEXT
                                            )"""

    @property
    def _pk_field_names(self):
        """Overrides BaseDeltaImporter._pk_field_names."""
        return ['imei_norm']

    @property
    def _input_csv_field_names(self):
        """Overrides BaseDeltaImporter._input_csv_field_names."""
        return ['imei', 'make', 'model', 'status']

    @property
    def _extra_field_names(self):
        """Overrides BaseDeltaImporter._extra_field_names."""
        return ['make', 'model', 'status']

    @property
    def _supports_imei_shards(self):
        """Overrides AbstractImporter._supports_imei_shards."""
        return True
