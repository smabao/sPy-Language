import sys
from ply.lex import TOKEN

# List of tokens


reserved = {
  'comienzo': 'start',
  'si': 'if',
  'otro': 'else',
  'mientras': 'while',
  'hacer':'do',
  'regresso':'return',
  'imprimir': 'print',
  'introducir': 'scan',
  'para': 'for',
  'avisar':'call',
  'es': 'is',
  'tratar':'try',
  'fin':'end',
  'romperse':'break',
  'clase':'class',
  'explicar':'def',
  'fin_explicar':'end_def',
  'Int' : 'int',
  'String' : 'string'
}

tokens =(
  'VAR',
  'LT',
  'GT',
  'LEQ',
  'GEQ',
  'EQ',
  'NEQ',
  'NOT',
  'OR',
  'AND',
  'STRLIT',
  'CHRLIT',
  'INTLIT',
  'FLTLIT',
  'DBLLIT',
  'BOOLEAN',
  'PLUS',
  'MINUS',
  'MUL',
  'DIV',
  'MOD',
  'OPENPAR',
  'CLOSEPAR',
  'OPENCURLY',
  'CLOSECURLY',
  'OPENBRACE',
  'CLOSEBRACE',
  'ASSIGN',
  'COMMA',
  'TILDE',
  'QUOTATION',
  'UNDERSCORE',
  'SINGLE_COMMENT',
  'MULTI_COMMENT'
)

literals = ['+','-','*','/','%']

tokens = list(reserved.values()) + list(tokens)

# Regular expression rules for simple tokens
t_LT = r'\<'
t_GT = r'\>'
t_LEQ = r'\<\='
t_GEQ = r'\>\='
t_EQ = r'\=\='
t_NEQ = r'\!='
t_NOT = r'\!' 
t_OR = r'\|\|' 
t_AND = r'\&\&' 
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'\%' 
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENCURLY = r'\{'
t_CLOSECURLY = r'\}'
t_OPENBRACE = r'\['
t_CLOSEBRACE = r'\]'
t_ASSIGN = r'\='
t_TILDE = r'\~'
t_QUOTATION = r'\"'
t_UNDERSCORE = r'\_'

# Ignore whitespaces
t_ignore = r' t'

def t_FLTLIT(t):
	r'\d\.\d+'
	t.value = float(t.value)
	return t

def t_INTLIT(t):
	r'\d+'
	t.value = int(t.value)
	return t
	
# Determining if reserved word
def t_VAR(t):
  r'[a-z][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value.lower(), 'VAR')
  return t
	
# Match the first quotes for strings
def t_STRLIT(t):
	r'[\"][^\"]+[\"]'
	t.value = str(t.value).strip('\"')
	return t
	
# Defining a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# RegExp for single line comments: No return value. Token discarded.
def t_SINGLE_COMMENT(t):
  r'\*\*.*'
  pass

# RegExp for single line comments: No return value. Token discarded.
def t_MULTI_COMMENT(t):
  r'\~\*(.|\n)*\*\~'
  pass
 
def t_error(t):
	print("SYNTAX ERROR: Illegal character: '%s' \n\tLine number: %d" (t.value[0], t.lineno))
	t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

#---------------- end of lexer---------------------

import ply.yacc as yacc

precedence = (
  ('left','PLUS','MINUS'),
  ('left','MUL','DIV', 'MOD'),
)


# def p_main_program(p):    
#     '''
#         main_program : start OPENCURLY statements TILDE CLOSECURLY end
#     '''
  
# def p_statements(p):
#     '''
#         statements  : expression
#                     | function_heading
#                     | classes
#                     | scan VAR
#                     | statements_print
#                     | return OPENPAR expression_list CLOSEPAR
#                     | optional_statements
#                     | if_stmt 
#                     | while_stmt
#                     | statement_assign
#                     | comment
#                     | empty
#     '''

# def p_statements_print(p):
#     '''
#     statements_print : PRINT OPENPAR STRLIT CLOSEPAR
#                      | PRINT identifier_list
#     '''
#     print(p[3])

# def p_identifier_list(p):
#     '''
#         identifier_list : VAR identifier_list
#                         | UNDERSCORE
#                         | empty
#     '''
#     p[0] = p[1]
    
# def p_statement_assign(t):
#   '''  
#       statement_assign : VAR ASSIGN expression

#   '''

# def p_empty(p):
#     '''
#         empty : 
#     '''
#     p[0] = None

# def p_expression(p):
  
#     '''
#         expression  : expression_list
#                     | identifier_list
#     '''
    
