#!/bin/bash

export FLASK_APP=FlaskApiServerAws.py

flask run -h 0.0.0.0 --cert=cert.pem --key=key.pem
