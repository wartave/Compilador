# Generated from ParserVictor.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,2,1,2,3,2,54,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,67,8,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,81,8,6,10,6,12,6,84,
        9,6,1,6,3,6,87,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,105,8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,
        113,8,10,10,10,12,10,116,9,10,1,10,1,10,3,10,120,8,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,
        5,16,150,8,16,10,16,12,16,153,9,16,1,17,1,17,1,17,5,17,158,8,17,
        10,17,12,17,161,9,17,1,18,3,18,164,8,18,1,18,1,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        183,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,203,8,19,10,19,12,19,206,
        9,19,1,19,0,1,38,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,0,2,1,0,6,7,1,0,8,10,217,0,40,1,0,0,0,2,46,1,0,0,0,4,53,
        1,0,0,0,6,55,1,0,0,0,8,62,1,0,0,0,10,71,1,0,0,0,12,86,1,0,0,0,14,
        88,1,0,0,0,16,90,1,0,0,0,18,104,1,0,0,0,20,106,1,0,0,0,22,121,1,
        0,0,0,24,127,1,0,0,0,26,133,1,0,0,0,28,139,1,0,0,0,30,144,1,0,0,
        0,32,146,1,0,0,0,34,154,1,0,0,0,36,163,1,0,0,0,38,182,1,0,0,0,40,
        41,3,2,1,0,41,42,5,0,0,1,42,1,1,0,0,0,43,45,3,4,2,0,44,43,1,0,0,
        0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,3,1,0,0,0,48,46,1,
        0,0,0,49,54,3,6,3,0,50,54,3,8,4,0,51,54,3,10,5,0,52,54,3,18,9,0,
        53,49,1,0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,5,1,0,
        0,0,55,56,5,1,0,0,56,57,5,41,0,0,57,58,5,11,0,0,58,59,3,30,15,0,
        59,60,5,21,0,0,60,61,6,3,-1,0,61,7,1,0,0,0,62,63,5,2,0,0,63,64,5,
        41,0,0,64,66,5,23,0,0,65,67,3,12,6,0,66,65,1,0,0,0,66,67,1,0,0,0,
        67,68,1,0,0,0,68,69,5,24,0,0,69,70,3,16,8,0,70,9,1,0,0,0,71,72,5,
        30,0,0,72,73,5,23,0,0,73,74,3,30,15,0,74,75,5,24,0,0,75,76,5,21,
        0,0,76,11,1,0,0,0,77,82,3,14,7,0,78,79,5,22,0,0,79,81,3,14,7,0,80,
        78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,87,1,0,0,
        0,84,82,1,0,0,0,85,87,1,0,0,0,86,77,1,0,0,0,86,85,1,0,0,0,87,13,
        1,0,0,0,88,89,5,41,0,0,89,15,1,0,0,0,90,91,5,25,0,0,91,92,3,2,1,
        0,92,93,5,26,0,0,93,17,1,0,0,0,94,105,3,28,14,0,95,96,3,30,15,0,
        96,97,5,21,0,0,97,105,1,0,0,0,98,99,3,30,15,0,99,100,5,21,0,0,100,
        105,1,0,0,0,101,105,3,20,10,0,102,105,3,24,12,0,103,105,3,26,13,
        0,104,94,1,0,0,0,104,95,1,0,0,0,104,98,1,0,0,0,104,101,1,0,0,0,104,
        102,1,0,0,0,104,103,1,0,0,0,105,19,1,0,0,0,106,107,5,34,0,0,107,
        108,5,23,0,0,108,109,3,30,15,0,109,110,5,24,0,0,110,114,3,16,8,0,
        111,113,3,22,11,0,112,111,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,
        0,114,115,1,0,0,0,115,119,1,0,0,0,116,114,1,0,0,0,117,118,5,35,0,
        0,118,120,3,16,8,0,119,117,1,0,0,0,119,120,1,0,0,0,120,21,1,0,0,
        0,121,122,5,33,0,0,122,123,5,23,0,0,123,124,3,30,15,0,124,125,5,
        24,0,0,125,126,3,16,8,0,126,23,1,0,0,0,127,128,5,31,0,0,128,129,
        5,23,0,0,129,130,3,30,15,0,130,131,5,24,0,0,131,132,3,16,8,0,132,
        25,1,0,0,0,133,134,5,32,0,0,134,135,5,23,0,0,135,136,3,30,15,0,136,
        137,5,24,0,0,137,138,3,16,8,0,138,27,1,0,0,0,139,140,5,41,0,0,140,
        141,5,11,0,0,141,142,3,30,15,0,142,143,5,21,0,0,143,29,1,0,0,0,144,
        145,3,32,16,0,145,31,1,0,0,0,146,151,3,34,17,0,147,148,7,0,0,0,148,
        150,3,34,17,0,149,147,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,
        152,1,0,0,0,152,33,1,0,0,0,153,151,1,0,0,0,154,159,3,36,18,0,155,
        156,7,1,0,0,156,158,3,36,18,0,157,155,1,0,0,0,158,161,1,0,0,0,159,
        157,1,0,0,0,159,160,1,0,0,0,160,35,1,0,0,0,161,159,1,0,0,0,162,164,
        7,0,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,
        3,38,19,0,166,37,1,0,0,0,167,168,6,19,-1,0,168,169,5,41,0,0,169,
        183,6,19,-1,0,170,183,5,42,0,0,171,183,5,43,0,0,172,183,5,5,0,0,
        173,183,5,38,0,0,174,175,5,23,0,0,175,176,3,32,16,0,176,177,5,24,
        0,0,177,183,1,0,0,0,178,179,5,20,0,0,179,183,3,38,19,2,180,181,5,
        7,0,0,181,183,3,38,19,1,182,167,1,0,0,0,182,170,1,0,0,0,182,171,
        1,0,0,0,182,172,1,0,0,0,182,173,1,0,0,0,182,174,1,0,0,0,182,178,
        1,0,0,0,182,180,1,0,0,0,183,204,1,0,0,0,184,185,10,8,0,0,185,186,
        5,14,0,0,186,203,3,38,19,9,187,188,10,7,0,0,188,189,5,15,0,0,189,
        203,3,38,19,8,190,191,10,6,0,0,191,192,5,16,0,0,192,203,3,38,19,
        7,193,194,10,5,0,0,194,195,5,17,0,0,195,203,3,38,19,6,196,197,10,
        4,0,0,197,198,5,18,0,0,198,203,3,38,19,5,199,200,10,3,0,0,200,201,
        5,19,0,0,201,203,3,38,19,4,202,184,1,0,0,0,202,187,1,0,0,0,202,190,
        1,0,0,0,202,193,1,0,0,0,202,196,1,0,0,0,202,199,1,0,0,0,203,206,
        1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,39,1,0,0,0,206,204,1,
        0,0,0,14,46,53,66,82,86,104,114,119,151,159,163,182,202,204
    ]

