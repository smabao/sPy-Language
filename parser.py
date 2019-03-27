#!/usr/bin/python
import ply.yacc as yacc
from lexer import *  

precedence = (
  ('left','PLUS','MINUS'),
  ('left','MUL','DIV', 'MOD'),
)

def p_main_program(p):    
    '''
        main_program : comienzo OPENCURLY statements CLOSECURLY fin
                     | comienzo classes fin
                     | comienzo function_heading fin                    
    '''
def p_statements(p):
    '''
        statements  : identifier_list EQ expression
                    | introducir type
                    | imprimir OPENPAR identifier_list CLOSEPAR
                    | imprimir QUOTATION identifier_list QUOTATION
                    | regresso OPENPAR expression_list CLOSEPAR
                    | si OPENPAR expression_list CLOSEPAR otro statements
                    | optional_statements
                    | if 
                    | while 
                    | COMMENT
    '''
def p_identifier_list(p):
    '''
        identifier_list : (A|B|C|D|...|Z) identifier_list
                        | (a|b|c|d|...|Z) identifier_list
                        | (0|1|2|3|...|9) identifier_list
                        | UNDERSCORE
                        | empty
    '''
    p[0] = p[1]

def p_empty(p):
    '''
        empty: 
    '''
    p[0] = None

def p_expression(p):
    '''
        expression  : expression
                    | expression_list COMMA expression
                    | identifier_list
    '''
    
def p_expression_list(p):
    '''
        expression_list : logical_expression
                        |  arithmetic_expression
    '''
def p_logical_expression(p):
    '''
        logical_expression  : expression '<' expression 
                            | expression '>' expression
                            | expression '<=' expression
                            | expression '>=' expression
                            | expression '=' expression
                            | expression '!=' expression
                            | expression '==' expression
                            | expression '!' expression
                            | expression '||' expression
                            | expression '&&' expression
    '''
    if p[2]=='<':
        p[0] = p[1] < p[3]
    elif p[2]=='>':
        p[0]= p[1] > p[3]
    elif p[2]=='<=':
        p[0]= p[1] <= p[3]
    elif p[2]=='>=':
        p[0]= p[1] >= p[3]
    elif p[2]=='==':
        p[0]= p[1] == p[3]
    elif p[2]=='!':
        p[0]= p[1] != p[3]
    elif p[2]=='||':
        p[0]= p[1] or p[3]
    elif p[2]=='&&':
        p[0]= p[1] and p[3]

def p_arithmetic_expression(p):
    '''
        arithmetic_expression : expression '+' expression
                              |  expression '-' expression
                              |  expression '*' expression
                              |  expression '/' expression
                              |  expression '%' expression
    '''
    if p[2]=='+':
        p[0]= p[1] + p[3]
    elif p[2]=='-':
        p[0]= p[1] - p[3]
    elif p[2]=='*':
        p[0]= p[1] * p[3]
    elif p[2]=='/':
        p[0]= p[1] / p[3]
    elif p[2]=='%':
        p[0]= p[1] % p[3]

def p_type(p):
    '''
        type : int identifier_list TILDE
             | float identifier_list TILDE 
             | double identifier_list TILDE 
             | char identifier_list TILDE 
             | string identifier_list TILDE 
    '''
    p[0] = (p[1], p[2])

def p_optional_statements(p):
    '''
        optional_statements : statement_list
                            | empty 
    '''

def p_statement_list(p):
    '''
        statement_list : statements
                       | statement_list statements 
    '''
def p_if(p):
    '''
        if  : si OPENPAR expression_list CLOSEPAR statements
            | si OPENPAR expression_list CLOSEPAR statements else_if
    '''

def p_else_if(p):
    '''
        else_if : otro OPENPAR expression CLOSEPAR statements else_if
                | empty
    '''

def p_while(p):
    '''
        while : mientras OPENPAR expression_list CLOSEPAR TILDE optional_statements TILDE
              | mientras OPENPAR expression_list CLOSEPAR TILDE optional_statements TILDE romperse
    '''

def p_comment(p):
    '''
        comment : '**' statements comment
                | '*~' statements '*~' comment
    '''

def p_classes(p): 
    '''
        classes : clase OPENCURLY identifier_list optional_statements CLOSECURLY
    '''

def p_function_heading(p):
    '''
        function_heading : explicar identifier_list OPENPAR parameters TILDE CLOSEPAR statements fin_explicar
    '''
def p_parameters(p):
    '''
        parameters : type
                   | type COMMA parameters
                   | empty
    '''



        

