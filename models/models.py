# -*- coding: utf-8 -*-

from odoo import models, fields


class student_management(models.Model):
    _name = 'student.info'
    _description = 'student information'

    studentid=fields.Char(string="studentid",required=True)
    studentname=fields.Char(string="studentname",required=True)
    score=fields.Float(string="score",required=True)

    
class student_management1(models.Model):
    _name = 'student.exam'
    _description = 'student information'

    questionid=fields.Char(string="questionid",required=True)
    question=fields.Text(string="question",required=True)
    answer=fields.Text(string="answer",required=True)
    marks=fields.Float(string="marks",required=True)