class ParserVictor ( Parser ):

    grammarFileName = "ParserVictor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'versa'", "'work'", "'int'", "'float'", 
                     "'bool'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", "'||'", 
                     "'&&'", "'!'", "';'", "','", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'inputText'", "'showText'", "'during'", 
                     "'when'", "'elseif'", "'if'", "'else'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'falso'" ]

    symbolicNames = [ "<INVALID>", "VERSA", "WORK", "ENTERO", "FLOTANTE", 
                      "BOOLEANO", "MAS", "MENOS", "MULTIPLICACION", "DIVISION", 
                      "MODULO", "IGUAL", "MAYOR", "MENOR", "IGUAL_IGUAL", 
                      "DIFERENTE_QUE", "MAYOR_IGUAL_QUE", "MENOR_IGUAL_QUE", 
                      "OR", "AND", "NOT", "PUNTO_Y_COMA", "COMA", "PARENTESIS_IZQ", 
                      "PARENTESIS_DER", "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", 
                      "CORCHETE_DER", "INPUTTEXT", "SHOWTEXT", "DURING", 
                      "WHEN", "ELSEIF", "IF", "ELSE", "ESPACIO", "COMENTARIO", 
                      "CADENA", "TRUE", "FALSE", "IDENTIFICADOR", "NUMERO_ENTERO", 
                      "NUMERO_FLOTANTE" ]

    RULE_programa = 0
    RULE_declaraciones = 1
    RULE_declaracion = 2
    RULE_declaracion_variable = 3
    RULE_declaracion_funcion = 4
    RULE_imprimir = 5
    RULE_parametros = 6
    RULE_parametro = 7
    RULE_bloque = 8
    RULE_sentencia = 9
    RULE_if_statement = 10
    RULE_elseif_statement = 11
    RULE_while_statement = 12
    RULE_for_statement = 13
    RULE_asignacion = 14
    RULE_expresion = 15
    RULE_expresion_aditiva = 16
    RULE_expresion_multiplicativa = 17
    RULE_expresion_unaria = 18
    RULE_expresion_primaria = 19

    ruleNames =  [ "programa", "declaraciones", "declaracion", "declaracion_variable", 
                   "declaracion_funcion", "imprimir", "parametros", "parametro", 
                   "bloque", "sentencia", "if_statement", "elseif_statement", 
                   "while_statement", "for_statement", "asignacion", "expresion", 
                   "expresion_aditiva", "expresion_multiplicativa", "expresion_unaria", 
                   "expresion_primaria" ]

    EOF = Token.EOF
    VERSA=1
    WORK=2
    ENTERO=3
    FLOTANTE=4
    BOOLEANO=5
    MAS=6
    MENOS=7
    MULTIPLICACION=8
    DIVISION=9
    MODULO=10
    IGUAL=11
    MAYOR=12
    MENOR=13
    IGUAL_IGUAL=14
    DIFERENTE_QUE=15
    MAYOR_IGUAL_QUE=16
    MENOR_IGUAL_QUE=17
    OR=18
    AND=19
    NOT=20
    PUNTO_Y_COMA=21
    COMA=22
    PARENTESIS_IZQ=23
    PARENTESIS_DER=24
    LLAVE_IZQ=25
    LLAVE_DER=26
    CORCHETE_IZQ=27
    CORCHETE_DER=28
    INPUTTEXT=29
    SHOWTEXT=30
    DURING=31
    WHEN=32
    ELSEIF=33
    IF=34
    ELSE=35
    ESPACIO=36
    COMENTARIO=37
    CADENA=38
    TRUE=39
    FALSE=40
    IDENTIFICADOR=41
    NUMERO_ENTERO=42
    NUMERO_FLOTANTE=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.variable_declaradas = set()



    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaraciones(self):
            return self.getTypedRuleContext(ParserVictor.DeclaracionesContext,0)


        def EOF(self):
            return self.getToken(ParserVictor.EOF, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ParserVictor.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.declaraciones()
            self.state = 41
            self.match(ParserVictor.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserVictor.DeclaracionContext)
            else:
                return self.getTypedRuleContext(ParserVictor.DeclaracionContext,i)


        def getRuleIndex(self):
            return ParserVictor.RULE_declaraciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraciones" ):
                listener.enterDeclaraciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraciones" ):
                listener.exitDeclaraciones(self)




    def declaraciones(self):

        localctx = ParserVictor.DeclaracionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaraciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15692746195174) != 0):
                self.state = 43
                self.declaracion()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_variable(self):
            return self.getTypedRuleContext(ParserVictor.Declaracion_variableContext,0)


        def declaracion_funcion(self):
            return self.getTypedRuleContext(ParserVictor.Declaracion_funcionContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(ParserVictor.ImprimirContext,0)


        def sentencia(self):
            return self.getTypedRuleContext(ParserVictor.SentenciaContext,0)


        def getRuleIndex(self):
            return ParserVictor.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = ParserVictor.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.declaracion_variable()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.declaracion_funcion()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.imprimir()
                pass
            elif token in [5, 6, 7, 20, 23, 31, 32, 34, 38, 41, 42, 43]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.sentencia()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._IDENTIFICADOR = None # Token

        def VERSA(self):
            return self.getToken(ParserVictor.VERSA, 0)

        def IDENTIFICADOR(self):
            return self.getToken(ParserVictor.IDENTIFICADOR, 0)

        def IGUAL(self):
            return self.getToken(ParserVictor.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ParserVictor.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_declaracion_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_variable" ):
                listener.enterDeclaracion_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_variable" ):
                listener.exitDeclaracion_variable(self)




    def declaracion_variable(self):

        localctx = ParserVictor.Declaracion_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ParserVictor.VERSA)
            self.state = 56
            localctx._IDENTIFICADOR = self.match(ParserVictor.IDENTIFICADOR)
            self.state = 57
            self.match(ParserVictor.IGUAL)
            self.state = 58
            self.expresion()
            self.state = 59
            self.match(ParserVictor.PUNTO_Y_COMA)

            if (None if localctx._IDENTIFICADOR is None else localctx._IDENTIFICADOR.text) in self.variable_declaradas:
                offending_token = localctx._IDENTIFICADOR if localctx._IDENTIFICADOR is not None else self.getCurrentToken()
                error_message = f"La variable '{localctx._IDENTIFICADOR.text}' ya ha sido declarada en este bloque."
                self.notifyErrorListeners(error_message, offending_token, None)
            else:
                self.variable_declaradas.add((None if localctx._IDENTIFICADOR is None else localctx._IDENTIFICADOR.text))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORK(self):
            return self.getToken(ParserVictor.WORK, 0)

        def IDENTIFICADOR(self):
            return self.getToken(ParserVictor.IDENTIFICADOR, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(ParserVictor.PARENTESIS_IZQ, 0)

        def PARENTESIS_DER(self):
            return self.getToken(ParserVictor.PARENTESIS_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(ParserVictor.BloqueContext,0)


        def parametros(self):
            return self.getTypedRuleContext(ParserVictor.ParametrosContext,0)


        def getRuleIndex(self):
            return ParserVictor.RULE_declaracion_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_funcion" ):
                listener.enterDeclaracion_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_funcion" ):
                listener.exitDeclaracion_funcion(self)




    def declaracion_funcion(self):

        localctx = ParserVictor.Declaracion_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ParserVictor.WORK)
            self.state = 63
            self.match(ParserVictor.IDENTIFICADOR)
            self.state = 64
            self.match(ParserVictor.PARENTESIS_IZQ)
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 65
                self.parametros()


            self.state = 68
            self.match(ParserVictor.PARENTESIS_DER)
            self.state = 69
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOWTEXT(self):
            return self.getToken(ParserVictor.SHOWTEXT, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(ParserVictor.PARENTESIS_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(ParserVictor.PARENTESIS_DER, 0)

        def PUNTO_Y_COMA(self):
            return self.getToken(ParserVictor.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)




    def imprimir(self):

        localctx = ParserVictor.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ParserVictor.SHOWTEXT)
            self.state = 72
            self.match(ParserVictor.PARENTESIS_IZQ)
            self.state = 73
            self.expresion()
            self.state = 74
            self.match(ParserVictor.PARENTESIS_DER)
            self.state = 75
            self.match(ParserVictor.PUNTO_Y_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserVictor.ParametroContext)
            else:
                return self.getTypedRuleContext(ParserVictor.ParametroContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserVictor.COMA)
            else:
                return self.getToken(ParserVictor.COMA, i)

        def getRuleIndex(self):
            return ParserVictor.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = ParserVictor.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.parametro()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==22:
                    self.state = 78
                    self.match(ParserVictor.COMA)
                    self.state = 79
                    self.parametro()
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ParserVictor.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)




    def parametro(self):

        localctx = ParserVictor.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ParserVictor.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_IZQ(self):
            return self.getToken(ParserVictor.LLAVE_IZQ, 0)

        def declaraciones(self):
            return self.getTypedRuleContext(ParserVictor.DeclaracionesContext,0)


        def LLAVE_DER(self):
            return self.getToken(ParserVictor.LLAVE_DER, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = ParserVictor.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ParserVictor.LLAVE_IZQ)
            self.state = 91
            self.declaraciones()
            self.state = 92
            self.match(ParserVictor.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(ParserVictor.AsignacionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ParserVictor.PUNTO_Y_COMA, 0)

        def if_statement(self):
            return self.getTypedRuleContext(ParserVictor.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(ParserVictor.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ParserVictor.For_statementContext,0)


        def getRuleIndex(self):
            return ParserVictor.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = ParserVictor.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sentencia)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.expresion()
                self.state = 96
                self.match(ParserVictor.PUNTO_Y_COMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.expresion()
                self.state = 99
                self.match(ParserVictor.PUNTO_Y_COMA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 103
                self.for_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ParserVictor.IF, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(ParserVictor.PARENTESIS_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(ParserVictor.PARENTESIS_DER, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserVictor.BloqueContext)
            else:
                return self.getTypedRuleContext(ParserVictor.BloqueContext,i)


        def elseif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserVictor.Elseif_statementContext)
            else:
                return self.getTypedRuleContext(ParserVictor.Elseif_statementContext,i)


        def ELSE(self):
            return self.getToken(ParserVictor.ELSE, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = ParserVictor.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ParserVictor.IF)
            self.state = 107
            self.match(ParserVictor.PARENTESIS_IZQ)
            self.state = 108
            self.expresion()
            self.state = 109
            self.match(ParserVictor.PARENTESIS_DER)
            self.state = 110
            self.bloque()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 111
                self.elseif_statement()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 117
                self.match(ParserVictor.ELSE)
                self.state = 118
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(ParserVictor.ELSEIF, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(ParserVictor.PARENTESIS_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(ParserVictor.PARENTESIS_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(ParserVictor.BloqueContext,0)


        def getRuleIndex(self):
            return ParserVictor.RULE_elseif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_statement" ):
                listener.enterElseif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_statement" ):
                listener.exitElseif_statement(self)




    def elseif_statement(self):

        localctx = ParserVictor.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ParserVictor.ELSEIF)
            self.state = 122
            self.match(ParserVictor.PARENTESIS_IZQ)
            self.state = 123
            self.expresion()
            self.state = 124
            self.match(ParserVictor.PARENTESIS_DER)
            self.state = 125
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DURING(self):
            return self.getToken(ParserVictor.DURING, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(ParserVictor.PARENTESIS_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(ParserVictor.PARENTESIS_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(ParserVictor.BloqueContext,0)


        def getRuleIndex(self):
            return ParserVictor.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = ParserVictor.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ParserVictor.DURING)
            self.state = 128
            self.match(ParserVictor.PARENTESIS_IZQ)
            self.state = 129
            self.expresion()
            self.state = 130
            self.match(ParserVictor.PARENTESIS_DER)
            self.state = 131
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(ParserVictor.WHEN, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(ParserVictor.PARENTESIS_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(ParserVictor.PARENTESIS_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(ParserVictor.BloqueContext,0)


        def getRuleIndex(self):
            return ParserVictor.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = ParserVictor.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ParserVictor.WHEN)
            self.state = 134
            self.match(ParserVictor.PARENTESIS_IZQ)
            self.state = 135
            self.expresion()
            self.state = 136
            self.match(ParserVictor.PARENTESIS_DER)
            self.state = 137
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(ParserVictor.IDENTIFICADOR, 0)

        def IGUAL(self):
            return self.getToken(ParserVictor.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(ParserVictor.ExpresionContext,0)


        def PUNTO_Y_COMA(self):
            return self.getToken(ParserVictor.PUNTO_Y_COMA, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = ParserVictor.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ParserVictor.IDENTIFICADOR)
            self.state = 140
            self.match(ParserVictor.IGUAL)
            self.state = 141
            self.expresion()
            self.state = 142
            self.match(ParserVictor.PUNTO_Y_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion_aditiva(self):
            return self.getTypedRuleContext(ParserVictor.Expresion_aditivaContext,0)


        def getRuleIndex(self):
            return ParserVictor.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = ParserVictor.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.expresion_aditiva()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_aditivaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion_multiplicativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserVictor.Expresion_multiplicativaContext)
            else:
                return self.getTypedRuleContext(ParserVictor.Expresion_multiplicativaContext,i)


        def MAS(self, i:int=None):
            if i is None:
                return self.getTokens(ParserVictor.MAS)
            else:
                return self.getToken(ParserVictor.MAS, i)

        def MENOS(self, i:int=None):
            if i is None:
                return self.getTokens(ParserVictor.MENOS)
            else:
                return self.getToken(ParserVictor.MENOS, i)

        def getRuleIndex(self):
            return ParserVictor.RULE_expresion_aditiva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_aditiva" ):
                listener.enterExpresion_aditiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_aditiva" ):
                listener.exitExpresion_aditiva(self)




    def expresion_aditiva(self):

        localctx = ParserVictor.Expresion_aditivaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expresion_aditiva)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.expresion_multiplicativa()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.expresion_multiplicativa()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_multiplicativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion_unaria(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserVictor.Expresion_unariaContext)
            else:
                return self.getTypedRuleContext(ParserVictor.Expresion_unariaContext,i)


        def MULTIPLICACION(self, i:int=None):
            if i is None:
                return self.getTokens(ParserVictor.MULTIPLICACION)
            else:
                return self.getToken(ParserVictor.MULTIPLICACION, i)

        def DIVISION(self, i:int=None):
            if i is None:
                return self.getTokens(ParserVictor.DIVISION)
            else:
                return self.getToken(ParserVictor.DIVISION, i)

        def MODULO(self, i:int=None):
            if i is None:
                return self.getTokens(ParserVictor.MODULO)
            else:
                return self.getToken(ParserVictor.MODULO, i)

        def getRuleIndex(self):
            return ParserVictor.RULE_expresion_multiplicativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_multiplicativa" ):
                listener.enterExpresion_multiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_multiplicativa" ):
                listener.exitExpresion_multiplicativa(self)




    def expresion_multiplicativa(self):

        localctx = ParserVictor.Expresion_multiplicativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expresion_multiplicativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.expresion_unaria()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 155
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.expresion_unaria()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_unariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion_primaria(self):
            return self.getTypedRuleContext(ParserVictor.Expresion_primariaContext,0)


        def MAS(self):
            return self.getToken(ParserVictor.MAS, 0)

        def MENOS(self):
            return self.getToken(ParserVictor.MENOS, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_expresion_unaria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_unaria" ):
                listener.enterExpresion_unaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_unaria" ):
                listener.exitExpresion_unaria(self)




    def expresion_unaria(self):

        localctx = ParserVictor.Expresion_unariaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expresion_unaria)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 165
            self.expresion_primaria(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_primariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._IDENTIFICADOR = None # Token

        def IDENTIFICADOR(self):
            return self.getToken(ParserVictor.IDENTIFICADOR, 0)

        def NUMERO_ENTERO(self):
            return self.getToken(ParserVictor.NUMERO_ENTERO, 0)

        def NUMERO_FLOTANTE(self):
            return self.getToken(ParserVictor.NUMERO_FLOTANTE, 0)

        def BOOLEANO(self):
            return self.getToken(ParserVictor.BOOLEANO, 0)

        def CADENA(self):
            return self.getToken(ParserVictor.CADENA, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(ParserVictor.PARENTESIS_IZQ, 0)

        def expresion_aditiva(self):
            return self.getTypedRuleContext(ParserVictor.Expresion_aditivaContext,0)


        def PARENTESIS_DER(self):
            return self.getToken(ParserVictor.PARENTESIS_DER, 0)

        def NOT(self):
            return self.getToken(ParserVictor.NOT, 0)

        def expresion_primaria(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserVictor.Expresion_primariaContext)
            else:
                return self.getTypedRuleContext(ParserVictor.Expresion_primariaContext,i)


        def MENOS(self):
            return self.getToken(ParserVictor.MENOS, 0)

        def IGUAL_IGUAL(self):
            return self.getToken(ParserVictor.IGUAL_IGUAL, 0)

        def DIFERENTE_QUE(self):
            return self.getToken(ParserVictor.DIFERENTE_QUE, 0)

        def MAYOR_IGUAL_QUE(self):
            return self.getToken(ParserVictor.MAYOR_IGUAL_QUE, 0)

        def MENOR_IGUAL_QUE(self):
            return self.getToken(ParserVictor.MENOR_IGUAL_QUE, 0)

        def OR(self):
            return self.getToken(ParserVictor.OR, 0)

        def AND(self):
            return self.getToken(ParserVictor.AND, 0)

        def getRuleIndex(self):
            return ParserVictor.RULE_expresion_primaria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_primaria" ):
                listener.enterExpresion_primaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_primaria" ):
                listener.exitExpresion_primaria(self)



    def expresion_primaria(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserVictor.Expresion_primariaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expresion_primaria, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.state = 168
                localctx._IDENTIFICADOR = self.match(ParserVictor.IDENTIFICADOR)

                if ((None if localctx._IDENTIFICADOR is None else localctx._IDENTIFICADOR.text)) not in self.variable_declaradas:
                     print("Error: La variable {} no ha sido declarada previamente".format((None if localctx._IDENTIFICADOR is None else localctx._IDENTIFICADOR.text)))

                pass
            elif token in [42]:
                self.state = 170
                self.match(ParserVictor.NUMERO_ENTERO)
                pass
            elif token in [43]:
                self.state = 171
                self.match(ParserVictor.NUMERO_FLOTANTE)
                pass
            elif token in [5]:
                self.state = 172
                self.match(ParserVictor.BOOLEANO)
                pass
            elif token in [38]:
                self.state = 173
                self.match(ParserVictor.CADENA)
                pass
            elif token in [23]:
                self.state = 174
                self.match(ParserVictor.PARENTESIS_IZQ)
                self.state = 175
                self.expresion_aditiva()
                self.state = 176
                self.match(ParserVictor.PARENTESIS_DER)
                pass
            elif token in [20]:
                self.state = 178
                self.match(ParserVictor.NOT)
                self.state = 179
                self.expresion_primaria(2)
                pass
            elif token in [7]:
                self.state = 180
                self.match(ParserVictor.MENOS)
                self.state = 181
                self.expresion_primaria(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = ParserVictor.Expresion_primariaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_primaria)
                        self.state = 184
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 185
                        self.match(ParserVictor.IGUAL_IGUAL)
                        self.state = 186
                        self.expresion_primaria(9)
                        pass

                    elif la_ == 2:
                        localctx = ParserVictor.Expresion_primariaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_primaria)
                        self.state = 187
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 188
                        self.match(ParserVictor.DIFERENTE_QUE)
                        self.state = 189
                        self.expresion_primaria(8)
                        pass

                    elif la_ == 3:
                        localctx = ParserVictor.Expresion_primariaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_primaria)
                        self.state = 190
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 191
                        self.match(ParserVictor.MAYOR_IGUAL_QUE)
                        self.state = 192
                        self.expresion_primaria(7)
                        pass

                    elif la_ == 4:
                        localctx = ParserVictor.Expresion_primariaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_primaria)
                        self.state = 193
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 194
                        self.match(ParserVictor.MENOR_IGUAL_QUE)
                        self.state = 195
                        self.expresion_primaria(6)
                        pass

                    elif la_ == 5:
                        localctx = ParserVictor.Expresion_primariaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_primaria)
                        self.state = 196
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 197
                        self.match(ParserVictor.OR)
                        self.state = 198
                        self.expresion_primaria(5)
                        pass

                    elif la_ == 6:
                        localctx = ParserVictor.Expresion_primariaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_primaria)
                        self.state = 199
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 200
                        self.match(ParserVictor.AND)
                        self.state = 201
                        self.expresion_primaria(4)
                        pass

             
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expresion_primaria_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_primaria_sempred(self, localctx:Expresion_primariaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




