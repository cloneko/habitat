import nose
import json
import sys
from py_w3c.validators.html.validator import HTMLValidator

validator = HTMLValidator()
validator.validate_file('index.html') 


def test_has_no_error():
	assert len(validator.errors) == 0

def test_has_no_warning():
	assert len(validator.warnings) == 0




