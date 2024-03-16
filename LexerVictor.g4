lexer grammar LexerVictor;

// Palabras reservadas
VERSA : 'versa';
WORK : 'work';

// Tipos de datos
ENTERO : 'int';
FLOTANTE : 'float';


// Operadores y delimitadores
MAS : '+';
MENOS : '-';
MULTIPLICACION : '*';
DIVISION : '/';
MODULO : '%';
IGUAL : '=';
MAYOR : '>';
MENOR : '<';

//OPERACIONES BOOLENAS
IGUAL_IGUAL       : '==';
DIFERENTE_QUE     : '!=';
MAYOR_IGUAL_QUE   : '>=';
MENOR_IGUAL_QUE   : '<=';
OR                : '||';
AND               : '&&';
NOT               :'!';

PUNTO_Y_COMA : ';';
COMA : ',';
PARENTESIS_IZQ : '(';
PARENTESIS_DER : ')';
LLAVE_IZQ : '{';
LLAVE_DER : '}';
CORCHETE_IZQ : '[';
CORCHETE_DER : ']';

INPUTTEXT         : 'inputText';
SHOWTEXT          : 'showText';
DURING            : 'during';
WHEN              : 'when';
ELSEIF            : 'elseif';
IF                : 'if';
ELSE              : 'else';



// Espacios en blanco y caracteres ignorados
ESPACIO : [ \t\r\n]+ -> skip;
COMENTARIO : '//' ~[\r\n]* -> skip;

// Cadena entre comillas dobles
CADENA : '"' (~["\r\n])* '"';

// Booleanos
TRUE : 'true';
FALSE : 'falso';
BOOLEANO : 'bool';


// Identificadores y números
IDENTIFICADOR : ('a'..'z'|'A'..'Z'|'_')+;
NUMERO_ENTERO : [0-9]+;
NUMERO_FLOTANTE : [0-9]*'.'[0-9]+;