# def p_expression_list(p):
#     '''
#         expression_list : logical_expression
#                         | arithmetic_expression
#     '''
# def p_logical_expression(p):
#     '''
#         logical_expression  : expression '<' expression 
#                             | expression '>' expression
#                             | expression LEQ expression
#                             | expression GEQ expression
#                             | expression '=' expression
#                             | expression NEQ expression
#                             | expression EQ expression
#                             | expression '!' expression
#                             | expression OR expression
#                             | expression AND expression
#     '''
#     if p[2]=='<':
#         p[0] = p[1] < p[3]
#     elif p[2]=='>':
#         p[0]= p[1] > p[3]
#     elif p[2]=='LEQ':
#         p[0]= p[1] <= p[3]
#     elif p[2]=='GEQ':
#         p[0]= p[1] >= p[3]
#     elif p[2]=='EQ':
#         p[0]= p[1] == p[3]
#     elif p[2]=='!':
#         p[0]= p[1] != p[3]
#     elif p[2]=='OR':
#         p[0]= p[1] or p[3]
#     elif p[2]=='AND':
#         p[0]= p[1] and p[3]

# def p_arithmetic_expression(p):
#     '''
#         arithmetic_expression : expression '+' expression
#                               |  expression '-' expression
#                               |  expression '*' expression
#                               |  expression '/' expression
#                               |  expression '%' expression
#     '''
#     if p[2]=='+':
#         p[0]= p[1] + p[3]
#     elif p[2]=='-':
#         p[0]= p[1] - p[3]
#     elif p[2]=='*':
#         p[0]= p[1] * p[3]
#     elif p[2]=='/':
#         p[0]= p[1] / p[3]
#     elif p[2]=='%':
#         p[0]= p[1] % p[3]

# def p_type(p):
#     '''
#         type : INTLIT 
#              | FLTLIT  
#              | DBLLIT 
#              | CHRLIT 
#              | STRLIT 
#     '''
#     p[0] = p[1]

# def p_optional_statements(p):
#     '''
#         optional_statements : statement_list
#                             | empty 
#     '''

# def p_statement_list(p):
#     '''
#         statement_list : statements
#                        | statement_list statements 
#     '''
# def p_if_stmt(p):
#     '''
#         if_stmt  : if OPENPAR expression_list CLOSEPAR else statements
#                  | if OPENPAR expression_list CLOSEPAR statements
#                  | if OPENPAR expression_list CLOSEPAR statements else_if
#     '''

# def p_else_if(p):
#     '''
#         else_if : else OPENPAR expression CLOSEPAR statements else_if
#                 | empty
#     '''

# def p_while_stmt(p):
#     '''
#         while_stmt : while OPENPAR expression_list CLOSEPAR TILDE optional_statements TILDE
#                    | while OPENPAR expression_list CLOSEPAR TILDE optional_statements TILDE break
#     '''

# def p_classes(p): 
#     '''
#         classes : class identifier_list OPENCURLY optional_statements CLOSECURLY
#     '''

# def p_function_heading(p):
#     '''
#         function_heading : def identifier_list OPENPAR parameters TILDE CLOSEPAR statements TILDE end_def
#     '''

# def p_parameters(p):
#     '''
#         parameters : type
#                    | type COMMA parameters
#                    | empty
#     '''

# def p_comment(p):
#     '''
#         comment : SINGLE_COMMENT statements
#                 | MULTI_COMMENT statements MULTI_COMMENT
#     '''
#     p[0] = None

  
# def p_error(p):
#      print("PARSER ERROR!: ",p)

def p_main_program(p):
    '''main_program : start OPENCURLY statement CLOSECURLY end'''

def p_statement_empty(t):
    '''statement : empty'''

def p_empty_stmt(t):
    '''empty :  '''
    t[0] = None

def p_statement_loop(p):
    '''statement : statement statement statement'''

def p_statement_assign(t):
   '''statement : VAR ASSIGN expression TILDE'''

def p_statement_expr(t):
    '''statement : expression TILDE'''

def p_statement_function(p):
    '''statement : def VAR OPENPAR parameter CLOSEPAR statement end_def'''

def p_parameter_int(t):
    '''parameter : int VAR'''

def p_parameter_string(t):
    '''parameter : string VAR'''

def p_statement_class(p):
    '''statement : class VAR OPENCURLY statement CLOSECURLY'''

def p_statement_scan(t):
    '''statement : VAR ASSIGN expression TILDE scan OPENPAR VAR CLOSEPAR TILDE'''

def p_statement_scan_string(t):
    '''statement : VAR ASSIGN STRLIT TILDE scan OPENPAR VAR CLOSEPAR TILDE'''

