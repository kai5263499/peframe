#!/usr/bin/env python

# ----------------------------------------------------------------------
# This file is part of PEframe.
#
# PEframe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PEframe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PEframe. If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import json
import rfc3987

import pefile
import peutils

import info
import cert
import peid
import loadfile
import apiantidbg
import xor
import antivm
import apialert
import secalert
import fileurl
import meta

import funcimport
import funcexport
import sections
import strings
import dump
import directory

global filename
global pe

def get_info(pe, filename):
	show_info = json.loads(info.get(pe, filename))
	return show_info


def get_cert(pe):
	show_cert = json.loads(cert.get(pe))
	return show_cert


def get_packer(pe):
	show_packer = peid.get(pe)
	return show_packer


def get_antidbg(pe):
	show_antidbg = apiantidbg.get(pe)
	return show_antidbg


def get_xor(pe):
	show_xor = xor.get(pe)
	return show_xor

		
def get_antivm(filename):
	show_antivm = antivm.get(filename)
	return show_antivm

	
def get_apialert(pe):
	show_apialert = apialert.get(pe)
	return show_apialert

		
def get_secalert(pe):
	show_secalert = secalert.get(pe)
	return show_secalert


def get_fileurl(filename):
	show_fileurl = fileurl.get(filename)
	return show_fileurl

	
def get_meta(pe):
	show_meta = meta.get(pe)
	return show_meta



# Options

def get_import(pe):
	show_import = funcimport.get(pe)
	return json.dumps({"Imported Functions": show_import}, indent=4, separators=(',', ': '))

def get_export(pe):
	show_export = funcexport.get(pe)
	return json.dumps({"Exported Functions": show_export}, indent=4, separators=(',', ': '))

def get_sections(pe):
	show_sections = sections.get(pe)
	return json.dumps({"Sections": show_sections}, indent=4, separators=(',', ': '))

def get_strings(filename):
	show_strings = strings.get(filename)
	return show_strings

def get_dump(pe):
	return dump.get(pe)

def get_dir(pe, d):
	if d == "import":
		return directory.get_import(pe)
	if d == "export":
		return directory.get_export(pe)
	if d == "resource":
		return directory.get_resource(pe)
	if d == "debug":
		return directory.get_debug(pe)
	if d == "tls":
		return directory.get_tls(pe)

def get_uris(strings, min_length=10):
    # used when calling .extract_fileurl() before .extract_strings()
    if len(strings) <= 0:
        return

    _uri_matcher = rfc3987.get_compiled_pattern('^%(URI)s$')

    extracted_uris = [uri for uri in strings if
                                len(uri) > min_length and
                                _uri_matcher.match(uri)]
    return extracted_uris
