"""Key to PDF, abs and src for a given ID"""

import re
from typing import Union, Literal, Optional

from arxiv.identifier import Identifier

Formats = Literal["pdf", "ps"]


def _ps_cache_part(format: Formats, arxiv_id: Identifier) -> str:
    archive = arxiv_id.archive if arxiv_id.is_old_id else 'arxiv'
    return f"ps_cache/{archive}/{format}/{arxiv_id.yymm}"

def ps_cache_pdf_path(format:Formats, arxiv_id: Identifier, version=0)  -> str:
    """Returns the path for a PDF from the ps_cache for a version.

    For PDFs in ps_cache, all of the versions are in the same directory so
    there is no current/non-current distinction when using the ps_cache.

    All the PDFs in ps_cache should have been built from tex.

    This will return the proper path if it exists or not.

    if version is passed, that will be used instead of the version on arxiv_id."""
    dir = _ps_cache_part(format, arxiv_id)
    if not version:
        version = arxiv_id.version
    return f"{dir}/{arxiv_id.filename}v{version}.pdf"


def current_pdf_path(arxiv_id: Identifier) -> str:
    """Returns the path for a PDF only submission for a current version.

    This will return the proper path if it exists or not."""
    archive = arxiv_id.archive if arxiv_id.is_old_id else 'arxiv'
    return f"ftp/{archive}/papers/{arxiv_id.yymm}/{arxiv_id.filename}.pdf"


def previous_pdf_path(arxiv_id: Identifier) -> str:
    """Returns the path for a PDF only submission for a non current version.

    This will return the proper path if it exists or not."""
    archive = arxiv_id.archive if arxiv_id.is_old_id else 'arxiv'
    return f"orig/{archive}/papers/{arxiv_id.yymm}/{arxiv_id.filename}v{arxiv_id.version}.pdf"

def abs_path_orig_parent(arxiv_id: Identifier) -> str:
    """Returns the path to the directory of the abstract in orig"""
    archive = arxiv_id.archive if arxiv_id.is_old_id else 'arxiv'
    return f"orig/{archive}/papers/{arxiv_id.yymm}"

def abs_path_orig(arxiv_id: Identifier, version=0) -> str:
    """Returns the path to the abstract in orig.

    If version is passed, that will be used instead of the version on arxiv_id."""
    if not version:
        version = arxiv_id.version
    return f"{abs_path_orig_parent(arxiv_id)}/{arxiv_id.filename}v{version}.abs"

def abs_path_current_parent(arxiv_id: Identifier) -> str:
    """Returns the path to the parent dirctory of the abstract in the current version location"""
    archive = arxiv_id.archive if arxiv_id.is_old_id else 'arxiv'
    return f"ftp/{archive}/papers/{arxiv_id.yymm}"

def abs_path_current(arxiv_id: Identifier) -> str:
    """Returns the path to the abstract in the current version location"""
    archive = arxiv_id.archive if arxiv_id.is_old_id else 'arxiv'
    return f"{abs_path_current_parent(arxiv_id)}/{arxiv_id.filename}.abs"