def p_statement_return(t):
    '''statement : VAR ASSIGN expression TILDE return OPENPAR VAR CLOSEPAR TILDE'''
    return(t[3])

def p_statement_return_string(t):
    '''statement : VAR ASSIGN STRLIT TILDE return OPENPAR VAR CLOSEPAR TILDE'''
    return(t[3])

def p_statement_print(t):
    '''statement : print OPENPAR expression CLOSEPAR TILDE'''
    print(t[3])

def p_statement_print_string(t):
    '''statement : print OPENPAR STRLIT CLOSEPAR TILDE'''
    print(t[3])

def p_statement_print_var(t):
    '''statement : VAR ASSIGN expression TILDE print OPENPAR VAR CLOSEPAR TILDE'''
    print(t[3])

def p_statement_print_var_string(t):
    '''statement : VAR ASSIGN STRLIT TILDE print OPENPAR VAR CLOSEPAR TILDE'''
    print(t[3])

def p_statement_if(t):
    '''statement : if_statement'''

def p_statement_if_stmt(p):
    '''if_statement : if OPENPAR boolean CLOSEPAR statement'''
    if (p[3]):
        p[0] = p[5]

def p_statement_if_else(p):
    '''if_statement : if OPENPAR boolean CLOSEPAR statement else statement'''
    if (p[3]):
        p[5]
    else:
        p[7]

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_expression_boolean(p):
    '''expression : boolean'''
    p[0] = p[1]

# def p_boolean(p):
#     '''boolean : expression GT term
#                | expression GEQ term
#                | expression LT term
#                | expression LEQ term
#                | expression EQ term
#                | expression NEQ term
#                | expression AND term
#                | expression OR term'''
#     if(p[2] == '>'):
#       p[0] = p[1] > p[3]
#     elif(p[2] == '>='):
#       p[0] = p[1] >= p[3]
#     elif(p[2] == '<'):
#       p[0] = p[1] < p[3]
#     elif(p[2] == '<='):
#       p[0] = p[1] <= p[3]
#     elif(p[2] == '=='):
#       p[0] = p[1] == p[3]
#     elif(p[2] == '!'):
#       p[0] = p[1] != p[3]
#     elif(p[2] == '&&'):
#       p[0] = p[1] and p[3]
#     elif(p[2] == '||'):
#       p[0] = p[1] or  p[3]

def p_expression_PLUS(p):
    '''expression : expression PLUS term'''
    p[0] = p[1] + p[3]

def p_expression_MINUS(p):
    '''expression : expression MINUS term'''
    p[0] = p[1] - p[3]

def p_expression_GT(p):
    '''boolean : expression GT term'''
    p[0] = p[1] > p[3]

def p_expression_GEQ(p):
    '''boolean : expression GEQ term'''
    p[0] = p[1] >= p[3]

def p_expression_LT(p):
    '''boolean : expression LT term'''
    p[0] = p[1] < p[3]

def p_expression_LEQ(p):
    '''boolean : expression LEQ term'''
    p[0] = p[1] <= p[3]

def p_expression_EQ(p):
    '''boolean : expression EQ term'''
    p[0] = p[1] == p[3]

def p_expression_NEQ(p):
    '''boolean : expression NEQ term'''
    p[0] = p[1] != p[3]

def p_expression_AND(p):
    '''boolean : expression AND term'''
    p[0] = p[1] and p[3]

def p_expression_OR(p):
    '''boolean : expression OR term'''
    p[0] = p[1] or p[3]

def p_term_MUL(p):
    '''term : term MUL factor'''
    p[0] = p[1] * p[3]

def p_term_DIV(p):
    '''term : term DIV factor'''
    p[0] = p[1] / p[3]

def p_term_MOD(p):
    '''term : term MOD factor'''
    p[0] = p[1] % p[3]

def p_term_STR(p):
    '''term : STRLIT'''
    p[0] = p[1]

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_INT(p):
    '''factor : INTLIT'''
    p[0] = p[1]

def p_factor_expr(p):
    '''factor : OPENPAR expression CLOSEPAR'''
    p[0] = p[2]

def p_error(p):
     print("PARSER ERROR!: ",p)

parser = yacc.yacc()

# getting the file input from cmd
try:
    file_input = sys.argv[1];
    pass
except Exception as e:
    print("Missing file input!")
    print("Try this: python main.py <filename>")
    sys.exit()

# Open the input file.
f = open(file_input, 'r')
data = f.read()
f.close()

# Build the lexer
lexer.input(data)
print("TOKENS:")
while True:
    tok = lexer.token()
    if not tok: 
        break
    print("\t",tok)
print("\nEVALUATION:")

#print(statementlist)

parser.parse(data)



