#!/usr/bin/env python

"""Tests for `qube` package."""
import os

import pytest


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import requests
    return requests.get('https://github.com/torvalds/linux')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')


def test_command_line_interface():
    """Test the CLI."""
    pass
    # runner = CliRunner()
    # result = runner.invoke(qube_cli.main)
    # assert result.exit_code == 0
    # assert 'qube.cli.main' in result.output
    # help_result = runner.invoke(qube_cli.main, ['--help'])
    # assert help_result.exit_code == 0
