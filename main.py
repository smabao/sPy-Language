import sys
from ply.lex import TOKEN

# List of tokens


reserved = {
  'comienzo': 'start',
  'si': 'if',
  'otro': 'else',
  'mientras': 'while',
  #'hacer':'do',
  'regresso':'return',
  'imprimir': 'print',
  'introducir': 'scan',
  #'para': 'for',
  #'avisar':'call',
  'es': 'is',
  #'tratar':'try',
  'fin':'end',
  'romperse':'break',
  'clase':'class',
  'explicar':'def',
  'fin_explicar':'end_def',

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
  'MULTI_COMMENT',
  'IS'
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
t_ignore = r' \t'

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

def p_main_program(p):
    '''main_program : start OPENCURLY statement CLOSECURLY end'''

def p_statement_empty(t):
    '''statement : empty'''

def p_empty_stmt(t):
    '''empty :  '''
    t[0] = None

def p_statement_stmtList(p):
    '''statement : statement_list'''

def p_statementList(p):
    '''statement_list : statement
                      | statement statement_list'''

def p_statement_assign(t):
    '''statement : VAR ASSIGN expression TILDE
                 | VAR ASSIGN INTLIT TILDE '''
    t[0]=t[3]

def p_statement_expr(t):
    '''statement : expression TILDE'''

def p_statement_function(p):
    '''statement : def VAR OPENPAR CLOSEPAR OPENCURLY statement  CLOSECURLY end_def'''

def p_func_parameter(t):
    '''parameter : INTLIT
                 | STRLIT'''
    p[0] = p[1]

def p_statement_class(p):
    '''statement : class VAR OPENCURLY statement CLOSECURLY'''

def p_statement_scan(t):
    '''statement : VAR ASSIGN OPENPAR expression CLOSEPAR TILDE scan OPENPAR VAR CLOSEPAR TILDE'''

def p_statement_scan_string(t):
    '''statement : VAR ASSIGN OPENPAR STRLIT CLOSEPAR TILDE scan OPENPAR VAR CLOSEPAR TILDE'''

def p_statement_return(t):
    '''statement : VAR ASSIGN expression TILDE return OPENPAR VAR CLOSEPAR TILDE'''
    return(t[3])
    #List.append(t[3])

def p_statement_return_string(t):
    '''statement : VAR ASSIGN STRLIT TILDE return OPENPAR VAR CLOSEPAR TILDE'''
    return(t[3])
    #List.append(t[3])

def p_statement_print(t):
    '''statement : print OPENPAR expression CLOSEPAR TILDE'''
    print(t[3])
    #List.append(t[3])

def p_statement_print_string(t):
    '''statement : print OPENPAR STRLIT CLOSEPAR TILDE'''
    print(t[3])
    #List.append(t[3])

def p_statement_print_var(t):
    '''statement : VAR ASSIGN expression TILDE print OPENPAR VAR CLOSEPAR TILDE'''
    print(t[3])
    #List.append(t[3])

def p_statement_print_var_string(t):
    '''statement : VAR ASSIGN STRLIT TILDE print OPENPAR VAR CLOSEPAR TILDE'''
    print(t[3])
    #List.append(t[3])

def p_statement_if(t):
    '''statement : if_statement'''

def p_if_statement(p):
    '''if_statement : if OPENPAR boolean CLOSEPAR OPENCURLY statement CLOSECURLY'''
    if (p[3]):
        p[0] = p[5]
    #List.append(p[0])

def p_if_else(p):
    '''if_statement : if OPENPAR boolean CLOSEPAR print OPENPAR STRLIT CLOSEPAR TILDE else OPENCURLY print OPENPAR STRLIT CLOSEPAR TILDE CLOSECURLY
                    | if OPENPAR boolean CLOSEPAR print OPENPAR INTLIT CLOSEPAR TILDE else OPENCURLY print OPENPAR INTLIT CLOSEPAR TILDE CLOSECURLY
                    | if OPENPAR boolean CLOSEPAR print OPENPAR expression CLOSEPAR TILDE else OPENCURLY print OPENPAR expression CLOSEPAR TILDE CLOSECURLY
    '''                
    if (p[3]==True):
        print(p[7])
        #if_list.append(p[5])
    else:
        print(p[14])
        #if_list.append(p[8])

# def p_if_else_exp(p):
#   '''if_statement : if OPENPAR boolean CLOSEPAR print OPENPAR expression CLOSEPAR TILDE else OPENCURLY print OPENPAR expression CLOSEPAR TILDE CLOSECURLY
#     '''

def p_statement_while(p):
    '''statement : while_stmt'''

def p_while_stmt(p):
    '''while_stmt : VAR ASSIGN INTLIT TILDE while OPENPAR boolean CLOSEPAR OPENCURLY statement CLOSECURLY if_statement'''
    while(p[3]):
      p[6]
    p[0] = p[8]

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_expression_boolean(p):
    '''expression : boolean'''
    p[0] = p[1]

def p_boolean(p):
    '''boolean : expression GT term
               | expression GEQ term
               | expression LT term
               | expression LEQ term
               | expression EQ term
               | expression NEQ term
               | expression AND term
               | expression OR term
               | expression is term'''
    if(p[2] == '>'):
      p[0] = p[1] > p[3]
    elif(p[2] == '>='):
      p[0] = p[1] >= p[3]
    elif(p[2] == '<'):
      p[0] = p[1] < p[3]
    elif(p[2] == '<='):
      p[0] = p[1] <= p[3]
    elif(p[2] == '=='):
      p[0] = p[1] == p[3]
    elif(p[2] == '!'):
      p[0] = p[1] != p[3]
    elif(p[2] == '&&'):
      p[0] = p[1] and p[3]
    elif(p[2] == '||'):
      p[0] = p[1] or  p[3]
    elif(p[2] == 'es'):
      p[0] = p[1] == p[3]

def p_expression_PLUS(p):
    '''expression : expression PLUS term'''
    p[0] = p[1] + p[3]

def p_expression_MINUS(p):
    '''expression : expression MINUS term'''
    p[0] = p[1] - p[3]

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
    '''factor : INTLIT
              | FLTLIT
              | DBLLIT'''
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

parser.parse(data)



