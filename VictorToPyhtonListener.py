from antlr4 import *
from LexerVictor import LexerVictor
from ParserVictor import ParserVictor
from antlr4.error.ErrorListener import ConsoleErrorListener
from SemanticListener import SemanticListener

class VictorToPyhtonListener(ParseTreeListener):
    def __init__(self):
        self.output = ""
        self.inside_function = False
        self.asignaciones_bloque = set()
        self.indentation_level = 0  # Agregar una variable para el nivel de indentación

    def generate_indentation(self):
        # Método para generar la indentación adecuada según el nivel actual
        return "\t" * self.indentation_level

    def is_inside_block(self, ctx):
        current_ctx = ctx
        while current_ctx is not None:
            if isinstance(current_ctx, ParserVictor.BloqueContext):
                return True
            current_ctx = current_ctx.parentCtx
        return False

    def enterPrograma(self, ctx:ParserVictor.ProgramaContext):
        self.output += "# Código generado en Python\n"

    def enterDeclaracion_variable(self, ctx:ParserVictor.Declaracion_variableContext):
        if self.is_inside_block(ctx):
            self.output += f"\t"
        identificador = ctx.IDENTIFICADOR().getText()
        valor = ctx.expresion().getText()
        self.output += f"{identificador} = {valor};\n"

    def enterAsignacion(self, ctx):
        identificador = ctx.IDENTIFICADOR().getText()
        valor = ctx.expresion().getText()
        if self.is_inside_block(ctx):
            self.asignaciones_bloque.add(identificador)
            self.output += f"\t{identificador} = {valor};\n"
        else:
            if identificador not in self.asignaciones_bloque:
                print(  self.asignaciones_bloque);
                self.output += f"{identificador} = {valor};\n"

    def enterWhile_statement(self, ctx:ParserVictor.While_statementContext):
        expresion = ctx.expresion().getText()
        self.output += f"while({expresion}):"
        self.output += "\n"

    def exitWhile_statement(self, ctx:ParserVictor.While_statementContext):
        pass

    def enterBloque(self, ctx:ParserVictor.BloqueContext):
        # Aumentar el nivel de indentación al entrar en un bloque
        self.indentation_level += 1
        for declaracion in ctx.declaraciones().declaracion():
            if isinstance(declaracion, ParserVictor.Declaracion_variableContext):
                identificador = declaracion.IDENTIFICADOR().getText()
                valor = declaracion.expresion().getText()
                self.output += f"{identificador} = {valor}\n"
            elif isinstance(declaracion, ParserVictor.ImprimirContext):
                expresion = declaracion.expresion().getText()
                self.output += f"print({expresion})\n"
        

    def exitBloque(self, ctx:ParserVictor.BloqueContext): 
        # Reducir el nivel de indentación al salir de un bloque
        self.indentation_level -= 1
        self.output += "\n"   

    def enterDeclaracion_funcion(self, ctx:ParserVictor.Declaracion_funcionContext):
        self.inside_function = True
        nombre_funcion = ctx.IDENTIFICADOR().getText()
        parametros = ", ".join([parametro.getText() for parametro in ctx.parametros().parametro()])
        bloque = ctx.bloque().getText()
        self.output += f"def  {nombre_funcion}({parametros}):\n "

    def enterImprimir(self, ctx:ParserVictor.ImprimirContext):
        if self.is_inside_block(ctx):
             self.output += f"\t"
        expresion = ctx.expresion().getText()
        self.output += f"print({expresion})\n"
            
    def enterIf_statement(self, ctx:ParserVictor.If_statementContext):
        if self.is_inside_block(ctx):
            self.output += f"\t"
        expresion  = ctx.expresion().getText()
        self.output += f"if { expresion}:\n \t"


    def exitIf_statement(self, ctx:ParserVictor.If_statementContext):
        
        self.output += "\n"

    def enterElseif_statement(self, ctx:ParserVictor.Elseif_statementContext):
        if self.is_inside_block(ctx):
            self.output += f"\t"
        expresion  = ctx.expresion().getText()
        self.output += f"elif { expresion}:\n \t"

    def exitElseif_statement(self, ctx:ParserVictor.Elseif_statementContext):
        self.output += "\n"


    def enterExpresion(self, ctx:ParserVictor.ExpresionContext):
        # No hace nada aquí para evitar agregar el ';' al final
        pass

    def exitDeclaracion_funcion(self, ctx:ParserVictor.Declaracion_funcionContext):
        self.inside_function = False
    





