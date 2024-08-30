import os
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from helpers import 

from cs50 import SQL as sl
print("test")
