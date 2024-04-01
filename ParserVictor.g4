parser grammar ParserVictor;
options {
  tokenVocab = LexerVictor;
}

@parser::members {
    self.variable_declaradas = set()
}

programa : declaraciones EOF;

declaraciones : declaracion*;

declaracion : declaracion_variable
            | declaracion_funcion
            | imprimir
            | capturar
            | sentencia;
            

declaracion_variable : VERSA IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA {
if $IDENTIFICADOR.text in self.variable_declaradas:
    offending_token = localctx._IDENTIFICADOR if localctx._IDENTIFICADOR is not None else self.getCurrentToken()
    error_message = f"La variable '{localctx._IDENTIFICADOR.text}' ya ha sido declarada en este bloque."
    self.notifyErrorListeners(error_message, offending_token, None)
else:
    self.variable_declaradas.add($IDENTIFICADOR.text)
};

declaracion_funcion : WORK IDENTIFICADOR PARENTESIS_IZQ parametros? PARENTESIS_DER bloque;

imprimir : SHOWTEXT PARENTESIS_IZQ expresion PARENTESIS_DER PUNTO_Y_COMA;
capturar : INPUTTEXT PARENTESIS_IZQ CADENA COMA IDENTIFICADOR PARENTESIS_DER PUNTO_Y_COMA;

parametros : parametro (COMA parametro)* | /* vacío */;
parametro : IDENTIFICADOR;

bloque : LLAVE_IZQ declaraciones LLAVE_DER;

sentencia : asignacion 
            | expresion PUNTO_Y_COMA
            | expresion PUNTO_Y_COMA
            | if_statement
            | while_statement
            | for_statement
            ;

if_statement : IF PARENTESIS_IZQ expresion PARENTESIS_DER bloque (elseif_statement)* (ELSE bloque)?;

elseif_statement : ELSEIF PARENTESIS_IZQ expresion PARENTESIS_DER bloque;


while_statement : DURING PARENTESIS_IZQ expresion PARENTESIS_DER bloque;

for_statement : WHEN PARENTESIS_IZQ declaracion_variable expresion PUNTO_Y_COMA asignacion_expresion PARENTESIS_DER bloque;

asignacion_expresion : asignacion | expresion;      

asignacion : IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA;

expresion : expresion_aditiva;

expresion_aditiva : expresion_multiplicativa ( (MAS | MENOS) expresion_multiplicativa )*;

expresion_multiplicativa : expresion_unaria ( (MULTIPLICACION | DIVISION | MODULO) expresion_unaria )*;

expresion_unaria : (MAS | MENOS)? expresion_primaria;

expresion_primaria : IDENTIFICADOR {
if ($IDENTIFICADOR.text) not in self.variable_declaradas:
     print("Error: La variable {} no ha sido declarada previamente".format($IDENTIFICADOR.text))
}
                   | NUMERO_ENTERO
                   | NUMERO_FLOTANTE
                   | booleano
                   | CADENA
                   | PARENTESIS_IZQ expresion_aditiva PARENTESIS_DER
                   | expresion_primaria IGUAL_IGUAL expresion_primaria
                   | expresion_primaria DIFERENTE_QUE expresion_primaria
                   | expresion_primaria MAYOR_IGUAL_QUE expresion_primaria
                   | expresion_primaria MENOR_IGUAL_QUE expresion_primaria
                   | expresion_primaria MAYOR expresion_primaria
                   | expresion_primaria MENOR expresion_primaria
                   | expresion_primaria OR expresion_primaria
                   | expresion_primaria AND expresion_primaria
                   | NOT expresion_primaria
                   | MENOS expresion_primaria
                   ;

booleano : TRUE | FALSE;